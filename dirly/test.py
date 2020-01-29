from PIL import Image
import numpy as np

from dirly import img_dirly

IN_DIR = 'test/data/in/'
OUT_DIR = 'test/data/out/'

@img_dirly(IN_DIR, OUT_DIR, ext=['.png']) 
def resize(_f, sz):
    """Open, resize and save files with `ext` in `IN_DIR` to `OUT_DIR`"""
    return Image.open(_f).resize(sz)

assert resize((640, 320)) is None

@img_dirly(IN_DIR, None, None)
def resize(_f, sz):
    """Open, resize and return all files in `IN_DIR` as a list"""
    return np.array(Image.open(_f).resize(sz))

assert isinstance(resize((640,320)), list)
assert isinstance(resize((640,320))[0], np.ndarray)

exception = False

try:
    @img_dirly(IN_DIR, None, None)
    def resize(sz):
        """Open, resize and return all files in `IN_DIR` as a list"""
        return np.array(Image.open(None).resize(sz))
except Exception: exception = True
    
assert exception

# Add test for recursive directories.
# Add test for OUT_DIR and np.array.