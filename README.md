# Перед вами телеграм бот для мониторинга изменений курса валютной пары доллар/рубль.
## Чтобы запустить код:
### Клонируйте репозиторий
### Установите docker 
### Получите свой API-token в BotFather(телеграм) и токен в сервисе apilayer.com
### Подставьте свои токены в файл tok.py
### Создайте образ командой:
```
docker build -t {имя_вашего_образа} .
```
### Запустите контейнер:
```
docker run {имя_вашего_образа}
```