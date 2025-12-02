from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    projects = Project.objects.filter(published=True).order_by('-created_at')[:6]
    return render(request, "home.html", {"projects": projects})

def about(request):
    return render(request, "about.html")

def projects_list(request):
    projects = Project.objects.filter(published=True).order_by('-created_at')
    return render(request, "projects.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {"project": project})

def contact(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Dev: چاپ در کنسول؛ Prod: ارسال ایمیل
            print("Contact submitted:", form.cleaned_data)
            # optionally send mail:
            # send_mail(form.cleaned_data['subject'], form.cleaned_data['message'],
            #           form.cleaned_data['email'], [settings.DEFAULT_FROM_EMAIL])
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def contact_success(request):
    return render(request, "contact_success.html")
