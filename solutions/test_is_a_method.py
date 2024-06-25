class ismethod:

    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        def f(*args, **kwargs):
            return self.fun(instance or owner, *args, **kwargs)
        return f

    def __call__(self, *args, **kwargs):
        return self.fun(None, *args, **kwargs)
    
