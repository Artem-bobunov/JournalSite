from django.db import models
from django.conf import settings


# Create your models here.
class Journal(models.Model):
    objectType = (
        ('ЗУ', 'ЗУ'),
        ('ОКС', 'ОКС'),
    )
    res_ch = (
        ('В работе', 'В работе'),
        ('На отправку', 'На отправку'),
        ('Подготовлено', 'Подготовлено'),
    )
    choicesZU = (
        ('земли сельскохозяйственного назначения','земли сельскохозяйственного назначения'),
        ('земли населенных пунктов','земли населенных пунктов'),
        ('земли особо охраняемых территорий и объектов','земли особо охраняемых территорий и объектов'),
        ('земли водного фонда','земли водного фонда'),
    )


    npp = models.IntegerField('N п/п', blank=True, null=True)
    numberinput = models.CharField('№ Входящий', blank=True, null=True,max_length=100)
    dateInput = models.DateField('Дата входящего', blank=True, null = True)
    date1 = models.DateField('Дата возникновения основания для определения КС',blank=True, null=True)
    viewObject = models.CharField('Вид объекта', blank=True, null=True, choices=objectType,max_length=100)
    categoryZU = models.CharField('Категория ЗУ', blank=True, null=True, choices=choicesZU,max_length=100)
    dateKP = models.DateField('Дата исх. № КП',blank=True, null=True)

    numberKP = models.CharField('Номер исх. КП.', blank=True, null=True,max_length=100)
    numberACT = models.CharField('№ акта',blank=True, null=True,max_length=100)
    dateACT = models.DateField('Дата акта',blank=True, null=True)
    countAllObj = models.IntegerField('Количество загруженных объектов',blank=True, null=True, default=0)
    countBalObj = models.IntegerField('Количество оцененных объектов',blank=True, null=True, default=0)
    countNBObj = models.IntegerField('Количество неоцененных объектов', blank=True, null=True, default=0)
    dateSend = models.DateField('Дата отправки по ФЗ (срок 10 раб дней)', blank=True, null=True)
    dateFactSend = models.DateField('Дата фактической отправки (3 дня после даты акта)',blank=True, null=True)

    sendMail = models.CharField('Номер сопроводительного письма Учреждения',blank=True, null=True,max_length=100)
    countObjXML = models.IntegerField('Количество объектов в XML',blank=True, null=True, default=0)
    note = models.CharField('Примечание',blank=True, null=True,max_length=100)
    duplicateObject = models.CharField('Повторяющиеся объекты',blank=True, null=True,max_length=100, default='0')
    anotherRegion = models.CharField('Другой регион',blank=True, null=True,max_length=100, default='0')
    negativeSquare = models.CharField('Отрицательная площадь',blank=True, null=True,max_length=100, default='0')
    BK = models.CharField('Б/К',blank=True, null=True,max_length=100, default='0')
    ZZ = models.CharField('ЗЗ',blank=True, null=True,max_length=100, default='0')
    LF = models.CharField('ЛФ',blank=True, null=True,max_length=100, default='0')
    PROM = models.CharField('ПРОМ',blank=True, null=True,max_length=100, default='0')
    ENK = models.CharField('ЕНК',blank=True, null=True,max_length=100, default='0')
    conditional = models.CharField('Условные',blank=True, null=True,max_length=100, default='0')

    CE1 = models.CharField('Условные Ошибки (Номер объекта недвижимости)', blank=True, null=True, max_length=40000)
    ENK1 = models.CharField('ЕНК (Номер объекта недвижимости)', blank=True, null=True, max_length=40000)
    NS1 = models.CharField('Отрицательная площадь (Номер объекта недвижимости)', blank=True, null=True, max_length=40000)
    DR1 = models.CharField('Другой регион (Номер объекта недвижимости)', blank=True, null=True, max_length=40000)
    userbti = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, blank=True)

    check = models.BooleanField(null=True, blank=True)
    
    res = models.CharField('Статус',null=True, blank=True,choices = res_ch,max_length=100)



class TechnicalError(models.Model):
    objectType1 = (
        ('ЗУ', 'ЗУ'),
        ('ОКС', 'ОКС'),
    )
    choicesZU1 = (
        ('земли сельскохозяйственного назначения', 'земли сельскохозяйственного назначения'),
        ('зземли населенных пунктов', 'земли населенных пунктов'),
        ('земли особо охраняемых территорий и объектов', 'земли особо охраняемых территорий и объектов'),
        ('земли водного фонда', 'земли водного фонда'),
    )
    npp = models.IntegerField("№ п/п", blank=True, null=True)
    numberinput = models.CharField('№ Входящий', blank=True, null=True,max_length=100)
    dateInput = models.DateField('Дата входящего', blank=True, null = True)
    date1 = models.DateField('Дата возникновения основания для определения КС',blank=True, null=True)
    viewObject = models.CharField('Вид объекта', blank=True, null=True, choices=objectType1,max_length=100)
    categoryZU = models.CharField('Категория ЗУ', blank=True, null=True, choices=choicesZU1,max_length=100)
    dateKP = models.DateField('Дата исх. № КП',blank=True, null=True)
    numberKP = models.CharField('Номер исх. КП.', blank=True, null=True,max_length=100)
    numberACT = models.CharField('№ акта',blank=True, null=True,max_length=100)
    dateACT = models.DateField('Дата акта',blank=True, null=True)
    numberSolution = models.CharField('№ Решения', blank=True, null=True,max_length=100)
    dateSolution = models.DateField('Дата решения',blank=True, null=True)

    countAllObj = models.CharField('Количество загруженных объектов',blank=True, null=True,max_length=100)
    countBalObj = models.CharField('Количество оцененных объектов', blank=True, null=True, max_length=100)
    countNBObj = models.CharField('Количество неоцененных объектов', blank=True, null=True, max_length=100)
    dateSend = models.DateField('Дата отправки по ФЗ (срок 10 раб дней)', blank=True, null=True)
    dateFactSend = models.DateField('Дата фактической отправки (3 дня после даты акта)', blank=True, null=True)

    sendMail = models.CharField('Номер сопроводительного письма Учреждения', blank=True, null=True, max_length=100)
    countObjXML = models.CharField('Количество объектов в XML', blank=True, null=True, max_length=100)
    note = models.CharField('Примечание', blank=True, null=True, max_length=100)
    userbti = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, blank=True)













