from django.shortcuts import render
from apps.models import App

# Create your views here.
def index(request):
    template_name="accounts/landing-page.html"
    apps = App.objects.all()
    args={'apps':apps}
    return render(request,template_name,args)


def app(request):
    template_name="accounts/app.html"
    apps = App.objects.all()
    args={'apps':apps}
    return render(request,template_name,args)