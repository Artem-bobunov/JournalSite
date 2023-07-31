from django.shortcuts import render, redirect
from .forms import journalForms
from  .models import Journal
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .filter import JournalFilter,exportCSV
import time
import datetime
import csv
import docxtpl
import numpy as np
from .logger import LoggerPasport
from django.db.models import Q


# Create your views here.
BLOG_POSTS_PER_PAGE = 20

def exportcsv(request):
    obj = Journal.objects.all()
    # id_build = Building.objects.latest('id').id
    # print(id_build)
    myFilter = exportCSV(request.GET, queryset=obj)
    obj = myFilter.qs
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Article_16_237.csv"'
    writer = csv.writer(response)
    writer.writerow(['№ пп', '№ Входящий', 'Дата входящего',
                     'Дата возникновения основания для определения КС', 'Вид объекта','Категория ЗУ',
                     'Дата исх. № КП','Номер исх. КП.', '№ акта','Дата акта','Количество загруженных объектов',
                     'Количество оцененных объектов','Количество неоцененных объектов', 'Дата отправки по ФЗ (срок 10 раб дней)',
                     'Дата фактической отправки (3 дня после даты акта)', 'Номер сопроводительного письма Учреждения',
                     'Примечание','Повторяющиеся объекты','Другой регион', 'Отрицательная площадь', 'Б/К',
                     'ЗЗ', 'ЛФ','ПРОМ','ЕНК','Условные','Условные Ошибки (Номер объекта недвижимости)', 'ЕНК (Номер объекта недвижимости)',
                     'Отрицательная площадь (Номер объекта недвижимости)','Другой регион (Номер объекта недвижимости)'])

    for e in obj.values_list('npp', 'numberinput', 'dateInput', 'date1','viewObject','categoryZU',
                             'dateKP','numberKP','numberACT','dateACT','countAllObj','countBalObj',
                             'countNBObj', 'dateSend', 'dateFactSend', 'sendMail',
                             'note', 'duplicateObject', 'anotherRegion', 'negativeSquare','BK', 'ZZ',
                             'LF', 'PROM', 'ENK', 'conditional','CE1','ENK1','NS1','DR1'):
        writer.writerow(e)
    return response


