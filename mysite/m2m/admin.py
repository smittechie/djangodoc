from django.contrib import admin

from .models import Group, Membership, Person

# Register your models here.
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Membership)
