from twisted.internet import protocol
import re
import functools

class MyPP(protocol.ProcessProtocol):
    def __init__(self, verses, reactor):
        self.verses = verses
        self.data = ""
        self.processEnded = functools.partial(self.processEnded, reactor)

    def connectionMade(self):
        print("connectionMade!")
        for _ in range(self.verses):
            data = "Aleph-null bottles of beer on the wall,\n" +\
                   "Aleph-null bottles of beer,\n" +\
                   "Take one down and pass it around,\n" +\
                   "Aleph-null bottles of beer on the wall.\n"
            self.transport.write(data.encode('ascii'))
        self.transport.closeStdin() # tell them we're done

    def outReceived(self, data):
        print("outReceived! with %d bytes!" % len(data))
        self.data = self.data + data

    def errReceived(self, data):
        print("errReceived! with %d bytes!" % len(data))

    def inConnectionLost(self):
        print("inConnectionLost! stdin is closed! (we probably did it)")

    def outConnectionLost(self):
        print("outConnectionLost! The child closed their stdout!")
        # now is the time to examine what they wrote
        #print "I saw them write:", self.data
        parts = re.split(r'\s+', self.data.decode('utf-8'))
        print('***********', parts)
        (dummy, lines, _, _, _) = parts
        print("I saw %s lines" % lines)

    def errConnectionLost(self):
        print("errConnectionLost! The child closed their stderr.")

    def processExited(self, reason):
        print("processExited, status %d" % (reason.value.exitCode,))

    def processEnded(self, reason, reactor):
        print(dir(reason))
        print("processEnded, status %d" % (reason.value.exitCode,))
        print("quitting")
        reactor.stop()

def main():
    from twisted.internet import reactor
    pp = MyPP(10, reactor)
    reactor.spawnProcess(pp, "wc", ["wc"], {})
    reactor.run()

if __name__ == '__main__':
    main()