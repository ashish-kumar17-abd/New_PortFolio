from django.shortcuts import render, get_object_or_404
from .models import Project  # Project model import karo

def home(request):
    # Latest 3 projects
    latest_projects = Project.objects.all().order_by('-id')[:3]
    context = {'latest_projects': latest_projects}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def projects(request):
    all_projects = Project.objects.all()  # sab projects fetch karo
    return render(request, "projects.html", {'projects': all_projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


# def contact(request):
#     return render(request, "contact.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


