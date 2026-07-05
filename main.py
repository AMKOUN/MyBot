from neeeed.models import app


if __name__ == '__main__':
    # Запускаем Flask-сервер в режиме отладки
    # (при изменении кода сервер перезапускается автоматически)
    app.run(debug=True)

with app.app_context():
    # Создаёт все таблицы, если их ещё нет в базе данных
    db.create_all()