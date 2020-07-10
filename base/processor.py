import functools

class MessageProcessor(object):
    def __init__(self, reactor, queue):
        self._client = None
        self.start          = functools.partial(self._start, reactor)
        self.stop           = functools.partial(self._stop, reactor)
        self.subscribe      = functools.partial(self._subscribe, queue)
        self.unsubscribe    = functools.partial(self._unsubscribe, queue)
        self.initialize     = functools.partial(self._initialize, reactor)

    @property
    def client(self):
        if not self._client:
            import redis
            from   constants.redis_constants import REDIS_HOST, REDIS_PORT
            self._client = redis.Redis(REDIS_HOST, REDIS_PORT, db=0, socket_connect_timeout=2, socket_timeout=2).pubsub()
        return self._client

    def _subscribe(self, queue):
        self.client.subscribe(queue)

    def _unsubscribe(self, queue):
        self.client.unsubscribe(queue)

    def onMessage(self):
        msg = self.client.get_message()
        if msg:
            self.handleMessage(msg)

    def handleMessage(self, msg):
        print(msg)

    def _initialize(self, reactor):
        from twisted.internet.task import LoopingCall
        self.subscribe()
        loop = LoopingCall(self.onMessage)
        loop.start(1.0)

    def _start(self, reactor):
        self.initialize()
        reactor.run()

    def _stop(self, reactor):
        self.client.unsubscribe()
        reactor.stop()

