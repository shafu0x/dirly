import os

class dirly:
    def __init__(self, i, o=None, ext=None):
        self.i, self.o = i, o
        self.ext = ext
    def __call__(self, *args):
        def fn(*kwargs):
            o_s = []
            for fp in os.listdir(self.i):
                o = args[0](os.path.join(self.i, fp), kwargs[0])
                if self.o:  o.save(os.path.join(self.o, fp))
                else:       o_s.append(o)
            if not o_s: return None
            else:       return o_s
        return fn 