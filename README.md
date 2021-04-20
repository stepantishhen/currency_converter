# Конвертер валют
Реализовано на веб-фреймворке Flask. Конвертирует валюту одной страны в валюту
другой. Первое что видит пользователь - главную страницу. На ней представлена
шапка страницы - с названием приложения и картинкой логотипом. Далее идет карточка
с названием приложения и его маленьким описанием. Внизу также располагается кнопка
к активному призыву перехода на следующую страницу. Дополнительно добавлено маленькое
изображение. Сайт является адаптивным для большинства устройств. При переходе по
нажатию на кнопку, попадаем на страницу конвертации валюты. Нам доступна форма ввода
данных - количество единиц валюты, исходная валюта и валюта в которую хотим конвертировать.
Пользователю достаточно легко будет разобраться в этом интерфейсе. После заполнения
можно нажать на кнопку и получить результат. Он отображается ниже и поясняет нам:
какую в какую валюту мы конвертировали, наш результат и дополнительное сведение
о стоимости одной единицы валюты. Внизу есть изображение, взятое из открытых источников
информации. Также пользователь может воспользоваться комментариями. Оставить свой комментарий,
представиться, ввести почту. Также чтобы защитить сайт от ботов и нежелательных комментариев
существует проверка по капче. После этого можно отправить комментарий. Будет видно только
дату размещения комментария, сам комментарий и имя пользователя. В дальнейших планах
можно усовершенствовать систему проверки комментария. Также расширить список валют, усовершенствовать
систему склонения слов при отображении в результате.
# Как запустить
Чтобы запустить, в файле server.py нужно разкоментировать строчки после TESTING и закомментироваль все что ниже. Пример ниже
```python
# TESTING
# if __name__ == '__main__':
#     db_session.global_init("db/comments.db")
#     port = int(os.environ.get("PORT", 5000))
#     app.run(port=port, debug=True)

if __name__ == '__main__':
    db_session.global_init("db/comments.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
```
