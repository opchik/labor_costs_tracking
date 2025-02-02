# labor_costs_tracking

## 1. Проверка установленной версии Python

Введите следующую команду в терминале:
```bash
python3 --version
```

Если Python 3 установлен, вы увидите сообщение с номером версии, например:
```
Python 3.9.1
```

Если вы получите сообщение об ошибке, такое как "command not found", это означает, что Python 3 не установлен.

## 2. Установка Python3 (ЕСЛИ В ПРЕДЫДУЩЕМ ПУНКТЕ БЫЛО СООБЩЕНИЕ ОБ ОШИБКЕ)

Если Python 3 не установлен, вы можете установить его с помощью Homebrew, который является популярным менеджером пакетов для macOS. Если у вас еще нет Homebrew, вы можете установить его, выполнив следующую команду в терминале:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
После установки Homebrew вы можете установить Python 3 с помощью следующей команды:
```bash
brew install python
```

После этого необходимо проверить, установлен ли Python (пункт 2)


## 3. Скачивание программы (репозитория в котором она лежит)

Необходимо выполнить команду в терминале для скачивания и перехода в папку проекта:
```bash
git clone git@github.com:opchik/labor_costs_tracking.git
cd labor_costs_tracking
```


## 4. Запуск программы

Выдаем права на запуск программы 

```bash
chmod u+x script.sh
```

Вызываем команду запуска:

```bash
./start.sh
```

## 5. Последующие запуски

После открытия терминала необходимо попасть в скачанную папку
и запустить выполнение файла ```start.sh```. Это делается следующими командами:

```bash
cd labor_costs_tracking
./start.sh
```
