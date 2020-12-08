from .base_page import BasePage
from selenium.webdriver.common.by import By


class AboutPage(BasePage):


    ALL_LEADERS_CARDS = (By.CLASS_NAME, "card medium card--dark")
    CAREERS_ARROW_BTN = (By.CLASS_NAME, "arrow")
    ACCEPT_ALL_COOKIES_BTN = (By.ID, "onetrust-accept-btn-handler")
    SEE_OUR_JOB_OPENINGS_LINK = (By.PARTIAL_LINK_TEXT, "See our job openings")
    ALL_FULL_TIME_POSITIONS_LINKS_XPATH = '//div[@class="job"]//a[@class="hed"]'
