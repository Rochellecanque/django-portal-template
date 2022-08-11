#DJANGO Imports
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render

#Internationalization and Translations
from django.utils import translation

#CORE Models
from core import models

def context_maker (request, context):
    context['SupportedLanguages'] = models.SupportedLanguage.objects.all()
    return context


def togglelanguage(request, language_id):
    language = models.SupportedLanguage.objects.get(pk=language_id)

    translation.activate(language.languageKey)
    return redirect(request.META.get('HTTP_REFERER'))