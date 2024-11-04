import subprocess
import sys
import os
import time
import requests
import signal
import logging
from colorama import init, Fore, Style
from Functions import run_fullAnonymous, run_wifi_jammer, subdomainfinder

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

# Initialize colorama
init(autoreset=True)

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
    print(f"  {Fore.GREEN}3: fullano{Style.RESET_ALL} - Complete Anonymous ")
    print(f"  {Fore.GREEN}exit{Style.RESET_ALL}   - Exit the tool")

def show_wifi_commands():
    print(f"  {Fore.RED}If Use This You Requires SUPER USER{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}w1: wifi_jammer{Style.RESET_ALL}   - Wifi Jammer ")
    print(f"  {Fore.GREEN}w2: wifi{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}exit{Style.RESET_ALL}   - Exit the tool")

def process_command(cmd):
    cmd = cmd.lower()

    if cmd == "iam":
        os.system("cls" if os.name == "nt" else "clear")
        
        def create_responsive_box(content):
            # Get terminal width
            terminal_width = os.get_terminal_size().columns
            
            # Calculate box width (80% of terminal width)
            box_width = min(int(terminal_width * 0.8), 80)  # max width of 80 chars
            
            # Create decorative borders
            top_border = f"{Fore.CYAN}╔{'═' * (box_width-2)}╗{Style.RESET_ALL}"
            bottom_border = f"{Fore.CYAN}╚{'═' * (box_width-2)}╝{Style.RESET_ALL}"
            empty_line = f"{Fore.CYAN}║{' ' * (box_width-2)}║{Style.RESET_ALL}"
            
            # Print top decoration
            print(f"{Fore.CYAN}{'═' * box_width}{Style.RESET_ALL}")
            print(top_border)
            print(empty_line)
            
            # Print content
            for color, text in content:
                # Word wrap for long lines
                words = text.split()
                current_line = []
                current_length = 0
                
                for word in words:
                    if current_length + len(word) + 1 <= box_width - 6:  # -6 for margins and decorations
                        current_line.append(word)
                        current_length += len(word) + 1
                    else:
                        # Print current line
                        if current_line:
                            line_text = ' '.join(current_line)
                            padding = box_width - len(line_text) - 4
                            print(f"{Fore.CYAN}║{Style.RESET_ALL} {color}{line_text}{' ' * padding}{Fore.CYAN}║{Style.RESET_ALL}")
                        current_line = [word]
                        current_length = len(word)
                
                # Print remaining words
                if current_line:
                    line_text = ' '.join(current_line)
                    padding = box_width - len(line_text) - 4
                    print(f"{Fore.CYAN}║{Style.RESET_ALL} {color}{line_text}{' ' * padding}{Fore.CYAN}║{Style.RESET_ALL}")
                print(empty_line)
            
            # Print bottom decoration
            print(bottom_border)
            print(f"{Fore.CYAN}{'═' * box_width}{Style.RESET_ALL}")

        # Content with proper spacing
        content = [
            (Fore.GREEN, "Hi, I'm Kushal Pipalya!"),
            (Fore.YELLOW, "A cybersecurity enthusiast and developer."),
            (Fore.MAGENTA, "I specialize in creating command-line tools"),
            (Fore.RED, "and exploring cybersecurity concepts."),
            (Fore.BLUE, "Feel free to ask me about various tools and techniques.")
        ]

        print()
        create_responsive_box(content)
        print()

    elif cmd in ["showcmd", "ls", "show", "option"]:
        show_all_commands()
        print("-----------------------------------------------------")

    elif cmd in ["1", "wifi"]:
        show_wifi_commands()
        print("-----------------------------------------------------")

    elif cmd in ["2", "subdomainfinder"]:
        print(f"  {Fore.LIGHTMAGENTA_EX}Running Sub Domain Finder...!{Style.RESET_ALL}")
        subdomainfinder()

    elif cmd in ["3", "fullano"]:
        print(f"  {Fore.LIGHTMAGENTA_EX}Running Full Anonymous setup...!{Style.RESET_ALL}")
        run_fullAnonymous()

    elif cmd in ["w1", "wifi_jammer"]:
        print(f"  {Fore.LIGHTMAGENTA_EX}Running Wi-Fi jammer script...!{Style.RESET_ALL}")
        run_wifi_jammer()

    elif cmd in ["clear", "clr"]:
        os.system("cls" if os.name == "nt" else "clear")

    elif cmd in ["exit", "quit"]:
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Thank you for using the Cybersecurity Command Tool!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Kushal Pipalya | {Fore.BLUE}https://github.com/Kushal129/{Style.RESET_ALL}")
        print(f"{Fore.CYAN}------------------------------------------------{Style.RESET_ALL}")
        sys.exit()
    else:
        print(f"  {Fore.RED}Unknown command try again..!{Style.RESET_ALL}")

# Signal handler for SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print(f"\n{Fore.RED}Process interrupted by user (Ctrl+C). Exiting...{Style.RESET_ALL}")
    sys.exit(0)

# Register only SIGINT handler (works on both Windows and Unix)
signal.signal(signal.SIGINT, signal_handler)

def main():
    display_welcome_message()
    while True:
        try:
            user_input = input(f"{Fore.GREEN}-> {Style.RESET_ALL}")
            process_command(user_input)
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
            logging.error(f"Error in main loop: {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
