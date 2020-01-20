# dirly
Quickly map your function to every file in a directory (verb: to dirl). You can 'dirl'
images and text files (more are coming!).

Do you have a function that you need to apply to every file in a directory? Writing the same
~~~
for f in os.listdir(YOUR_DIR):
    your_function(os.path.join(YOUR_DIR, f))
~~~

every single time sucks and I agree. Simply write your function to handle a single file and dirly will take care of mapping it to every element in your directory. 

### How to use

~~~
from dirly import img_dirly

@img_dirly(i=IN_DIR, ext=['.png'], o=OUT_DIR) 
def resize(_fp, sz):
    """Open, resize and save files with `ext` in `IN_DIR` to `OUT_DIR`"""
    return Image.open(_fp).resize(sz)

resize((300, 300))
~~~

```_fp``` is a special placeholder that dirly uses internaly. Use it to tell dirly where to input the full path to your file.

If you just want to return the elements as a list and don't want to save them to a directory, simply set o=None.

~~~
from dirly import img_dirly

@img_dirly(i=IN_DIR, ext=['.png'], o=None) 
def resize(_fp, sz):
    """Open, resize and return files with `ext` in `IN_DIR` to `OUT_DIR` as a list"""
    return Image.open(_fp).resize(sz)

resized_imgs = resize((300, 300))
~~~
