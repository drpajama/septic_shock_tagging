from django.contrib import admin
from .models import CaseQuestion
from .models import CaseResponse

# Register your models here.

admin.site.register(CaseQuestion)



@admin.register(CaseResponse)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'subject_id', 'responder_id', 'answer', 'note', 'tagged')
    pass