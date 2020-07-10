from base.processor import MessageProcessor
from constants.queues import CALCULATION_REQUEST_QUEUE
from commands import Command
import simplejson

class MyProcessor(MessageProcessor):
    def handleMessage(self, msg):
        if msg.get('data') and isinstance(msg['data'], (bytes, str)):
            cmd = Command.fromJson(msg['data'].decode('utf-8'))
            result = cmd.execute()
            print(result)
            return result

def main():
    from twisted.internet import reactor
    processor = MyProcessor(reactor, CALCULATION_REQUEST_QUEUE)
    try:
        processor.start()
    except KeyboardInterrupt:
        processor.stop()

if __name__ == '__main__':
    main()