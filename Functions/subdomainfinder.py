import os
import sys
import signal
import logging
import requests
from colorama import Fore, Style

# Define hyperlink format for terminal
HYPERLINK = "\033]8;;{url}\033\\{text}\033]8;;\033\\"

def subdomainfinder():
    DEFAULT_SUBDOMAINS_URL = (
        "https://github.com/Kushal129/Sub-Domain-Finder/raw/main/Subdomain.txt"
    )

    # Setup logging with a try-except block to handle permission issues
    try:
        logging.basicConfig(
            filename="subdomain_finder.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
    except PermissionError:
        print(f"{Fore.YELLOW}Warning: Could not create log file due to permissions. Logging to console only.{Style.RESET_ALL}")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    # Signal handler for graceful exit
    def signal_handler(sig, frame):
        print(f"\n{Fore.YELLOW}[!] Interrupted! Exiting gracefully.{Style.RESET_ALL}")
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
                    f"{Fore.GREEN}[+] Subdomain discovered!\n"
                    f"{'-' * 50}\n"
                    f"{Fore.BLUE}🔗 URL: {HYPERLINK.format(url=url, text=url)}\n"
                    f"{Fore.GREEN}{'-' * 50}{Style.RESET_ALL}\n"
                )
                print(output)
                logging.info(f"Subdomain discovered: {url}")
                discovered_subdomains.append(url)  # Add discovered subdomain to list
            else:
                print(f"{Fore.RED}[-] Non-200 status code for ----> {url}{Style.RESET_ALL}")
                logging.info(f"Non-200 status code for {url}")
        except requests.ConnectionError:
            print(f"{Fore.RED}[-] Connection Error for ----> {url}{Style.RESET_ALL}")
            logging.error(f"Connection Error for {url}")
        except requests.Timeout:
            print(f"{Fore.RED}[-] Timeout Error for ----> {url}{Style.RESET_ALL}")
            logging.error(f"Timeout Error for {url}")
        except requests.RequestException:
            print(f"{Fore.RED}[-] Failed to request ----> {url}{Style.RESET_ALL}")
            logging.error(f"Failed to request {url}")

    def intro():
        border = "*" * 55
        title = "SubDomain Finder Tool"
        subtitle = "GitHub: www.github.com/Kushal129/"

        khp_logo = """
        
            $$\   $$\ $$\   $$\ $$$$$$$\  
            $$ | $$  |$$ |  $$ |$$  __$$\ 
            $$ |$$  / $$ |  $$ |$$ |  $$ |
            $$$$$  /  $$$$$$$$ |$$$$$$$  |
            $$  $$<   $$  __$$ |$$  ____/ 
            $$ |\$$\  $$ |  $$ |$$ |      
            $$ | \$$\ $$ |  $$ |$$ |      
            \__|  \__|\__|  \__|\__|      
                              
        """

        # Centering the title and subtitle
        khp_logo = f"{' ' * ((50 - len(khp_logo)) // 2)}{khp_logo}"
        title_line = f"{' ' * ((50 - len(title)) // 2)}{title}"
        subtitle_line = f"{' ' * ((50 - len(subtitle)) // 2)}{subtitle}"

        # Printing the intro
        print(f"\n{Fore.GREEN}{border}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{khp_logo}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{title_line}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{subtitle_line}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{border}{Style.RESET_ALL}\n")

    def download_default_subdomains_file(file_path):
        try:
            response = requests.get(DEFAULT_SUBDOMAINS_URL)
            response.raise_for_status()  # Raise an exception for HTTP errors
            with open(file_path, "w") as file:
                file.write(response.text)
            print(
                f"{Fore.GREEN}[+] Default subdomains file downloaded and saved to {file_path}{Style.RESET_ALL}"
            )
        except requests.RequestException as e:
            print(f"{Fore.RED}[-] Failed to download default subdomains file: {e}{Style.RESET_ALL}")
            sys.exit(1)

    def run():
        intro()
        try:
            target_url = input("Enter Target URL (e.g., example.com): ").strip()
            if not target_url:
                print(f"{Fore.RED}[-] No target URL provided.{Style.RESET_ALL}")
                sys.exit(1)

            # Set default subdomains file path
            subdomains_file = "default_subdomains.txt"

            # Check if the default subdomains file already exists
            if os.path.isfile(subdomains_file):
                print(
                    f"{Fore.GREEN}Using existing subdomains file: '{subdomains_file}'{Style.RESET_ALL}"
                )
            else:
                print(f"{Fore.YELLOW}Default subdomains file not found.{Style.RESET_ALL}")
                # Option to choose between custom subdomains file or default file
                choice = input(
                    "Choose an option:\n1. Provide your own subdomains file\n2. Download default subdomains file\nEnter choice (1 or 2): "
                ).strip()

                if choice == "1":
                    subdomains_file = input(
                        "Enter path to subdomains file (e.g., Subdomain.txt): "
                    ).strip()
                elif choice == "2":
                    download_default_subdomains_file(subdomains_file)
                else:
                    print(
                        f"{Fore.YELLOW}[-] Invalid choice. Defaulting to using the default subdomains file.{Style.RESET_ALL}"
                    )
                    download_default_subdomains_file(subdomains_file)

            # Expand user directory
            subdomains_file = os.path.expanduser(subdomains_file)

            if not os.path.isfile(subdomains_file):
                print(f"{Fore.RED}[-] The file '{subdomains_file}' does not exist.{Style.RESET_ALL}")
                sys.exit(1)

            print(f"Using subdomains file: '{subdomains_file}'")
            global discovered_subdomains
            discovered_subdomains = []

            protocol = input(
                "Choose protocol (http [Enter-1] or https [Enter-2]): "
            ).strip()
            if protocol == "1":
                protocol = "http"
            elif protocol == "2":
                protocol = "https"
            else:
                print(f"{Fore.YELLOW}[-] Invalid choice. Defaulting to https.{Style.RESET_ALL}")
                protocol = "https"

            with open(subdomains_file, "r") as wordlist:
                subdomains = [
                    f"{protocol}://{line.strip()}.{target_url}" for line in wordlist
                ]

            for index, subdomain in enumerate(subdomains, start=1):
                print(f"[*] Checking {index}/{len(subdomains)}: {subdomain}")
                request(subdomain)

            if discovered_subdomains:
                output_file = f"discovered_subdomains_{target_url}.txt"
                with open(output_file, "w") as f:
                    for subdomain in discovered_subdomains:
                        f.write(subdomain + "\n")
                print(f"{Fore.GREEN}[+] Discovered subdomains saved to {output_file}{Style.RESET_ALL}")
                logging.info(f"Discovered subdomains saved to {output_file}")
            else:
                print(f"{Fore.RED}[-] No subdomains discovered.{Style.RESET_ALL}")
                logging.info("No subdomains discovered.")

        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Interrupted! Exiting gracefully.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] An unexpected error occurred: {e}{Style.RESET_ALL}")
            logging.error(f"Unexpected error: {e}")
        finally:
            print(f"\n{Fore.GREEN}Goodbye!{Style.RESET_ALL}")

    run()

if __name__ == "__main__":
    subdomainfinder()
