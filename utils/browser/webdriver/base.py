from selenium.webdriver.remote.webelement import WebElement


class BaseWebDriver:
    """Class for web driver."""
    __slots__ = ()
    __instance = None
    __driver = None

    def __new__(cls, driver):
        if cls.__instance is None:
            cls.__driver = driver
            cls.__instance = super(BaseWebDriver, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def get_driver(cls):
        """Method to get driver."""
        return cls.__driver

    @classmethod
    def scroll_to_element(cls, element: WebElement) -> None:
        """Method to scroll while element won't visible."""
        cls.__driver.execute_script(
            "arguments[0].scrollIntoView();", element
        )

    @classmethod
    def get_frame_page_source(cls) -> str:
        """Method to get page source from frame."""
        return cls.__driver.page_source

    @classmethod
    def get_current_window_handle(cls) -> str:
        """Method to get current window handle."""
        return cls.__driver.current_window_handle

    @classmethod
    def get_all_window_handles(cls) -> list:
        """Method to get all window handles."""
        return cls.__driver.window_handles

    @classmethod
    def switch_to_window(cls, handle: str) -> None:
        """Method to switch driver on window by handle."""
        cls.__driver.switch_to.window(handle)

    @classmethod
    def close_frame(cls) -> None:
        """Method to close frame."""
        cls.__driver.switch_to.default_content()

    @classmethod
    def close(cls):
        """Method to close current page."""
        if len(cls.get_all_window_handles()) == 1:
            cls.quit()
        else:
            cls.__driver.close()

    @classmethod
    def quit(cls) -> None:
        """Method to close driver."""
        cls.__driver.quit()
        cls.__driver = None
        cls.__instance = None
