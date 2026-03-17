from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

TRAIN_PATH = DATA_DIR / "raw" / "train.csv"
TEST_PATH = DATA_DIR / "raw" / "test.csv"

PROCESSED_TRAIN_PATH = DATA_DIR / "processed" / "train_processed.csv"
PROCESSED_TEST_PATH = DATA_DIR / "processed" / "test_processed.csv"
