from django.db import models

# Create your models here.
class Advs(models.Model):
    title = models.CharField('Заголовок', max_length = 128) # max_length - обязательный параметр, макс кол-во символов
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits = 10, decimal_places = 2) # max_digits - макс кол-во цифр в числе, в том числе после запятой. decimal_places - кол-во знаков после запятой
    auction = models.BooleanField('Торг', help_text = 'Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add = True) # заполнение только при создании
    updated_at = models.DateTimeField(auto_now = True) # заполнение при любом обновлении
    class Meta:
        db_table = 'advertisements'
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'