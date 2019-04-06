# Гайд по деплою Django приложение на Heroku 
## Последовательность действий
1. Подключить [Travis](travis-ci.com) к репозиторию на GitHub
2. Создать аккаунт на [Heroku](heroku.com)
4. Создаем app в Heroku
3. Скачать CLI Travis и Heroku
5. Логинимся в Heroku и Travis
6. Создаем ключи шифрования как описано в [гайде](https://docs.travis-ci.com/user/deployment/heroku/)
7. Оформляем `.travis.yml`
8. Создаем `Procfile`
9. Подготавливаем приложение к деплою
10. Пушим в репозиторий, радуемся


## Подключаем Travis
Все просто, идем на сайт [Travis](travis-ci.com), логинимся через GitHub, даем доступ к нужным репозиториям

## Регистрируемся на [Heroku](heroku.com)
А потом создаем application

## Установка Travis
```bash
sudo apt install ruby ruby-dev
sudo gem install travis
```

Если уже поставили через apt, делаем [вот это](https://github.com/travis-ci/travis.rb/issues/400)

## Travis login
```bash
travis login --pro
```

## [Установка Heroku](https://devcenter.heroku.com/articles/heroku-cli)

## Генерируем ключи
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key --pro
```

## Оформляем конфиг Travis
Пример для django смотри в репозитории

## Создаем Procfile
Пример для django смотри в репозитории

## Подготавливаем приложение к деплою
На что обратить внимание: 
- Статичные файлы
- База данных (в т.ч. миграции)
- Написанные тесты (очень желательно)
- Пути до файлов

# В случае Django просто добавьте код ниже в settings.py
Библиотека django_heroku делает все за нас.

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

try:
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False
```
## Оформляем requirements.txt
1. Создаем файл с помощью pip freeze > requirements.txt
2. Travis не умеет работать с django_heroku, поэтому нужно создать отдельный файл, по которому будет собираться Travis
3. pip freeze > requirements-build.txt
4. Проверям, чтобы в `.travis.yml` устанавливался второй файл

## На этом все
Ваше приложение должно успешно задеплоиться (см. на сайте heroku). Если появились какие-то проблемы - гугл знает на них ответ.
