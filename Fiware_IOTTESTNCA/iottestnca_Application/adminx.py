#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import *
from xadmin.layout import *

from xadmin.plugins.inline import Inline


class ProductItemAdminInline(object):
    model = ProductItem
    extra = 3
    style = 'table'


class ProductAdmin(object):
    model = Product
    inlines = [ProductItemAdminInline]
    #form = forms.ProductForm
    form_layout = (
        Main(
            Fieldset('Produit', HTML('Le nom doit être détaillé'), 'name', 'code'),
            Inline(ProductItem),
            #TabHolder(
             #   Tab('Tab1', 'code', 'name'),
              #  Tab('Tab2', Field('price_ht', css_class="class1"))
            #)
        ),
        Side(
           Fieldset('Prix {{var1}}',  Row(PrependedText('price_ht', '&euro;', placeholder="0.0"), PrependedText('price_ttc', '&euro;', placeholder="0.0"))),
        )
        #PrependedText('price_ht', '&euro;', placeholder="0.0")
    )
class ProductAttributeValueAdminInline(object):
    model = ProductAttributeValue
    extra = 3
    style = 'table'


class ProductAttributeAdmin(object):
    model = ProductAttribute
    inlines = [ProductAttributeValueAdminInline]


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(ProductAttribute, ProductAttributeAdmin)