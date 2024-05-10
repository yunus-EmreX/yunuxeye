import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return e.output

def gather_information(ip, url):
    print("[*] Starting reconnaissance on " + url + " (" + ip + ")")
    print("[*] Tool: Yunuxeye (Version: V0.24)")
    print("[*] Developed by Yunus")
    
    # Nmap -sS (TCP SYN scan) and -sV (Version Detection) scan
    print("[*] Gathering information using Nmap (TCP SYN scan)...")
    nmap_sS_result = run_command("nmap -sS " + ip)
    print("[Nmap -sS Output]\n", nmap_sS_result)

    print("[*] Gathering information using Nmap (Version Detection)...")
    nmap_sV_result = run_command("nmap -sV " + ip)
    print("[Nmap -sV Output]\n", nmap_sV_result)

    # Whois
    print("[*] Gathering information using Whois...")
    whois_result = run_command("whois " + ip)
    print("[Whois Output]\n", whois_result)

    # Masscan
    print("[*] Gathering information using Masscan...")
    masscan_result = run_command("masscan " + ip)
    print("[Masscan Output]\n", masscan_result)

    # Other tools
    print("[*] Gathering information using additional tools...")

    # DirBuster
    print("[*] Gathering information using DirBuster...")
    dirbuster_result = run_command("dirb http://" + url)
    print("[DirBuster Output]\n", dirbuster_result)

    # OWASP ZAP
    print("[*] Gathering information using OWASP ZAP (Zed Attack Proxy)...")
    zap_result = run_command("zap-cli quick-scan --spider -r " + url)
    print("[OWASP ZAP Output]\n", zap_result)

    # Fierce
    print("[*] Gathering information using Fierce...")
    fierce_result = run_command("fierce -dns " + url)
    print("[Fierce Output]\n", fierce_result)

    # nslookup
    print("[*] Gathering information using nslookup...")
    nslookup_result = run_command("nslookup " + url)
    print("[Nslookup Output]\n", nslookup_result)

    # dig
    print("[*] Gathering information using dig...")
    dig_result = run_command("dig " + url)
    print("[Dig Output]\n", dig_result)

    # dnsmap
    print("[*] Gathering information using dnsmap...")
    dnsmap_result = run_command("dnsmap " + url)
    print("[Dnsmap Output]\n", dnsmap_result)

    # Netcat (nc)
    print("[*] Gathering information using Netcat...")
    nc_result = run_command("nc -vz " + ip + " 1-1023")
    print("[Netcat Output]\n", nc_result)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_url = input("Enter the target URL: ")

    gather_information(target_ip, target_url)
