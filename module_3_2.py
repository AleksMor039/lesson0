def send_email (message, recipient, *, sender="university.help@gmail.com"):
    simbol = "@"
    while 1 > 0:
        if recipient.endswith((".com", ".ru", ".net")) and sender.endswith((".com", ".ru", ".net")):
            if simbol not in recipient and sender:
                result = "Невозможно отправить письмо с адреса", sender, "на адрес", recipient
                break
        else:
            result = "Невозможно отправить письмо с адреса", sender, "на адрес", recipient
            break
        if sender == recipient:
            result = "Нельзя отправить письмо самому себе!"
            break
        elif sender == "university.help@gmail.com":
            result = "Письмо успешно отправлено с адреса", sender, "на адрес", recipient
            break
        elif sender != "university.help@gmail.com":
            result = (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", {sender}, "на адрес", {recipient})
            break
    return result

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
