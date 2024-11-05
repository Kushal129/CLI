from colorama import Fore, Style, init

def display_options():
    options = [
        "Information Gathering",
        "Wireless Hacking Tools",
        "Exploitation Tools",
        "Web Application Assessment Tools",
        "Forensics Tools",
        "Network Security Tools",
        "Vulnerability Assessment Tools",
        "Penetration Testing Tools",
        "Malware Analysis Tools",
        "Endpoint Security Tools",
        "Logging and Monitoring Tools",
        "Security Information and Event Management Tools",
        "Identity and Access Management Tools",
        "Risk Management Tools",
        "Security Awareness Tools",
        "Direct Terminal Run /usr/local/bin/",
        "All Shows",
    ]

    title = f"{Fore.YELLOW}Available options for help...{Style.RESET_ALL}"
    
    # Print title centered with a border
    print("═" * 80)
    print(title.center(80))
    print("═" * 80)
    
    # Print options with a border and spacing
    for index, option in enumerate(options, start=1):
        display_text = f"{index}. {Fore.GREEN}{option}{Style.RESET_ALL}"
        print(f"║ {display_text.ljust(80)} ║")
    
    print("═" * 80)
    print(f"{Fore.RED}{Style.BRIGHT}{'99. Exit'}{Style.RESET_ALL}")


