from pathlib import Path
from datetime import datetime as dt

from django.shortcuts import render

from utils.file_manager import FileManager
from config.settings import BASE_DIR

# Create your views here.
message_file = FileManager(Path(BASE_DIR, 'fixtures'), 'message_box.json')


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # формирование сообщения
        time = dt.now()
        message = {str(time.isoformat()): {name: f'{phone}. {message}'}}
        message_file.update_file(message)
    return render(request, 'catalog/contacts.html')
