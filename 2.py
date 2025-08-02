import random

def generate_phone():
    """Генерация российского номера: +7 (XXX) XXX-XX-XX"""
    code = random.choice(['901', '902', '916', '925', '926'])
    num = f"{random.randint(0, 999):03}-{random.randint(0, 99):02}-{random.randint(0, 99):02}"
    return f"+7 ({code}) {num}"

# Мужские имена, фамилии и отчества
MALE_NAMES = [
    "Александр", "Дмитрий", "Сергей", "Андрей", "Алексей", "Иван", "Максим", 
    "Михаил", "Артем", "Даниил", "Кирилл"]

MALE_SURNAMES = [
    "Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", "Васильев",
    "Новиков", "Федоров", "Морозов", "Волков", "Алексеев"]

MALE_PATRONYMICS = [
    "Александрович", "Дмитриевич", "Сергеевич", "Андреевич", "Алексеевич", "Иванович", 
    "Максимович", "Михайлович", "Артемович", "Даниилович", "Кириллович"]

# Женские имена, фамилии и отчества
FEMALE_NAMES = [
    "Александра", "Мария", "Анна", "Елена", "Ольга", "Наталья", "Ирина",
    "Татьяна", "Екатерина", "Юлия", "Дарья"]

FEMALE_SURNAMES = [
    "Иванова", "Петрова", "Сидорова", "Смирнова", "Кузнецова", "Попова", "Васильева",
    "Новикова", "Федорова", "Морозова", "Волкова", "Алексеева"]

FEMALE_PATRONYMICS = [
    "Александровна", "Дмитриевна", "Сергеевна", "Андреевна", "Алексеевна", "Ивановна",
    "Максимовна", "Михайловна", "Артемовна", "Данииловна", "Кирилловна"]

# Список доменов
CUSTOM_DOMAINS = [
    "supermail.xyz", "fastbox.pro", "megahost.net", "quickpost.tech",
    "cybermail.io", "databox.biz", "virtualpost.cloud", "netexpress.digital",
    "ultramail.space", "quantumail.ai", "neomail.live", "hyperpost.online",
    "mailfaster.com", "inboxrush.ru", "postalwave.net", "digitalpost.site",
    "netletter.org", "speedmail.tech", "webpost.pro", "cloudinbox.xyz"
]

def generate_email(first_name, last_name):
    """Генерация email на основе имени и фамилии"""
    
    # Варианты формирования email
    patterns = [
        f"{first_name[0].lower()}{last_name.lower()}",
        f"{first_name.lower()}.{last_name.lower()}",
        f"{last_name.lower()}{random.randint(10, 199)}"
    ]
    
    return f"{random.choice(patterns)}@{random.choice(CUSTOM_DOMAINS)}{random.randint(10, 199)}"

def generate_person():
    # Случайно выбираем пол
    is_male = random.choice([True, False])
    
    if is_male:
        name = random.choice(MALE_NAMES)
        surname = random.choice(MALE_SURNAMES)
        patronymic = random.choice(MALE_PATRONYMICS)
    else:
        name = random.choice(FEMALE_NAMES)
        surname = random.choice(FEMALE_SURNAMES)
        patronymic = random.choice(FEMALE_PATRONYMICS)
    
    unique_num = random.randint(1, 100)
    
    # Формируем данные персоны
    person_data = {
        "name": name,
        "patronymic": patronymic,
        "surname": f"{surname}_{unique_num}",
        "phone": generate_phone(),
    }
    
    # Генерируем email
    person_data["email"] = generate_email(name, person_data["surname"])
    
    return person_data

# первое письмо
def create_eml_file(name, from_email, num):
    received_date = "Thu, 31 Jul 2025 10:19:54 +0700"
    message_id = from_email+name
    email_date = "Thu, 31 Jul 2025 10:19:53 +0700"
    user_agent = "Mozilla Thunderbird"
    content_language = "ru"
    to_email = "E В Ч <тестирование@наша.работа>"
    subject = f"Пример письма {name}"
    body = "Это тестовое письмо."

    filename= num +"_email.eml"
    
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

# референс письмо
def create_refer_eml_file(name, from_email):
    received_date = "Thu, 31 Jul 2025 10:19:54 +0700"
    message_id = from_email+name+str(random.randint(1, 100))
    References = from_email+name
    email_date = "Thu, 31 Jul 2025 10:19:53 +0700"
    user_agent = "Mozilla Thunderbird"
    content_language = "ru"
    to_email = "E В Ч <тестирование@наша.работа>"
    subject = f"Пример второго письма {name}"
    body = "Это второе тестовое письмо."

    filename="№2_email.eml"
    
    eml_content = f"""Received: {received_date}
Message-ID: <{message_id}>
References: <{References}>
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

def main():
    print("Добро пожаловать в генератор тестовых данных!")
    print("Для выполнения программы нажмите 1, для выхода - любую другую клавишу...")
    
    # Ждем ввода пользователя
    user_input = input()
    
    if user_input != '1':
        print("Программа завершена.")
        return
    
    print("\nГенерация данных...\n")
    
    # Генерируем и выводим информацию о персоне
    person = generate_person()
    print("Имя:", person["name"])
    print("Отчество:", person["patronymic"])
    print("Фамилия:", person["surname"])
    print("Телефон:", person["phone"])
    print("Email:", person["email"])
    create_eml_file(person["name"], person["email"], "№1")
    create_refer_eml_file(person["name"], person["email"])

    person2 = generate_person()
    print("\nИмя:", person2["name"])
    print("Отчество:", person2["patronymic"])
    print("Фамилия:", person2["surname"])
    print("Телефон:", person2["phone"])
    print("Email:", person2["email"])
    create_eml_file(person2["name"], person2["email"],"№3")
    
    print("\nПрограмма завершена. Нажмите Enter для выхода...")
    input()

if __name__ == "__main__":
    main()