def help():
    # Initialize colorama
    init(autoreset=True)

    # Call display_options here if needed
    display_options()

    def show_info_gather():
        print(f"{Fore.BLUE}{Style.BRIGHT}Information Gathering Tools\n")
        
        print(f"{Fore.YELLOW}Network Scanning Tools:")
        print(f"    - {Fore.CYAN}Nmap{Style.RESET_ALL}: A powerful network scanning tool for discovering hosts and services.")
        print(f"    - {Fore.CYAN}Angry IP Scanner{Style.RESET_ALL}: A fast and simple network scanner for IP addresses and ports.")
        print(f"    - {Fore.CYAN}Advanced IP Scanner{Style.RESET_ALL}: A free network scanner that detects all network devices.")
        
        print(f"\n{Fore.YELLOW}DNS Enumeration Tools:")
        print(f"    - {Fore.CYAN}dnsenum{Style.RESET_ALL}: A tool for DNS enumeration that gathers various DNS information.")
        print(f"    - {Fore.CYAN}dnsrecon{Style.RESET_ALL}: A DNS enumeration tool to gather various DNS records.")
        
        print(f"\n{Fore.YELLOW}Web Scraping and Recon Tools:")
        print(f"    - {Fore.CYAN}HTTPrint{Style.RESET_ALL}: A web server fingerprinting tool to identify web technologies.")
        print(f"    - {Fore.CYAN}Wappalyzer{Style.RESET_ALL}: A browser extension for detecting technologies on websites.")
        
        print(f"\n{Fore.YELLOW}Social Media and Public Information Gathering Tools:")
        print(f"    - {Fore.CYAN}Maltego{Style.RESET_ALL}: A tool for open-source intelligence and graphical link analysis.")
        print(f"    - {Fore.CYAN}theHarvester{Style.RESET_ALL}: A tool for gathering emails, subdomains, hosts, and more.")
        
        print(f"{Style.RESET_ALL}")

    def show_wireless_hacking_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Wireless Hacking Tools\n")

        print(f"{Fore.YELLOW}WiFi Security Assessment Tools:")
        print(f"    - {Fore.CYAN}Aircrack-NG{Style.RESET_ALL}: A comprehensive suite for assessing WiFi network security")
        print(f"    - {Fore.CYAN}Wifite{Style.RESET_ALL}: An automated wireless attack tool for pentesting WiFi networks")
        print(f"    - {Fore.CYAN}Fluxion{Style.RESET_ALL}: A tool that automates WiFi attacks")
        print(f"    - {Fore.CYAN}Wifiphisher{Style.RESET_ALL}: A social engineering tool for WiFi phishing attacks")

        print(f"\n{Fore.YELLOW}Packet Analyzers:")
        print(f"    - {Fore.CYAN}Kismet{Style.RESET_ALL}: A tool for detecting, sniffing, and intrusion detection in wireless networks")
        print(f"    - {Fore.CYAN}TCPDump{Style.RESET_ALL}: A command-line packet analyzer")
        print(f"    - {Fore.CYAN}Airsnort{Style.RESET_ALL}: A tool to recover encryption keys from WLAN")

        print(f"\n{Fore.YELLOW}WPS Attack Tools:")
        print(f"    - {Fore.CYAN}Reaver{Style.RESET_ALL}: A tool to recover WPS PINs")
        print(f"    - {Fore.CYAN}WPS Connect{Style.RESET_ALL}: A tool to connect to routers with WPS enabled")
        print(f"    - {Fore.CYAN}Netstumbler{Style.RESET_ALL}: A Windows tool for detecting Wireless LANs on 802.11b, 802.11a, and 802.11g networks")
        print(f"{Style.RESET_ALL}")


    def show_exploitation_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Exploitation Tools\n")

        print(f"{Fore.YELLOW}Web Application Exploitation Tools:")
        print(f"    - {Fore.CYAN}Burp Suite{Style.RESET_ALL}: A platform for comprehensive web application security testing")
        print(f"    - {Fore.CYAN}ZAP (Zed Attack Proxy){Style.RESET_ALL}: A user-friendly tool for finding vulnerabilities in web applications")
        print(f"    - {Fore.CYAN}BeEF (Browser Exploitation Framework){Style.RESET_ALL}: A tool focused on targeting web browsers")
        print(f"    - {Fore.CYAN}SQL Map{Style.RESET_ALL}: A tool that automates detection and exploitation of SQL injection flaws")

        print(f"\n{Fore.YELLOW}General Exploitation Frameworks:")
        print(f"    - {Fore.CYAN}Metasploit Framework{Style.RESET_ALL}: A tool for developing and executing exploit code against remote targets")
        print(f"    - {Fore.CYAN}Core Impact{Style.RESET_ALL}: A commercial tool for extensive network system penetration testing")
        print(f"    - {Fore.CYAN}Cobalt Strike{Style.RESET_ALL}: A tool for advanced adversary simulation and post-exploitation")
        print(f"    - {Fore.CYAN}Empire{Style.RESET_ALL}: A post-exploitation framework for Windows environments")

        print(f"\n{Fore.YELLOW}Social Engineering and Specialized Tools:")
        print(f"    - {Fore.CYAN}SET (Social Engineering Toolkit){Style.RESET_ALL}: A toolkit for creating social engineering attacks")
        print(f"    - {Fore.CYAN}ExploitDB{Style.RESET_ALL}: A public repository of exploits and vulnerable software for research purposes")
        print(f"{Style.RESET_ALL}")


    def show_web_application_assessment_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Web Application Assessment Tools\n")

        print(f"{Fore.YELLOW}General Web Security Scanners:")
        print(f"    - {Fore.CYAN}OWASP ZAP (Zed Attack Proxy){Style.RESET_ALL}: Open-source scanner for finding vulnerabilities in web applications")
        print(f"    - {Fore.CYAN}Nikto{Style.RESET_ALL}: A web server scanner that performs multiple tests against web servers for vulnerabilities")
        print(f"    - {Fore.CYAN}Arachni{Style.RESET_ALL}: Open-source scanner with advanced scanning capabilities")
        print(f"    - {Fore.CYAN}Vega{Style.RESET_ALL}: A GUI-based web application scanner designed to find vulnerabilities in web apps")
        print(f"    - {Fore.CYAN}AppSpider{Style.RESET_ALL}: A dynamic web application security scanner")

        print(f"\n{Fore.YELLOW}Specialized Web Vulnerability Scanners:")
        print(f"    - {Fore.CYAN}WPScan{Style.RESET_ALL}: A WordPress vulnerability scanner for detecting security issues in WordPress sites")
        print(f"    - {Fore.CYAN}Gobuster{Style.RESET_ALL}: A tool for brute-forcing URIs (directories and files) in web applications")
        print(f"{Style.RESET_ALL}")


    def show_forensics_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Forensics Tools\n")

        print(f"{Fore.YELLOW}Disk Analysis and File Recovery:")
        print(f"    - {Fore.CYAN}SleuthKit{Style.RESET_ALL}: Command-line tools and library for analyzing disk images and recovering files")
        print(f"    - {Fore.CYAN}Autopsy{Style.RESET_ALL}: Graphical interface for The Sleuth Kit and other digital forensics tools")
        print(f"    - {Fore.CYAN}Foremost{Style.RESET_ALL}: Console program for recovering files based on headers, footers, and internal structures")
        print(f"    - {Fore.CYAN}Guymager{Style.RESET_ALL}: Free forensic imager for media acquisition")
        print(f"    - {Fore.CYAN}Binwalk{Style.RESET_ALL}: Tool for analyzing, reverse engineering, and extracting firmware images")

        print(f"\n{Fore.YELLOW}Network and Memory Analysis:")
        print(f"    - {Fore.CYAN}Wireshark{Style.RESET_ALL}: Comprehensive network protocol analyzer for inspecting data traffic")
        print(f"    - {Fore.CYAN}Volatility{Style.RESET_ALL}: Tool for memory forensics and incident response")
        print(f"    - {Fore.CYAN}Plaso{Style.RESET_ALL}: Tool for digital forensics and incident response, focused on timeline creation")
        print(f"    - {Fore.CYAN}Rekall{Style.RESET_ALL}: Open-source tool for memory analysis and incident response")
        print(f"{Style.RESET_ALL}")


    def show_network_security_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Network Security Tools\n")

        print(f"    - {Fore.CYAN}Wireshark{Style.RESET_ALL}: A network protocol analyzer for troubleshooting and analysis.")
        print(f"    - {Fore.CYAN}Nmap{Style.RESET_ALL}: A network scanner for discovering hosts and services.")
        print(f"    - {Fore.CYAN}Snort{Style.RESET_ALL}: An open-source intrusion detection system (IDS) for monitoring traffic.")
        print(f"    - {Fore.CYAN}TCPdump{Style.RESET_ALL}: A command-line packet analyzer for capturing and analyzing packets.")
        print(f"{Style.RESET_ALL}")


    def show_vulnerability_assessment_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Vulnerability Assessment Tools\n")

        print(f"    - {Fore.CYAN}Nessus{Style.RESET_ALL}: A vulnerability scanner for identifying weaknesses in systems and applications.")
        print(f"    - {Fore.CYAN}OpenVAS{Style.RESET_ALL}: An open-source vulnerability scanner for assessing security vulnerabilities.")
        print(f"    - {Fore.CYAN}Qualys{Style.RESET_ALL}: Cloud-based security and compliance solutions, including vulnerability scanning.")
        print(f"{Style.RESET_ALL}")


    def show_penetration_testing_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Penetration Testing Tools\n")

        print(f"    - {Fore.CYAN}Metasploit{Style.RESET_ALL}: A penetration testing framework for exploiting vulnerabilities in systems.")
        print(f"    - {Fore.CYAN}Burp Suite{Style.RESET_ALL}: A web application security testing tool for finding and exploiting vulnerabilities.")
        print(f"    - {Fore.CYAN}OWASP ZAP{Style.RESET_ALL}: An open-source web application security scanner for identifying security vulnerabilities.")
        print(f"{Style.RESET_ALL}")


    def show_malware_analysis_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Malware Analysis Tools\n")

        print(f"    - {Fore.CYAN}Cuckoo Sandbox{Style.RESET_ALL}: An automated malware analysis system for examining suspicious files.")
        print(f"    - {Fore.CYAN}IDA Pro{Style.RESET_ALL}: A powerful disassembler and debugger for reverse engineering and analyzing malware.")
        print(f"    - {Fore.CYAN}VirusTotal{Style.RESET_ALL}: An online service for scanning files and URLs for malware using multiple antivirus engines.")
        print(f"{Style.RESET_ALL}")


    def show_endpoint_security_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Endpoint Security Tools\n")

        print(f"    - {Fore.CYAN}Symantec Endpoint Protection{Style.RESET_ALL}: An antivirus and endpoint protection platform.")
        print(f"    - {Fore.CYAN}CrowdStrike Falcon{Style.RESET_ALL}: A cloud-delivered endpoint protection platform for detecting and responding to threats.")
        print(f"    - {Fore.CYAN}Carbon Black{Style.RESET_ALL}: A security platform for endpoint detection and response.")
        print(f"{Style.RESET_ALL}")


    def show_logging_and_monitoring_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Logging and Monitoring Tools\n")

        print(f"    - {Fore.CYAN}Splunk{Style.RESET_ALL}: A platform for searching, analyzing, and visualizing machine-generated big data.")
        print(f"    - {Fore.CYAN}Loggly{Style.RESET_ALL}: A cloud-based log management and analysis tool.")
        print(f"    - {Fore.CYAN}Graylog{Style.RESET_ALL}: An open-source log management tool for collecting, indexing, and analyzing log data.")
        print(f"{Style.RESET_ALL}")


    def show_security_information_and_event_management_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Security Information and Event Management (SIEM) Tools\n")

        print(f"    - {Fore.CYAN}Splunk{Style.RESET_ALL}: A SIEM platform for searching and analyzing security data.")
        print(f"    - {Fore.CYAN}ArcSight{Style.RESET_ALL}: A SIEM solution for real-time monitoring and threat detection.")
        print(f"    - {Fore.CYAN}QRadar{Style.RESET_ALL}: A security intelligence platform for detecting and responding to security threats.")
        print(f"{Style.RESET_ALL}")


    def show_iam_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Identity and Access Management (IAM) Tools\n")

        print(f"    - {Fore.CYAN}Okta{Style.RESET_ALL}: A cloud-based IAM solution for secure user authentication and access management.")
        print(f"    - {Fore.CYAN}Microsoft Azure AD{Style.RESET_ALL}: A cloud-based IAM solution for managing user identities and access.")
        print(f"    - {Fore.CYAN}AWS IAM{Style.RESET_ALL}: A service for managing access to AWS resources.")
        print(f"{Style.RESET_ALL}")


    def show_risk_management_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Risk Management Tools\n")

        print(f"    - {Fore.CYAN}RiskLens{Style.RESET_ALL}: A platform for cyber risk quantification and management.")
        print(f"    - {Fore.CYAN}LogicManager{Style.RESET_ALL}: A risk management software for managing enterprise risks.")
        print(f"    - {Fore.CYAN}RSA Archer{Style.RESET_ALL}: A risk management platform for managing enterprise risks and compliance.")
        print(f"{Style.RESET_ALL}")


    def show_security_awareness_tools():
        print(f"{Fore.BLUE}{Style.BRIGHT}Security Awareness Tools\n")

        print(f"    - {Fore.CYAN}KnowBe4{Style.RESET_ALL}: A platform for security awareness training and simulated phishing attacks.")
        print(f"    - {Fore.CYAN}CybSafe{Style.RESET_ALL}: A behavioral security awareness platform for organizations.")
        print(f"    - {Fore.CYAN}PhishMe{Style.RESET_ALL}: A platform for phishing simulations and security awareness training.")
        print(f"{Style.RESET_ALL}")


    def direct_terminal_run():
        print(f"{Fore.BLUE}{Style.BRIGHT}Direct Terminal Run{Style.RESET_ALL}\n")

        print(f"{Fore.CYAN}1. Navigate to the directory: {Fore.YELLOW}/usr/local/bin/{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}2. Create a new file using the following command:\n")
        print(f"   {Fore.YELLOW}nano abc{Style.RESET_ALL} (Do not include an extension)\n")
        print(f"{Fore.CYAN}3. Inside the nano editor, write your bash script as needed for direct execution.\n")
        print(f"{Fore.CYAN}4. Save and exit the nano editor (use Ctrl + X, then Y to confirm).\n")
        print(f"{Fore.CYAN}5. Open the terminal and run the following command to execute your script:\n   {Fore.YELLOW}abc{Style.RESET_ALL}\n")



    while True:
        try:
            option = input(f"{Fore.CYAN}Please enter a number to get help : {Style.RESET_ALL}")
            
            if option == '1':
                print(f"{Fore.CYAN}{'-'*90}")
                show_info_gather()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                
            elif option == '2':
                print(f"{Fore.CYAN}{'-'*90}")
                show_wireless_hacking_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '3':
                print(f"{Fore.CYAN}{'-'*90}")
                show_exploitation_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '4':
                print(f"{Fore.CYAN}{'-'*90}")
                show_web_application_assessment_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '5':
                print(f"{Fore.CYAN}{'-'*90}")
                show_forensics_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '6':
                print(f"{Fore.CYAN}{'-'*90}")
                show_network_security_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '7':
                print(f"{Fore.CYAN}{'-'*90}")
                show_vulnerability_assessment_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '8':
                print(f"{Fore.CYAN}{'-'*90}")
                show_penetration_testing_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '9':
                print(f"{Fore.CYAN}{'-'*90}")
                show_malware_analysis_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '10':
                print(f"{Fore.CYAN}{'-'*90}")
                show_endpoint_security_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '11':
                print(f"{Fore.CYAN}{'-'*90}")
                show_logging_and_monitoring_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '12':
                print(f"{Fore.CYAN}{'-'*90}")
                show_security_information_and_event_management_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '13':
                print(f"{Fore.CYAN}{'-'*90}")
                show_iam_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '14':
                print(f"{Fore.CYAN}{'-'*90}")
                show_risk_management_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '15':
                print(f"{Fore.CYAN}{'-'*90}")
                show_security_awareness_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
            
            elif option == '16':
                print(f"{Fore.CYAN}{'-'*90}")
                direct_terminal_run()()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
            
            elif option == '17':
                print(f"{Fore.CYAN}{'='*99}")
                show_wireless_hacking_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_exploitation_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_web_application_assessment_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_forensics_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_network_security_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_vulnerability_assessment_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_penetration_testing_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_malware_analysis_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_endpoint_security_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_logging_and_monitoring_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_security_information_and_event_management_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_iam_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_risk_management_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")
                show_security_awareness_tools()
                print(" ")
                print(f"{Fore.CYAN}{'-'*90}")

            elif option == '99':
                print(f"{Fore.RED}{Style.BRIGHT}Exiting the program. Goodbye!")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.")
                
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.")
