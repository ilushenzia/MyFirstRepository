from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

user = get_user_model()

class Advs(models.Model):
    title = models.CharField('Заголовок', max_length = 128) # max_length - обязательный параметр, макс кол-во символов
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits = 10, decimal_places = 2) # max_digits - макс кол-во цифр в числе, в том числе после запятой. decimal_places - кол-во знаков после запятой
    auction = models.BooleanField('Торг', help_text = 'Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add = True) # заполнение только при создании
    updated_at = models.DateTimeField(auto_now = True) # заполнение при любом обновлении
    user = models.ForeignKey(user, verbose_name = 'пользователь', on_delete = models.CASCADE) # делаем так, чтобы в объявлении было видно, кто автор. опредляем поведение постов при удалении пользователя. CASCAD - удаление всего, что связано с пользователем
    image = models.ImageField('изображение', upload_to = 'advs/')

    @admin.display(description = 'дата создания') # создание столбца с красивым отображением времени создания объявления
    def created_date(self):
        if self.created_at.date() == timezone.now().date(): # если выложили сегодня, то
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color : green; font-weight : bold">Сегодня в {}</span>', created_time # зелёным цветом показываем только время создания
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S') # если нет, то полностью пишем дату и время. После добавляем в admin в list_display

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "text-shadow : 0 0 2px Lime; font-weight : bold">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description = 'Изображение')
    def image_func(self):
        if self.image:
            return format_html(
                '<img src = "{}" style = "width : 55px;">', self.image.url
            )
        return 'no image'

    class Meta:
        db_table = 'advertisements' # отображение названия
    def __str__(self): # настройка отображения при запросе через
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

    def get_absolute_url(self):
        return reverse('adv', kwargs={'pk':self.pk})