from datetime       import date, datetime
from marshmallow    import Schema, fields, pprint
'''
@processor.Task
def foo(x, y, z=10):
    pass

@processor.Task(inQueue='/CalculationEvent/Rquest', outQueue='/CalculationEvent/Response')
def bar(a, b, c=10):
    pass

@processor.Task(inQueue='/CalculationEvent/Rquest', outQueue='/CalculationEvent/Response')
def foo1(d, e, f=10):
    pass

@processor.Task(inQueue='/CalculationEvent/Rquest', outQueue='/CalculationEvent/Response')
def bar1(g, h, i=10):
    pass

flowParams = FrozenDict(assetName='MLEIICUS', changeIn='IndexLevel')
flow = WorkFlow(flowParams)
flow.addTasks([foo, bar])
flow.addDependentTasks(foo, [foo1, foo2])
flow.addDependentTasks(bar, [bar1, bar2])
flow.correlationId()
flow.write()
flow.serialize()
{   correlationId: 'klfjw4q2341l2kh',
    tasks: { foo: {function: 'lib.foomodule.foo', args=[], kwargs={}, destQueue='/CalculationEvent/Request', status=PENDING},
             bar: {function: 'lib.barmodule.bar', args=[], kwargs={}, destQueue='/CalculationEvent/Request', status=PENDINT}}
            },
    flow: {foo: [foo1, foo2],
           bar: [bar1, bar2]},
    executionPointer: foo,
}
path = '/EQ/Data/QIS/Portal/DataProcessor/WorkFlow/' + hash(flowParams)
flow.read(path)
flow.deserialize(str(flow.serialize()))
flow.percentageCompletion()
flow.currentTask()
flow.executeCurrentTask()


changeReactor = yawnet.ChangeReactor('PriceChangeReactor')
changeReactor.getWorkflow()
changeReactor.start()
changeReactor.stop()

returnCalulator = yawnet.DataProcessor('ReturnCalculator', queue='/CalculationEvents/ReturnCalculator/Queue')
returnCalculator.start()
returnCalculator.stop()

riskCalculator = yawnet.DataProcessor('RiskCalculator', queue='/CalculationEvents/RiskCalculator/Queue')
riskCalculator.start()
riskCalculator.stop()
'''
class WorkflowSchema(Schema):
    

class Workflow(object):

class EventSchema(Schema):
    eventId                 = fields.Str()
    correlationId           = fields.Str()
    eventCreateTimestamp    = fields.DateTime()
    eventTriggrEventId      = fields.Str()
    eventCode               = fields.Str()
    applicationPayload      = fields.Dict()
    applicationOutput       = fields.Dict()

class ApplicationMessage(fields.Field):
    pass

class EventBase(object):
    def __init__(self, correlationId, inputData):
