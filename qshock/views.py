from django.shortcuts import render, get_object_or_404
from django.template import loader
from qshock.models import CaseQuestion, CaseResponse
from django.http import Http404

# Create your views here.

from django.http import HttpResponse

def index(request):
    template = loader.get_template('qshock/index.html')

  #  responder = request.session.get('current_responder')

    context = {
        #'responder': str(responder)
    }

    return HttpResponse(template.render(context, request))

def dashboard(request):

    case_list = CaseQuestion.objects.all()


    try:
        responder_id = int(request.POST['responder_identity'])
        request.session.set('current_responder', responder_id)
    except:
        responder_id = request.session.get('current_responder')


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
        'case_list_not_responded': cases_not_responded
    }


    # it should return HttpResponse onject which contain he content for the requested page, or raising an exception such as Http404.
    return HttpResponse(template.render (context, request) )


def detail(request, case_id):

    case = get_object_or_404(CaseQuestion, pk = case_id)
    template = loader.get_template('qshock/detail.html')
    context = {
        'case': case
    }
    return HttpResponse(template.render( context, request) )


def answer(request, case_id):
    case = get_object_or_404(CaseQuestion, pk=case_id)
    choice = int(request.POST['answer'])
    note = request.POST['answer_text']
    responder_id = int(request.session.get('current_responder'))

    response = CaseResponse()
    response.question = case
    response.subject_id = case.subject_id
    response.case_id = case_id
    response.responder_id = responder_id
    response.answer = choice
    response.note = note

    response.occurrence_date = case.occurrence_date
    response.tag1 = 0
    response.tag2 = 0

    if responder_id != 999: # 999 is the test user
        response.save()

    template = loader.get_template('qshock/response_submitted.html')
    context = {}

    return HttpResponse(template.render(context, request))