def home(request):
    list = Journal.objects.all().order_by('-id')
    
    myFilter = JournalFilter(request.GET, queryset=list)
    list = myFilter.qs
    counts = list.count()
    id_journal = np.array(list.values_list('id', flat=True))
    print(id_journal)
    dinput = np.array(list.values_list('date1',flat=True))

    res_sum = []

    for i in id_journal:
        summ = Journal.objects.get(pk = i)
        res_sum.append(int(summ.countAllObj))
        res_sum.append(int(summ.duplicateObject))
        res_sum.append(int(summ.anotherRegion))
        res_sum.append(int(summ.negativeSquare))
        res_sum.append(int(summ.BK))
        res_sum.append(int(summ.ZZ))

        res_sum.append(int(summ.LF))
        res_sum.append(int(summ.PROM))
        res_sum.append(int(summ.ENK))
        res_sum.append(int(summ.conditional))
    res_sum1 = sum(res_sum)
    count = []
    c_xml = []
    count_L = []
    count_M = []
    for i in id_journal:
        summ = Journal.objects.get(pk = i)
        count.append(int(summ.countAllObj))
        c_xml.append(int(summ.countObjXML))
    count_sum = sum(count)
    for i in id_journal:
        summ = Journal.objects.get(pk=i)
        count_L.append(int(summ.countBalObj))
        count_M.append(int(summ.countNBObj))
    count_L_arr = sum(count_L)
    pcount_M_arr = sum(count_M)
    
    paginator = Paginator(list, BLOG_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    
    datesearch = list.values_list('dateInput',flat=True).exclude(dateInput__isnull=True)
    date_res = []
    for i in datesearch:
        date_res.append(i.strftime('%d.%m.%Y'))
    date_first = str(date_res[0])
    #print(date_first)
    date_last = str(date_res[-1])
    #Текущая дата
    current_date = str(datetime.datetime.now().date())
    date2 = datetime.datetime.strptime(current_date, '%Y-%m-%d')
    date_now = date2.strftime('%d.%m.%Y')
    #Количество обектов ЗУ
    zu = list.filter(viewObject = 'ЗУ').count()
    oks = list.filter(viewObject = 'ОКС').count()
    document = docxtpl.DocxTemplate('C:\\JournalSite\\journal_set\\media\\logger\\Отчет_Кошелева.docx')
    context_doc = {'counts': counts, 'oks': oks,'zu':zu,'date_now':date_now,'res_sum1':res_sum1,'count_sum':count_sum,'count_L_arr':count_L_arr,'count_M_arr':pcount_M_arr,'date_first':date_first,'date_last':date_last}
    document.render(context_doc)
    document.save('C:\\JournalSite\\journal_set\\media\\Отчет'+'_'+ date_now + '.docx' )
    file_download = 'Отчет'+'_'+ date_now + '.docx'
                #return file_download
    return render(request,'home.html',{'file_download':file_download,'list':list,'page':pages, 'filter':myFilter, 'counts':counts,'res_sum1':res_sum1,'count_sum':count_sum,'count_L_arr':count_L_arr,'count_M_arr':pcount_M_arr})

@login_required
def create(request):
    ca = None
    cb = None
    cn = None
    if request.method == "POST":
        journal_form = journalForms(request.POST or None)
        if journal_form.is_valid():
            try:
                ca = journal_form.cleaned_data['countAllObj']
                
                instance = journal_form.save()
                instance.userbti = request.user
                instance.countObjXML = ca
                instance.save()
                x = LoggerPasport(request.user, instance.numberACT)
                x.add_record()

                print("Выполнилось")
                return redirect('/')
            except:
                print("Не удалось сохранить")
    else:
        journal_form = journalForms()
    return render(request,'create.html',{'form':journal_form})

def detail(request,id):

    if request.method=="GET":
        try:
            detail = Journal.objects.get(id=id)
        except:
            print("Детали не работают")
    return render(request,'detail.html',{'details':detail})
    
@login_required
def update (request,id):

    journal = Journal.objects.get(id=id)
    form1 = journalForms(instance=journal)
    if request.method == 'POST':
        form1 = journalForms(request.POST or None,instance = journal)
        if form1.is_valid():
                try:
                    instance = form1.save()
                    instance.userbti = request.user
                    if form1.cleaned_data['check'] == True:
                        # Шаблон из 6 нулей
                        shablon = ['0', '0', '0', '0', '0', '0']
                        # Вывести последний id
                        last_id = Journal.objects.values_list('id',flat=True).get(id=id)
                        #last_id += 1
                        max_nact = []
                        for i in Journal.objects.all().exclude(numberACT__isnull=True):
                            nact = i.numberACT
                            max_nact.append(int(nact.split('АОКС-34/2022/')[1]))

                        max_value_for_act = max(max_nact) + 1
                        print(max_value_for_act)
                        len_vst = len(str(max_value_for_act))
                        split_len_vst = shablon[:-len_vst]
                        int_res = ''.join(split_len_vst) + str(max_value_for_act)
                        res_act_num = 'АОКС-34/2022/' + str(int_res)
                        instance.numberACT = res_act_num
                        #print('Сюда я дошел')
                    ca = form1.cleaned_data['countAllObj']
                    cb = form1.cleaned_data['countBalObj']
                    cn = form1.cleaned_data['countNBObj']
                    res_xml = int(ca)+int(cb)+int(cn)
                    instance.countObjXML = res_xml
                    instance.save()
                    x = LoggerPasport(instance.userbti,instance.numberACT)
                    x.update_record()
                    return redirect('/')

                except Exception as e:
                    print("Не удалось сохранить данные, ошибка:",e)
    else:
        form1 = journalForms()


    return render(request, 'update.html', {'form': form1})


def search(request):
    start_time = time.time()
    query_dict = request.GET
    query = query_dict.get("q")
    list_object = None
    if query is not None:
        list_object = Journal.objects.filter(Q(numberinput__icontains=query) |
                                                  Q(viewObject__icontains=query) |
                                                  Q(categoryZU__icontains=query))
    print(list_object.values())
    paginator = Paginator(list_object, BLOG_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    try:
        pages = paginator.page(page_number)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    count_oblect = list_object.count()

    return render(request, 'home.html', {'page':pages,'list_object':list_object,'count_oblect':count_oblect})

