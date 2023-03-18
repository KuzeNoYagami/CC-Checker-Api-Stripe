import requests
import json

#membaca file cc.txt
with open('cc.txt', 'r') as f:
    cc_list = f.readlines()

#membuat file live.txt dan dead.txt
live = open('live.txt', 'w') 
dead = open('dead.txt', 'w') 
  
#mengambil data dari api stripe 
for cc in cc_list: 

    #memisahkan nomor kartu, tanggal, tahun, dan cvv 
    cc_number, date, year, cvv = cc.split('|')

    #membuat payload untuk request api stripe 
    payload = {'card[number]': cc_number, 'card[exp_month]': date, 'card[exp_year]': year, 'card[cvc]': cvv}

    #request api stripe dengan apikey 
    r = requests.post('https://api.stripe.com/v1/tokens', data=payload, auth=('sk_test_apikey', ''))

    #mengubah response menjadi json format 
    response = json.loads(r.text)

    #cek jika response adalah live maka masukkan ke file live.txt 
    if response['livemode'] == True: 
        live.write(cc)

    #cek jika response adalah dead maka masukkan ke file dead.txt 
    elif response['livemode'] == False: 
        dead.write(cc)
