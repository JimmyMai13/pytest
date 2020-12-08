from api.base import Base as api_base
from api.accounts import Accounts
from pageobjects.base_page import BasePage
from pageobjects.about_page import AboutPage
import os
from selenium import webdriver
import configparser


class Base:

    def __init__(self):
        self.base = api_base()
        self.inst_api()

    def browser_driver(self, browser_type='chrome'):
        if browser_type.lower() == '"chrome"':
            driver = webdriver.Chrome(executable_path="{}/drivers/chromedriver".format(os.getcwd()))
        return driver

    def inst_pages(self):
        self.driver = self.browser_driver(browser_type=self.base.get_config()['browser'])
        self.basepage = BasePage(driver=self.driver)
        self.aboutpage = AboutPage(driver=self.driver)

    def inst_api(self):
        self.accounts = Accounts()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read('{}/config.ini'.format(os.getcwd()))
        return config['DEFAULT']

    def teardown_ui(self):
        self.driver.quit()
