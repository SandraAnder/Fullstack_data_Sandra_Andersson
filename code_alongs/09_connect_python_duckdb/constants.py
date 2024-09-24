from pathlib import Path


# databas skapas i samma mapp (.parent)
DATABASE_PATH = Path(__file__).parent / "goteborg_stad.db"
DATA_PATH = Path(__file__).parents[2] / "data"
