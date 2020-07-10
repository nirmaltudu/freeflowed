from collections import deque
import inspect
class Command(object):
    _CLASS = 'commands'
    def __init__(self, func):
        self.command = func

    # def toJson(self):
    #     return simplejson.dumps(self._data)

    # @classmethod
    # def fromJson(cls, jsonMsg):
    #     _data = simplejson.loads(jsonMsg)
    #     klass = _getClassFromFullyQualifiedName(_data['objectType'])
    #     return klass(*_data['args'], **_data['kwargs'])

    # @property
    # def command(self):
    #     return lambda: None

    # def successCallback(self, result):


    def __call__(self, paramsDict):
        sig = inspect.signature(self.command)
        params = dict()
        for name, param in sig.parameters.items():
            if not paramsDict.get(name) and param.default == param.empty:
                raise RuntimeError(f"Parameter '{name}' not found, while executing '{self.command.__name__}'")
            params[name] = paramsDict.get(name) or param.default
        args = sig.bind(**params).arguments
        return self.command(**args)

@Command
def add(x, y):
    return x+y

def mult(x, y):
    return x*y
pd = dict(x=10)
print(add(pd))