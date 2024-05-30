"""Configuration class to store the state of bools for different scripts access."""
import os

from colorama import Fore
from dotenv import load_dotenv

from autogpt.config.singleton import Singleton

load_dotenv(verbose=True)


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """
    def __init__(self) -> None:
        """Initialize the Config class"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_api_env = os.getenv("PINECONE_API_ENV")

def check_openai_api_key() -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    cfg = Config()
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        exit(1)
