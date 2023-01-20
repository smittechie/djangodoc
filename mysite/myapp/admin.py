from django.contrib import admin

from .models import Person, Group, Person1, Membership

# Register your models here.
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Person1)
admin.site.register(Membership)
