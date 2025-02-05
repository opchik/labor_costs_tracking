#!/bin/bash


echo "Активируем виртуальное окружение..."
source venv/bin/activate


cd labor_costs_tracking


echo "Запускаем сервер Django..."
python3 manage.py runserver


deactivate