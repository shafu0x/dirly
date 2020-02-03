import os
from dirly import txt_dirly

IN_DIR = './tests/data/text/in'
OUT_DIR = './tests/data/text/out'

def test_txt_dirly_without_o_dir():

    @txt_dirly(i=IN_DIR)    
    def write_to_file(_f, txt):
        with open(_f, 'w') as f:
            f.write(txt)

    write_to_file('txt_dirly is very cool!')

def test_txt_dirly_with_o_dir():

    @txt_dirly(i=IN_DIR, o=OUT_DIR)    
    def write_to_file(_f, txt):
        with open(_f, 'w') as f:
            f.write(txt)
            return f

    write_to_file('txt_dirly is very cool!')

    assert len(os.listdir(OUT_DIR)) > 0