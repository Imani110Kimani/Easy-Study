from django.contrib import admin
# Correctly import the students model
from .models import Students, Contact, Course, Trainer, Enrollment

# Register the students model with the admin site
admin.site.register(Students)
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Enrollment)









