# dirly
Eesily map your function to all files inside a directory.

### Example
Resize all images inside `in` with a `.png` extension and save it to `out`.

~~~
from dirly import dirly as d

@d(i='/Desktop/Images', o='/Desktop/Resized_Images', ext=['png'])
def resize(p, s):
  """Open, resize and return `PIL.Image` given by path `p` to size `s`""" 
  return Image.open(path).resize(s)
~~~
