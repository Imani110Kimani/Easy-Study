from django.contrib import admin
# Correctly import the students model
from .models import Students, Contact, Course

# Register the students model with the admin site
admin.site.register(Students)
admin.site.register(Contact)
admin.site.register(Course)









