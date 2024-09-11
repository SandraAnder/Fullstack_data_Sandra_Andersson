import subprocess
from pathlib import Path

if __name__ == "__main__":
    dashboard_path = Path(__file__).parent / "dashboard.py"
    subprocess.run(["streamlit", "run", str(dashboard_path)], shell=True)
