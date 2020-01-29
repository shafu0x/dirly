import os, mimetypes
from pathlib import Path
import numpy as np
from PIL import Image

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
            if not self.o.is_dir(): os.mkdir(o)
        else: self.o = None
        self.ext = ext
        self.recurse = recurse

    def __call__(self, *args):
        def fn(*kwargs):
            fps = get_files(self.i, self.ext, self.recurse)
            items = [args[0](str(fp), kwargs[0]) for fp in fps]
            if self.o: self._save(fps, items)
            else     : return items
        return fn

    def _save(self, fps, items):
        for fp, o in zip(fps, items): self.save(self.o/fp.name, o)

    def save(self, fp, i):
        return None

class img_dirly(dirly):
    "Dirl `PIL.Image` or img_arr objs"
    def __init__(self, i, o=None, ext=None, recurse=False):
        super().__init__(i, o, ext, recurse)
        if not self.ext: img_extensions

    def save(self, fp, i):
        if isinstance(i, np.ndarray): Image.fromarray(i).save(fp)
        else                        : i.save(fp)                    

class txt_dirly(dirly):
    "Dirl txt files"
    def __init__(self, i, o=None, recurse=False):
        super().__init__(i, ext)
        if not self.ext: ['txt']

    def save(fp, i):
        pass # TODO
