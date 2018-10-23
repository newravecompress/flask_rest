import requests
from random import randint

r = requests.get('http://localhost:5000/statistics')
# r = requests.post('http://localhost:5000/sales', data={'sum': randint(1000, 1000000)})

print(r.text)

# orders = ({'sum': randint(100, 1000000)} for i in range(10000))
# for o in orders:
#     total = sum(o['sum'])
#     count = sum(1)
# print(orders)
# print(total)
# print(count)


# total = sum(o['sum'] for o in orders if o['timestamp'] > time.time() - 60)
