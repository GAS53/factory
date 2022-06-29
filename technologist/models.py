from django.db import models

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


class Agregat_func(models.Model):
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
    agregat_func = models.OneToOneField(Agregat_func, on_delete=models.PROTECT)
    num_in_aggregat = models.PositiveSmallIntegerField(null=True)
    param = models.OneToOneField(Params, on_delete=models.PROTECT)
    socket = models.FileField(verbose_name='путь к сокету')
    crytiсal_= models.IntegerField(null=True, default=None)
    high = models.IntegerField(null=True, default=None)
    low = models.IntegerField(null=True, default=None)
    crytiсal_low = models.IntegerField(null=True, default=None)
    # number_of_measurements = models.IntegerField(default=604800)


class History_Params(models.Model): # может как то переработать чтобы каждый раз не указывать время
    device_id = models.OneToOneField(Devices, on_delete=models.PROTECT)
    pv = models.PositiveSmallIntegerField(null=True, default=None)
    op = models.PositiveSmallIntegerField(null=True, default=None)
    sp =models.PositiveSmallIntegerField(null=True, default=None)
    time = models.DateTimeField()

class Dedtcts(models.Model):
    ...







class History_params(models.Model):
    device_id = models.IntegerField()

