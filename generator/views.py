from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import FormClass


# Create your views here.


class HomeView(TemplateView):
    template_name = "home_view.html"


class AboutView(TemplateView):
    template_name = "about_view.html"


class GenerateView(View):
    context = {}
    template_name = "generate.html"

    def get(self, request, *args, **kwargs):
        form = FormClass()
        self.context["form"] = form
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = FormClass(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            self.context["word_from_view"] = name
            self.context["created"] = True
        else:
            self.context["created"] = False
        self.context["form"] = form
        return render(request, self.template_name, context=self.context)
