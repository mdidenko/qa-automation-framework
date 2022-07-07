from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exc
from ..webdriver import WebDriver


class UiWait:
    """Class for working with user interface waits."""
    __slots__ = ("__max_timeout",)

    def __init__(self, max_timeout: int):
        self.__max_timeout = max_timeout

    def get_explicit(self) -> WebDriverWait:
        """Method to get explicit wait instance."""
        return WebDriverWait(WebDriver.get_driver(), self.__max_timeout)

    def presence_of_element_located(self, locator: tuple) -> WebElement:
        """Method for "presence_of_element_located" condition wait."""
        return self.get_explicit().until(
            exc.presence_of_element_located(locator)
        )

    def presence_all_elements_located(self, locator: tuple) -> list:
        """Method for "presence_all_elements_located" condition wait."""
        return self.get_explicit().until(
            exc.presence_of_all_elements_located(locator)
        )

    def visibility_of_element_located(self, locator: tuple) -> WebElement:
        """Method for "visibility_of_element_located" condition wait."""
        return self.get_explicit().until(
            exc.visibility_of_element_located(locator)
        )

    def element_to_be_clickable(self, locator: tuple) -> WebElement:
        """Method for "element_to_be_clickable" condition wait."""
        return self.get_explicit().until(exc.element_to_be_clickable(locator))

    def alert_is_present(self) -> None:
        """Method for "alert_is_present" condition wait."""
        self.get_explicit().until(
            exc.alert_is_present(), "Alert isn't present!"
        )

    def iframe_to_be_available(self, locator: tuple) -> None:
        """
        Method for "frame_to_be_available_and_switch_to_it" condition wait.
        """
        self.get_explicit().until(
            exc.frame_to_be_available_and_switch_to_it(locator),
            "Frame isn't available!"
        )
