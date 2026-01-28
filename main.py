from api.models import app


if __name__ == '__main__':
    # Запускаем Flask-сервер в режиме отладки
    # (при изменении кода сервер перезапускается автоматически)
    app.run(debug=True)