from django.forms import *
from .models import *
import django_filters
from django_filters import DateFromToRangeFilter, AllValuesFilter, CharFilter, DateFilter, NumberFilter, ChoiceFilter, \
    RangeFilter, DateRangeFilter,ModelChoiceFilter
from django_filters.widgets import RangeWidget, LinkWidget

class TechnicalErrorFilter(django_filters.FilterSet):
    numberACT = CharFilter(widget=TextInput(attrs={'class': 'form-control'}), label="Номер акта")
    numberSolution = CharFilter(widget=TextInput(attrs={'class': 'form-control'}), label="№ решения")

    class Meta:
        model = TechnicalError
        fields = ['numberACT','numberSolution']

class JournalFilter(django_filters.FilterSet):
    objectType = (
        ('ОКС', 'ОКС'),
        ('ЗУ', 'ЗУ'),
    )
    numberinput = CharFilter(widget=TextInput(attrs={'class': 'form-control'}), label="№ Входящий")
    dateInput = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type': 'date'}),label="Дата входящего")
    date1 = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type': 'date'}),label="Дата определения КС")
    viewObject = ChoiceFilter(widget = Select(attrs={'class': 'form-control'}),choices = objectType,label="Вид объекта")
    dateFacrSend = DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control','type': 'date'}),label="Дата фактической отправки")


    class Meta:
        model = TechnicalError
        fields = ['numberinput','dateInput','date1','viewObject','dateFacrSend']

class exportCSV(django_filters.FilterSet):
    class Meta:
        model = Journal
        fields = ['npp', 'numberinput', 'dateInput', 'date1','viewObject','categoryZU',
                             'dateKP','numberKP','numberACT','dateACT','countAllObj','countBalObj',
                             'countNBObj', 'dateSend', 'dateFactSend', 'sendMail', 'countObjXML',
                             'note', 'duplicateObject', 'anotherRegion', 'negativeSquare','BK', 'ZZ',
                             'LF', 'PROM', 'ENK', 'conditional','CE1','ENK1','NS1','DR1']
                             
class exportCSVTE(django_filters.FilterSet):
    class Meta:
        model = TechnicalError
        fields = ['npp', 'numberinput', 'dateInput', 'date1','viewObject','categoryZU',
                             'dateKP','numberKP','numberACT','dateACT','numberSolution','dateSolution',
                             'countAllObj','countBalObj',
                             'countNBObj', 'dateSend', 'dateFactSend', 'sendMail', 'countObjXML',
                             'note']                          