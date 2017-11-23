#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import *
import django_select2


class MultiAttribute(django_select2.AutoModelSelect2MultipleField):
    queryset = ProductAttributeValue.objects
    search_fields = ['value__icontains', ]


class ProductItemForm(forms.ModelForm):
    attributes = MultiAttribute(required=False)