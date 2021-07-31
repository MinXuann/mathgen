import os
import re

from aqt import mw
from aqt.utils import tooltip
from PyQt5.QtGui import QKeySequence
from mathgen.models.consts import MG_MODEL, MG_TYPE
from mathgen.models.templates import card_front, card_back
from mathgen.mathgen import path

# add mathgen note type

fields = ['Problem', 'Solution']

def addModel(col):
    models = col.models
    model = models.new(MG_MODEL)
    model['type'] = MG_TYPE

    # add fields shown during addition of card
    for fieldName in fields:
        field = models.newField(fieldName)
        models.addField(model, field)
    
    # add templates shown during preview of card
    template = models.newTemplate('Mathgen')
    template['qfmt'] = card_front
    template['afmt'] = card_back

    models.addTemplate(model, template)
    models.add(model)    

    return model


def onMathgen(self):
    if mw.col.models.current()['name'] != MG_MODEL:
        tooltip('Mathgen will only work on "Mathgen" note types.')
    # find the highest existing variable
    highest = 0
    for name, val in list(self.note.items()):
        no = re.findall(r"\{\{m(\d+)::", val)
        if no:
            highest = max(highest, sorted([int(x) for x in no])[-1])

    highest += 1
    # must start at 1
    highest = max(1, highest)
    self.web.eval("wrap('{{m%d::', '}}');" % highest)


# add mathgen button into editor
def addMathgenButton(buttons, editor):
    key = QKeySequence('Ctrl+Shift+M')
    btn = editor.addButton(
            os.path.join(path, 'assets', 'logo.svg'),
            'mathgenbtn',
            lambda e=editor: onMathgen(e),
            keys = key,
            tip = f'Mathgen {(key.toString())}'
          )
    buttons.append(btn)

    return buttons
