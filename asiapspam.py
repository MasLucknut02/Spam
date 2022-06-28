import requests, os

url_api_spam_wa_mantan = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"

os.system("clear")
os.system("figlet Spam")
print("[-] Creator : MasLucknut_2")
print("[-] Instagram : maslucknut2")
print("[-] Wa : +6281384307028")
print(" Have fun aja banh")
print("Jangan dibuat serius")
nomor = input("\n[?] input Nomor : ")
jumlah = input("[?] input berapa banh : ")
print()
data = {
"nomor": nomor
}
for MasLucknut_2 in range(int(jumlah)):
        sanz = requests.get(url_api_spam_wa_mantan, params=data)
        if "Berhasil Ngab ! .. Subrek Yt FREE TUTORIAL." in sanz.text:
                 print("[+] Berhasil Ya Banh")
        else:
                 print("[!] Waduh kok gagal banh")