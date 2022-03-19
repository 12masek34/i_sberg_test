import random
import asyncpg

QUERY_ADD_DEVICE = """INSERT INTO devices VALUES ($1, $2, $3)"""
QUERY_GET_ALL_DEVICES_ID = """SELECT id FROM devices"""
QUERY_ADD_ENDPOINT = """INSERT INTO endpoints VALUES ($1, $2, $3)"""
QUERY_GET_ALL_DEVICES = """SELECT dev_type, COUNT(*) AS count_dev_type FROM devices
                                            WHERE id NOT IN
                                            (SELECT DISTINCT device_id FROM endpoints)
                                            GROUP BY dev_type"""

dev_id = "52:54:00:%02x:%02x:%02x" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
)

dt = ['emeter', 'zigbee', 'lora', 'gsm']
dev_type = random.choice(dt)


async def create_pool():
    return await asyncpg.create_pool('postgresql://127.0.0.1:5432/postgres')


async def add_device(device_id):
    db_pool = await create_pool()
    await db_pool.fetch(QUERY_ADD_DEVICE, device_id, dev_id, dev_type)


async def get_all_device_id():
    db_pool = await create_pool()
    all_device = await db_pool.fetch(QUERY_GET_ALL_DEVICES_ID)
    res = []
    for i in all_device:
        res.append(int(i['id']))
    return res


async def get_all_devices():
    db_pool = await create_pool()
    all_device = await db_pool.fetch(QUERY_GET_ALL_DEVICES)
    return all_device


async def add_endpoint(endpoint_id: int, device_id: int, text: str):
    db_pool = await create_pool()
    await db_pool.fetch(QUERY_ADD_ENDPOINT, endpoint_id, device_id, text)
