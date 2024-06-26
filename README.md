# Автотесты для интернет-магазина DEMOWEBSHOP
https://demowebshop.tricentis.com/

---

# Сделано

```
Авторизация
Регистрация
Навигация
Поиск
```

# В процессе

```
Фильрация
Добавление в корзину
Изменение корзины
```

---

## О проекте
Этот проект представляет собой комплекс автоматизированных тестов для веб-платформы интернет-магазина. Тесты разработаны для обеспечения качества основных функциональных возможностей сайта, включая пользовательские взаимодействия и бизнес-процессы. Автоматизация тестирования помогает обеспечить стабильность, производительность и надежность веб-сайта, минимизируя возможность возникновения ошибок во время реальных пользовательских сессий.

## Особенности реализации
- Page Object Pattern
- Тестирование на основе PyTest
- Selenium WebDriver

## Используемые технологии
- Python
- Selenium WebDriver
- PyTest
- Git

### Функциональность
Тестируемые функции интернет-магазина:
- Регистрация
- Авторизация
- Навигация по сайту
- Поиск товаров
- Фильтрация товаров
- Добавление товара в корзину
- Редактирование корзины

## Начало работы
Эти инструкция поможет вам получить копию проекта на локальной машине для разработки и тестирования.

## Предварительные требования

Убедитесь, что у вас установлены следующие компоненты:

- Python версии 3.8 или выше
- pip (менеджер пакетов для Python, обычно устанавливается вместе с Python).

## Установка необходимых зависимостей
Клонирование репозитория: Сначала вам нужно скопировать проект на вашу локальную машину. Откройте терминал и выполните следующую команду:

```

git clone https://github.com/JJNikJJ/AutotestWebsite
cd AutotestWebsite

```
Настройка виртуального окружения: Рекомендуется использовать виртуальное окружение для изоляции зависимостей проекта от системных библиотек. Для создания виртуального окружения выполните:

```
python -m venv venv
```
Активируйте виртуальное окружение:

На Windows:
```
.\venv\Scripts\activate
```
На Unix или MacOS:
```
source venv/bin/activate
```

### Установка зависимостей: Установите все зависимости, указанные в файле requirements.txt, используя pip:
```
pip install -r requirements.txt
```
Теперь все зависимости должны быть установлены, и вы можете запускать автотесты в вашем проекте.

## Запуск тестов
Для запуска тестов используйте команду pytest в терминале:

```
pytest
```
Эта команда найдет и выполнит все тесты, определенные в вашем проекте, выводя результаты в терминал.

## Структура папок

```
your-project-directory/
│
├── pages/                  # Папка с модулями Page Objects
│   ├── __init__.py
│   ├── login_page.py
│   └── cart_page.py
│
├── tests/                  # Папка с тестовыми скриптами
│   ├── __init__.py
│   ├── test_login.py
│   └── test_cart.py
│
└── requirements.txt        # Зависимости проекта
```
