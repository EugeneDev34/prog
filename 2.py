Чтобы добавить случайную цифру к домену в email-адресе, модифицируем функцию `generate_email()`. Вот обновлённый код с изменениями:

def generate_email(first_name, last_name):
    """Генерация email с выдуманными доменами и случайной цифрой"""
    prefixes = [
        f"{first_name.lower()}.{last_name.lower()}",
        f"{last_name.lower()}.{first_name.lower()}",
        f"{first_name.lower()}_{last_name.lower()}",
        f"{first_name[0].lower()}{last_name.lower()}"
    ]
    
    # Добавляем случайную цифру (0-9) к домену
    domain = random.choice(CUSTOM_DOMAINS)
    if random.choice([True, False]):  # 50% вероятность добавления цифры
        digit = random.randint(0, 9)
        # Вставляем цифру либо перед точкой, либо в конце домена
        if '.' in domain and random.choice([True, False]):
            parts = domain.split('.')
            domain = f"{parts[0]}{digit}.{parts[1]}"
        else:
            domain = f"{domain}{digit}"
    
    return f"{random.choice(prefixes)}@{domain}"


