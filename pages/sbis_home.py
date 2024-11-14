from selenium.webdriver.common.by import By
from loguru import logger
from pages.page import Page
from pages.sbis_contacts import SbisContactsPage
from pages.sbis_download import SbisDownloadPage


class SbisHomePage(Page):
    '''Класс описывает домашнюю страницу "SBIS".'''
    SBIS_CONTACTS_PAGE = (By.XPATH, '//a[contains(@href, "/contacts")]')
    SBIS_DOWNLOAD_PAGE = (By.LINK_TEXT, 'Скачать локальные версии')

    def click_contacts(self):
        '''Кликает по ссылке "Контакты". Возвращает страницу "Контакты".'''
        url = self.get_url(self.SBIS_CONTACTS_PAGE)
        self.go_to_url(url)
        logger.info('\nУСПЕШНО. Клик по ссылке "Контакты".')
        return SbisContactsPage(self.browser)

    def click_download_(self):
        '''Кликает по ссылке "Скачать локальные версии". Возвращает страницу "Загрузки".'''
        url = self.get_url(self.SBIS_DOWNLOAD_PAGE)
        self.go_to_url(url)
        logger.info('\nУСПЕШНО. Клик по ссылке "Скачать локальные версии".')
        return SbisDownloadPage(self.browser)
