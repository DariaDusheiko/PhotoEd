# <center>**<span style='color: #00EFFF;'>P</span>hoto<span style='color: #FF0091;'>E</span>d**</center>

"<span style='color: #00EFFF;'>P</span>hoto<span style='color: #FF0091;'>E</span>d" - это уникальное веб-приложение, которое позволяет 
вам преобразовать ваши современные фотографии в старины, 
наполненные атмосферой прошлого. Хотя такие снимки не отличаются высокой четкостью и яркостью цветов, 
рассматривать их очень интересно, ведь они возвращают нас к истокам прошлого.

#### <span style='color: #00EFFF;'>Возможности:</span>

* Преобразование фотографий в старые с эффектами, имитирующими старые фотографии
* Выбор из различных стилей и эффектов
* Возможность сохранять и скачивать результаты
* Возможность просмотра и настраивания эффектов
* Воссоздать царапины и потертости


### <center>**<span style='color: #FF0091;'>Запуск проекта с использованием Docker</span>**</center>

Для запуска веб-проекта, запакованного в Docker, рекомендуется использовать способ запуска через саму платформу, 
так как это обеспечивает изоляцию и воспроизводимость окружения. Выполните шаги, указанные ниже, 
введя команды в командную строку.

#### <span style='color: #00EFFF;'>1. </span>Склонируйте репозиторий:

```
    git clone https://git.miem.hse.ru/dvdusheiko/photoed.git
```

#### <span style='color: #FF0091;'>2. </span>Перейдите в директорию проекта:
```
    cd photoed
```

#### <span style='color: #00EFFF;'>3. </span>Запустите контейнер:

```
    docker build -t photoed .
```

#### <span style='color: #FF0091;'>4. </span>Перейдите в директорию проекта:
```
    docker run -d -p 8000:8000 photoed
```
<span style='color: #00EFFF;'>Откройте проект в браузере:</span> Перейдите по адресу http://localhost:8000.


### <center>**<span style='color: #FF0091;'>Запуск проекта без использования Docker</span>**</center>
Если вы хотите запустить проект без Docker, вам потребуется установить все зависимости вручную. Выполните шаги, указанные ниже, 
также введя команды в командную строку.

#### <span style='color: #00EFFF;'>1. </span>Убедитесь, что у вас установлен Python и pip:

```
    python --version 
```

<span style='color: #00EFFF;'>Если установлен Python, вы должны увидеть номер версии</span> (например, Python 3.9.5).
```
    pip --version
```

<span style='color: #00EFFF;'>Если pip установлен, вы должны увидеть номер версии</span> (например, pip 21.2.4).


#### <span style='color: #FF0091;'>2. </span>Создайте виртуальное окружение:
```
    python -m venv venv
    source venv/bin/activate  # Для macOS/Linux
    venv\Scripts\activate     # Для Windows
```

#### <span style='color: #00EFFF;'>3. </span>Установите зависимости:

```
    pip install -r requirements.txt
```

#### <span style='color: #FF0091;'>4. </span>Запустите сервер разработки:

```
    python manage.py runserver
```
<span style='color: #00EFFF;'>Откройте проект в браузере:</span> Перейдите по адресу http://127.0.0.1:8000.

#### <center>**Попробуйте <span style='color: #FF0091;'>PhotoEd</span> сегодня и откройте для себя новые возможности в мире фотографии!**</center>
