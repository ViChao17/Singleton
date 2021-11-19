class Singleton:
    class __Singleton:
        def __init__(self, arg):
            self.val = arg

    instance = None

    def __init__(self, arg=''):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton(arg)
        else:
            Singleton.instance.val = arg

    def __str__(self):
        return Singleton.instance.val


s = Singleton('s')
print(s)
s1 = Singleton('s1')
print(s1)
print(s)
