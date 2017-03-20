from django.shortcuts import render, get_object_or_404
from django.template import loader
#from django.contrib import messages

from .models import CaseQuestion, CaseResponse, Case

from .forms import NameForm
from .forms import MainShockTypeForm
from .forms import UnusualShockTypeForm
from .forms import RequireSecondCause
from .forms import Slider
from .forms import SlideForm
from constants import *
import ClinicalData

from datetime import timedelta
from datetime import time
from datetime import date

from .fusioncharts import fusioncharts


# Create your views here.
# Think CRUD (Create, Retrieve, Update and Delete + List)

from django.http import HttpResponse
from django.http import HttpResponseRedirect


def test(request):

    template_path = 'qshock/test.html'

    print (request.user)
    return render(request, template_path, {})

def othershock(request, case_id):

    template = 'qshock/detail_othershock.html'
    context = {
        "case_id": case_id,
        "message": request.session['selected_message'],
    }
    return render (request, template, context )




def test_create(request):

    if request.method == 'POST':

        form = MainShockTypeForm()

        if request.POST['type'] == SEPTIC_SHOCK:
            print("It is septic shock!!")

        if request.POST['type'] == OTHER_SHOCK:
            request.session['selected_case_id'] = 1
            request.session['selected_message'] = 'Babo!!'
            return HttpResponseRedirect("/qshock/{case_id}/othershock".format(case_id = '1'))

    form = MainShockTypeForm()
    context = {
        "form": form,
    }

    template = 'qshock/test2.html'

    return render( request, template, context )


def index2(request):
    datasource = {}

    datasource["chart"] = {
        "caption": "Creatinine Level",
        "xaxisname": "DateTime",
        "yaxisname": "mg/dL",
        "numberprefix": "",
        "numbersuffix": "mg/dL",
        "theme": "ocean",
        "lineThickness": "2",
        "paletteColors": "#0075c2",
        "baseFontColor": "#333333",
        "yAxisValueDecimals": 1,
        "forceYAxisValueDecimals": 1,

        "anchorRadius": "6",

    }


    datasource["categories"] = [{
        "category": [
            {"label": '1/18 6am'},
            {"label": "Feb"},
            {"label": "Mar"},
            {"label": "Apr"},
            {"label": "May"},
            {"label": "Jun"},
            {"label": "Jul"},
            {"label": "Aug"},
            {"label": "Sep"},
            {"label": "Oct"},
            {"label": "Nov"},
            {"label": "Dec"}
        ]
    }]

    datasource["dataset"] = [ {
        "seriesname": "Cr Level",
        "renderas": "line",
        "showvalues": "0",
        "data": [
            {"value": 1.5},
            {"value": "1.6"},
            {"value": "2.0"},
            {"value": "3.7"},
            {"value": "4.4"},
            {"value": "5.6"},
            {"value": "7.3"},
            {"value": "6.5"},
            {"value": "3.3"},
            {"value": "2.1"},
            {"value": "1.0"},
            {"value": "0.8"}
        ]
        }
    ]

    # Create an object for the mscombi2d chart using the FusionCharts class constructor
    mscombi2dChart = fusioncharts.FusionCharts("zoomline", "ex3", "100%", 400, "chart-1", "json", datasource)
    template = loader.get_template('qshock/index.html')

    context = {
        'output' : mscombi2dChart.render(),
    }


    return HttpResponse( template.render( context, request) )


def index(request):
    template = loader.get_template('qshock/index.html')

  #  responder = request.session.get('current_responder')

    context = {
        #'responder': str(responder)
    }

    return HttpResponse(template.render(context, request))






