from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Case (models.Model):
    case_id = models.IntegerField(default=0)
    subject_id = models.IntegerField(default=0)

    responded_by_1 = models.NullBooleanField(default=False, null=True)
    responded_by_2 = models.NullBooleanField(default=False, null=True)
    responded_by_3 = models.NullBooleanField(default=False, null=True)
    responded_by_4 = models.NullBooleanField(default=False, null=True)
    responded_by_5 = models.NullBooleanField(default=False, null=True)
    responded_by_6 = models.NullBooleanField(default=False, null=True)
    responded_by_7 = models.NullBooleanField(default=False, null=True)

class CaseQuestion(models.Model):
    subject_id = models.IntegerField(default=0)
    group_assigned = models.IntegerField(default=0)
    patient_summary = models.TextField(default='')
    occurrence_date = models.DateField()
    pressor_events_day_summary = models.TextField(blank=True, null=True)
    bp_trend_day_summary= models.TextField(blank=True, null=True)
    culture_all_summary = models.TextField(blank=True, null=True)
    abx_day_summary = models.TextField(blank=True, null=True)
    abx_all_summary = models.TextField(blank=True, null=True)
    lactate_all_summary = models.TextField(blank=True, null=True)
    measurement_day_summary = models.TextField(blank=True, null=True)
    dc_note = models.TextField(blank=True, null=True)
    tag = models.NullBooleanField(default=False, null=True)

    def __str__(self):
        temp = self.patient_summary
        if (self.tag == True ) :
            temp = temp + " (*Tagged*)"

        return temp



class CaseResponse(models.Model):
    question = models.ForeignKey(Case, on_delete=models.CASCADE)

    case_id = models.IntegerField(default=0)
    subject_id = models.IntegerField(default=0)
    occurrence_date = models.DateField()

    responder_id = models.IntegerField(default=0)

    answer = models.IntegerField(default=None)
    answer_secondary = models.IntegerField(default=None )
    primary_proportion = models.IntegerField(default=100, null=True)

    note = models.CharField(max_length=255, blank=True, null=True)

    tagged = models.BooleanField ( default = False  )
    tag1 = models.IntegerField()
    tag2 = models.IntegerField()

    confidence = models.IntegerField(default=None, null=True)
    confidence_why = models.TextField(default=None, null=True)