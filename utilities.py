import subprocess
import sys


def install_dep():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
