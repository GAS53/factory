from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


class CustomUser(AbstractBaseUser, PermissionsMixin):
    login_validator = ASCIIUsernameValidator()
    username = models.CharField(max_length=128, unique=True, 
        help_text = ('Не больше 128 символов цифры и латинские буквы'),
        validators = [login_validator], verbose_name='Логин',
        error_messages= {"unique": ("Пользователь с таким логином уже существует")})
    password = models.CharField(verbose_name='Пароль', max_length=256)
    first_name = models.CharField(verbose_name='имя', max_length=128, blank=False)
    last_name = models.CharField(verbose_name='фамилия', max_length=128, blank=False)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    phone = models.CharField(verbose_name='Номер телефона в формате 9.. ... .. ..', max_length=10)
    date_of_birth = models.DateField(verbose_name='День рождения', null=True)
    is_active = models.BooleanField(default=True)
    is_technologist = models.BooleanField(default=False, verbose_name='Технолог')
    is_mechanic = models.BooleanField(default=False, verbose_name='механик')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания учетной записи')
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'phone']
    EMAIL_FIELD = "email"

    class Meta:
        verbose_name = ('пользователь')
        verbose_name_plural = ('пользователи')



    def get_name(self):
        return self.first_name

    def make_active(self):
        self.is_active = True
        self.save()
    
    def delete(self):
        self.is_active = False
        self.save()

    def make_technologist(self, val=True):
        self.is_technologist = val

    def make_mechanic(self, val=True):
        self.is_mechanic = val





