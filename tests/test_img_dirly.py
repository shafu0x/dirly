from PIL import Image
import numpy as np

from dirly import img_dirly

IN_DIR = './tests/data/in'
OUT_DIR = './tests/data/out'

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

    assert resize((640, 320)) is None

def test_img_dirly_as_arr_with_o_dir():
    
    @img_dirly(IN_DIR, OUT_DIR, ext=['.png'])
    def resize(_f, sz):
        return np.array(Image.open(_f).resize(sz))

    assert resize((640,320)) is None

def test_img_dirly_without_o_dir():
    
    @img_dirly(IN_DIR)
    def resize(_f, sz):
        return Image.open(_f).resize(sz)

    assert isinstance(resize((640,320)), list)
    assert isinstance(resize((640,320))[0], Image.Image)

def test_img_dirly_as_arr_without_o_dir():

    @img_dirly(IN_DIR)
    def resize(_f, sz):
        return np.array(Image.open(_f).resize(sz))

    assert isinstance(resize((640,320)), list)
    assert isinstance(resize((640,320))[0], np.ndarray)

# Add test for recursive directories.
