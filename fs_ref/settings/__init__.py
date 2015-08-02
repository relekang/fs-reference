# -*- coding: utf8 -*-
from fs_ref.settings.base import *

try:
    from fs_ref.settings.local import *
except ImportError, e:
    raise ImportError("Couldn't load local settings")
