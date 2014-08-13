import os
import sys
import platform

import django
from django.views.generic import TemplateView

class AboutView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['python_version'] = sys.version
        context['django_version'] = django.get_version()
        context['django_path'] = os.path.dirname(django.__file__)
        try:
            context['platform'] = platform.uname()[2]
        except IndexError:
            context['platform'] = os.uname()[2]
        context['distro'] = platform.linux_distribution

        return context

