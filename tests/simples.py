# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

def testar__appium_inspector():
    caps = {}
    caps["platformName"] = "Android"
    # caps["appium:platformVersion"] = "10.0" # versão do emulador local
    caps["appium:platformVersion"] = "9.0"  # versão do emulador no Saucelabs
    caps["browserName"] = ""
    # caps["appium:appiumVersion"] = "1.22.0"    # apenas quando local ou próprio (rede)
    # caps["appium:deviceName"] = "emulator5554" # aparelho ou emulador local
    caps["appium:deviceName"] = "Galaxy S9 FHD GoogleAPI Emulator" # emulador no Saucelabs
    caps["appium:deviceOrientation"] = "portrait"
    caps["appium:app"] = 'storage:filename=mda-1.0.10-12.apk'
    caps["appium:appPackage"] = "com.saucelabs.mydemoapp.android"
    caps["appium:appActivity"] = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    caps["appium:ensureWebviewsHavePages"] = True
    caps["appium:nativeWebScreenshot"] = True
    caps["appium:newCommandTimeout"] = 3600
    caps["appium:connectHardwareKeyboard"] = True

    driver = webdriver.Remote("https://karladaiany:435a31e1-3d5f-452d-818a-0e49cc1d3547@ondemand.us-west-1.saucelabs.com:443/wd/hub", caps)

    el1 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]")
    el1.click()

    el2 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
    el2.click()
    el3 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
    el3.click()
    TouchAction(driver).press(x=927, y=2073).move_to(x=967, y=1313).release().perform()

    el4 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[4]")
    el4.click()
    el5 = driver.find_element_by_accessibility_id("Increases number of products")
    el5.click()
    el6 = driver.find_element_by_accessibility_id("Tap to add product to cart")
    el6.click()
    el7 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/cartTV")
    el7.click()
    el8 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/productTV")
    el8.click()
    el9 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/titleTV")
    el9.click()
    el10 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/priceTV")
    el10.click()

    el11 = driver.find_element_by_accessibility_id("Displays color of selected product")
    el11.click()
    el12 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/noTV")
    el12.click()
    el13 = driver.find_element_by_id("com.saucelabs.mydemoapp.android:id/totalPriceTV")
    el13.click()

    driver.quit()