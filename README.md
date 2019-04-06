https://pandao.github.io/editor.md/en.html
# Гайд по деплою Django приложение на Heroku 
## Последовательность действий
1. Подключить [Travis](travis-ci.com) к репозиторию на GitHub
2. Создать аккаунт на [Heroku](heroku.com)
3. Скачать CLI Travis и Heroku
4. Логинимся в Heroku и Travis
5. Создаем ключи шифрования как описано в [гайде](https://docs.travis-ci.com/user/deployment/heroku/)

## Установка Travis
```bash
$ sudo apt install ruby ruby-dev
$ sudo gem install travis```
Если уже поставили через apt, делаем [вот это ](https://github.com/travis-ci/travis.rb/issues/400)

## Travis login
```bash
$ travis login --pro```
