# renga-json

## RU

### Предварительные требования
1. Python 3.11 или выше
2. pip 23.1.2 или выше (чтобы обновить pip необходимо выполнить `python -m pip install --upgrade pip`)

### Установка проекта
1. Скачать файлы проекта
2. Выполнить `pip install .` для установки зависимостей
3. Выполнить `pre-commit install` для установки pre commit хуков

### Запуск проекта
выполните `python generateJSON.py` или `python3 generateJSON.py` в вашем терминале, либо запустите python удобным для вас способом

### Тесты
чтобы запустить тесты выполните `pytest` в вашем терминале

### Линтинг кода
чтобы выполнить линтинг с помощью ruff выполните `ruff check .` в вашем терминале
чтобы выполнить линтинг с помощью black выполните `black --check .` в вашем терминале

## EN

### Prerequisites
1. Python 3.11 or above
2. pip 23.1.2 or above (to upgrade pip run `python -m pip install --upgrade pip`)

### project setup
1. clone this repository
2. run `pip install .` for install dependencies
3. run `pre-commit install` for setup pre commit hooks

### project startup
run `python generateJSON.py` or `python3 generateJSON.py` in your terminal or run python in a way that is convenient for you

### tests
to run tests execute `pytest` in your terminal

### code linting
to lint code with ruff execute `ruff check .` in your terminal  
to lint code with black execute `black --check .` in your terminal