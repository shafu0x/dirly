from dirly import txt_dirly

IN_DIR = './tests/texts/data/in'
OUT_DIR = './tests/texts/data/out'

@txt_dirly(i=IN_DIR, o=OUT_DIR)
def test_txt_dirly_with_o_dir(_f):
    with open(_f, 'w') as f:
        f.write('txt_dirly is very cool!')


def test_txt_dirly_without_o_dir(): pass

test_txt_dirly_with_o_dir()
