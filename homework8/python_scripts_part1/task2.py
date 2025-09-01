email = " USER@DOMAIN.COM "

# Очищаем и форматируем строку
clean_email = email.strip().lower()

# Отделяем имя пользователя и домен
user_name = clean_email[:clean_email.find("@")]
domain = clean_email[clean_email.find("@") + 1:]

print(f"Username: {user_name}, Domain: {domain}")
