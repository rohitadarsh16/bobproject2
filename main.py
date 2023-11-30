import requests
from bs4 import BeautifulSoup

# cookies = {
#     'secure_customer_sig': '',
#     'localization': 'DE',
#     'cart_currency': 'EUR',
#     '_cmp_a': '%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22NL%22%2C%22sale_of_data_region%22%3Afalse%7D',
#     '_shopify_y': '6b1011db-24a9-4db2-bc7f-a5f008a50eff',
#     '_shopify_s': '01750188-c246-4434-b542-9653246815c7',
#     '_orig_referrer': '',
#     '_landing_page': '%2F',
#     '_fbp': 'fb.1.1701376335316.1738973483',
#     '_gid': 'GA1.2.512450080.1701376336',
#     '_gcl_au': '1.1.321558212.1701376336',
#     'cart': 'c1-ca460bbf0870f27f597296f4f1115012',
#     'checkoutDomain': 'https://pay.checkify.pro',
#     'cart_sig': 'fd7a3dbabcc6a8ae67ea423022c6b16d',
#     '_shopify_sa_p': '',
#     '_pin_unauth': 'dWlkPVlUbGpabVF3TjJFdE9UQTNOaTAwTUdJNExUa3hOVFl0T1RKaE5XTmxZV1k1TlRNdw',
#     'keep_alive': '4f416da8-9a3b-4251-a819-6fb0eb721c0d',
#     '_ga': 'GA1.1.742406853.1701376336',
#     '__kla_id': 'eyJjaWQiOiJZemM1T0RVd09ERXRPV0V4TWkwME5tUmhMVGt4TldVdE16azNaV0l3WkdJeVpXUTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDEzNzYzMzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vdGhvdXNhaW50c2xhYmVsLmRlLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcwMTM3NzY1NSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly90aG91c2FpbnRzbGFiZWwuZGUvIn19',
#     'cart_ts': '1701377659',
#     '_shopify_sa_t': '2023-11-30T20%3A55%3A03.468Z',
#     '_ga_3WDFBMZC87': 'GS1.1.1701377069.1.1.1701377703.0.0.0',
#     '_ga_6469VMVDN0': 'GS1.1.1701376336.1.1.1701377703.0.0.0',
#     'dynamic_checkout_shown_on_cart': '1',
# }

# headers = {
#     'authority': 'thousaintslabel.de',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6,gu;q=0.5,de;q=0.4',
#     # 'cookie': 'secure_customer_sig=; localization=DE; cart_currency=EUR; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22NL%22%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=6b1011db-24a9-4db2-bc7f-a5f008a50eff; _shopify_s=01750188-c246-4434-b542-9653246815c7; _orig_referrer=; _landing_page=%2F; _fbp=fb.1.1701376335316.1738973483; _gid=GA1.2.512450080.1701376336; _gcl_au=1.1.321558212.1701376336; cart=c1-ca460bbf0870f27f597296f4f1115012; checkoutDomain=https://pay.checkify.pro; cart_sig=fd7a3dbabcc6a8ae67ea423022c6b16d; _shopify_sa_p=; _pin_unauth=dWlkPVlUbGpabVF3TjJFdE9UQTNOaTAwTUdJNExUa3hOVFl0T1RKaE5XTmxZV1k1TlRNdw; keep_alive=4f416da8-9a3b-4251-a819-6fb0eb721c0d; _ga=GA1.1.742406853.1701376336; __kla_id=eyJjaWQiOiJZemM1T0RVd09ERXRPV0V4TWkwME5tUmhMVGt4TldVdE16azNaV0l3WkdJeVpXUTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDEzNzYzMzYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vdGhvdXNhaW50c2xhYmVsLmRlLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcwMTM3NzY1NSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly90aG91c2FpbnRzbGFiZWwuZGUvIn19; cart_ts=1701377659; _shopify_sa_t=2023-11-30T20%3A55%3A03.468Z; _ga_3WDFBMZC87=GS1.1.1701377069.1.1.1701377703.0.0.0; _ga_6469VMVDN0=GS1.1.1701376336.1.1.1701377703.0.0.0; dynamic_checkout_shown_on_cart=1',
#     'dnt': '1',
#     'if-none-match': 'W/"cacheable:963b9dae964cd8563fd4364e7322ba1a"',
#     'referer': 'https://thousaintslabel.de/search?page=3&q=jacket&type=product',
#     'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
# }

params = {
    'page': '2',
    'q': 'jacket',
    'type': 'product',
}

response = requests.get('https://thousaintslabel.de/search', params=params)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

with open('index.html', 'w') as file:
    file.write(soup.prettify())


import requests

