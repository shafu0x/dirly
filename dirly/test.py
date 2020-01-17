from PIL import Image
from dirly import dirly

IN_DIR = 'test/data/in/'
OUT_DIR = 'test/data/out/'

@dirly(IN_DIR, OUT_DIR, '.png')
def resize(_fp, sz):
    return Image.open(_fp).resize(sz)

assert resize((640, 320)) is None

@dirly(IN_DIR, None, None)
def resize(_fp, sz):
    return Image.open(_fp).resize(sz)

assert isinstance(resize((640, 320)), list)