def dashboard_neo(request):

    import pickle
    import os
    from django.conf import settings


  #  f = open(os.path.join(settings.BASE_DIR, 'shock_patients.data'))
  #  cases = pickle.load(f)


    try:
        responder_id = int(request.POST['responder_identity'])
        request.session['current_responder'] = responder_id
    except:
        responder_id = int(request.session.get('current_responder'))

    patient_id_list = []

    cases_db = Case.objects.order_by('?')
    cases_responded = []
    cases_not_responded = []

    for case_db in cases_db:
        responded_boolean = None

        if responder_id == 1:
            responded_boolean = case_db.responded_by_1
        elif responder_id == 2:
            responded_boolean = case_db.responded_by_2
        elif responder_id == 3:
            responded_boolean = case_db.responded_by_3
        elif responder_id == 4:
            responded_boolean = case_db.responded_by_4
        elif responder_id == 5:
            responded_boolean = case_db.responded_by_5
        elif responder_id == 6:
            responded_boolean = case_db.responded_by_6
        elif responder_id == 7:
            responded_boolean = case_db.responded_by_7
        else:
            responded_boolean = False

        if responded_boolean == True:
            cases_responded.append(case_db)
        else: # False or None
            cases_not_responded.append(case_db)


    template = loader.get_template('qshock/dashboard.html')


    context = {
        'responder_id': responder_id,
        'cases_responded' : cases_responded,
        'cases_not_responded' : cases_not_responded
    }

    '''
    case_list = CaseQuestion.objects.order_by('?')



    try:
        responder_id = int(request.POST['responder_identity'])
        request.session['current_responder'] = responder_id
    except:zzz
        responder_id = int(request.session.get('current_responder'))


    cases_responded  = []
    cases_not_responded = []



    for case in case_list:

        responded = False
        response_set = case.caseresponse_set.all()

        for single_response in response_set:
            if single_response.responder_id == responder_id:
                responded = True

        if responded == True:
            cases_responded.append (case)
        else:
            cases_not_responded.append (case)


    template = loader.get_template('qshock/dashboard.html')


    context = {
        'responder_id': responder_id,
        'case_list_responded': cases_responded,
        'case_list_not_responded': cases_not_responded,
        'number_all': len(case_list),
        'number_responded': len(cases_responded),
        'number_not_responded': len(cases_not_responded)
    }


    # it should return HttpResponse onject which contain he content for the requested page, or raising an exception such as Http404.
    return HttpResponse(template.render (context, request) )

    '''
    return HttpResponse(template.render (context, request) )

def dashboard(request):

    case_list = CaseQuestion.objects.order_by('?')

    try:
        responder_id = int(request.POST['responder_identity'])
        request.session['current_responder'] = responder_id
    except:
        responder_id = int(request.session.get('current_responder'))


    cases_responded  = []
    cases_not_responded = []



    for case in case_list:

        responded = False
        response_set = case.caseresponse_set.all()

        for single_response in response_set:
            if single_response.responder_id == responder_id:
                responded = True

        if responded == True:
            cases_responded.append (case)
        else:
            cases_not_responded.append (case)


    template = loader.get_template('qshock/dashboard.html')


    context = {
        'responder_id': responder_id,
        'case_list_responded': cases_responded,
        'case_list_not_responded': cases_not_responded,
        'number_all': len(case_list),
        'number_responded': len(cases_responded),
        'number_not_responded': len(cases_not_responded)
    }


    # it should return HttpResponse onject which contain he content for the requested page, or raising an exception such as Http404.
    return HttpResponse(template.render (context, request) )


def second(request, id):

    case = get_object_or_404(Case, pk = id)

    template = loader.get_template('qshock/secondfactor.html')
    primary = request.session['primary_type']



    context = {
        'case': case,
        'form' : MainShockTypeForm( primary ),
        'slider' : SlideForm(),
        'primary_type' : primary,
    }


    return HttpResponse(template.render( context, request) )


def str_list( list ):
    temp = ""

    if len(list) == 0:
        return "None"

    for single in list:
        try:
            temp = temp + str(single) + "\n"
        except TypeError:
            temp = temp + "Unknown Value (The data element might be damaged)\n"

    return temp

