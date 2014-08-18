# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, unicode_literals

import uuid
import os

def get_upload_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)
