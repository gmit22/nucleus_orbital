from django import forms
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


squash_options = '''University Sports Center, Court 4 0700 : 0800
University Sports Center, Court 4 0800 : 0900
University Sports Center, Court 4 0900 : 1000
University Sports Center, Court 4 1000 : 1100
University Sports Center, Court 4 1100 : 1200
University Sports Center, Court 4 1200 : 1300
University Sports Center, Court 4 1300 : 1400
University Sports Center, Court 4 1400 : 1500
University Sports Center, Court 4 1500 : 1600
University Sports Center, Court 4 1600 : 1700
University Sports Center, Court 4 1700 : 1800
University Sports Center, Court 3 0800 : 0900
University Sports Center, Court 3 0900 : 1000
University Sports Center, Court 3 1000 : 1100
University Sports Center, Court 3 1100 : 1200
University Sports Center, Court 3 1200 : 1300
University Sports Center, Court 3 1300 : 1400
University Sports Center, Court 3 1400 : 1500
University Sports Center, Court 3 1500 : 1600
University Sports Center, Court 3 1600 : 1700
University Sports Center, Court 3 1700 : 1800
University Sports Center, Court 3 1800 : 1900
University Sports Center, Court 2 0900 : 1000
University Sports Center, Court 2 1000 : 1100
University Sports Center, Court 2 1100 : 1200
University Sports Center, Court 2 1200 : 1300
University Sports Center, Court 2 1300 : 1400
University Sports Center, Court 2 1400 : 1500
University Sports Center, Court 2 1500 : 1600
University Sports Center, Court 2 1600 : 1700
University Sports Center, Court 2 1700 : 1800
University Sports Center, Court 2 1800 : 1900
University Sports Center, Court 2 1900 : 2000
University Sports Center, Court 1 1000 : 1100
University Sports Center, Court 1 1100 : 1200
University Sports Center, Court 1 1200 : 1300
University Sports Center, Court 1 1300 : 1400
University Sports Center, Court 1 1400 : 1500
University Sports Center, Court 1 1500 : 1600
University Sports Center, Court 1 1600 : 1700
University Sports Center, Court 1 1700 : 1800
University Sports Center, Court 1 1800 : 1900
University Sports Center, Court 1 1900 : 2000
University Sports Center, Court 1 2000 : 2100'''
basketball_options = '''Caged Court, Prince George's Park Residences 0700 : 0800
Caged Court, Prince George's Park Residences 0800 : 0900
Caged Court, Prince George's Park Residences 0900 : 1000
Caged Court, Prince George's Park Residences 1000 : 1100
Caged Court, Prince George's Park Residences 1100 : 1200
Caged Court, Prince George's Park Residences 1200 : 1300
Caged Court, Prince George's Park Residences 1300 : 1400
Caged Court, Prince George's Park Residences 1400 : 1500
Caged Court, Prince George's Park Residences 1500 : 1600
Caged Court, Prince George's Park Residences 1600 : 1700
Caged Court, Prince George's Park Residences 1700 : 1800
Court 1, Prince George's Park Residences 0800 : 0900
Court 1, Prince George's Park Residences 0900 : 1000
Court 1, Prince George's Park Residences 1000 : 1100
Court 1, Prince George's Park Residences 1100 : 1200
Court 1, Prince George's Park Residences 1200 : 1300
Court 1, Prince George's Park Residences 1300 : 1400
Court 1, Prince George's Park Residences 1400 : 1500
Court 1, Prince George's Park Residences 1500 : 1600
Court 1, Prince George's Park Residences 1600 : 1700
Court 1, Prince George's Park Residences 1700 : 1800
Court 1, Prince George's Park Residences 1800 : 1900
Court 2, Prince George's Park Residences 0900 : 1000
Court 2, Prince George's Park Residences 1000 : 1100
Court 2, Prince George's Park Residences 1100 : 1200
Court 2, Prince George's Park Residences 1200 : 1300
Court 2, Prince George's Park Residences 1300 : 1400
Court 2, Prince George's Park Residences 1400 : 1500
Court 2, Prince George's Park Residences 1500 : 1600
Court 2, Prince George's Park Residences 1600 : 1700
Court 2, Prince George's Park Residences 1700 : 1800
Court 2, Prince George's Park Residences 1800 : 1900
Court 2, Prince George's Park Residences 1900 : 2000
Main Court, University Sports Centre 1000 : 1100
Main Court, University Sports Centre 1100 : 1200
Main Court, University Sports Centre 1200 : 1300
Main Court, University Sports Centre 1300 : 1400
Main Court, University Sports Centre 1400 : 1500
Main Court, University Sports Centre 1500 : 1600
Main Court, University Sports Centre 1600 : 1700
Main Court, University Sports Centre 1700 : 1800
Main Court, University Sports Centre 1800 : 1900
Main Court, University Sports Centre 1900 : 2000
Main Court, University Sports Centre 2000 : 2100'''
tabletennis_options ='''Table Tennis : Prince George's Park Residences, PGPH 1200 : 1300
Table Tennis : Prince George's Park Residences, PGPH 1300 : 1400
Table Tennis : Prince George's Park Residences, PGPH 1400 : 1500
Table Tennis : Prince George's Park Residences, PGPH 1500 : 1600'''

squash_options = squash_options.split('\n')
basketball_options = basketball_options.split('\n')
tabletennis_options = tabletennis_options.split('\n')
a = []
b = []
c = []
for lt in squash_options:
    a.append((lt,lt))
for lt in basketball_options:
    b.append((lt,lt))
for lt in tabletennis_options:
    c.append((lt,lt))

squash_options = tuple(a)
basketball_options = tuple(b)
tabletennis_options = tuple(c)

class basketball(forms.Form):

    date = forms.DateField(label='booking date', widget = forms.SelectDateWidget())
    lt = forms.ChoiceField(choices=basketball_options)

class squash(forms.Form):

    date = forms.DateField(label='booking date', widget = forms.SelectDateWidget())
    lt = forms.ChoiceField(choices=squash_options)

class tabletennis(forms.Form):

    date = forms.DateField(label='booking date', widget = forms.SelectDateWidget())
    lt = forms.ChoiceField(choices=tabletennis_options)



