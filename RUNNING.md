# Просмотр и повторный запуск проектов

[Вернуться к портфолио](../README.md)

Описания и метрики основаны на коде и сохранённых выводах ноутбуков. Полный запуск всех работ в чистом окружении пока не подтверждён: часть исходных данных отсутствует, точные версии зависимостей не зафиксированы.

## 1. Получить репозиторий

```bash
git clone https://github.com/Alfredgazza23/Data-Scientist.git
cd Data-Scientist
```

Для просмотра решений достаточно открыть ноутбуки на GitHub. Дальнейшие шаги нужны для выполнения кода локально.

## 2. Создать окружение для ML1–ML5

В метаданных ML1–ML5 указан Python 3.12. Пример для Linux/macOS с установленным Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel numpy pandas matplotlib seaborn scikit-learn
```

Для Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyterlab ipykernel numpy pandas matplotlib seaborn scikit-learn
```

Дополнительные зависимости конкретных проектов:

| Раздел | Пакеты |
|---|---|
| ML3 | `optuna shap` |
| ML5 | `catboost xgboost lightgbm` |
| DSB10/DSB11 | `joblib tqdm ipywidgets` |

Например, для ML3:

```bash
python -m pip install optuna shap
```

Для ML5:

```bash
python -m pip install catboost xgboost lightgbm
```

Эти команды составлены по используемым библиотекам. Они устанавливают незакреплённые версии и не являются проверенным файлом окружения. После успешного полного запуска стоит зафиксировать фактические версии пакетов. В DSB11 встречаются старые вызовы API Scikit-learn, поэтому перенос этих упражнений в новое окружение может потребовать изменений кода.

## 3. Подготовить данные

### ML1–ML3: объявления об аренде

Источник — [Two Sigma Connect: Rental Listing Inquiries](https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data). Для скачивания Kaggle может потребовать вход и принятие условий соревнования.

Загрузите и распакуйте данные. Код ожидает:

| Проект | Пути относительно корня репозитория |
|---|---|
| ML1 | `ML1_Introduction/data/train.json` |
| ML2 | `ML2_Supervised_learning/data/train.json` и `ML2_Supervised_learning/data/test.json` |
| ML3 | `ML3_Validation/data/train.json` и `ML3_Validation/data/test.json` |

В учебных работах прогнозируется `price`. В исходном соревновании целевая переменная — `interest_level`; не следует подменять учебную задачу задачей соревнования или смешивать эти метрики.

### ML4–ML5: покупки автомобилей

Источник — [Don't Get Kicked!](https://www.kaggle.com/competitions/DontGetKicked/data). Нужен файл `training.csv` со столбцами `IsBadBuy` и `PurchDate`.

Разместите копию исходного файла в каждой папке:

- `ML4_Classification problems/data/training.csv`;
- `ML5_Decision_trees/data/training.csv`.

В сохранённых выводах исходный файл содержит 72 983 записи и 34 столбца. Файл `training.csv` в текущий репозиторий не включён.

### DSB10 и DSB11: имена CSV

В DSB10 часть данных уже загружена. Ноутбук `ex02/02_multiclass_one-hot.ipynb` сохраняет `../data/dayofweek.csv`; этот файл нужен упражнению `ex03`.

При использовании уже загруженных CSV нужно согласовать имена:

| Загруженный файл | Имя, ожидаемое кодом |
|---|---|
| `DSB10_Intro_to_ML/data/dayofweek (1).csv` | `DSB10_Intro_to_ML/data/dayofweek.csv` |
| `DSB11 _ML_Advanced/data/checker_submits (1).csv` | `DSB11 _ML_Advanced/data/checker_submits.csv` |

Можно создать локальные копии без замены существующих файлов. Выполните этот Python-код из корня репозитория:

```python
from pathlib import Path
from shutil import copyfile

pairs = [
    (
        Path("DSB10_Intro_to_ML/data/dayofweek (1).csv"),
        Path("DSB10_Intro_to_ML/data/dayofweek.csv"),
    ),
    (
        Path("DSB11 _ML_Advanced/data/checker_submits (1).csv"),
        Path("DSB11 _ML_Advanced/data/checker_submits.csv"),
    ),
]

for source, target in pairs:
    if not target.exists():
        copyfile(source, target)
```

Для DSB11 этого недостаточно: `ex00` ожидает `data/dayofweek.csv`, а `ex01`–`ex03` — ещё и `data/day-of-week-not-scaled.csv` относительно папки DSB11. Эти файлы отсутствуют. Подготовленные признаки и их порядок нужно восстановить по [условиям раздела](../DSB11%20_ML_Advanced/README_RUS%20%286%29.md) и используемой в ноутбуках предобработке.

### DSB8/DSB9: SQLite

Файл `checking-logs.sqlite` находится в папке `data` каждого раздела. Задания DSB8 создают таблицы в базе; повторное выполнение отдельных ячеек может конфликтовать с уже существующими таблицами.

В `DSB8_SQL_Pandas/ex02/ex02_joins.ipynb` сохранена ошибка `Table 'test' already exists.` Для повторяемого запуска нужно определить, создаются ли таблицы заново или используются уже существующие, и согласовать с этим вызовы записи. Одна очистка вывода ячейки проблему не исправляет.

## 4. Открыть ноутбук и выбрать рабочую папку

Для примера ML4 после подготовки `data/training.csv`:

```bash
cd "ML4_Classification problems"
python -m jupyter lab
```

Откройте `ML4_Classification problems.ipynb` и выберите ядро созданного окружения. Ожидаемая рабочая папка ядра — папка проекта. Проверить её можно через `Path.cwd()` после `from pathlib import Path`.

В упражнениях DSB10/DSB11 рабочая папка — конкретная `ex00`, `ex01` и т. д.; пути `../data/...` рассчитаны на такое расположение.

Перезапустите ядро и выполните ячейки по порядку. Сохранённые результаты прежнего запуска не подтверждают успешное выполнение текущего кода в новом окружении.

## 5. Как интерпретировать результаты

| Проект | Что учитывать |
|---|---|
| ML1 | Отбор по цене выполнен до разбиения; используется готовый `interest_level` |
| ML2 | Лучшая конфигурация выбирается по `R2_test`; для независимой оценки нужен отдельный test |
| ML3 | До разбиения отбирается диапазон цены; test неоднократно используется для сравнения вариантов |
| ML4 | ROC-AUC 0,736346 относится к базовой Logistic Regression на validation; порог по F1 подбирается с использованием test |
| ML4/ML5 | Gini вычисляется с модулем; для стандартного нормированного Gini нужен знак выражения `2 * ROC_AUC - 1` |
| DSB11, ex04 | Предобработка обучается до разбиения; её нужно перенести внутрь корректной схемы обучения и валидации |

Дополнительно в ML4 следует проверить собственную реализацию Average Precision при одинаковых предсказанных вероятностях.

Для новой итоговой оценки параметры предобработки определяются на train, выбор признаков, модели и порога выполняется по validation или кросс-валидации, а test используется для заключительной проверки. См. [руководство Scikit-learn по утечкам данных](https://scikit-learn.org/stable/common_pitfalls.html).

## 6. Другие незавершённые элементы

Файл `DSB2_syntax_semantics/ex01/read_and_write.py` содержит только пробельные символы. Этот файл нужно дополнить решением перед представлением упражнения как завершённого.

Описания портфолио фиксируют текущее содержимое и не означают, что перечисленные исправления кода уже выполнены.

