#!/bin/bash



DIRECTORY="venv"
if [ ! -d "$DIRECTORY" ]; then
    echo "Создаем виртуальное окружение..."
    python3 -m venv venv
fi


echo "Активируем виртуальное окружение..."
source venv/bin/activate


if [ -f requirements.txt ]; then
    PIP_FREEZE=$(pip freeze)
    REQUIREMENTS=$(cat requirements.txt)
    if [ "$PIP_FREEZE" != "$REQUIREMENTS" ]; then
        echo "Устанавливаем зависимости из requirements.txt..."
        pip install -r requirements.txt
    fi
fi


cd labor_costs_tracking

# проверка миграций
UNAPPLIED_MIGRATIONS=$(python3 manage.py makemigrations | grep 'No changes detected' | wc -l);

if [ "$UNAPPLIED_MIGRATIONS" -gt 0 ]; then
    echo "Обнаружены неприменённые миграции. Применяем их..."
    python manage.py migrate
fi


echo "Запускаем сервер Django..."
python3 manage.py runserver