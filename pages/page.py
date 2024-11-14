class Page:
    '''Класс описывает базовый функционал всех страниц.'''

    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        '''Найти элемент по указанному локатору.'''
        return self.browser.find_element(*locator)

    def find_all(self, locator):
        '''Найти все элементы по указанному локатору.'''
        return self.browser.find_elements(*locator)

    def get_url(self, locator):
        '''Получить url адрес локатора.'''
        link = self.find(locator)
        url = link.get_attribute('href')
        return url

    def go_to_url(self, url):
        '''Перейти по url адресу.'''
        self.browser.get(url)

    def click(self, locator):
        '''Нажать на элемент локатора.'''
        self.find(locator).click()
