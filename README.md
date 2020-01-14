# dirly
Eesily map your function to all files inside a directory.

### How to use

~~~
from dirly import dirly as d

@d(i='/Desktop/images', o='/Desktop/resized-images', ext=['png', 'jpg'])
def resize(p, s):
  """Open, resize and return `PIL.Image` given by path `p` to size `s`""" 
  return Image.open(path).resize(s)
~~~
