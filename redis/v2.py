import redis
import time

# Redis-server'ga bog'lanish
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

# Ma'lumotni yozish va muddatini belgilash
redis_client.set('salom', 'Hello, Redis!')

# 1 soat otkazib bo'lgan vaqt o'tib, ma'lumotni o'qish
time.sleep(3601)
result = redis_client.get('salom')

if result is None:
    print('Ma\'lumot otkazib ketdi')
else:
    print(result.decode('utf-8'))
