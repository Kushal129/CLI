import os
from colorama import Fore, Style, init

def help():
        
    # Initialize colorama
    init(autoreset=True)

    def display_options():
        print(f"{Fore.CYAN}{Style.BRIGHT}Choose an option:")
        print(f"{Fore.YELLOW}1. {Fore.GREEN}Information Gathering")
        print(f"{Fore.YELLOW}2. {Fore.GREEN}Web Search [Footprinting]")
        print(f"{Fore.YELLOW}3. {Fore.GREEN}Email Footprinting")
        print(f"{Fore.YELLOW}4. {Fore.GREEN}Networking Attacks")
        print(f"{Fore.RED}99. {Fore.GREEN}Exit")

    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_info_gather():
        print(f"{Fore.BLUE}{Style.BRIGHT}Information Gathering... TOOLS & WEB")
        print(f"{Fore.YELLOW}    Website FTP Search Engine: {Fore.WHITE}https://www.searchftps.net/")
        print(f"{Fore.YELLOW}    Website IOT Search Engine: {Fore.WHITE}https://www.shodan.io/")
        print(f"{Fore.YELLOW}    Website: {Fore.WHITE}https://centralops.net/co/")
        print(f"{Fore.WHITE}    ----------------------------------------------------------------------")
        print(f"{Fore.YELLOW}    Tool: nmap {Fore.WHITE}nmap")
        print(f"{Fore.YELLOW}    Tool: dmitry {Fore.WHITE}dmitry")

    def show_websearch_info():
        print(f"{Fore.CYAN}{'='*100}")
        print(f"{Fore.BLUE}{Style.BRIGHT}                                   Web Search - Footprinting")
        print(f"{Fore.CYAN}{'='*100}")
        print(f"{Fore.YELLOW}                   We have Multiple Options ")
        print(f"{Fore.GREEN}{'-'*70}")
        print(f"{Fore.GREEN}| {Fore.RED}Ping: {Fore.WHITE}cmd")
        print(f"{Fore.GREEN}{'-'*70}")

        print(f"{Fore.GREEN}| {Fore.RED}Sub-domains: {Fore.WHITE}https://sitereport.netcraft.com/")
        print(f"{Fore.GREEN}{'-'*70}")

        print(f"{Fore.GREEN}| {Fore.RED}Photon = tool: {Fore.WHITE}sudo python3 Photon -u url")
        print(f"{Fore.GREEN}|                 {Fore.WHITE}- Its create a Directory Open it. It has files inside of it with links.")
        print(f"{Fore.GREEN}|                 {Fore.WHITE}- Multiple options available")
        print(f"{Fore.GREEN}|  {Fore.YELLOW}~ Explanation: {Fore.WHITE}sudo python3 Photon -u url -l [level] -t [threads] --wayback")
        print(f"{Fore.GREEN}|  {Fore.YELLOW}~ Example:     {Fore.WHITE}sudo python3 photon.py -u http://ex.com -l 3 -t 200 --wayback")
        print(f"{Fore.GREEN}{'-'*70}")

        print(f"{Fore.GREEN}| {Fore.RED}theHarvester = tool: {Fore.WHITE}sudo theHarvester -d example.com -l 200 -b google")
        print(f"{Fore.GREEN}|   {Fore.YELLOW}~ Explanation:   {Fore.WHITE}sudo theHarvester -d [url] -l [results] -b [data source]")
        print(f"{Fore.GREEN}|   {Fore.YELLOW}~ Data Sources:  {Fore.WHITE}Baidu, bing, binaryedge, censys, google, linkedin, twitter, virustotal, thereatcrowd, crtsh, netcraft, yahoo")
        print(f"{Fore.GREEN}{'-'*70}")

    def email_footprinting():
        print(f"{Fore.CYAN}{Style.BRIGHT}Email Footprinting... TOOLS in Windows")
        print(f"{Fore.YELLOW}    - eMailTrackerPro")

    def Networking_Attacks():
        print(f"{Fore.GREEN}{Style.BRIGHT}Networking Attacks... TOOLS in Linux")
        print(f"{Fore.YELLOW}    - ARP Spoofing [ sudo python3 kickthemout.py ]")
        print(f"{Fore.YELLOW}    - ")






    # ================================================================================================================
    def main():
        while True:
            clear_console()
            display_options()

            option = input(f"\n{Fore.CYAN}{Style.BRIGHT}Enter Your Choice: {Fore.WHITE}")

            if option == '1':
                print(f"{Fore.CYAN}{'-'*90}")
                show_info_gather()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '2':
                print(f"{Fore.CYAN}{'-'*90}")
                show_websearch_info()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '3':
                print(f"{Fore.CYAN}{'-'*90}")
                email_footprinting()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                
            elif option == '4':
                print(f"{Fore.CYAN}{'-'*90}")
                Networking_Attacks()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '99':
                print(f"{Fore.RED}{Style.BRIGHT}Exiting the program. Goodbye!")
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.")

            input(f"\n{Fore.GREEN}Press Enter to return to the main menu...")

    if __name__ == "__main__":
        main()