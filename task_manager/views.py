from django.views.generic import TemplateView
import os

class IndexView(TemplateView):
    template_name = os.path.join("index.html")
