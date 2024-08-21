from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline
from .models import Home, About, Profile, Category, Skills, Projects, Work, Email, Phone, ProjectLink, ProjectRequirements, Highlights, Services

# Register your models here.

# HOME
admin.site.register(Home)

admin.site.register(Highlights)


# ABOUT
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
        EmailInline,
        PhoneInline,
    ]


# SKILLS
class SkillInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]
    

# SERVICES
admin.site.register(Services)

# PROJECTS
class ProjectLinkInline(NestedStackedInline):
    model = ProjectLink
    extra = 1

class ProjectRequirementsInline(NestedStackedInline):
    model = ProjectRequirements
    extra = 1

class ProjectInLine(NestedModelAdmin):
    model = Projects
    extra = 1
    inlines = [
        ProjectRequirementsInline,
        ProjectLinkInline,
    ]


admin.site.register(Projects, ProjectInLine)


# WORK
admin.site.register(Work)

