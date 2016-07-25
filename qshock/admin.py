from django.contrib import admin
from .models import CaseQuestion
from .models import CaseResponse

# Register your models here.

admin.site.register(CaseQuestion)
admin.site.register(CaseResponse)