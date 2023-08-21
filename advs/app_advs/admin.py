from django.contrib import admin
from .models import Advs
from django.db.models.query import QuerySet

# Register your models here.
class AdvsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date', ] # столбцы для отображения в таблице, сюда добавил функцию created_date для красивого отображения
    list_filter = ['price', 'auction', 'created_at', 'updated_at', ] # способы фильтрации
    actions = ['make_action_as_false', 'make_action_as_true'] # методы для выбранных записей
    fieldsets = (
        ('Общие', {# название блока
            'fields' : (
                'title', 'description'# содержимое блока: в данном случае название и описание
            )
        }),
        ('Финансы', {
            'fields': (
                'price', 'auction'
            ),
            'classes' : ['collapse'] # функция скрытия/появления блока (show/hide)
        }),
    )

    @admin.action(description = 'убрать возможность торга') # создание методов для выбранных записей через декоратор
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description = 'добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)

admin.site.register(Advs, AdvsAdmin) # подключение модели бд и админской модели в админку