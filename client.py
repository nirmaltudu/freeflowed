import redis
from constants.redis_constants import REDIS_HOST, REDIS_PORT
from constants.queues import CALCULATION_REQUEST_QUEUE
from commands import Add, Multiply, Command

class MyClient(object):
    def __init__(self):
        self._redisClient = None

    @property
    def redisClient(self):
        if self._redisClient is None:
            self._redisClient = redis.Redis(REDIS_HOST, REDIS_PORT)
        return self._redisClient

    def publish(self, message):
        # TODO: check if message is json serialized
        if message:
            self.redisClient.publish(CALCULATION_REQUEST_QUEUE, message)

def main():
    client = MyClient()
    client.publish(Add(23423,342342).toJson())
    client.publish(Multiply(123, 345).toJson())

if __name__ == '__main__':
    main()