import aioredis
import config

cfg = config.Settings()

redis = aioredis.from_url('redis://{}:{}'.format(cfg.redis_host,cfg.redis_port))

print("Connected Redis")