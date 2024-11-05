import os
from colorama import Fore, Style, init

def help():
        
    # Initialize colorama
    init(autoreset=True)

    def display_options():
        print(f"{Fore.CYAN}{Style.BRIGHT}Choose an option:")
        print(f"{Fore.YELLOW}1. {Fore.GREEN}Information Gathering")
        print(f"{Fore.YELLOW}2. {Fore.GREEN}Password Cracking")
        print(f"{Fore.YELLOW}3. {Fore.GREEN}Vulnerability Scanning")
        print(f"{Fore.YELLOW}4. {Fore.GREEN}Wireless Hacking")
        print(f"{Fore.YELLOW}5. {Fore.GREEN}Exploitation")
        print(f"{Fore.YELLOW}6. {Fore.GREEN}Web Application Assessment")
        print(f"{Fore.YELLOW}7. {Fore.GREEN}Forensics")
        print(f"{Fore.RED}99. {Fore.GREEN}Exit")

    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_info_gather():
        print(f"{Fore.BLUE}{Style.BRIGHT}Information Gathering Tools")
        print(f"{Fore.YELLOW}    > Nmap: A network scanning tool")
        print(f"{Fore.YELLOW}    > Shodan: A search engine for Internet-connected devices")
        print(f"{Fore.YELLOW}    > Maltego: A data mining tool")
        print(f"{Fore.YELLOW}    > TheHarvester: A tool for gathering e-mail accounts, subdomains, hosts, employee names, open ports and banners from different public sources like search engines, PGP key servers and SHODAN computer database")
        print(f"{Fore.YELLOW}    > Recon-NG: A full-featured Web Reconnaissance framework written in Python")
        print(f"{Fore.YELLOW}    > Amass: A tool to help information security professionals perform network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques")
        print(f"{Fore.YELLOW}    > Censys: A search engine that allows computer scientists to ask questions about the devices and networks that compose the Internet")
        print(f"{Fore.YELLOW}    > OSINT Framework: A collection of various tools and resources that have been found to be useful for recon")
        print(f"{Fore.YELLOW}    > Gobuster: A tool used to brute-force: URIs (directories and files) in web sites")
        print(f"{Fore.YELLOW}    > Subfinder: A subdomain discovery tool")
        print(f"{Fore.YELLOW}    > DNSRecon: A DNS reconnaissance tool")
        print(f"{Fore.YELLOW}    > DNSDumpster: A DNS reconnaissance tool")
        print(f"{Fore.YELLOW}    > Hunter: A tool for identifying valid email addresses")

    def show_password_cracking():
        print(f"{Fore.BLUE}{Style.BRIGHT}Password Cracking Tools")
        print(f"{Fore.YELLOW}    > John The Ripper: A fast password cracker")
        print(f"{Fore.YELLOW}    > Hydra: A parallelized login cracker which supports numerous protocols to attack")
        print(f"{Fore.YELLOW}    > Hashcat: An advanced password recovery utility")
        print(f"{Fore.YELLOW}    > OPHCrack: A Windows password cracker based on rainbow tables")
        print(f"{Fore.YELLOW}    > Medusa: A speedy, massively parallel, modular, login brute-forcer for network services")
        print(f"{Fore.YELLOW}    > THC-Hydra: A very fast network logon cracker which support many different services")
        print(f"{Fore.YELLOW}    > Cain & Abel: A password recovery tool for Microsoft Operating Systems")
        print(f"{Fore.YELLOW}    > Aircrack-ng: A suite of tools to crack WEP/WPA/WPA2")
        print(f"{Fore.YELLOW}    > Wifite: An automated wireless attack tool")
        print(f"{Fore.YELLOW}    > Kismet: A wireless network detector, sniffer, and intrusion detection system")
        print(f"{Fore.YELLOW}    > TCPDump: A packet analyzer")
        print(f"{Fore.YELLOW}    > Airsnort: A wireless LAN (WLAN) tool which recovers encryption keys")
        print(f"{Fore.YELLOW}    > Netstumbler: A tool for Windows that facilitates detection of Wireless LANs using the 802.11b, 802.11a and 802.11g WLAN standards")
        print(f"{Fore.YELLOW}    > Reaver: A WPS pin generator")

    def show_vulnerability_scanning():
        print(f"{Fore.BLUE}{Style.BRIGHT}Vulnerability Scanning Tools")
        print(f"{Fore.YELLOW}    > OpenVAS: A full-featured vulnerability scanner")
        print(f"{Fore.YELLOW}    > Nessus: A proprietary comprehensive vulnerability scanner")
        print(f"{Fore.YELLOW}    > AppScan: A family of web security testing and monitoring tools")
        print(f"{Fore.YELLOW}    > LYNIS: A security auditing tool for UNIX derivatives like Linux, macOS, BSD, and others")
        print(f"{Fore.YELLOW}    > Retina: A vulnerability management tool")
        print(f"{Fore.YELLOW}    > Nexpose: A vulnerability management solution")
        print(f"{Fore.YELLOW}    > ZAP: An open-source web application security scanner")
        print(f"{Fore.YELLOW}    > Burp Suite: An integrated platform for performing security testing of web applications")
        print(f"{Fore.YELLOW}    > SQL Map: An open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws")
        print(f"{Fore.YELLOW}    > ExploitDB: An archive of public exploits and corresponding vulnerable software")
        print(f"{Fore.YELLOW}    > Core Impact: A commercial, comprehensive penetration testing product for assessing the security of network systems")
        print(f"{Fore.YELLOW}    > Cobalt Strike: A commercial, full-featured, penetration testing tool which bills itself as adversary simulation software")

    def show_wireless_hacking():
        print(f"{Fore.BLUE}{Style.BRIGHT}Wireless Hacking Tools")
        print(f"{Fore.YELLOW}    > Aircrack-NG: A complete suite of tools to assess WiFi network security")
        print(f"{Fore.YELLOW}    > Wifite: An automated wireless attack tool")
        print(f"{Fore.YELLOW}    > Kismet: A wireless network detector, sniffer, and intrusion detection system")
        print(f"{Fore.YELLOW}    > TCPDump: A packet analyzer")
        print(f"{Fore.YELLOW}    > Airsnort: A wireless LAN (WLAN) tool which recovers encryption keys")
        print(f"{Fore.YELLOW}    > Netstumbler: A tool for Windows that facilitates detection of Wireless LANs using the 802.11b, 802.11a and 802.11g WLAN standards")
        print(f"{Fore.YELLOW}    > Reaver: A WPS pin generator")
        print(f"{Fore.YELLOW}    > WPS Connect: A tool to connect to WPS enabled routers")
        print(f"{Fore.YELLOW}    > Fluxion: A tool for automating Wi-Fi hacking")
        print(f"{Fore.YELLOW}    > Wifiphisher: A tool for automating Wi-Fi hacking")

    def show_exploitation_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Exploitation Tools")
        print(f"{Fore.YELLOW}    > Burp Suite: An integrated platform for performing security testing of web applications")
        print(f"{Fore.YELLOW}    > Metasploit Framework: A tool for developing, testing, and executing exploit code against a remote target machine")
        print(f"{Fore.YELLOW}    > SQL Map: An open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws")
        print(f"{Fore.YELLOW}    > ZAP: An easy to use integrated penetration testing tool for finding vulnerabilities in web applications")
        print(f"{Fore.YELLOW}    > ExploitDB: An archive of public exploits and corresponding vulnerable software")
        print(f"{Fore.YELLOW}    > Core Impact: A commercial, comprehensive penetration testing product for assessing the security of network systems")
        print(f"{Fore.YELLOW}    > Cobalt Strike: A commercial, full-featured, penetration testing tool which bills itself as adversary simulation software")
        print(f"{Fore.YELLOW}    > BeEF: A penetration testing tool focused on the web browser")
        print(f"{Fore.YELLOW}    > SET: A tool for social engineering attacks")
        print(f"{Fore.YELLOW}    > Empire: A post-exploitation framework for Windows")

    def show_web_application_assessment():
        print(f"{Fore.BLUE}{Style.BRIGHT}Web Application Assessment Tools")
        print(f"{Fore.YELLOW}    > OWASP ZAP: An open-source web application security scanner")
        print(f"{Fore.YELLOW}    > Burp Suite: An integrated platform for performing security testing of web applications")
        print(f"{Fore.YELLOW}    > Nikto: A web server scanner which performs comprehensive tests against web servers for multiple items")
        print(f"{Fore.YELLOW}    > ZAP: An easy to use integrated penetration testing tool for finding vulnerabilities in web applications")
        print(f"{Fore.YELLOW}    > WPScan: A black box WordPress vulnerability scanner")
        print(f"{Fore.YELLOW}    > Gobuster: A tool used to brute-force: URIs (directories and files) in web sites")
        print(f"{Fore.YELLOW}    > App Spider: A web application security scanner")
        print(f"{Fore.YELLOW}    > Arachni: An open-source web application security scanner")
        print(f"{Fore.YELLOW}    > Vega: A web application security scanner")

    def show_forensics_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Forensics Tools")
        print(f"{Fore.YELLOW}    > SleuthKit: A collection of command line tools and a C library that allows you to analyze disk images and recover files from them")
        print(f"{Fore.YELLOW}    > Autopsy: A graphical interface to The Sleuth Kit and other digital forensics tools")
        print(f"{Fore.YELLOW}    > Guymager: A free forensic imager for media acquisition")
        print(f"{Fore.YELLOW}    > Foremost: A console program to recover files based on their headers, footers, and internal data structures")
        print(f"{Fore.YELLOW}    > Binwalk: A fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images")
        print(f"{Fore.YELLOW}    > Wireshark: A network protocol analyzer")
        print(f"{Fore.YELLOW}    > Volatility: A digital forensics and incident response tool")
        print(f"{Fore.YELLOW}    > Plaso: A digital forensics and incident response tool")
        print(f"{Fore.YELLOW}    > Rekall: A digital forensics and incident response tool")

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
                show_password_cracking()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '3':
                print(f"{Fore.CYAN}{'-'*90}")
                show_vulnerability_scanning()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '4':
                print(f"{Fore.CYAN}{'-'*90}")
                show_wireless_hacking()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '5':
                print(f"{Fore.CYAN}{'-'*90}")
                show_exploitation_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '6':
                print(f"{Fore.CYAN}{'-'*90}")
                show_web_application_assessment()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '7':
                print(f"{Fore.CYAN}{'-'*90}")
                show_forensics_tools()
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
