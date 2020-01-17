def what_are_the_vars(*args, **kwargs):
    o = ObjectC()
    if (len(args) > 0):
        for idx, attr in enumerate(args):
            key = "var_" + str(idx)
            if (hasattr(o, key)):
                return None
            setattr(o, key, attr)
    if (len(kwargs) > 0):
        for key, value in kwargs.items():
            if (hasattr(o, key)):
                return None
            setattr(o, key, value)
    return o

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
        if obj is None:
            print("ERROR")
            print("end")
            return
        for attr in dir(obj):
            if attr[0] != '_':
                value = getattr(obj, attr)
                print("{}: {}".format(attr, value))
        print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)