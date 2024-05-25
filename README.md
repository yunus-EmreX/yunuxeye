# Yunuxeye - Pentest Tool Integration

Yunuxeye is a Python script used to gather comprehensive information about target systems by bringing together various pentest tools. This tool integrates tools such as Nmap, Masscan, Nikto, SSLyze, Lynis, PEASS-ng, DNSenum, DirBuster, OWASP ZAP, Fierce, Nslookup, Dig, and Dnsmap, and presents the outputs to the user with detailed explanations.

## Features

- **Nmap**: Port scanning and service version detection
- **Whois**: Retrieving registration information about the target IP
- **Masscan**: Fast port scanning
- **Nikto**: Web server security scanning
- **SSLyze**: SSL/TLS configuration analysis
- **Lynis**: Security auditing of the target system
- **PEASS-ng**: Identifying potential privilege escalation paths
- **DNSenum**: DNS information gathering
- **DirBuster**: Directory and file brute-force scanning
- **OWASP ZAP**: Web application security scanning
- **Fierce**: DNS reconnaissance
- **Nslookup** and **Dig**: DNS queries
- **Dnsmap**: Subdomain brute-force scanning
- **Netcat**: Open port scanning

## Requirements

- Python 3.x
- Nmap
- Masscan
- Nikto
- SSLyze
- Lynis
- PEASS-ng (LinPEAS and WinPEAS)
- DNSenum
- DirBuster
- OWASP ZAP
- Fierce
- Nslookup (bind-utils package)
- Dig (bind-utils package)
- Dnsmap
- Netcat

## Installation

First, make sure the required tools are installed on your system:

```bash
sudo apt-get update
sudo apt-get install nmap masscan nikto sslyze lynis dnsenum dirbuster fierce dnsutils netcat

Download the PEASS-ng tools and place them in appropriate directories:

bash

git clone https://github.com/carlospolop/PEASS-ng.git

Usage

To run the script, follow these steps:

    Download or copy the Python script.
    Navigate to the directory where the script is located in the terminal.
    Run the script:

bash

python yunuxeye.py

    Enter the desired target IP address and URL.
    The script will start gathering information about the target system using the specified tools.

Outputs

Each tool provides its output after execution, along with explanations of what the output means. These explanations facilitate understanding and interpretation of the obtained data.
Contributing

If you would like to contribute to this project, please follow these steps:

    Fork this repository.
    Create your feature branch (git checkout -b feature/AmazingFeature).
    Commit your changes (git commit -m 'Add some AmazingFeature').
    Push to the branch (git push origin feature/AmazingFeature).
    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

If you have any questions or feedback, please contact us via email.

Yunuxeye helps you to detect security vulnerabilities more effectively by providing comprehensive and detailed information in your pentest operations. Use this tool to enhance the security of your systems and keep them more secure.
