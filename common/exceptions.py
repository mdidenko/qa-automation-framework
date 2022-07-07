

class WebDriverError(Exception):
    """Exception class for WebDriver."""


class UnknownBrowserNameError(WebDriverError):
    """Raises when detect trying to get driver for unknown browser."""
