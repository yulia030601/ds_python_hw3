# Описание шагов запуска #
## Запуск pytest для файла *test.py* с проверкой покрытия файла *what_is_year_now.py* ##
    python -m pytest -q test.py --cov=what_is_year_now
## Получение отчета о покрытии в виде директории с html файлами ##
    python -m pytest -q test.py --cov=what_is_year_now --cov-report html
