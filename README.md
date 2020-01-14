# dirly
Eesily map your function to all files inside a directory.

### Example
Resize all images inside `in` with a `.png` extension and save it to `out`.

~~~
from dirly import dirly as d

@d(in='/Desktop/Images', out='/Desktop/Resized_Images', extensions=['png'])
def resize(path, s):
  return Image.open(path).resize(size)
~~~
