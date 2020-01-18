import os, mimetypes
from pathlib import Path

img_extensions = set(k for k,v in mimetypes.types_map.items() if v.startswith('image/'))

def _get_files(parent, p, f, extensions):
    p = Path(p) 
    if isinstance(extensions, str):
        extensions = [extensions]
    low_extensions = [e.lower()
                      for e in extensions] if extensions is not None else None
    res = [p/o for o in f if not o.startswith('.')
           and (extensions is None or f'.{o.split(".")[-1].lower()}' in low_extensions)]
    return res

def get_files(path, extensions=None, recurse=False, exclude=None, include=None,
                presort=False, followlinks=False):
"Return list of files in `path` that have a suffix in `extensions`; optionally `recurse`."
if recurse:
    res = []
    for i, (p, d, f) in enumerate(os.walk(path, followlinks=followlinks)):
        # skip hidden dirs
        if include is not None and i == 0:
            d[:] = [o for o in d if o in include]
        elif exclude is not None and i == 0:
            d[:] = [o for o in d if o not in exclude]
        else:
            d[:] = [o for o in d if not o.startswith('.')]
        res += _get_files(path, p, f, extensions)
    if presort:
        res = sorted(
            res, key=lambda p: _path_to_same_str(p), reverse=False)
    return res
else:
    f = [o.name for o in os.scandir(path) if o.is_file()]
    res = _get_files(path, path, f, extensions)
    if presort:
        res = sorted(
            res, key=lambda p: _path_to_same_str(p), reverse=False)
    return res

class dirly:
    def __init__(self, i, o=None, ext=None, recurse=False):
        self.i = Path(i)
        if o:
            self.o = Path(o)
            if not self.o.exists(): os.mkdir(o)
        self.ext = ext
        self.recurse = recurse

    def __call__(self, *args):
        def fn(*kwargs):
            o_s = []
            for fp in get_files(self.i, self.ext, self.recurse)
                o = args[0](self.i/fp, kwargs[0])
                o_s.append(fp, o)
            if not self.o = return o_s
            for o in o_s: self.save(self.i/fp, o)  # TODO: Change parent dir.
        return fn

    def save(self, fp, i):
        return None

class img_dirly(dirly):
    "Dirl `PIL.Image` objs"
    def __init__(self, i, o=None, ext=None, recurse=False):
        super().__init__(i, o, ext, recurse)
        if not self.ext: img_extensions

    def save(self, fp, i):
        i.save(fp)

class txt_dirly(dirly):
    "Dirl txt files"
    def __init__(self, i, o=None, recurse=False):
        super().__init__(i, ext)
        if not self.ext: ['txt']

    def save(fp, i):
        pass # TODO
