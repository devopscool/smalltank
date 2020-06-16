from django.conf import settings

ENTRY_BASIC_MODEL = getattr(settings, 'BASIC_MODEL',
                            'core.models_bases.entry.AbstractEntry')

UPLOAD_DEST = getattr(settings, 'UPLOAD_DEST', 'uploads/smalltank')
PAGINATION = getattr(settings, 'PAGINATION', 10)