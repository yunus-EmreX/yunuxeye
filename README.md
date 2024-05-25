# Yunuxeye - Pentest Araçları Entegrasyonu

Yunuxeye, çeşitli pentest araçlarını bir araya getirerek hedef sistemler hakkında kapsamlı bilgi toplamak için kullanılan bir Python scriptidir. Bu araç, Nmap, Masscan, Nikto, SSLyze, Lynis, PEASS-ng, DNSenum, DirBuster, OWASP ZAP, Fierce, Nslookup, Dig ve Dnsmap gibi araçları entegre eder ve çıktıları kullanıcıya detaylı açıklamalarla sunar.

## Özellikler

- **Nmap** ile port taraması ve servis versiyon tespiti
- **Whois** ile hedef IP hakkında kayıt bilgileri
- **Masscan** ile hızlı port taraması
- **Nikto** ile web sunucusu güvenlik taraması
- **SSLyze** ile SSL/TLS yapılandırma analizi
- **Lynis** ile hedef sistem güvenlik taraması
- **PEASS-ng** ile potansiyel yetki yükseltme yolları tespiti
- **DNSenum** ile DNS bilgi toplama
- **DirBuster** ile dizin ve dosya brute-force taraması
- **OWASP ZAP** ile web uygulama güvenlik taraması
- **Fierce** ile DNS keşfi
- **Nslookup** ve **Dig** ile DNS sorgulamaları
- **Dnsmap** ile subdomain brute-force taraması
- **Netcat** ile açık port taraması

## Gereksinimler

- Python 3.x
- Nmap
- Masscan
- Nikto
- SSLyze
- Lynis
- PEASS-ng (LinPEAS ve WinPEAS)
- DNSenum
- DirBuster
- OWASP ZAP
- Fierce
- Nslookup (bind-utils paketi)
- Dig (bind-utils paketi)
- Dnsmap
- Netcat

## Kurulum

Öncelikle, gerekli araçların sisteminizde yüklü olduğundan emin olun:

```bash
sudo apt-get update
sudo apt-get install nmap masscan nikto sslyze lynis dnsenum dirbuster fierce dnsutils netcat

PEASS-ng araçlarını indirin ve uygun dizinlere yerleştirin:

bash

git clone https://github.com/carlospolop/PEASS-ng.git

Kullanım

Script'i çalıştırmak için aşağıdaki adımları izleyin:

    Python scriptini indirin veya kopyalayın.
    Terminalden scriptin bulunduğu dizine gidin.
    Scripti çalıştırın:

bash

python yunuxeye.py

    İstenilen hedef IP adresi ve URL'yi girin.
    Script, belirtilen araçları kullanarak hedef sistem hakkında bilgi toplamaya başlayacaktır.

Çıktılar

Her araç, çalıştırıldıktan sonra çıktısını ve bu çıktının ne anlama geldiğini açıklayan bilgiler sunar. Bu açıklamalar, elde edilen verilerin anlaşılmasını ve yorumlanmasını kolaylaştırır.
Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen şu adımları izleyin:

    Bu depoyu fork edin.
    Kendi dalınızı oluşturun (git checkout -b ozellik/AmazingFeature).
    Değişikliklerinizi commit edin (git commit -m 'AmazingFeature ekle').
    Dalınıza push edin (git push origin ozellik/AmazingFeature).
    Bir Pull Request açın.

Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
İletişim

Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen e-posta ile iletişime geçin.

Yunuxeye, pentest işlemlerinizde size kapsamlı ve detaylı bilgi sağlayarak güvenlik açıklarını daha etkili bir şekilde tespit etmenize yardımcı olur. Hedef sistemlerin güvenliğini artırmak için bu aracı kullanın ve sistemlerinizi daha güvende tutun.

css


Bu README dosyası, projenizin amacını, kullanımını, gereksinimlerini ve nasıl katkıda bulunulabileceğini açıkça anlatır. Ayrıca, kullanıcıların projenizle ilgili daha fazla bilgi edinmesini sağlar.
