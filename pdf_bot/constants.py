import gettext

from telegram.ext import Filters

t = gettext.translation("pdf_bot", localedir="locale", languages=["en_GB"])
_ = t.gettext

TEXT_FILTER = Filters.text & ~Filters.command

# Bot constants
CHANNEL_NAME = "gunasekharravilla"
SET_LANG = "set_lang"

# PDF file validation constants
PDF_OK = 0
PDF_INVALID_FORMAT = 1
PDF_TOO_LARGE = 2

# PDF file constants
WAIT_DOC_TASK = 0
WAIT_PHOTO_TASK = 1
WAIT_CROP_TYPE = 2
WAIT_CROP_PERCENT = 3
WAIT_CROP_OFFSET = 4
WAIT_DECRYPT_PW = 5
WAIT_ENCRYPT_PW = 6
WAIT_FILE_NAME = 7
WAIT_ROTATE_DEGREE = 8
WAIT_SPLIT_RANGE = 9
WAIT_SCALE_TYPE = 10
WAIT_SCALE_PERCENT = 11
WAIT_SCALE_DIMENSION = 12
WAIT_EXTRACT_PHOTO_TYPE = 13
WAIT_TO_PHOTO_TYPE = 14
WAIT_TEXT_TYPE = 15

# Keyboard constants
CANCEL = _("Cancel")
DONE = _("Done")
BACK = _("Back")
BY_PERCENT = _("By Percentage")
BY_SIZE = _("By Margin Size")
PREVIEW = _("Preview")
DECRYPT = _("Decrypt")
ENCRYPT = _("Encrypt")
EXTRACT_PHOTO = _("Extract Photos")
TO_PHOTO = _("To Photos")
ROTATE = _("Rotate")
SCALE = _("Scale")
SPLIT = _("Split")
BEAUTIFY = _("Beautify")
TO_PDF = _("To PDF")
RENAME = _("Rename")
CROP = _("Crop")
COMPRESSED = _("Compressed")
PHOTOS = _("Photos")
REMOVE_LAST = _("Remove Last File")
TO_DIMENSIONS = _("To Dimensions")
EXTRACT_TEXT = _("Extract Text")
TEXT_MESSAGE = _("Text Message")
TEXT_FILE = _("Text File")
OCR = "OCR"
COMPRESS = _("Compress")

# Rotation constants
ROTATE_90 = "90"
ROTATE_180 = "180"
ROTATE_270 = "270"

# User data constants
PDF_INFO = "pdf_info"

# Payment Constants
PAYMENT = "payment"
PAYMENT_PAYLOAD = "payment_payload"
CURRENCY = "INR"
PAYMENT_PARA = "payment_para"
THANKS = _("Say Thanks 😁 (₹10)")
COFFEE = _("Coffee ☕ (₹30)")
BEER = _("Book 🍺 (₹50)")
MEAL = _("Meal 🍲 (₹100)")
PAYMENT_DICT = {THANKS: 10, COFFEE: 30, BEER: 50, MEAL: 100}
WAIT_PAYMENT = 0

# Datastore constants
USER = "User"
LANGUAGE = "language"

# Language constants
LANGUAGES = {
    "🇬🇧 English (UK)": "en_GB",
    "🇺🇸 English (US)": "en_US",    
    "🇮🇳 हिन्दी": "hi_IN",
}

LANGS_SHORT = {x.split("_")[0]: x for x in LANGUAGES.values()}
