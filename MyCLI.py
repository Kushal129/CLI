import sys
import subprocess
import os
import time
import requests
import signal
import logging
from colorama import init, Fore, Style

# Define color codes
WHITE = "\033[0;37m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
BYELLOW = "\033[1;33m"
YELLOW = "\033[0;33m"

HYPERLINK = "\033]8;;{url}\033\\{text}\033]8;;\033\\"

init()

def display_welcome_message():
    print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Welcome to the Cybersecurity Command Tool [KP].{Style.RESET_ALL}")
    print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Available commands:{Style.RESET_ALL}")
    print(f"    {Fore.GREEN}iam{Style.RESET_ALL} - Developer Intro")
    print(f"    {Fore.GREEN}showcmd{Style.RESET_ALL} - Show all available commands")
    print(f"    {Fore.GREEN}exit{Style.RESET_ALL} - Exit the tool")
    print(f"{Fore.YELLOW}Type a command and press Enter:{Style.RESET_ALL}")

def show_all_commands():
    print(f"  {Fore.GREEN}1: wifi{Style.RESET_ALL}   - Show Wi-Fi related commands")
    print(f"  {Fore.GREEN}2: subdomainfinder{Style.RESET_ALL}   - Sub-Domain Finder")
    print(f"  {Fore.GREEN}exit{Style.RESET_ALL}   - Exit the tool")

def show_wifi_commands():
    print(f"  {Fore.RED} If Use This You Requires SUPER USER ")
    print(f"  {Fore.GREEN}wifi_jammer{Style.RESET_ALL}   - Wifi Jammer ")
    print(f"  {Fore.GREEN}fullano{Style.RESET_ALL} - Complete Anonymous ")
    print(f"  {Fore.GREEN}exit{Style.RESET_ALL}   - Exit the tool")

def process_command(cmd):
    cmd = cmd.lower()
    
    if cmd == 'iam':
        intro_text = f"""
    {Fore.CYAN}Hi, I'm Kushal Pipalya, a {Fore.GREEN}cybersecurity enthusiast{Fore.CYAN} and {Fore.YELLOW}developer.{Style.RESET_ALL}
    {Fore.CYAN}I specialize in creating {Fore.MAGENTA}command-line tools{Fore.CYAN} and exploring {Fore.RED}cybersecurity concepts.{Style.RESET_ALL}
    {Fore.CYAN}Feel free to ask me about various tools and techniques.{Style.RESET_ALL}
        """
        typing_speed = 0.05

        os.system('cls' if os.name == 'nt' else 'clear')

        for char in intro_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed)
        print()
        
    elif cmd == 'showcmd':
        show_all_commands()
        print('-----------------------------------------------------')
        
    elif cmd in ['1', 'wifi']:
        show_wifi_commands()
        print('-----------------------------------------------------')
        
    elif cmd == 'wifi_jammer':
        print(f"  {Fore.LIGHTMAGENTA_EX} Running Wi-Fi jammer script...! {Style.RESET_ALL}")
        run_wifi_jammer()
        
    elif cmd in ['2', 'subdomainfinder']:
        print(f"  {Fore.LIGHTMAGENTA_EX} Running Sub Domain Finder...! {Style.RESET_ALL}")
        subdomainfinder()
        
    elif cmd == 'fullano':
        print(f"  {Fore.LIGHTMAGENTA_EX} Running Full Anonymous setup...! {Style.RESET_ALL}")
        run_fullAnonymous()

    elif cmd in ['clear', 'clr']:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif cmd in ['exit', 'quit']:
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Thank you for using the Cybersecurity Command Tool!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Kushal Pipalya | {Fore.BLUE}https://github.com/Kushal129/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        sys.exit()
    else:
        print(f"  {Fore.RED} Unknown command try again..! {Style.RESET_ALL}")

