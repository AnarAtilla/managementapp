# Project Management App

## Описание

**Project Management App** — это веб-приложение для управления проектами, задачами и пользователями. Оно включает в себя аутентификацию пользователей с помощью сторонних сервисов (Google, Facebook), API на основе Django REST Framework и JWT-токенов для защиты маршрутов.

## Функционал

- Регистрация и аутентификация пользователей через Google и Facebook.
- Создание, редактирование и удаление проектов.
- Управление задачами в рамках проектов.
- Аутентификация и авторизация с использованием JWT.
- Поддержка REST API для взаимодействия с фронтендом или мобильными приложениями.

## Технологии

- **Python 3.x**: основной язык программирования.
- **Django**: основной веб-фреймворк.
- **Django Allauth**: для аутентификации пользователей через Google и Facebook.
- **Django REST Framework**: для создания RESTful API.
- **Simple JWT**: для генерации и управления JWT-токенами.
- **SQLite**: в качестве базы данных по умолчанию (можно заменить на другую, например, PostgreSQL).
- **dotenv**: для управления конфиденциальными данными через `.env` файл.

## Установка

### Клонирование репозитория

```bash
git clone https://github.com/AnarAtilla/managementapp.git
cd project-management-app

# Создание виртуального окружения
python3 -m venv env
source env/bin/activate

# Установка зависимостей
python -m venv env
.\env\Scripts\activate

# Установка зависимостей
pip install -r requirements.txt

# Создание файла .env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Конфигурация для Google и Facebook
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_secret
SOCIALACCOUNT_FACEBOOK_CLIENT_ID=your_facebook_app_id
SOCIALACCOUNT_FACEBOOK_SECRET=your_facebook_app_secret

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver


## Использование
После запуска сервера перейдите в браузер по адресу http://127.0.0.1:8000/ для доступа к приложению.

## API
Приложение предоставляет REST API, защищенный JWT-токенами. Документация API доступна через /api/docs/.

# Развертывание
Для развертывания на продакшене:

# Установите DEBUG=False в .env.
Настройте базу данных на использование PostgreSQL (или другой базы данных, подходящей для продакшена).
Настройте сервер, например, с помощью Gunicorn и Nginx.
Обеспечьте защиту секретных ключей и других конфиденциальных данных.

## Вклад
# Если вы хотите внести свой вклад в проект, сделайте форк репозитория, создайте ветку для ваших изменений, а затем отправьте pull request.

git checkout -b feature/some-feature
git commit -m "Add some feature"
git push origin feature/some-feature


## Лицензия
Этот проект лицензирован под лицензией MIT. Подробности см. в файле [LICENSE](docs/LICENSE).


### Примечания:
- Вставьте настоящие значения в `.env` файл.
- Замените ссылки и команды на свои актуальные данные и конфигурацию.
- Расширяйте и обновляйте `README.md` по мере добавления нового функционала и изменений в проект.
