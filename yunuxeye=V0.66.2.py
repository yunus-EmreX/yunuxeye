import subprocess
import time

def run_command(command, timeout):
    start_time = time.time()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    while process.poll() is None:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            process.terminate()
            print("[*] Command execution timed out. Exiting...")
            break

    stdout, stderr = process.communicate()
    return stdout

def gather_information(ip, url):
    print("[*] Starting reconnaissance on " + url + " (" + ip + ")")
    print("[*] Tool: Yunuxeye (Version: V0.66.2)")
    print("[*] Developed by Yunus")
    
    # Nmap -sS (TCP SYN scan) and -sV (Version Detection) scan
    print("[*] Gathering information using Nmap (TCP SYN scan)...")
    nmap_sS_result = run_command("nmap -sS " + ip, timeout=120)
    print("[Nmap -sS Output]\n", nmap_sS_result)

    print("[*] Gathering information using Nmap (Version Detection)...")
    nmap_sV_result = run_command("nmap -sV " + ip, timeout=120)
    print("[Nmap -sV Output]\n", nmap_sV_result)

    # Whois
    print("[*] Gathering information using Whois...")
    whois_result = run_command("whois " + ip, timeout=30)
    print("[Whois Output]\n", whois_result)

    # Masscan
    print("[*] Gathering information using Masscan...")
    masscan_result = run_command("masscan " + ip, timeout=60)
    print("[Masscan Output]\n", masscan_result)

    # Nikto
    print("[*] Gathering information using Nikto...")
    nikto_result = run_command("nikto -h " + ip, timeout=60)
    print("[Nikto Output]\n", nikto_result)

    # SSLyze
    print("[*] Gathering information using SSLyze...")
    sslyze_result = run_command("sslyze --regular " + url, timeout=120)
    print("[SSLyze Output]\n", sslyze_result)

    # Lynis
    print("[*] Gathering information using Lynis (Targeted scan)...")
    lynis_result = run_command("lynis audit system", timeout=180)
    print("[Lynis Output]\n", lynis_result)

    # PEASS-ng (Linux)
    print("[*] Gathering information using PEASS-ng (Linux)...")
    peass_linux_result = run_command("linpeas.sh", timeout=180)
    print("[PEASS-ng (Linux) Output]\n", peass_linux_result)

    # PEASS-ng (Windows)
    print("[*] Gathering information using PEASS-ng (Windows)...")
    peass_windows_result = run_command("winPEAS.bat", timeout=180)
    print("[PEASS-ng (Windows) Output]\n", peass_windows_result)

    # DNSenum
    print("[*] Gathering information using DNSenum...")
    dnsenum_result = run_command("dnsenum " + url, timeout=120)
    print("[DNSenum Output]\n", dnsenum_result)

    # DirBuster
    print("[*] Gathering information using DirBuster...")
    dirbuster_result = run_command("dirb http://" + url, timeout=180)
    print("[DirBuster Output]\n", dirbuster_result)

    # OWASP ZAP
    print("[*] Gathering information using OWASP ZAP (Zed Attack Proxy)...")
    zap_result = run_command("zap-cli quick-scan --spider -r " + url, timeout=300)
    print("[OWASP ZAP Output]\n", zap_result)

    # Fierce
    print("[*] Gathering information using Fierce...")
    fierce_result = run_command("fierce -dns " + url, timeout=120)
    print("[Fierce Output]\n", fierce_result)

    # nslookup
    print("[*] Gathering information using nslookup...")
    nslookup_result = run_command("nslookup " + url, timeout=60)
    print("[Nslookup Output]\n", nslookup_result)

    # dig
    print("[*] Gathering information using dig...")
    dig_result = run_command("dig " + url, timeout=60)
    print("[Dig Output]\n", dig_result)

    # dnsmap
    print("[*] Gathering information using dnsmap...")
    dnsmap_result = run_command("dnsmap " + url, timeout=120)
    print("[Dnsmap Output]\n", dnsmap_result)

    # Netcat (nc)
    print("[*] Gathering information using Netcat...")
    nc_result = run_command("nc -vz " + ip + " 20-400", timeout=120)
    print("[Netcat Output]\n", nc_result)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_url = input("Enter the target URL: ")

    gather_information(target_ip, target_url)
