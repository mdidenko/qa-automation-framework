from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from ....common.browser_name import BrowserName
from ....common.exceptions import UnknownBrowserNameError
from .base import BaseWebDriver


class WebDriverFactory:
    """Class for web driver factory."""
    __slots__ = ()

    @staticmethod
    def get_browser(name: str, options=None) -> BaseWebDriver:
        """Method to get driver for required browser."""
        if name == BrowserName.Chrome:
            chrome_manager = ChromeDriverManager().install()
            chrome_service = ChromeService(chrome_manager)
            chrome_driver = webdriver.Chrome(
                service=chrome_service, options=options
            )
            return BaseWebDriver(chrome_driver)

        elif name == BrowserName.Firefox:
            gecko_manager = GeckoDriverManager().install()
            firefox_service = FirefoxService(gecko_manager)
            firefox_driver = webdriver.Firefox(
                service=firefox_service, options=options
            )
            return BaseWebDriver(firefox_driver)

        else:
            raise UnknownBrowserNameError(name)

    @staticmethod
    def get_chrome_options(
            lang_locale: str = None,
            window_size: tuple = None,
            download_directory: str = None
    ) -> ChromeOptions:
        """Method to set chrome options."""
        chrome_options = ChromeOptions()

        if lang_locale:
            chrome_options.add_argument(f"--lang={lang_locale}")

        if window_size:
            chrome_options.add_argument(
                f"--window-size={window_size[0]},{window_size[1]}"
            )

        if download_directory:
            chrome_options.add_experimental_option(
                "prefs",
                {
                    "download": {
                        "default_directory": download_directory,
                        "prompt_for_download": False,
                        "directory_upgrade": True
                    }
                }
            )

        return chrome_options

    @staticmethod
    def get_firefox_options(
            lang_locale: str = None,
            window_size: tuple = None,
            download_directory: str = None
    ) -> FirefoxOptions:
        """Method to set firefox options."""
        firefox_options = FirefoxOptions()

        if lang_locale:
            firefox_options.set_preference(
                "intl.accept_languages", lang_locale
            )

        if window_size:
            firefox_options.add_argument(
                f"--width={window_size[0]}"
            )
            firefox_options.add_argument(
                f"--height={window_size[1]}"
            )

        if download_directory:
            firefox_options.set_preference(
                "browser.download.folderList", 2
            )
            firefox_options.set_preference(
                'browser.download.dir', download_directory
            )
            firefox_options.set_preference(
                "browser.helperApps.alwaysAsk.force", False
            )
            firefox_options.set_preference(
                "browser.download.manager.showWhenStarting", False
            )

        return firefox_options
