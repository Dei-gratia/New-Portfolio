from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from .fields import OrderField

# Create your models here.

# HOME SECTION
class Home(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    greeting = models.CharField(max_length=20)
    career = models.CharField(max_length=50)
    summary = models.TextField(blank=False)
    picture = models.ImageField(upload_to='home/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Highlights(models.Model):
    icon = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, default=0, for_fields=None)
    class Meta:
        ordering = ['order']
     
    def __str__(self):
        return f'{self.title} Highlight'



# ABOUT SECTION
class About(models.Model):
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.updated}'
    
class Email(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    primary = models.BooleanField()

class Phone(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    primary = models.BooleanField()

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=254)
    social_icon = models.CharField(max_length=100, blank=True)
    order = OrderField(blank=True, default=0, for_fields=['about'])
    class Meta:
        ordering = ['order']


# SERVICES SECTION
class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    icon = models.CharField(max_length=100, blank=True)
    order = OrderField(blank=True, default=0, for_fields=None)

    def __str__(self):
        return f'{self.title} Services'


# SKILLS SECTION
class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)
    order = OrderField(blank=True, default=0, for_fields=None)
    class Meta:
        ordering = ['order']

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(
        Category, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, blank=True)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    order = OrderField(blank=True, default=0, for_fields=['category'])
	
    class Meta:
        ordering = ['order']


# PROJECTS SECTION
class Projects(models.Model):
    image = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField()
    future_scope = models.TextField(blank=True)
    order = OrderField(blank=True, default=0, for_fields=None)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['order']

    def __str__(self):
        return f'{self.title} project'
    
    def first_link(self):
        return self.links.first()

class ProjectRequirements(models.Model):
    project = models.ForeignKey(Projects, related_name='requirements', on_delete=models.CASCADE)
    technology = models.CharField(max_length=254)
    icon = models.CharField(max_length=100, blank=True)
    order = OrderField(blank=True, default=0, for_fields=['project'])
    class Meta:
        ordering = ['order']

class ProjectLink(models.Model):
    project = models.ForeignKey(Projects, related_name='links', on_delete=models.CASCADE)
    link_text = models.CharField(max_length=50)
    link = models.URLField(max_length=254)
    icon = models.CharField(max_length=100, blank=True)
    order = OrderField(blank=True, default=0, for_fields=['project'])
    class Meta:
        ordering = ['order']
		


# WORK SECTION
class Work(models.Model):
    organisation = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.role} at {self.organisation}'


