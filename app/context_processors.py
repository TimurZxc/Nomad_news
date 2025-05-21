import json, os
from django.conf import settings

def translations(request):
    lang = request.session.get('lang', 'ru')           # default
    path = os.path.join(settings.BASE_DIR,
                        'app', 'translations', f'{lang}.json')
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return { 'T': data }