cookies = {
    'il-country': '{%22countryCode%22:%22IN%22%2C%22countryName%22:%22India%22}',
    'il-returning-user': '1',
    'session-id': '2e2970cc-cea1-4d51-9d86-521867f1079a',
    '_gcl_au': '1.1.557452850.1701378617',
    '_gid': 'GA1.2.1138170988.1701378617',
    '_rdt_uuid': '1701378617144.42cc0f35-5a13-486a-ad77-bc05dd8c86b4',
    't-ip': '1',
    '_pin_unauth': 'dWlkPVlUbGpabVF3TjJFdE9UQTNOaTAwTUdJNExUa3hOVFl0T1RKaE5XTmxZV1k1TlRNdw',
    'IR_gbd': 'iliabeauty.com',
    '_fbp': 'fb.1.1701378617332.565694461',
    'AMP_9bdc728a74': '{"deviceId":"7cc840b8-2c28-4d0c-ba48-8966c0f582de","sessionId":1701378618018,"optOut":false}',
    '__attentive_id': 'e3d88a83b9374efc8977b39f64991866',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzAxMzc4NjE4MTMyLFwidW9cIjoxNzAxMzc4NjE4MTMyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImUzZDg4YTgzYjkzNzRlZmM4OTc3YjM5ZjY0OTkxODY2XCJ9In0=',
    '__attentive_cco': '1701378618133',
    '__attentive_ss_referrer': 'ORGANIC',
    '__attentive_dv': '1',
    'tag_user_id': 'eb16e441-27e9-4169-80af-da77266a3fe6-1701378617979',
    '_uetsid': 'dc83a2a08fc411eea3746f4b93510677',
    '_uetvid': 'dc83e6c08fc411eeba2bd1ce593f14a6',
    '__kla_id': 'eyJjaWQiOiJNV0kyWW1RM1pqZ3RaalF5T1MwME1HRTBMV0V5TURBdFpXTXpOVGt4T0ROaE1EaGoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDEzNzg2MTYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vaWxpYWJlYXV0eS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzAxMzc4NzExLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL2lsaWFiZWF1dHkuY29tLyJ9fQ==',
    'tatari-cookie-test': '76840813',
    'tatari-session-cookie': '0206e803-c770-b56c-ade3-776ddbd50431',
    'IR_10539': '1701378710683%7C0%7C1701378710683%7C%7C',
    '_gat_UA-29268919-2': '1',
    '_ga': 'GA1.2.1571874966.1701378617',
    '_ga_HK5VFRR0G0': 'GS1.1.1701378617.1.1.1701378740.28.0.0',
    '__attentive_pv': '6',
}

headers = {
    'authority': 'iliabeauty.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6,gu;q=0.5,de;q=0.4',
    # 'cookie': 'il-country={%22countryCode%22:%22IN%22%2C%22countryName%22:%22India%22}; il-returning-user=1; session-id=2e2970cc-cea1-4d51-9d86-521867f1079a; _gcl_au=1.1.557452850.1701378617; _gid=GA1.2.1138170988.1701378617; _rdt_uuid=1701378617144.42cc0f35-5a13-486a-ad77-bc05dd8c86b4; t-ip=1; _pin_unauth=dWlkPVlUbGpabVF3TjJFdE9UQTNOaTAwTUdJNExUa3hOVFl0T1RKaE5XTmxZV1k1TlRNdw; IR_gbd=iliabeauty.com; _fbp=fb.1.1701378617332.565694461; AMP_9bdc728a74={"deviceId":"7cc840b8-2c28-4d0c-ba48-8966c0f582de","sessionId":1701378618018,"optOut":false}; __attentive_id=e3d88a83b9374efc8977b39f64991866; _attn_=eyJ1Ijoie1wiY29cIjoxNzAxMzc4NjE4MTMyLFwidW9cIjoxNzAxMzc4NjE4MTMyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImUzZDg4YTgzYjkzNzRlZmM4OTc3YjM5ZjY0OTkxODY2XCJ9In0=; __attentive_cco=1701378618133; __attentive_ss_referrer=ORGANIC; __attentive_dv=1; tag_user_id=eb16e441-27e9-4169-80af-da77266a3fe6-1701378617979; _uetsid=dc83a2a08fc411eea3746f4b93510677; _uetvid=dc83e6c08fc411eeba2bd1ce593f14a6; __kla_id=eyJjaWQiOiJNV0kyWW1RM1pqZ3RaalF5T1MwME1HRTBMV0V5TURBdFpXTXpOVGt4T0ROaE1EaGoiLCIkcmVmZXJyZXIiOnsidHMiOjE3MDEzNzg2MTYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vaWxpYWJlYXV0eS5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzAxMzc4NzExLCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL2lsaWFiZWF1dHkuY29tLyJ9fQ==; tatari-cookie-test=76840813; tatari-session-cookie=0206e803-c770-b56c-ade3-776ddbd50431; IR_10539=1701378710683%7C0%7C1701378710683%7C%7C; _gat_UA-29268919-2=1; _ga=GA1.2.1571874966.1701378617; _ga_HK5VFRR0G0=GS1.1.1701378617.1.1.1701378740.28.0.0; __attentive_pv=6',
    'dnt': '1',
    'if-none-match': 'W/"db7ff639d676cecd90a2ced07fb6ff15"',
    'referer': 'https://iliabeauty.com/search?q=wanderlust',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

response = requests.get('https://iliabeauty.com/search--en-us.json', cookies=cookies, headers=headers)