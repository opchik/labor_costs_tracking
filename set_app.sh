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
python3 manage.py makemigrations
python3 manage.py migrate


python3 manage.py createsuperuser


deactivate