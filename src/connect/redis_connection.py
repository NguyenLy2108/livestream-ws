import redis
import config as config

cfg = config.Settings()

redis = redis.Redis(
            host=cfg.redis_host,
            port=cfg.redis_port,
            decode_responses=True
        )  
print("----Connected Redis----")