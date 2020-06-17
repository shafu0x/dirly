!['dirly'](logo/logo.png)

Quickly map your function to every file in a directory (verb: to dirl). You can "*dirl*"
images and text files (you can easily add your own).

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
def resize(_f, sz):
    """Open, resize and save files with `ext` in `IN_DIR` to `OUT_DIR`"""
    return Image.open(_f).resize(sz)

resize((300, 300))
~~~

```_f``` is a special placeholder that dirly uses internaly. Use it to tell dirly where to input your file.

If you don't set the output directory `o` your function will be applied to the elements in place. 

~~~
from dirly import img_dirly

@img_dirly(i=IN_DIR, ext=['.png']) 
def resize(_fp, sz):
    """Open, resize and return files with `ext` in `IN_DIR` as a list"""
    return Image.open(_fp).resize(sz)

resized_imgs = resize((300, 300))
~~~

This will return a list of resized PIL.Image objects.

### Coming soon!

Text and Video Dirly are currently being developed in will be finished very soon.
