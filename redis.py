# import asyncio
# import aioredis
#
#
# async def redis_set(anagram, count):
#     redis = aioredis.from_url(
#         'redis://localhost', encoding='utf-8', decode_responses=True
#     )
#     async with redis.client() as conn:
#         await conn.set('anagram', anagram)
#
#
# async def redis_get():
#     redis = aioredis.from_url(
#         'redis://localhost', encoding='utf-8', decode_responses=True
#     )
#     async with redis.client() as conn:
#         res = await conn.get('count')
#     return await res
