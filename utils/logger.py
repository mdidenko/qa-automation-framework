import logging
import datetime
from importlib import reload


class LoggerUtils:
    """Class for working with logger."""
    __slots__ = ()

    @staticmethod
    def configure_logger(
            file_path: str,
            file_mode: str,
            level: int,
            message_format: str,
            datetime_format: str
    ) -> None:
        """Method to config logger."""
        reload(logging)
        logging.basicConfig(
            filename=file_path,
            filemode=file_mode,
            level=level,
            format=message_format,
            datefmt=datetime_format
        )

    @staticmethod
    def log_test(test_name: str) -> None:
        """Method to log new test."""
        logging.info(
            f"START TEST NAMED \"{test_name}\" at "
            f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M')}..."
        )

    @staticmethod
    def log_test_case(case_name: str) -> None:
        """Method to log new test case."""
        logging.info(f"** Start test case named \"{case_name}\"...")

    @staticmethod
    def log_test_step(step_name: str) -> None:
        """Method to log new case step."""
        logging.info(f"---- Start test step named \"{step_name}\"...")

    @staticmethod
    def log_element_action(action_name: str, element_name: str) -> None:
        """Method to log new element action."""
        logging.info(f"-------- {action_name} \"{element_name}\" element...")
