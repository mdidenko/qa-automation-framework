from selenium.common.exceptions import TimeoutException
from ..webdriver import WebDriver
from .ui_wait import UiWait


class Alert:
    """Class for alerts."""
    __slots__ = ()

    @staticmethod
    def is_present(max_timeout: int) -> bool:
        """Method to check that alert is present."""
        try:
            UiWait(max_timeout).alert_is_present()
        except TimeoutException:
            return False
        return True

    @staticmethod
    def get_text(max_timeout: int) -> str:
        """Method to get alert text."""
        UiWait(max_timeout).alert_is_present()
        return WebDriver.get_driver().switch_to.alert.text

    @staticmethod
    def accept(max_timeout: int) -> None:
        """Method to accept alert."""
        UiWait(max_timeout).alert_is_present()
        WebDriver.get_driver().switch_to.alert.accept()

    @staticmethod
    def dismiss(max_timeout: int) -> None:
        """Method to dismiss alert."""
        UiWait(max_timeout).alert_is_present()
        WebDriver.get_driver().switch_to.alert.dismiss()

    @staticmethod
    def input_text(text: str, max_timeout: int) -> None:
        """Method to input text in alert."""
        UiWait(max_timeout).alert_is_present()
        WebDriver.get_driver().switch_to.alert.send_keys(text)
