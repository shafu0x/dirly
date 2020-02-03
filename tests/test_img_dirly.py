from PIL import Image
from pathlib import Path
import os, shutil

from dirly import img_dirly

IN_DIR = Path('./tests/data/image/in')
OUT_DIR = Path('./tests/data/image/out')

OG_SZ = (500, 500)
SZ = (100, 100)

Path.ls = lambda d: [os.path.join(d, x) for x in os.listdir(d)]

def check_imgs(dir, sz):
    "Returns `True` if images in `dir` have size `sz`."
    for f in dir.ls(): 
        if not Image.open(f).size == SZ: return False
    return True

def revert_imgs(dir, sz):
    "Resize images in `dir` to size `sz`."
    for f in dir.ls(): Image.open(f).resize(sz).save(f)

def rm_imgs(dir): shutil.rmtree(dir)

def test_throw_exception_f_not_defined():
    exception = False
    try:
        @img_dirly(IN_DIR, None, None)
        def resize(sz):
            """Open, resize and return all files in `IN_DIR` as a list"""
            return np.array(Image.open(None).resize(sz))
    except Exception: exception = True
        
    assert exception

def test_img_dirly_with_o_dir():
    
    @img_dirly(IN_DIR, OUT_DIR, ext=['.png']) 
    def resize(_f, sz):
        return Image.open(_f).resize(sz)

    assert resize(SZ) is None
    assert check_imgs(OUT_DIR, SZ)

    rm_imgs(OUT_DIR)

def test_img_dirly_without_o_dir():
    
    @img_dirly(IN_DIR)
    def resize(_f, sz):
        return Image.open(_f).resize(sz)

    assert resize(SZ) is None
    assert check_imgs(IN_DIR, SZ)

    revert_imgs(IN_DIR, OG_SZ)