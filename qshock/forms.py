
from django import forms
from constants import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UnusualShockTypeForm(forms.Form):
    ANAPHYLAXIS, OBSTRUCTIVE = 'anaphylaxis', 'obstructive_shock'
    TYPE_CHOICES = (
        (ANAPHYLAXIS, 'Anaphylactic Shock'),

    )

    def __init__(self, *args, **kwargs):
        super(UnusualShockTypeForm, self).__init__(*args, **kwargs)
        self.fields['choices'] = forms.ChoiceField( choices = self.TYPE_CHOICES, widget=forms.RadioSelect)
'''
    type = forms.ChoiceField(
        choices = TYPE_CHOICES, widget=forms.RadioSelect
    )


'''

class RequireSecondCause(forms.Form):
    def __init__(self, data=None, *args, **kwargs):
        super(RequireSecondCause, self).__init__(data, *args, **kwargs)
        self.fields[0] = forms.BooleanField(initial=False, required=False)

    #require_second_cause = forms.BooleanField()

class MainShockTypeForm(forms.Form):

    '''TYPE_CHOICES = (
        (SEPTIC_SHOCK, 'Septic Shock'),
        (CARDIOGENIC_SHOCK, 'Cardiogenic Shock'),
        (HYPOVOLEMIC_SHOCK, 'Hypovolemic Shock'),
        (OTHER_SHOCK, 'Other Shock'),
        (NO_SHOCK, 'No Shock'),
        (UNDETERMINED, 'Undetermined')
    )'''

    '''type = forms.ChoiceField(
        choices=TYPE_CHOICES, widget=forms.RadioSelect)'''

    def build_choices(self, exclude=None):

        temp_array = []

        if exclude != SEPTIC_SHOCK:
            temp_array.append ( (SEPTIC_SHOCK, 'Septic Shock') )

        if exclude != CARDIOGENIC_SHOCK:
            temp_array.append ( (CARDIOGENIC_SHOCK, 'Cardiogenic Shock') )

        if exclude != HYPOVOLEMIC_SHOCK:
            temp_array.append ( (HYPOVOLEMIC_SHOCK, 'Hypovolemic Shock') )

        if exclude != OTHER_SHOCK:
            temp_array.append ( (OTHER_SHOCK, 'Other Shock') )

        if exclude == None:
            temp_array.append ( (NO_SHOCK, 'No Shock')  )
            temp_array.append( (UNDETERMINED, 'Undetermined') )

        self.TYPE_CHOICES = tuple (temp_array)

    def __init__(self, primary=None, *args, **kwargs):
        super(MainShockTypeForm, self).__init__(None, *args, **kwargs)

        self.build_choices( exclude = primary )
        self.fields['type'] = forms.ChoiceField(choices=self.TYPE_CHOICES, widget=forms.RadioSelect)



class TypeForm(forms.Form):
    SHOCK, NOSHOCK = 'shock', 'no_shock'
    TYPE_CHOICES = (
        (SHOCK, 'Shock'),
        (NOSHOCK, 'No shock'),
    )
    type = forms.ChoiceField(
        choices=TYPE_CHOICES, widget=forms.RadioSelect)
    send_date = forms.DateTimeField(label="--", required=False)

    def __init__(self, data=None, *args, **kwargs):
        super(TypeForm, self).__init__(data, *args, **kwargs)

        '''
        if data:
            print data.get('type', None)

        if data and data.get('type', None) == self.NOSHOCK:

            self.fields['send_date'].required = True

        '''

        # If 'later' is chosen, set send_date as required
        ##if data and data.get('type', None) == self.NOSHOCK:
        ##


import floppyforms as forms

class Slider(forms.RangeInput):
    min = 0
    max = 100
    step = 5
    template_name = 'slider.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }


class Slider(forms.RangeInput):
    min = 0
    max = 100
    step = 10
    template_name = 'slider.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }


class SlideForm(forms.Form):
    num = forms.IntegerField(widget=Slider, label= "Ratio of Contribution (each step = 10%, In the middle = 50%/50%)")

    def clean_num(self):
        num = self.cleaned_data['num']
        if not 0 <= num <= 100:
            raise forms.ValidationError("Enter a value between 0 and 100")

        if not num % 10 == 0:
            raise forms.ValidationError("Enter a multiple of 5")
        return num