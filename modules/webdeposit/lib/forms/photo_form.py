import os
from wtforms import Form, \
                    TextField, \
                    FileField, \
                    FormField, \
                    SubmitField

from invenio.webinterface_handler_flask_utils import _
from invenio.webdeposit_load_fields import TitleField

__all__ = ['PhotoForm']


class Dimensions(Form):
    height = TextField('Height')
    width = TextField('Width')


class PhotoForm(Form):

    title = TitleField(_('Photo Title'))
    dimensions = FormField(Dimensions)
    file = FileField(_('File'))
    submit = SubmitField(_('Submit Photo'), widget=bootstrap_submit)

    #configuration variables
    _title = _("Submit a Photo")
    _drafting = True #enable and disable drafting