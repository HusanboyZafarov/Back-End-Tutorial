from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View, ListView
from .forms import MessageForm
from .models import Message, ClientsAboutUs, SmiAboutUs, BeforeAfter
# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"


class MasterClassView(ListView):
    model = BeforeAfter
    template_name = "master_class.html"
    context_object_name = "objects"


class FurnitureView(View):
    template_name = "furniture.html"
    form_class = MessageForm
    model = ClientsAboutUs
    context_object_name = "objects"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/furniture/')
        else:
            print("not valid")

        return render(request, self.template_name, {'form': form})


class AboutView(ListView):
    template_name = "about.html"
    model = SmiAboutUs
    context_object_name = "smiaboutus"


class RequestsView(ListView):
    template_name = "request.html"
    model = Message
    context_object_name = "messages"
