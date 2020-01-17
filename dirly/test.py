from PIL import Image
import numpy as np

from dirly import dirly

IN_DIR = 'test/data/in/'
OUT_DIR = 'test/data/out/'

@dirly(IN_DIR, OUT_DIR, ext=['.png']) 
def resize(_fp, sz):
    """Open, resize and save files with `ext` in `IN_DIR` to `OUT_DIR`"""
    return Image.open(_fp).resize(sz)

assert resize((640, 320)) is None

@dirly(IN_DIR, None, None)
def resize(_fp, sz):
    """Open, resize and return all files in `IN_DIR` as a list"""
    return np.array(Image.open(_fp).resize(sz))

assert isinstance(resize((640, 320)), list)