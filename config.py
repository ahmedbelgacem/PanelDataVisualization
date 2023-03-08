import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).parent
DATA_PATH = os.getenv('DATA_PATH')

DF_COLUMNS = ['Gender', 'Race/Ethnicity', 'Parental level education', 'Lunch', 'Test prep. course',
              'Math score (%)', 'Reading score (%)', 'Writing score (%)', 'Total score (%)']
SUMMARY_INDEX = ['math score', 'reading score', 'writing score', 'total score (%)']
SUMMARY_COLUMNS = ['Min. score', 'Avg. score', 'Q3', 'Max. score']