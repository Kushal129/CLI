import os
import subprocess
from colorama import Fore, Style

def run_fullAnonymous():
    # Check for root/sudo privileges
    if os.geteuid() != 0:
        print(f"{Fore.RED}This script must be run with sudo privileges.{Style.RESET_ALL}")
        return

    choice = input(
        f"{Fore.GREEN}Do you want to execute the script? Enter (1) or show the steps? Enter (2): {Style.RESET_ALL}"
    )
    if choice == "1":
        print("Using AnonGT...")

        # Define the path to the AnonGT directory
        anon_gt_dir = "AnonGT"

        # Step 1: Check if AnonGT is installed
        if not os.path.exists(anon_gt_dir):
            print("AnonGT is not installed. Cloning the repository...")
            try:
                # Clone the repository
                subprocess.run(
                    ["git", "clone", "https://github.com/gt0day/AnonGT.git"], check=True
                )
            except subprocess.CalledProcessError as e:
                print(f"Error cloning the repository: {e}")
                return

        # Step 2: Check if the AnonGT directory is writable
        if not os.access(anon_gt_dir, os.W_OK):
            print("Setting permissions for AnonGT...")
            try:
                subprocess.run(["chmod", "-R", "755", anon_gt_dir], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error setting permissions: {e}")
                return

        # Step 3: Run the installation script
        install_script = os.path.join(anon_gt_dir, "install.sh")
        if os.path.isfile(install_script):
            print("Installation script found. Proceeding with installation...")
            try:
                # Ask user for confirmation
                response = (
                    input("Do you want to run the installation script? (y/n): ")
                    .strip()
                    .lower()
                )
                if response in ["y", "yes"]:
                    # Run the installation script
                    subprocess.run(["sudo", "bash", install_script], check=True)
                    print("Installation completed successfully.")
                else:
                    print("Installation canceled.")
                    return
            except subprocess.CalledProcessError as e:
                print(f"Error running the installation script: {e}")
                return
        else:
            print("Installation script not found in the AnonGT directory.")
            return

        # Step 4: Run the AnonGT command to show all commands
        print("Running AnonGT to show all commands...")
        try:
            # Run AnonGT command
            result = subprocess.run(
                ["sudo", "AnonGT", "cmd"], capture_output=True, text=True, check=True
            )
            print("Available commands in AnonGT:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running AnonGT command: {e}")

    elif choice == "2":
        print(
            f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}"
        )
        print(
            f"        {Fore.YELLOW}Showing the steps to set up AnonGT: {Style.RESET_ALL}"
        )
        print(f"{Fore.RED}NOTE: You are in Super User mode. {Style.RESET_ALL}")
        print(
            f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}"
        )
        print(f"{Fore.GREEN}S-1.{Style.RESET_ALL} If AnonGT is not installed?")
        print(
            f"  {Fore.BLUE}git clone https://github.com/gt0day/AnonGT.git {Style.RESET_ALL}"
        )
        print("")
        print(
            f"{Fore.GREEN}S-2.{Style.RESET_ALL} Go to the AnonGT folder and run: sudo bash install.sh"
        )
        print("")
        print("- After successful installation, you can use AnonGT.")
        print(f"- Default help menu: {Fore.LIGHTCYAN_EX} sudo anongt {Style.RESET_ALL}")
        print(
            f"     Example: {Fore.LIGHTCYAN_EX} sudo anongt start {Style.RESET_ALL} or {Fore.LIGHTCYAN_EX} sudo anongt stop {Style.RESET_ALL}"
        )
        print("")
        print(
            f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}"
        )
    else:
        print("Invalid choice. Please enter 1 or 2.")