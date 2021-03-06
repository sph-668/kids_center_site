from django import forms
from django.forms import ModelChoiceField


from .models import *

from django.forms import Field
from django.utils.translation import ugettext_lazy
Field.default_error_messages = {
    'required': ugettext_lazy("This field is mandatory."),
}
# this is gonna work
class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} ({})".format(obj.name, obj.age)


class MyModelChoiceField1(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.age

my_default_errors = {
    'required': 'Заполните поле',
    'invalid': 'Enter a valid value'
}


subjects = list(Subject.objects.values_list('sub', flat = True))
subjects.sort()
sub = []
for i in range (len(subjects)):
    sub.append([subjects[i], subjects[i]])

temp = list(Age.objects.values_list('age', flat = True))
ages = []
for i in range (len(temp)):
    ages.append([temp[i], temp[i]])

t = list(Time.objects.values_list('time', flat = True))
all_times = []
for i in range(len(t)):
    all_times.append([t[i], t[i]])

week = list(Days_of_the_week.objects.values_list('day', flat = True))
days_of_the_week = []
for i in range (len(week)):
    days_of_the_week.append([week[i], week[i]])

cabs = list(Cabinets.objects.values_list('cab', flat = True))
cabs.sort()
all_cabinets = []
for i in range (len(cabs)):
    all_cabinets.append([cabs[i], cabs[i]])


temp = list(Teacher.objects.values_list('name', flat=True))
temp = set(temp)
temp = list(temp)
temp.sort()
all_teachers = []
for i in range(len(temp)):
    all_teachers.append([temp[i], temp[i]])



class AppendTeacher(forms.Form):
    name = forms.CharField(max_length=50, error_messages=my_default_errors, required=True)
    lesson = forms.ChoiceField(choices=sub)


class AppendGroup(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.ChoiceField(choices=ages)

class AppendLesson(forms.Form):
    time = forms.ChoiceField(choices=all_times)
    day_of_week = forms.ChoiceField(choices=days_of_the_week)
    cabinet = forms.ChoiceField(choices=all_cabinets)
    group = MyModelChoiceField(queryset=Group.objects.all(), to_field_name="name", empty_label=None)
    teacher = forms.ChoiceField(choices=all_teachers)
    lesson = forms.ChoiceField(choices=sub)



class Show_on_date(forms.Form):
    group = MyModelChoiceField(queryset=Group.objects.all(), to_field_name="name", empty_label=None)
    date = forms.DateField()

class Show_on_many_params(forms.Form):
    group = MyModelChoiceField(queryset=Group.objects.all(), to_field_name="name", empty_label="-не выбрано-", required=False)
    subjects = list(Subject.objects.values_list('sub', flat=True))
    subjects.sort()
    sub = [[None, '-не выбрано-']]
    for i in range(len(subjects)):
        sub.append([subjects[i], subjects[i]])
    lesson = forms.ChoiceField(choices=sub, required=False)

    temp = list(Teacher.objects.values_list('name', flat=True))
    temp = set(temp)
    temp = list(temp)
    temp.sort()
    all_teachers = [[None, '-не выбрано-']]
    for i in range(len(temp)):
        all_teachers.append([temp[i], temp[i]])
    teacher = forms.ChoiceField(choices=all_teachers, required=False)

    cabs = list(Cabinets.objects.values_list('cab', flat=True))
    cabs.sort()
    all_cabinets = [[None, '-не выбрано-']]
    for i in range(len(cabs)):
        all_cabinets.append([cabs[i], cabs[i]])
    cabinet = forms.ChoiceField(choices=all_cabinets, required=False)

    t = list(Time.objects.values_list('time', flat=True))
    all_times = [[None, '-не выбрано-']]
    for i in range(len(t)):
        all_times.append([t[i], t[i]])
    time = forms.ChoiceField(choices=all_times, required=False)

    date = forms.DateField(required=False)

    temp = list(Age.objects.values_list('age', flat=True))
    all_ages = [[None, '-не выбрано-']]
    for i in range(len(temp)):
        all_ages.append([temp[i], temp[i]])
    age = forms.ChoiceField(choices=all_ages, required=False)

