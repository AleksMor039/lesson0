def send_email(message, recipient, sender="university.help@gmail.com"):
    simbol_1 = "@"
    simbols = (".com", ".ru", ".net")
    if sender == recipient:
        result = "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        result = "Письмо успешно отправлено с адреса", sender, "на адрес", recipient
    elif sender != "university.help@gmail.com":
        result = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient
    elif (simbol_1 and simbols) not in (recipient or sender) or (simbol_1 or simbols) not in (recipient or sender):
        result = "Невозможно отправить письмо с адреса", sender, "на адрес", recipient
    
    return result
print (send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print (send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
            sender='urban.info@gmail.com'))
print (send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print (send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))