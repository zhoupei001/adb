from appium import webdriver

def get_driver():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'

    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'true'

    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
