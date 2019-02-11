# from urllib.request import Request as r, urlopen as u
#
# req=r('http://www.google.co.kr')
#
# response = u(req)
#
# k = response.status
#
# print(k)

import requests

r = requests.get('http://www.google.co.kr')

k = r.status_code

print(k)