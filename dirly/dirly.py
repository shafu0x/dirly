import os, mimetypes, inspect
import numpy as np
from pathlib import Path
from PIL import Image
from typing import List, Union, Any, Callable

FILE_PLACEHOLDER = '_f'

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
    "Dirly base class. Inherit from it to create your own dirlys."
    def __init__(self, type:str, i:Union[str, Path], o:Union[str, Path]=None, ext:List[str]=None, recurse:bool=False):
        "Apply a func to every file in `i`; optionally save them to `o`."
        self.i = Path(i)
        self.o = Path(o) if o else None
        if not ext: self.ext = set(k for k, v in mimetypes.types_map.items() if v.startswith(f'{type}/'))
        else      : self.ext = ext
        self.recurse = recurse

    def __call__(self, *args):
        if not dirly._check_signature(args[0]): raise Exception(f'{FILE_PLACEHOLDER} is not defined')
        def fn(*kwargs):
            fnames = get_files(self.i, self.ext, self.recurse)
            items = [args[0](str(fname), kwargs[0]) for fname in fnames]
            if self.o: self._save(fnames, items)
            else     : return items
        return fn

    @staticmethod
    def _check_signature(fn:Callable) -> bool: return FILE_PLACEHOLDER in inspect.getfullargspec(fn).args

    def _save(self, fnames:List[str], items:List[Any]):
        "Save every `item` in `items` to `o` with given `fname`."
        if not self.o.is_dir(): os.mkdir(self.o)
        for fname, item in zip(fnames, items): self.save(self.o/fname.name, item)

    def save(self, fname:str, i:Any): raise Exception('Only call `save` from a dirly subclass.')

class img_dirly(dirly):
    "Dirl `PIL.Image` or `np.ndarray` images."
    def __init__(self, i:Union[str, Path], o:Union[str, Path]=None, ext:List[str]=None, recurse:bool=False):
        super().__init__('image', i, o, ext, recurse)

    def save(self, fname:str, i:Union[Image.Image, np.ndarray]):
        if isinstance(i, np.ndarray): Image.fromarray(i).save(fname)
        else                        : i.save(fname)

class video_dirly(dirly):
    "Dirl videos"
    def __init__(self, i: Union[str, Path], o: Union[str, Path] = None, ext: List[str] = None, recurse: bool = False):
        super().__init__('video', i, o, ext, recurse)

    def save(self, fname, i): pass

class txt_dirly(dirly):
    "Dirl txt based files"
    def __init__(self, i: Union[str, Path], o: Union[str, Path] = None, ext: List[str] = None, recurse: bool = False):
        super().__init__('text', i, o, ext, recurse)

    def save(self, fname, i): pass
