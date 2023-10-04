from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Очистка таблицы 'catalog_category'
        Category.objects.all().delete()

        category_list = [
            {'category_name': 'ПЛК', 'category_description': 'Программируемые логические контроллеры'},
            {'category_name': 'Модули расширения', 'category_description': 'Модули расширения для ПЛК'},
            {'category_name': 'Промышленные компьютеры', 'category_description': 'Компьютеры для сервера умного дома'},
            {'category_name': 'Коммутационные устройства',
             'category_description': 'Устройства для управления питанием объектов'},
            {'category_name': 'Датчики освещения', 'category_description': 'Датчики освещения'},
            {'category_name': 'Датчики температуры', 'category_description': 'Датчики температуры'},
            {'category_name': 'Датчики утечек', 'category_description': 'Датчики утечек'},
            {'category_name': 'Датчики движения', 'category_description': 'Датчики движения'},
            {'category_name': 'Охранные извещатели', 'category_description': 'Извещатели охранного комплекса'},
            {'category_name': 'Пожарные извещатели', 'category_description': 'Извещатели противопожарного комплекса'},
            {'category_name': 'ППКП', 'category_description': 'Приемно-контрольные приборы пожарной сигнализации'},
            {'category_name': 'Электроприводы', 'category_description': 'Электроприводы'},
        ]

        category_for_create = list()
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)


