class Dirly:
    def __init__(self, i, o, ex):
        self.i = i
        self.o = o
        self.ex = []
    def __call__(f):
        pass

if __name__ == '__main__':
    from PIL import Image

    @d(i=, o=, ex=)
    def resize(path, s):
        return Image.open(path).resize(s)

