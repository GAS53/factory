from pyexpat import model
from django.db import models
from technologist.models import Defects
from authorization.models import CustomUser


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    is_over_date = models.DateField()



class Technical_Task(Tasks):
    # task_id = models.OneToOneField(Tasks, on_delete=models.DO_NOTHING)
    task = models.OneToOneField(Defects, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=500, verbose_name='комментарий к заданию')

class Other_Task(Tasks):
    # task_id = models.OneToOneField(Tasks, on_delete=models.DO_NOTHING)
    task_name = models.CharField(verbose_name='название', max_length=50)
    comment = models.CharField(max_length=500,verbose_name='комментарий к заданию')
    target = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    planned_fix_it = models.DateTimeField()
    factual_fix_it = models.DateTimeField()
    check_it = models.BooleanField(default=False)