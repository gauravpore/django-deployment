from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio, Gallery, Contact


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)

# GALLERY
admin.site.register(Gallery)

# CONTACT FORM
admin.site.register(Contact)