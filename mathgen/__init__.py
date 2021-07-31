from mathgen.models.add import addModel, addMathgenButton
from mathgen.models.consts import MG_MODEL

from anki.hooks import addHook
from aqt import mw
from aqt.qt import *

def registerModel():
    model = mw.col.models.byName(MG_MODEL)
    if not model:
        model = addModel(mw.col)


# initialize models once anki user profile is loaded
addHook('profileLoaded', registerModel)
addHook('setupEditorButtons', addMathgenButton)
