# Design patterns #


## Creational patterns ## 

**Abstract factory** - creates objects which somehow deal with each other. 
The simplest implementation consist of a few fabric methods, more complex factory
may content logic. Allows abstracting from concrete objects in code.

**Builder** - is used for building complex objects when the process of building consists 
of multiple steps. Allows creating even different objects with the same steps by 
delegating a building process to builders. Director only define a consistency of steps.

**Prototype** - creates objects by cloning them. The pattern can be used when we don't 
know about an object class (got it transferred from somewhere) or initialization 
process is complicated.


## Behavioral patterns ##

**Chain of responsibility** - decouples a client from handlers responsible for the 
result of the action. Dispatches responsibility to one or more handlers without knowing
which one is going to accept the request if any.

**Command** - decouples an invoker of the action from a receiver of the action. 
Encapsulates the action into a separate Command class.

**Mediator** - simplify a system where a lot of objects communicate to each other by
decoupling and implementing their collaboration into itself. The system objects know 
only a mediator but a mediator knows each object.

**State** - represents states of a process as classes with different behavior. Process
context or state objects can change the inner state of the context and by this avoid 
using multiple if else constructions.

**Template method** - consists of other operations which should be overwritten in 
subclasses. Those operations may be hook methods (on_create, on_delete, etc.) then a 
template method may have default implementation or fabric methods or both.

**Visitor** - implements double dispatch principle. Pattern is used when we have limited 
 amount of objects and multiple interfaces. Allows adding actions upon objects without
editing ones.


## Structural patterns ##

**Adapter** - adapts classes with incompatible interfaces to make possible the 
communication between them.

**Bridge** - decouples abstraction and implementation. Allows extending both 
independently. Can be used when a class may be extended in different ways.

**Decorator** - adds new functionality to a function or to an object without changing 
other same class objects.

**Proxy** - emulates behavior of the original object by giving access to it. The goal
is allowing additional functionality like restricting access or postpone getting the 
'expensive'/remote proxied object until it's required.