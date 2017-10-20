# -*- coding: utf-8 -*-
from django.conf.urls import url, include

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
]
