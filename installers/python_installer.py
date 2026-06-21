import subprocess

from installers.logger import get_logger


class PythonInstaller:

    @staticmethod
    def setup():
        PythonInstaller._install_python()

    @staticmethod
    def _is_python_installed():
        try:
            subprocess.run(
                ["python", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except Exception:
            return False

    @staticmethod
    def _install_python():
        if PythonInstaller._is_python_installed():
            print("✓ Python is already installed")
            return

        print("Installing Python...")
        get_logger().info("Installing Python")

        try:
            subprocess.run(
                [
                    "winget",
                    "install",
                    "-e",
                    "--id",
                    "Python.Python.3.13"
                ],
                check=True
            )

            print("✓ Python installed successfully")
            get_logger().info("Python installed successfully")

        except subprocess.CalledProcessError:
            print("✗ Failed to install Python")
            get_logger().error("Failed to install Python")