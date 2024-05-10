# yunuxeye
örnek çıktı:
python yunuxeye.py
Enter the target IP address: 64.226.98.205
Enter the target URL: http://64.226.98.205/
[*] Starting reconnaissance on http://64.226.98.205/ (64.226.98.205)
[*] Tool: Yunuxeye (Version: V0.24)
[*] Developed by Yunus
[*] Gathering information using Nmap (TCP SYN scan)...
[Nmap -sS Output]
 Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-10 15:01 +03
Nmap scan report for 64.226.98.205
Host is up (0.090s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 12.69 seconds

[*] Gathering information using Nmap (Version Detection)...
[Nmap -sV Output]
 Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-10 15:01 +03
Nmap scan report for 64.226.98.205
Host is up (0.063s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
80/tcp  open  http     nginx 1.18.0
443/tcp open  ssl/http nginx 1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.24 seconds

[*] Gathering information using Whois...
[Whois Output]
 
#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2024, American Registry for Internet Numbers, Ltd.
#


NetRange:       64.226.64.0 - 64.226.127.255
CIDR:           64.226.64.0/18
NetName:        DIGITALOCEAN-64-226-64-0
NetHandle:      NET-64-226-64-0-1
Parent:         NET64 (NET-64-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       AS14061
Organization:   DigitalOcean, LLC (DO-13)
RegDate:        2020-05-04
Updated:        2023-08-09
Comment:        Routing and Peering Policy can be found at https://www.as14061.net
Comment:        
Comment:        Please submit abuse reports at https://www.digitalocean.com/company/contact/#abuse
Ref:            https://rdap.arin.net/registry/ip/64.226.64.0



OrgName:        DigitalOcean, LLC
OrgId:          DO-13
Address:        101 Ave of the Americas
Address:        FL2
City:           New York
StateProv:      NY
PostalCode:     10013
Country:        US
RegDate:        2012-05-14
Updated:        2023-10-23
Ref:            https://rdap.arin.net/registry/entity/DO-13


OrgNOCHandle: NOC32014-ARIN
OrgNOCName:   Network Operations Center
OrgNOCPhone:  +1-347-875-6044 
OrgNOCEmail:  noc@digitalocean.com
OrgNOCRef:    https://rdap.arin.net/registry/entity/NOC32014-ARIN

OrgTechHandle: NOC32014-ARIN
OrgTechName:   Network Operations Center
OrgTechPhone:  +1-347-875-6044 
OrgTechEmail:  noc@digitalocean.com
OrgTechRef:    https://rdap.arin.net/registry/entity/NOC32014-ARIN

OrgAbuseHandle: ABUSE5232-ARIN
OrgAbuseName:   Abuse, DigitalOcean 
OrgAbusePhone:  +1-347-875-6044 
OrgAbuseEmail:  abuse@digitalocean.com
OrgAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE5232-ARIN


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2024, American Registry for Internet Numbers, Ltd.
#


[*] Gathering information using Masscan...
[Masscan Output]
 FAIL: no ports were specified
 [hint] try something like "-p80,8000-9000"
 [hint] try something like "--ports 0-65535"

[*] Gathering information using additional tools...
[*] Gathering information using DirBuster...
[DirBuster Output]
 
-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Fri May 10 15:01:51 2024
URL_BASE: http://http://64.226.98.205/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

*** Generating Wordlist...
                                                                               
GENERATED WORDS: 4612

---- Scanning URL: http://http://64.226.98.205/ ----
*** Calculating NOT_FOUND code...
                                                                               
(!) FATAL: Too many errors connecting to host
    (Possible cause: COULDNT RESOLVE HOST)
                                                                               
-----------------
END_TIME: Fri May 10 15:01:51 2024
DOWNLOADED: 0 - FOUND: 0

[*] Gathering information using OWASP ZAP (Zed Attack Proxy)...
[OWASP ZAP Output]
 /bin/sh: 1: zap-cli: not found

[*] Gathering information using Fierce...
[Fierce Output]
 usage: fierce [-h] [--domain DOMAIN] [--connect] [--wide]
              [--traverse TRAVERSE] [--search SEARCH [SEARCH ...]]
              [--range RANGE] [--delay DELAY]
              [--subdomains SUBDOMAINS [SUBDOMAINS ...] | --subdomain-file
              SUBDOMAIN_FILE] [--dns-servers DNS_SERVERS [DNS_SERVERS ...] |
              --dns-file DNS_FILE] [--tcp]
fierce: error: unrecognized arguments: -dns http://64.226.98.205/

[*] Gathering information using nslookup...
[Nslookup Output]
 Server:                192.168.1.1
Address:        192.168.1.1#53

** server can't find http://64.226.98.205/: NXDOMAIN


[*] Gathering information using dig...
[Dig Output]
 
; <<>> DiG 9.19.21-1-Debian <<>> http://64.226.98.205/
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 4858
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;http://64.226.98.205/.         IN      A

;; Query time: 0 msec
;; SERVER: 192.168.1.1#53(192.168.1.1) (UDP)
;; WHEN: Fri May 10 15:01:57 +03 2024
;; MSG SIZE  rcvd: 50


[*] Gathering information using dnsmap...
[Dnsmap Output]
 dnsmap 0.36 - DNS Network Mapper

[+] error: entered domain is not valid!

[*] Gathering information using Netcat...

(hedef gerçek değildir)

# Yunuxeye

Yunuxeye, hedef IP adresi ve URL üzerinde çeşitli penetrasyon test araçlarını otomatik olarak çalıştıran bir Python aracıdır.

## Kullanım

1. `yunuxeye.py` dosyasını çalıştırın.
2. İstenilen hedef IP adresini ve URL'yi girin.
3. Program, Nmap, Whois, Netcat, Masscan, DirBuster, OWASP ZAP, Fierce, nslookup, dig, dnsmap ve daha fazla aracı otomatik olarak çalıştıracaktır.
4. Her aracın çıktısı ekrana gösterilecektir.

## Gereksinimler

- Python 3.x
- Nmap
- Whois
- Netcat (nc)
- Masscan
- DirBuster
- OWASP ZAP (Zed Attack Proxy)
- Fierce
- nslookup
- dig
- dnsmap

## Yapımcı Bilgileri

- Tool: Yunuxeye
- Version: V0.24
- Geliştirici: Yunus
- [GitHub](https://github.com/yunus-EmreX/yunuxeye)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENCE dosyasına](LICENSE) bakın.
