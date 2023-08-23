from pydantic import BaseModel


class RedisRq(BaseModel):
    range_value: int
