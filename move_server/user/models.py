from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''用户模型类'''
    class Meta:
        db_table='m_user'
        verbose_name='用户'