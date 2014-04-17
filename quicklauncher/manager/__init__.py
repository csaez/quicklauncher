from __future__ import absolute_import
from wishlib import inside_maya, inside_softimage

if inside_softimage():
    from .softimage import Manager
elif inside_maya():
    from .maya import Manager
