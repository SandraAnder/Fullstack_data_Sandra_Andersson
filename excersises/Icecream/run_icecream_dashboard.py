import subprocess
from pathlib import Path

if __name__ == '__main__':
    dashboard_path = Path(__file__).parents[0] / 'Icecream_prediction_dashboard.py'
    subprocess.run(f'streamlit run {dashboard_path}', shell=True)