def chart_lab (chartname, case_summary, measurements, case_db, title = "Untitled", value_name = "unspecified", unit = "?", html_name = "unspecified", annotation = True):


    datasource = {}
    datasource["chart"] = {
        "caption": title,
        "xaxisname": "DateTime",
        "yaxisname": unit,
        "numberprefix": "",
        "numbersuffix": unit,
        "theme": "ocean",
        "lineThickness": "2",
        "paletteColors": "#0075c2",
        "baseFontColor": "#333333",
        "yAxisValueDecimals": 1,
        "forceYAxisValueDecimals": 1,

        "anchorRadius": "6",

    }

    x_axis = []
    y_axis = []
    index = 0
    today_index = -1

    for single in measurements:
        y_axis.append({"label": str(single.timepoint.month) + "-" + str(single.timepoint.day) + " / " + str(
            single.timepoint.hour) + ":00"})
        x_axis.append({"value": str(single.value)})

        if single.timepoint.month == case_summary.shock_date.month and single.timepoint.day == case_summary.shock_date.day:
            today_index = index

        index = index + 1

    if annotation == True:
        datasource["annotations"] = {
            "groups": [
                {
                    "id": "anchor-highlight",
                    "items": [
                        {
                            "id": "high-star",
                            "type": "circle",
                            "x": "$dataset.0.set." + str(today_index) + ".x",
                            "y": "$dataset.0.set." + str(today_index) + ".y",
                            "radius": "12",
                            "color": "#6baa01",
                            "border": "2",
                            "borderColor": "#f8bd19"
                        },
                        {
                            "id": "label",
                            "type": "text",
                            "text": "The current day",
                            "fillcolor": "#6baa01",
                            "rotate": "90",
                            "x": "$dataset.0.set." + str(today_index) + ".x",
                            "y": "$dataset.0.set." + str(today_index) + ".y-25"
                        }
                    ]
                }
            ]
        }

    datasource["categories"] = [{
        "category": y_axis
    }]

    datasource["dataset"] = [{
        "seriesname": value_name,
        "renderas": "line",
        "showvalues": "0",
        "data": x_axis
    }
    ]

    chart = fusioncharts.FusionCharts("zoomline", chartname, "100%", 400, html_name, "json", datasource)
    return chart


def detail2 (request, id):

    import pickle
    import os
    from django.conf import settings
    import require

    if request.method == "POST":
        type = request.POST['type']

        try:
            secondary = request.POST['0']
            if secondary == 'on':
                secondary = True
        except:
            secondary = False

        request.session['primary_type'] = type

        if secondary == True and (type != NO_SHOCK and type != UNDETERMINED):
            return HttpResponseRedirect("/qshock/{id}/secondfactor".format(id=id))


        if type == OTHER_SHOCK:
            request.session['selected_message'] = "success!"
            return HttpResponseRedirect("/qshock/{id}/othershock".format(id=id))


    case_db = get_object_or_404(Case, pk = id)
    f = open(os.path.join(settings.BASE_DIR, 'shock_patients.data'))

    case_summary_array =  pickle.load(f)
    case_summary = None

    for single in case_summary_array:

        if int(str(single.case_id)) == int(str(case_db.case_id)):
            case_summary = single


    creatinineChart = chart_lab("creatinine_chart", case_summary, case_summary.creatinine_measurements_all, case_db, title = "Creatinine Level", value_name= "Cr level", unit = 'mg/dL', html_name = "chart-creatinine")

    mapTodayChart = chart_lab("today_bp_chart", case_summary, case_summary.MAP_measurements_today, case_db, title = "Mean Arterial Pressure", value_name= "MAP", unit = 'mmHg', html_name = "chart-bp-today", annotation = False)

    mapYesterdayChart = chart_lab("yesterday_bp_chart", case_summary, case_summary.MAP_measurements_yesterday, case_db, title = "Mean Arterial Pressure (The day before)", value_name= "MAP", unit = 'mmHg', html_name = "chart-bp-yesterday", annotation = False)

    mapTomorrowChart = chart_lab("tomorrow_bp_chart", case_summary, case_summary.MAP_measurements_tomorrow, case_db, title = "Mean Arterial Pressure (Next Day)", value_name= "MAP", unit = 'mmHg', html_name = "chart-bp-tomorrow", annotation = False)

    #map_today = case_summary.MAP_measurements_today


    template = loader.get_template('qshock/detail2.html')
    context = {
        'case': case_db,
        'datetime': case_summary.shock_date,
        'dc_note' : case_summary.discharge_summary,
        'form' : MainShockTypeForm(),
        'checkbox': RequireSecondCause(),
        'pressor_today': str_list(case_summary.pressor_events),
        'pressor_tomorrow': str_list(case_summary.pressor_events_tomorrow),
        'pressor_yesterday': str_list(case_summary.pressor_events_yesterday),
        'creatinine_output': creatinineChart.render(),
        'map_today_output': mapTodayChart.render(),
        'map_yesterday_output': mapYesterdayChart.render(),
        'map_tomorrow_output': mapTomorrowChart.render(),
        'abx_events': str_list(case_summary.antibiotics_administration_events),
        'abx_events_all': str_list(case_summary.antibiotics_administration_events_all),
        'lactate_measurements': str_list(case_summary.lactate_measurements),
        'lactate_measurements_all': str_list(case_summary.lactate_measurements_all),
        'culture_sampling_all': str_list(case_summary.culture_sampling_events_all)
    }


    #return render (request, template, context )
    return HttpResponse(template.render( context, request) )


