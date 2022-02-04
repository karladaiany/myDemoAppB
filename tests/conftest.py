import pytest
from appium import webdriver

from . import config, credentials

# Definir os valores padrão / default
def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='@ondemand.us-west-1.saucelabs.com:443/wd/hub',
        help='caminho do Appium no SauceLabs dos EUA'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='provedor do Appium'
    )
    parser.addoption(
        '--platform_name',
        action='store',
        default='Android',
        help='Sistema Operacional do dispositivo ou emulador'
    )
    parser.addoption(
        '--platform_version',
        action='store',
        default='9.0',
        help='Versão do Sistema Operacional do dispositivo ou emulador'
    )

@pytest.fixture
def driver(request):
    # passa os valores do arquivo config.py ou os valores default do pytest.addoption
    config.baseurl = request.config.getoption('baseurl')
    config.host = request.config.getoption('host')
    config.platform_name = request.config.getoption('platform_name')
    config.platform_version = request.config.getoption('platform_version')
    
    # direciona para execução do Appium local ou na nuvem
    if config.host == 'saucelabs':
        test_name = request.node.name   # nome do teste
        caps = {
            'platformName': 'Android',
            # 'appium:platformVersion': '10.0' # versão do emulador local
            'appium:platformVersion': '9.0',  # versão do emulador no Saucelabs
            'browserName': '',
            # 'appium:appiumVersion': '1.22.0'    # apenas quando local ou próprio (rede)
            # 'appium:deviceName': 'emulator5554' # aparelho ou emulador local
            'appium:deviceName': 'Galaxy S9 FHD GoogleAPI Emulator',  # emulador no Saucelabs
            'appium:deviceOrientation': 'portrait',
            'appium:app': 'storage:filename=mda-1.0.10-12.apk',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity',
            'appium:ensureWebviewsHavePages': True,
            'appium:nativeWebScreenshot': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True,
            'sauce.options': {
                'name': test_name      # enviar o nome do nosso teste para o SauceLabs
            }
        }

        # Montar a credential e a url
        _credentials = credentials.SAUCE_USERNAME + ':' + credentials.SAUCE_ACCESS_KEY
        _url = 'https://' + _credentials + config.baseurl

        # Instanciar o SauceLabs
        driver_ = webdriver.Remote(_url, caps)

    # Execução local
    else:
        caps = {
            'platformName': config.platform_name,
            'appium:platformVersion': config.platform_version,
            'browserName': '',
            'appium:appiumVersion': '1.22.0',    # apenas quando local ou próprio (rede)
            'appium:deviceName': 'emulator5554',     # aparelho ou emulador local
            'appium:deviceOrientation': 'portrait',
            'appium:appPackage': 'com.saucelabs.mydemoapp.android',
            'appium:appActivity': 'com.saucelabs.mydemoapp.android.view.activities.SplashActivity',
            'appium:ensureWebviewsHavePages': True,
            'appium:nativeWebScreenshot': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True
        }

        # Instanciar o device ou emulador via Appium local
        driver_ = webdriver.Remote(config.baseurl + ':4723/wd/hub', caps)

    # Função de finalização
    def quit():
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
        driver_.execute_script('sauce:job-result={}'.format(sauce_result))
        driver_.quit()

    request.addfinalizer(quit)      # Definiu como uma requisição no Pytest acaba
    return driver_

# Configuração do Hook para relatórios
pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
