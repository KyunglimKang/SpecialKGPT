from autogpt.commands.command import command

from datetime import datetime

@command("get_datetime", "Get current datetime")
def get_datetime() -> str:
    """Return the current date and time

    Returns:
        str: The current date and time
    """
    return "Current date and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
