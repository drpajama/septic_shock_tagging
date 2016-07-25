from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CaseQuestion(models.Model):

    subject_id = models.IntegerField(default=0)
    group_assigned = models.IntegerField(default=0)
    patient_summary = models.TextField(default='')
    occurrence_date = models.DateField()
    pressor_events_day_summary = models.TextField()
    bp_trend_day_summary= models.TextField()
    culture_all_summary = models.TextField()
    abx_day_summary = models.TextField()
    abx_all_summary = models.TextField()
    lactate_all_summary = models.TextField()
    measurement_day_summary = models.TextField()
    dc_note = models.TextField()

    def __str__(self):
        return self.patient_summary


class CaseResponse(models.Model):
    question = models.ForeignKey(CaseQuestion, on_delete=models.CASCADE)

    case_id = models.IntegerField(default=0)
    subject_id = models.IntegerField(default=0)
    occurrence_date = models.DateField()

    responder_id = models.IntegerField(default=0)

    answer = models.IntegerField(default=None)
    note = models.CharField(max_length=255)

    tag1 = models.IntegerField()
    tag2 = models.IntegerField()
