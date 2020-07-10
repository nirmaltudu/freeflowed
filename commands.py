import simplejson
import logging

logger = logging.getLogger(__name__)

def add(x, y):
    return x+y

def multiply(x, y):
    return x * y


def _getClassFromFullyQualifiedName(path):
    parts = path.split('.')
    moduleName, className = '.'.join(parts[:-1]), parts[-1]
    try:
        pkg = __import__(moduleName)
        return getattr(pkg, className)
    except ImportError:
        logger.error(f"Cannot import module: {moduleName}")
    except AttributeError:
        logger.error(f"Cannot import object: {className}")

class Command(object):
    _CLASS = 'commands'
    def __init__(self, *args, **kwargs):
        self._data = dict(args=args, kwargs=kwargs, objectType=self._CLASS + '.' + self.__class__.__name__)

    def toJson(self):
        return simplejson.dumps(self._data)

    @classmethod
    def fromJson(cls, jsonMsg):
        _data = simplejson.loads(jsonMsg)
        klass = _getClassFromFullyQualifiedName(_data['objectType'])
        return klass(*_data['args'], **_data['kwargs'])

    @property
    def command(self):
        return lambda: None

    def execute(self):
        cmd, args, kwargs = self.command, self._data['args'], self._data['kwargs']
        return cmd(*args, **kwargs)

class Add(Command):
    @property
    def command(self):
        return add

class Multiply(Command):
    @property
    def command(self):
        return multiply
