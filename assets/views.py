from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "content/about.html"

class PrivacyView(TemplateView):
    template_name = "content/privacy.html"

class TermsView(TemplateView):
    template_name = "content/terms.html"
