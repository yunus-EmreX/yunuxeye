import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

def gather_information(ip, url):
    print("[*] Starting reconnaissance on " + url + " (" + ip + ")")
    print("[*] Tool: Yunuxeye (Version: V0.66.2)")
    print("[*] Developed by Yunus")
    
    # Nmap -sS (TCP SYN scan) and -sV (Version Detection) scan
    print("[*] Gathering information using Nmap (TCP SYN scan)...")
    nmap_sS_result = run_command("nmap -sS " + ip)
    print("[Nmap -sS Output]")
    print("Explanation: Nmap TCP SYN scan checks which ports are open and can respond to SYN packets.")
    print(nmap_sS_result)

    print("[*] Gathering information using Nmap (Version Detection)...")
    nmap_sV_result = run_command("nmap -sV " + ip)
    print("[Nmap -sV Output]")
    print("Explanation: Nmap version detection attempts to determine the version of the services running on open ports.")
    print(nmap_sV_result)

    # Whois
    print("[*] Gathering information using Whois...")
    whois_result = run_command("whois " + ip)
    print("[Whois Output]")
    print("Explanation: Whois provides information about the registered owner of a domain name or IP address.")
    print(whois_result)

    # Masscan
    print("[*] Gathering information using Masscan...")
    masscan_result = run_command("masscan " + ip + " --ports 0-200")
    print("[Masscan Output]")
    print("Explanation: Masscan is a fast port scanner that can scan the entire Internet in under 6 minutes.")
    print(masscan_result)

    # Nikto
    print("[*] Gathering information using Nikto...")
    nikto_result = run_command("nikto -h http://" + ip)
    print("[Nikto Output]")
    print("Explanation: Nikto is a web server scanner which performs comprehensive tests against web servers for multiple items, including over 6700 potentially dangerous files/programs.")
    print(nikto_result)

    # SSLyze
    print("[*] Gathering information using SSLyze...")
    sslyze_result = run_command("sslyze --regular " + ip)
    print("[SSLyze Output]")
    print("Explanation: SSLyze analyzes the SSL/TLS configuration of a server to ensure it is properly configured and secure.")
    print(sslyze_result)

    # Lynis (Targeted scan)
    print("[*] Gathering information using Lynis (Targeted scan)...")
    lynis_result = run_command(f"lynis audit remote {ip}")
    print("[Lynis Output]")
    print("Explanation: Lynis is a security auditing tool for Unix systems, which performs an extensive health scan of the system to support system hardening and compliance testing.")
    print(lynis_result)

    # PEASS-ng (Linux)
    print("[*] Gathering information using PEASS-ng (Linux)...")
    print("Note: This process may take a while, please be patient.")
    peass_linux_result = run_command("/path/to/linpeas.sh")
    print("[PEASS-ng (Linux) Output]")
    print("Explanation: LinPEAS searches for possible paths to escalate privileges on a Linux system.")
    print(peass_linux_result)

    # PEASS-ng (Windows)
    print("[*] Gathering information using PEASS-ng (Windows)...")
    print("Note: This process may take a while, please be patient.")
    peass_windows_result = run_command("/path/to/winPEAS.bat")
    print("[PEASS-ng (Windows) Output]")
    print("Explanation: WinPEAS searches for possible paths to escalate privileges on a Windows system.")
    print(peass_windows_result)

    # DNSenum
    print("[*] Gathering information using DNSenum...")
    dnsenum_result = run_command("dnsenum " + url.split("//")[1])
    print("[DNSenum Output]")
    print("Explanation: DNSenum is a DNS enumeration tool which can enumerate domain names, subdomains, and IP addresses.")
    print(dnsenum_result)

    # DirBuster
    print("[*] Gathering information using DirBuster...]")
    dirbuster_result = run_command("dirb http://" + url.split("//")[1])
    print("[DirBuster Output]")
    print("Explanation: DirBuster is a multi-threaded web application brute forcer that enumerates directories and files on web/application servers.")
    print(dirbuster_result)

    # OWASP ZAP
    print("[*] Gathering information using OWASP ZAP (Zed Attack Proxy)...")
    zap_result = run_command("zap-cli quick-scan --spider -r " + url)
    print("[OWASP ZAP Output]")
    print("Explanation: OWASP ZAP is an open-source web application security scanner, used for finding vulnerabilities in web applications.")
    print(zap_result)

    # Fierce
    print("[*] Gathering information using Fierce...")
    fierce_result = run_command("fierce -dns " + url.split("//")[1])
    print("[Fierce Output]")
    print("Explanation: Fierce is a DNS reconnaissance tool that attempts to find non-contiguous IP space and hostnames against specified domains.")
    print(fierce_result)

    # nslookup
    print("[*] Gathering information using nslookup...")
    nslookup_result = run_command("nslookup " + url.split("//")[1])
    print("[Nslookup Output]")
    print("Explanation: Nslookup is a network administration command-line tool for querying the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.")
    print(nslookup_result)

    # dig
    print("[*] Gathering information using dig...")
    dig_result = run_command("dig " + url.split("//")[1])
    print("[Dig Output]")
    print("Explanation: Dig (Domain Information Groper) is a network administration command-line tool for querying DNS name servers.")
    print(dig_result)

    # dnsmap
    print("[*] Gathering information using dnsmap...")
    dnsmap_result = run_command("dnsmap " + url.split("//")[1])
    print("[Dnsmap Output]")
    print("Explanation: Dnsmap is a subdomain brute-force tool that is used to find subdomains in a given domain.")
    print(dnsmap_result)

    # Netcat (nc)
    print("[*] Gathering information using Netcat...")
    print("Note: This process may take a while, please be patient.")
    nc_result = run_command("nc -vz " + ip + " 20-400")
    print("[Netcat Output]")
    print("Explanation: Netcat (nc) is a versatile networking tool used to read from and write to network connections using TCP or UDP. The -vz options are used for scanning open ports.")
    print(nc_result)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_url = input("Enter the target URL: ")

    gather_information(target_ip, target_url)
