# dirly
Quickly map any function to every item in a directory (verb: to dirl). You can 'dirl'
images and text files (more are coming!).

### How to use

~~~
from dirly import img_dirly

@img_dirly(IN_DIR, OUT_DIR, ext=['.png']) 
def resize(_fp, sz):
    """Open, resize and save files with `ext` in `IN_DIR` to `OUT_DIR`"""
    return Image.open(_fp).resize(sz)
~~~
