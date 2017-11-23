#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from .models import *
from xadmin.layout import *
from django.utils import timezone
from xadmin.plugins.inline import Inline
from .extras import *

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


#xadmin.site.register(Product, ProductAdmin)
#xadmin.site.register(ProductAttribute, ProductAttributeAdmin)


class Datamodel(models.Model):
    name = models.CharField(max_length=250, default='Datamodel-NCA-[Identifiant]', unique = True, verbose_name="Name", help_text="Schéma JSON du datamodel")
    description = models.TextField()
    date = models.DateTimeField(auto_now=False,
                               verbose_name="Date de création", default= timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Datamodel '
        verbose_name_plural = 'Datamodels '
    file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension_docs])

class SourceNCA(models.Model):
    name = models.CharField(max_length=250, default='Source-NCA-[Identifiant]', unique = True, verbose_name="Name", help_text="Source en xml | json | txt | csv")
    date = models.DateTimeField(auto_now=False,
                               verbose_name="Date de création", default= timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Source NCA '
        verbose_name_plural = 'Sources NCA '
    json = models.FileField(upload_to="documents/sources/%Y/%m/%d", validators=[validate_file_extension_json])
    otherFormat = models.FileField(upload_to="documents/sources/%Y/%m/%d", validators=[validate_file_extension_docs])

xadmin.site.register(Datamodel)
xadmin.site.register(SourceNCA)