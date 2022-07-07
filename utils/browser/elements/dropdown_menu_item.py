from .dropdown_menu import DropdownMenu


class DropdownMenuItem(DropdownMenu):
    """Class for dropdown menu item elements."""

    def __init__(self, name: str, locator: tuple, default_max_timeout: int):
        super().__init__(name, locator, default_max_timeout)
