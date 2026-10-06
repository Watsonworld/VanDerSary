"""Create the local virtual environment and install project requirements."""

from pathlib import Path
import subprocess
import sys
import venv


root = Path(__file__).resolve().parents[1]
venv_dir = root / ".venv"
python = venv_dir / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
if not python.is_file():
    venv.EnvBuilder(with_pip=True).create(venv_dir)
subprocess.run([str(python), "-m", "pip", "install", "-r", str(root / "requirements.txt")], check=True)
subprocess.run(
    [str(python), "-c", "import pandas, openpyxl, yaml, rapidfuzz, requests, dotenv"],
    check=True,
)
print(f"JCR Python environment ready: {python}")
