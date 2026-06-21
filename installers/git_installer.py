import subprocess

from installers.logger import get_logger


class GitInstaller:

    @staticmethod
    def setup():
        GitInstaller._install_git()

    @staticmethod
    def _is_git_installed():
        try:
            subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except Exception:
            return False

    @staticmethod
    def _install_git():
        if GitInstaller._is_git_installed():
            print("✓ Git is already installed")
            return

        print("Installing Git...")
        get_logger().info("Installing Git")

        try:
            subprocess.run(
                [
                    "winget",
                    "install",
                    "-e",
                    "--id",
                    "Git.Git"
                ],
                check=True
            )

            print("✓ Git installed successfully")
            get_logger().info("Git installed successfully")

        except subprocess.CalledProcessError:
            print("✗ Failed to install Git")
            get_logger().error("Failed to install Git")