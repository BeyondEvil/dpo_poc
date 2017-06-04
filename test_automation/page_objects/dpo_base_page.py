from basepage import BasePage


class DPOBasePage(BasePage):

    def go_to_page(self):
        self.get(self._url)
        self.maximize_window()
        self.verify_on_page()
        return self

    @staticmethod
    def get_compliant_locator(by, locator, params=None):
        """
        Returns a tuple of by and locator prepared with optional parameters.

        :param by: Type of locator (ie. CSS, ClassName, etc)
        :param locator: element locator
        :param params: (optional) locator parameters
        :return: tuple of by and locator with optional parameters
        """
        from selenium.webdriver.common.by import By

        if params is not None and not isinstance(params, dict):
            raise TypeError("<params> need to be of type <dict>, was <{}>".format(params.__class__.__name__))

        return getattr(By, by), locator.format(**(params or {}))
