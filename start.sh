#!/bin/bash


echo "Создаем виртуальное окружение..."
python3 -m venv venv

echo "Активируем виртуальное окружение..."
source venv/bin/activate

if [ -f requirements.txt ]; then
    echo "Устанавливаем зависимости из requirements.txt..."
    pip install -r requirements.txt
fi

cd labor_costs_tracking

echo "Запускаем сервер Django..."
python manage.py runserver