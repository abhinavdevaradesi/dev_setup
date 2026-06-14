from installers.gcc_installer import GCCInstaller
from installers.vscode_installer import VSCodeInstaller


def main():
    print("=== Dev Setup ===\n")

    GCCInstaller.setup()
    print()

    VSCodeInstaller.setup()

    print("\nSetup Complete!")


if __name__ == "__main__":
    main()