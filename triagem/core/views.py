# View core

from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from utils.decorators import LoginRequiredMixin

class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        return reverse('home')

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/home.html'

class AboutView(TemplateView):
	template_name = 'core/about.html'
