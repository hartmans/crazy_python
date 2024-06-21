import pytest
from pathlib import Path

class memoproperty:

    '''Implement memoproperty without looking at the implementation
    in Carthage.  memoproperty is a decorator. Like property, when a
    method is decorated, it is accessed using attribute access rather
    than method access. The first time the attribute is accessed, the decorated function is called, and its value returned. Future accesses return the same value exactly as efficiently as if it was set directly on the instance. If the property is deleted from the object, then the next access will call the decorated function again.

    Example::

        class square:
            side = 2

            @memoproperty
             def area(self):
                return self.side**2

        s = Square()

        s.area # 4
        s.side = 3
        s.area # 4
        del s.area
        s.area # 9

        Square.area #a memoproperty object
    '''

    def __init__(self, wrapped_function):
        # do stuff
        pass
# Solution
#exec(Path('../solutions/test_memoproperty.py').read_text())

# validation tests

def test_memoproperty():
    a_called = 0
    b_called = 0
    class test:

        def __init__(self, c):
            self.c = c

        @memoproperty
        def a(self):
            nonlocal a_called
            a_called += 1
            return self.c+2

        @memoproperty
        def b(self):
            nonlocal b_called
            b_called += 1
            return self.a+2

    t1 = test(20)
    t2 = test(30)
    assert a_called == 0
    assert b_called == 0
    assert t1.b == 24
    assert a_called == 1
    assert b_called == 1
    assert t1.a == 22
    assert a_called == 1
    t1.c += 1
    assert t1.a == 22
    del t1.a
    assert t1.a == 23
    assert a_called == 2
    assert t2.a == 32
    assert a_called == 3
    assert b_called == 1
    assert isinstance(test.a, memoproperty)
    del test.a
    assert t2.a == 32
    
