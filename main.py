from fastapi import FastAPI
from schemas import *
import asyncio
import aioredis
from postgres import *

app = FastAPI()


@app.post('/redis')
async def anagram(item: Anagram):
    res = {}
    redis = aioredis.from_url('redis://localhost', encoding='utf-8', decode_responses=True)
    count = await redis.get('count')
    count = int(count)
    res['anagram'] = sorted(item.first) == sorted(item.second)
    if res['anagram']:
        if count is None:
            count = 1
        count += 1
        await redis.set('count', count)
    if count is None:
        res['count'] = 0
    else:
        res['count'] = count
    return res


@app.post('/add_device', status_code=201)
async def add_devices(device: Device):
    task = asyncio.create_task(add_device(device.device_id))
    await asyncio.gather(task)


@app.post('/add_endpoint', status_code=201)
async def add_endpoint(endpoint: Endpoint):
    task = asyncio.create_task(get_all_device_id())
    all_device_id = await asyncio.gather(task)
    if endpoint.device_id in all_device_id[0]:
        task = asyncio.create_task(add_endpoint(endpoint.endpoint_id, endpoint.device_id, endpoint.text))
        await asyncio.gather(task)


@app.get('/all_device')
async def all_device():
    res = await get_all_devices()
    return res
