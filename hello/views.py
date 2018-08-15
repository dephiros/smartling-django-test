# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.utils.translation import pgettext
from django.shortcuts import render


def hello_view(request):
    return HttpResponse(pgettext("Hello {}".format('world'), 'hello view'))
