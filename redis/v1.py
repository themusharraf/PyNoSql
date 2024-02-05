import redis

# Redis-server'ga bog'lanish
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Ma'lumotni yozish va muddatini belgilash
redis_client.set('salom', 'Hello, Redis!')
redis_client.expire('salom', 3600)  # Ma'lumot 1 soat saqlanadi

# Muddati tugagan so'ng ma'lumotni o'qish (mavjud bo'lgan ma'lumotni o'chiradi)
result = redis_client.get('salom')

if result is None:
    print('Ma\'lumot otkazib ketdi')
else:
    print(result.decode('utf-8'))
"""Ushbu kod misolida, expire metodi orqali "salom" kalit so'zini 1 soat muddatida saqlaymiz.
Ma'lumotni o'qish urinishi esa bir soatdan so'ng, ma'lumotni topishda "None" qaytaradi.
Bunda, expire metodining ishlashi sababli avtomatik ravishda "salom" kalit so'zini o'chirib tashlaydi."""