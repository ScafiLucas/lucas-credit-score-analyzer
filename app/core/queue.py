import os
import json
import redis.asyncio as aioredis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
QUEUE_CHANNEL = os.getenv("QUEUE_CHANNEL", "credit_score_jobs")

redis = None

async def init_redis():
    global redis
    if not redis:
        redis = await aioredis.from_url(REDIS_URL, decode_responses=True)
    return redis

async def publish_job(job_id: str):
    redis_conn = await init_redis()
    payload = json.dumps({"job_id": job_id})
    await redis_conn.publish(QUEUE_CHANNEL, payload)
