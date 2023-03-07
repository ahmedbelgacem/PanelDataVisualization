import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

ROOT = Path(__file__).parent
DATA_PATH = os.getenv('DATA_PATH')