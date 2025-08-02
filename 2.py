def create_eml_file(name, to_email):
    received_date = "Thu, 31 Jul 2025 10:19:54 +0700"
    message_id = "8431527f-a8b7-4405-8611-5a7e172b8aab@arqatech.com"
    email_date = "Thu, 31 Jul 2025 10:19:53 +0700"
    user_agent = "Mozilla Thunderbird"
    content_language = "ru"
    from_email = "Evgeniy Cherepnin <echer@arqatech.com>"
    subject = f"Пример письма {name}"
    body = "Это тестовое письмо."

    filename="№1_email.eml"
    
    eml_content = f"""Received: {received_date}
Message-ID: <{message_id}>
Date: {email_date}
User-Agent: {user_agent}
Content-Language: {content_language}
To: {to_email}
From: {from_email}
Subject: {subject}

{body}
"""
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(eml_content)
    
    print(f"Файл {filename} успешно создан!")

# Пример использования:
create_eml_file("Jeka", "fdsdf@mail.ru")
