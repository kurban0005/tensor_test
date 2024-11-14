import os
import wget
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EС
from loguru import logger
from pages.page import Page



class SbisDownloadPage(Page):
    '''Класс описывает страницу "СКАЧАТЬ локальные версии" сайта SBIS.'''
    DOWNLOAD_SBIS_WINDOWS = (By.LINK_TEXT, 'Скачать (Exe 11.48 МБ)')

    def download(self):
        '''Кликает по ссылке "Скачать (Exe 11.48 МБ)" и начинает загрузку файла.'''
        url = self.get_url(self.DOWNLOAD_SBIS_WINDOWS)
        path = os.getcwd()
        logger.info('\nУСПЕШНО. Клик по ссылке "Скачать".')
        logger.info('\nЗагрузка началась.')
        wget.download(url, out=path)

    def download_complete(self):
        '''Подтверждает окончание загрузки файла.'''
        current_dir = os.getcwd()
        file_path = current_dir + '/sbisplugin-setup-web.exe'
        assert os.path.isfile(file_path), 'ОШИБКА. Загрузка файла НЕ ЗАВЕРШЕНА'
        logger.info('\nУСПЕШНО. Загрузка файла завершена.')

    def check_size_file(self):
        '''Проверяет размер загруженного файла.'''
        current_dir = os.getcwd()
        file_path = current_dir + '/sbisplugin-setup-web.exe'
        true_size = 11.48
        file_size = os.path.getsize(file_path) / 1048576
        file_size = round(file_size, 2)
        assert file_size == true_size, 'ОШИБКА. Проверка размера файла НЕ ПРОЙДЕНА'
        logger.info('\nУСПЕШНО. Проверка размера файла пройдена.')
