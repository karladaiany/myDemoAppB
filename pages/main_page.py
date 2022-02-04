from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class MainPage(BasePage):
    # definir os localizadores / locators
    image_view_locator = '(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]'
    _product_image_view = {'by': AppiumBy.XPATH, 'value': image_view_locator}

    # inicialização
    def __init__(self, driver):
        self.driver = driver

    # ações
    def selecionar_primeiro_produto(self):
        self._apertar(self._product_image_view)
