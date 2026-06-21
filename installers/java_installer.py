import subprocess


class JavaInstaller:

    @staticmethod
    def setup():
        JavaInstaller._install_java()

    @staticmethod
    def _is_java_installed():
        try:
            subprocess.run(
                ["java", "-version"],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except Exception:
            return False

    @staticmethod
    def _install_java():
        if JavaInstaller._is_java_installed():
            print("✓ Java is already installed")
            return

        print("Installing Java...")

        try:
            subprocess.run(
                [
                    "winget",
                    "install",
                    "-e",
                    "--id",
                    "Microsoft.OpenJDK.21"
                ],
                check=True
            )

            print("✓ Java installed successfully")

        except subprocess.CalledProcessError:
            print("✗ Failed to install Java")