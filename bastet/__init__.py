import gettext
import locale
import os

basedir = os.path.abspath(os.path.dirname(__file__))
localedir = os.path.join(basedir, "locale")

_: gettext.GNUTranslations = gettext.translation(
    "messages", localedir, languages=[locale.getdefaultlocale()[0][:2]]
).gettext
