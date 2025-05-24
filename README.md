**Design patterns.**

**Creational patterns:** 

**Abstract factory** - creates objects which somehow deal with each other. 
The simplest implementation consist of a few fabric methods, more complex factory
may content logic. Allows abstracting from concrete objects in code.

**Builder** - is used for building complex objects when the process of building consists 
of multiple steps. Allows creating even different objects with the same steps by 
delegating a building process to builders. Director only define a consistency of steps.

**Prototype** - creates objects by cloning them. The pattern can be used when we don't 
know about an object class (got it transferred from somewhere) or initialization 
process is complicated.


**Behavioral patterns:**

**Visitor** - implements double dispatch principle. Pattern is used when we have limited 
 amount of objects and multiple interfaces. Allows adding actions upon objects without
editing ones.