import pytest
from selenium import webdriver
from loguru import logger
from pages.sbis_home import SbisHomePage


@pytest.fixture()
def browser():
    url = "http://sbis.ru/"
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()


def test_scenario_1(browser):
    '''Первый тестовый сценарий.'''

    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №1. -')
    sbis_home = SbisHomePage(browser)
    sbis_contacts = sbis_home.click_contacts()
    tensor_home = sbis_contacts.click_tensor_banner()
    tensor_home.check_url()
    tensor_home.check_strength_people()
    tensor_about = tensor_home.click_about()
    tensor_about.check_url
    tensor_about.check_size_photo()
    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №1 ЗАВЕРШЁН УСПЕШНО. -\n')


def test_scenario_2(browser):
    '''Второй тестовый сценарий.'''

    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №2. -')
    sbis_home = SbisHomePage(browser)
    sbis_contacts = sbis_home.click_contacts()
    sbis_contacts.check_current_region()
    sbis_contacts.chek_current_partners()
    sbis_contacts.change_region()
    sbis_contacts.check_new_region()
    sbis_contacts.check_new_partners()
    sbis_contacts.check_region_title()
    sbis_contacts.check_region_url()
    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №2 ЗАВЕРШЁН УСПЕШНО. -\n')


def test_scenario_3(browser):
    '''Третий тестовый сценарий.'''

    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №3. -')
    sbis_home = SbisHomePage(browser)
    sbis_download = sbis_home.click_download_()
    sbis_download.download()
    sbis_download.download_complete()
    sbis_download.check_size_file()
    logger.info('\n- ТЕСТОВЫЙ СЦЕНАРИЙ №3 ЗАВЕРШЁН УСПЕШНО. -\n')
