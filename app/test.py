import requests
from time import sleep
from random import randint

# r = requests.get('http://localhost:5000/statistics', auth=('test', 'gfhjkm'))
while True:
    r = requests.post('http://localhost:8888/sales', auth=('test', 'gfhjkm'),
                      data={'sales_amount': randint(1000, 1000000)})
    print(r.text)
    sleep(randint(0, 100) / 1000)

