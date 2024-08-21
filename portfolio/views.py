from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import Home, About, Profile, Category, Projects, Work, Email, Phone, Highlights, Services
import os
from django.conf import settings

# Create your views here.
def index(request):
	home = Home.objects.latest('updated')
	about = About.objects.latest('updated')
	highlights = Highlights.objects.all()
      
	# Services
	services = Services.objects.all()
     
    # Projects
	projects = Projects.objects.all()
	
    
	# Skills
	categories = Category.objects.all()
	print(categories)
     
	# Email and Phone
	email = ''
	phone = ''
	if Email.objects.filter(primary=True):
		email = Email.objects.get(primary=True)
	if Phone.objects.filter(primary=True):
		phone = Phone.objects.get(primary=True)

	context = {
        'home': home,
		'about': about,
		'highlights': highlights,
        'services': services,
        'projects': projects,
        'categories': categories,
       
        'email': email,
        'phone': phone,
    }

	return render(request, 'index.html', context)


def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Nenyasha_Madyavanhu_Resume_2024.pdf')  # Adjust this path to your file
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response
    else:
        raise Http404("Resume not found.")