def detail(request, case_id):

    if request.method == "POST":
        # this is never executed

        print (request.POST)

    case = get_object_or_404(CaseQuestion, pk = case_id)
    template = loader.get_template('qshock/detail.html')
    context = {
        'case': case,
        'question_form' : NameForm(),
        'shock_type_form' : MainShockTypeForm(),
        'unusual_shock_form' : UnusualShockTypeForm()
    }

    #return render (request, template, context )
    return HttpResponse(template.render( context, request) )



def follow(request, case_id):

    if request.method == "POST":
        print (request.POST)

    case = get_object_or_404(CaseQuestion, pk=case_id)
    choice = int(request.POST['answer'])
    note = request.POST['answer_text']
    confidence = request.POST['confidenceradio']
    response_why = request.POST['confidencewhy']

    context = {
        'answer' : choice,
        'answer_text': note,
        'confidenceradio': confidence,
        'confidencewhy': response_why,
    }

    responder_id = int(request.session.get('current_responder'))


    response = CaseResponse()
    response.question = case
    response.subject_id = case.subject_id
    response.case_id = case_id
    response.responder_id = responder_id
    response.answer = choice
    response.note = note
    response.confidence = int(confidence)
    response.confidence_why = response_why

    response.occurrence_date = case.occurrence_date
    response.tag1 = 0
    response.tag2 = 0

    '''
    if (choice == 7):
        response.tagged = True

    if responder_id != 999: # 999 is the test user
        response_list = CaseQuestion.objects.all()
        for single in response_list:
            if single.id == case_id and single.responder_id == responder_id:
                single.delete()

        response.save()

    '''

    if choice == 4: # Unusual types of shock.
        template = loader.get_template('qshock/othershock.html')
    else:
        template = loader.get_template('qshock/follow.html')



    return HttpResponse(template.render(context, request))



def answer(request, case_id):

    case = get_object_or_404(CaseQuestion, pk=case_id)
    choice = int(request.POST['answer'])
    note = request.POST['answer_text']
    confidence = request.POST['confidenceradio']
    response_why = request.POST['confidencewhy']

    responder_id = int(request.session.get('current_responder'))


    response = CaseResponse()
    response.question = case
    response.subject_id = case.subject_id
    response.case_id = case_id
    response.responder_id = responder_id
    response.answer = choice
    response.note = note
    response.confidence = int(confidence)
    response.confidence_why = response_why

    response.occurrence_date = case.occurrence_date
    response.tag1 = 0
    response.tag2 = 0

    if (choice == 7):
        response.tagged = True

    if responder_id != 999: # 999 is the test user


        response.save()

    template = loader.get_template('qshock/response_submitted.html')
    context = {}

    return HttpResponse(template.render(context, request))

