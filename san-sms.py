#Xractz
#IndoSec

from requests import Session
import re, sys
s = Session()

try:
        print("T Make Pulsa By Sandi Pirmansyah - jang indoSec\nPake 62 (contol: 62xx)")
        no = int(input("No    : "))
        msg = input("Ek Nga Sms Naon Heula : ")
except:
        print("\n\t* cek heula pesana! *")
        sys.exit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/3>
    'Referer': 'http://sms.payuterus.biz/alpha/'
    }
    bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar", headers=headers).text
key = re.findall(r'value="(\d+)"', bypass)[0]
jml = re.findall(r'<span>(.*?) = </span>', bypass)[0]
captcha = eval(jml.replace("x", "*").replace(":", "/"))

data = {
        'nohp':no,
        'pesan':msg,
        'captcha':captcha,
        'key':key
}

send = s.post("http://sms.payuterus.biz/alpha/send.php", headers=headers, data=data).text

if 'Geus Dikirim Lur ah' in send:
        print(f"\nDagoan Geus Ngirim Da Sabar Kontol! \n[{no}] => {msg}")
        elif 'MAAF....!' in send:
        print("\n\t* Dagoan Heula 15 Menit Nyet Mun Ek Ngirim Nu Sarua Mah Bel *")
else:
        print("\n\t* Dagoan Heula Lur! *")