def run_wifi_jammer():
    try:
        def check_and_install_mdk3():
            print("Checking for mdk3...")
            result = subprocess.run(['command', '-v', 'mdk3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if result.returncode != 0:
                print('mdk3 is not installed.')
                install = input('Do you want to install mdk3? (yes/no): ').strip().lower()
                if install in ['yes', 'y']:
                    print('Updating and upgrading system...')
                    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                    subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], check=True)
                    print('Installing mdk3...')
                    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mdk3'], check=True)
                    # Check the installed version
                    result = subprocess.run(['mdk3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if result.returncode == 0:
                        print(f"mdk3 version: {result.stdout.decode().strip()}")
                    else:
                        print("Failed to check mdk3 version.")
                else:
                    print("Exiting as mdk3 is required.")
                    sys.exit(1)
            else:
                print('mdk3 is already installed.')

        def get_network_interface():
        
            print('Displaying network interfaces...')
            subprocess.run(['ifconfig'], check=True)
            
            interface = input('Enter the network interface to use (e.g., wlan0): ').strip()
            # Basic validation for interface name
            if not interface:
                print("Invalid interface name.")
                sys.exit(1)
            return interface

        def run_wifi_tools(interface):
            
            # Start airmon-ng
            print(f'Starting airmon-ng on {interface}...')
            subprocess.run(['sudo', 'airmon-ng', 'start', interface], check=True)

            # Display updated network interfaces
            print('Displaying updated network interfaces...')
            subprocess.run(['ifconfig'], check=True)
            
            # Start airodump-ng
            print(f'Starting airodump-ng on {interface}...')
            subprocess.Popen(['sudo', 'airodump-ng', interface])

        def handle_blacklist_whitelist():
            while True:
                # Remove file if it already exists
                if subprocess.run(['test', '-f', 'e.lst'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
                    subprocess.run(['rm', 'e.lst'])
                
                # Prompt user for MAC address
                macid = input('Enter a MAC address: ').strip()
                if not macid:
                    print("Invalid MAC address.")
                    continue
                
                # Convert MAC address to uppercase
                macid = macid.upper()
                
                # Create a new file with the MAC address
                with open('e.lst', 'w') as file:
                    file.write(macid + '\n')
                
                # Run mdk3 with the provided options
                print('Starting mdk3 with the provided options...')
                subprocess.run(['sudo', 'mdk3', 'wlan0', 'd', '-c', '1', '-b', 'e.lst'], check=True)
                
                cont = input('Do you want to enter another MAC address? (yes/no): ').strip().lower()
                if cont not in ['yes', 'y']:
                    break

        def runw():
            try:
                check_and_install_mdk3()
                interface = get_network_interface()
                run_wifi_tools(interface)
                handle_blacklist_whitelist()
            except subprocess.CalledProcessError as e:
                print(f"Error running Wi-Fi tool commands: {e}")

    except subprocess.CalledProcessError as e:
        print(f"Error running Wi-Fi jammer script: {e}")

def run_fullAnonymous():
    choice = input('Do you want to execute the script? Enter (1) or show the steps? Enter (2): ')
    if choice == '1':
        print('Using AnonGT...')

        # Define the path to the AnonGT directory
        anon_gt_dir = 'AnonGT'

        # Step 1: Check if AnonGT is installed
        if not os.path.exists(anon_gt_dir):
            print('AnonGT is not installed. Cloning the repository...')
            try:
                # Clone the repository
                subprocess.run(['git', 'clone', 'https://github.com/gt0day/AnonGT.git'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error cloning the repository: {e}")
                return

        # Step 2: Check if the AnonGT directory is writable
        if not os.access(anon_gt_dir, os.W_OK):
            print('Setting permissions for AnonGT...')
            try:
                subprocess.run(['chmod', '-R', '755', anon_gt_dir], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error setting permissions: {e}")
                return

        # Step 3: Run the installation script
        install_script = os.path.join(anon_gt_dir, 'install.sh')
        if os.path.isfile(install_script):
            print('Installation script found. Proceeding with installation...')
            try:
                # Ask user for confirmation
                response = input('Do you want to run the installation script? (y/n): ').strip().lower()
                if response in ['y', 'yes']:
                    # Run the installation script
                    subprocess.run(['sudo', 'bash', install_script], check=True)
                    print('Installation completed successfully.')
                else:
                    print('Installation canceled.')
                    return
            except subprocess.CalledProcessError as e:
                print(f"Error running the installation script: {e}")
                return
        else:
            print('Installation script not found in the AnonGT directory.')
            return

        # Step 4: Run the AnonGT command to show all commands
        print('Running AnonGT to show all commands...')
        try:
            # Run AnonGT command
            result = subprocess.run(['sudo', 'AnonGT', 'cmd'], capture_output=True, text=True, check=True)
            print('Available commands in AnonGT:')
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running AnonGT command: {e}")

    elif choice == '2':
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"        {Fore.YELLOW}Showing the steps to set up AnonGT: {Style.RESET_ALL}")
        print(f"{Fore.RED}NOTE: You are in Super User mode. {Style.RESET_ALL}")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.GREEN}S-1.{Style.RESET_ALL} If AnonGT is not installed?")
        print(f"  {Fore.BLUE}git clone https://github.com/gt0day/AnonGT.git {Style.RESET_ALL}")
        print("")
        print(f"{Fore.GREEN}S-2.{Style.RESET_ALL} Go to the AnonGT folder and run: sudo bash install.sh")
        print("")
        print("- After successful installation, you can use AnonGT.")
        print(f"- Default help menu: {Fore.LIGHTCYAN_EX} sudo anongt {Style.RESET_ALL}")
        print(f"     Example: {Fore.LIGHTCYAN_EX} sudo anongt start {Style.RESET_ALL} or {Fore.LIGHTCYAN_EX} sudo anongt stop {Style.RESET_ALL}")
        print("")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
    else:
        print('Invalid choice. Please enter 1 or 2.')
        
def subdomainfinder():
    
    DEFAULT_SUBDOMAINS_URL = "https://github.com/Kushal129/Sub-Domain-Finder/raw/main/Subdomain.txt"

    # Setup logging
    logging.basicConfig(filename="subdomain_finder.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

    # Signal handler for graceful exit
    def signal_handler(sig, frame):
        print(f"\n{YELLOW}[!] Interrupted! Exiting gracefully.{RESET}")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    def request(url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        try:
            result = requests.get(url, headers=headers, timeout=5)
            if result.status_code == 200:
                output = (
                    f"{GREEN}[+] Subdomain discovered!\n"
                    f"{'-' * 50}\n"
                    f"{BLUE}🔗 URL: {HYPERLINK.format(url=url, text=url)}\n"
                    f"{GREEN}{'-' * 50}{RESET}\n"
                )
                print(output)
                logging.info(f"Subdomain discovered: {url}")
            else:
                print(f"{RED}[-] Non-200 status code for ----> {url}{RESET}")
                logging.info(f"Non-200 status code for {url}")
        except requests.ConnectionError:
            print(f"{RED}[-] Connection Error for ----> {url}{RESET}")
            logging.error(f"Connection Error for {url}")
        except requests.Timeout:
            print(f"{RED}[-] Timeout Error for ----> {url}{RESET}")
            logging.error(f"Timeout Error for {url}")
        except requests.RequestException:
            print(f"{RED}[-] Failed to request ----> {url}{RESET}")
            logging.error(f"Failed to request {url}")

    def intro():
        border = "*" * 55
        title = "SubDomain Finder Tool"
        subtitle = "GitHub: www.github.com/Kushal129/"
        
        # ASCII Art for KHP Logo (Text Representation)
        khp_logo = """
        
            /$$   /$$ /$$   /$$ /$$$$$$$ 
            | $$  /$$/| $$  | $$| $$__  $$
            | $$ /$$/ | $$  | $$| $$  \ $$
            | $$$$$/  | $$$$$$$$| $$$$$$$/
            | $$  $$  | $$__  $$| $$____/ 
            | $$\  $$ | $$  | $$| $$      
            | $$ \  $$| $$  | $$| $$      
            |__/  \__/|__/  |__/|__/  
            
        """

        # Centering the title and subtitle
        khp_logo = f"{' ' * ((50 - len(khp_logo)) // 2)}{khp_logo}"
        title_line = f"{' ' * ((50 - len(title)) // 2)}{title}"
        subtitle_line = f"{' ' * ((50 - len(subtitle)) // 2)}{subtitle}"

        # Printing the intro
        print(f"\n{GREEN}{border}{RESET}")
        print(f"{PURPLE}{khp_logo}{RESET}")
        print(f"{BYELLOW}{title_line}{RESET}")
        print(f"{BYELLOW}{subtitle_line}{RESET}")
        print(f"{GREEN}{border}{RESET}\n")
        
    def download_default_subdomains_file(file_path):
        try:
            response = requests.get(DEFAULT_SUBDOMAINS_URL)
            response.raise_for_status()  # Raise an exception for HTTP errors
            with open(file_path, "w") as file:
                file.write(response.text)
            print(f"{GREEN}[+] Default subdomains file downloaded and saved to {file_path}{RESET}")
        except requests.RequestException as e:
            print(f"{RED}[-] Failed to download default subdomains file: {e}{RESET}")
            sys.exit(1)

    def run():
        intro()
        try:
            target_url = input("Enter Target URL (e.g., example.com): ").strip()
            if not target_url:
                print(f"{RED}[-] No target URL provided.{RESET}")
                sys.exit(1)

            # Set default subdomains file path
            subdomains_file = "default_subdomains.txt"

            # Check if the default subdomains file already exists
            if os.path.isfile(subdomains_file):
                print(f"{GREEN}Using existing subdomains file: '{subdomains_file}'{RESET}")
            else:
                print(f"{YELLOW}Default subdomains file not found.{RESET}")
                # Option to choose between custom subdomains file or default file
                choice = input("Choose an option:\n1. Provide your own subdomains file\n2. Download default subdomains file\nEnter choice (1 or 2): ").strip()

                if choice == '1':
                    subdomains_file = input("Enter path to subdomains file (e.g., Subdomain.txt): ").strip()
                elif choice == '2':
                    download_default_subdomains_file(subdomains_file)
                else:
                    print(f"{YELLOW}[-] Invalid choice. Defaulting to using the default subdomains file.{RESET}")
                    download_default_subdomains_file(subdomains_file)

            # Expand user directory
            subdomains_file = os.path.expanduser(subdomains_file)
            
            if not os.path.isfile(subdomains_file):
                print(f"{RED}[-] The file '{subdomains_file}' does not exist.{RESET}")
                sys.exit(1)

            print(f"Using subdomains file: '{subdomains_file}'")
            discovered_subdomains = []

            protocol = input("Choose protocol (http [Enter-1] or https [Enter-2]): ").strip()
            if protocol == '1':
                protocol = "http"
            elif protocol == '2':
                protocol = "https"
            else:
                print(f"{YELLOW}[-] Invalid choice. Defaulting to https.{RESET}")
                protocol = "https"

            with open(subdomains_file, "r") as wordlist:
                subdomains = [f"{protocol}://{line.strip()}.{target_url}" for line in wordlist]

            for index, subdomain in enumerate(subdomains, start=1):
                print(f"[*] Checking {index}/{len(subdomains)}: {subdomain}")
                request(subdomain)
            
            if discovered_subdomains:
                output_file = f"discovered_subdomains_{target_url}.txt"
                with open(output_file, "w") as f:
                    for subdomain in discovered_subdomains:
                        f.write(subdomain + "\n")
                print(f"{GREEN}[+] Discovered subdomains saved to {output_file}{RESET}")
                logging.info(f"Discovered subdomains saved to {output_file}")
            else:
                print(f"{RED}[-] No subdomains discovered.{RESET}")
                logging.info("No subdomains discovered.")

        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!] Interrupted! Exiting gracefully.{RESET}")
        except Exception as e:
            print(f"{RED}[-] An unexpected error occurred: {e}{RESET}")
        finally:
            print(f"\n{GREEN}Goodbye!{RESET}")

        if __name__ == "__main__":
            run()



def main():
    display_welcome_message()
    while True:
        user_input = input(f"{Fore.GREEN}-> {Style.RESET_ALL}")
        process_command(user_input)

if __name__ == '__main__':
    main()
