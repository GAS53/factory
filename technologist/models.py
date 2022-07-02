from importlib.resources import path
from authorization.models import CustomUser
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail

class Blocs(models.Model):
    id = models.AutoField(primary_key=True)
    min_description = models.CharField(max_length=30, verbose_name='название блока')
    max_description = models.CharField(null=True, max_length=256, verbose_name='полная расшифровка')

class Aggregates(models.Model):
    id = models.AutoField(primary_key=True)
    block_id = models.OneToOneField(Blocs, on_delete=models.PROTECT)
    num_in_block = models.PositiveSmallIntegerField()
    abb = models.CharField(max_length=2, verbose_name='буква обозначения функциональной работы')
    description = models.CharField(max_length=30, verbose_name='расшифровка названия')
    next_revision_date = models.DateField()
    next_comprehensive_test = models.DateField()


class Aggregat_func(models.Model):
    id = models.AutoField(primary_key=True)
    abb = models.CharField(max_length=2, verbose_name='буква обозначения функции агрегата')
    description = models.CharField(max_length=20, verbose_name='расшифровка названия')

class Params(models.Model):
    id = models.AutoField(primary_key=True)
    abb = models.CharField(max_length=5, verbose_name='букваы полная расшифровка прибора')
    description = models.CharField(max_length=20, verbose_name='расшифровка названия')

class Devices(models.Model):
    id = models.AutoField(primary_key=True)
    block_id = models.OneToOneField(Blocs, on_delete=models.PROTECT)
    aggregate_id = models.OneToOneField(Aggregates, on_delete=models.PROTECT)
    aggregat_func = models.OneToOneField(Aggregat_func, on_delete=models.PROTECT)
    num_in_aggregat = models.PositiveSmallIntegerField(null=True)
    param = models.OneToOneField(Params, on_delete=models.PROTECT)
    socket = models.FileField(verbose_name='путь к сокету')
    crytiсal_high= models.IntegerField(null=True, default=None)
    high = models.IntegerField(null=True, default=None)
    low = models.IntegerField(null=True, default=None)
    crytiсal_low = models.IntegerField(null=True, default=None)
    next_revision_date = models.DateField()
    alarm = models.BooleanField(default=False)
    # number_of_measurements = models.IntegerField(default=604800)


class History_Params(models.Model): # может как то переработать чтобы каждый раз не указывать время
    device_id = models.OneToOneField(Devices, on_delete=models.PROTECT)
    pv = models.PositiveSmallIntegerField(null=True, default=None)
    op = models.PositiveSmallIntegerField(null=True, default=None)
    sp =models.PositiveSmallIntegerField(null=True, default=None)
    time = models.DateTimeField()

class Defects(models.Model):
    id = models.AutoField(primary_key=True)
    defect_device = models.OneToOneField(Devices, null=True, default=None, on_delete=models.PROTECT)
    defect_aggregate = models.OneToOneField(Aggregates, null=True, default=None, on_delete=models.PROTECT)
    comment = models.CharField(max_length=512)
    who_find_defect = models.OneToOneField(CustomUser, on_delete=models.PROTECT)
    now_mechanic = models.DateTimeField(auto_now_add=True)
    now_electrician = models.DateTimeField(auto_now_add=True)
    now_KIP = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    planned_fix_it = models.DateTimeField()
    factual_fix_it = models.DateTimeField()


import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill


class Jobseeker(models.Model):
    photo = models.ImageField(verbose_name='Poster', upload_to='media/schems/')
