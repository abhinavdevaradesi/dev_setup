import os
import shutil
import subprocess
import zipfile

import requests

DOWNLOAD_DIR = "downloads"

GCC_URL = (
    "https://github.com/brechtsanders/winlibs_mingw/releases/latest/download/"
    "winlibs-x86_64-posix-seh-gcc.zip"
)

ZIP_NAME = os.path.join(DOWNLOAD_DIR, "gcc.zip")
INSTALL_DIR = os.path.join(
    os.environ["USERPROFILE"],
    "DevSetup",
    "gcc"
)


class GCCInstaller:

    @staticmethod
    def is_installed():
        return shutil.which("gcc") is not None

    @staticmethod
    def download():
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)

        print("[+] Downloading GCC...")

        response = requests.get(GCC_URL, stream=True)
        response.raise_for_status()

        with open(ZIP_NAME, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print("[✓] Download complete")

    @staticmethod
    def extract():
        print("[+] Extracting GCC...")

        os.makedirs(INSTALL_DIR, exist_ok=True)

        with zipfile.ZipFile(ZIP_NAME, "r") as zip_ref:
            zip_ref.extractall(INSTALL_DIR)

        print("[✓] Extraction complete")

    @staticmethod
    def find_bin_folder():
        for root, dirs, files in os.walk(INSTALL_DIR):
            if "gcc.exe" in files:
                return root

        return None

    @staticmethod
    def add_to_path(path):
        print("[+] Adding GCC to PATH...")

        subprocess.run(
            f'setx PATH "%PATH%;{path}"',
            shell=True,
            check=True
        )

        print("[✓] PATH updated")

    @staticmethod
    def verify():
        try:
            result = subprocess.run(
                ["gcc", "--version"],
                capture_output=True,
                text=True
            )

            return result.returncode == 0

        except Exception:
            return False

    @classmethod
    def setup(cls):

        if cls.is_installed():
            print("[✓] GCC already installed")
            return

        cls.download()
        cls.extract()

        bin_path = cls.find_bin_folder()

        if not bin_path:
            raise Exception("gcc.exe not found")

        cls.add_to_path(bin_path)

        print("\n[!] Open a new terminal after installation.\n")

        print("[✓] GCC installation finished")