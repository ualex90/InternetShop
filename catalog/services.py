from django.conf import settings
from django.core.cache import cache
from django.db.models import QuerySet


def get_object_list(model) -> QuerySet:
    """
    Кэширование списка объектов модели
    """
    if settings.CACHE_ENABLED:
        key = f'queryset_{model.__module__}'
        object_list = cache.get(key)
        if object_list is None:
            object_list = model.objects.all()
            cache.set(key, object_list)
            print(f'{model.__module__}, Перечитали из базы данных')
        else:
            print(f'{model.__module__}, Данные из кэша')
    else:
        object_list = model.objects.all()
    return object_list
