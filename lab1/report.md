#### 1. Скачать и установить Visual Studio Code.

Скачал с официального [сайта](https://visualstudio.microsoft.com/ru/)

#### 2. Сконфигуровать для запуска и отладки кода (любой из 3 языков java, python, c++).

Я выбрал язык **Python**
Установил [расширение](https://marketplace.visualstudio.com/items?itemName=ms-python.python) для данного языка.
Далее добавил интерпретатор и создалась конфигурация `settigns.json`

Конфигурация для запуска
 
```json
{
    "python.pythonPath": "/usr/local/bin/python3"
}
```

Далее

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Текущий файл",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```


|Свойство  |Описание  |
|---------|---------|
|version  |Версия конфигурации|
|configurations| Список конфигураций|
|name     | Имя конфигурации        |
|type     | Тип конфигурации        |
|request  | Запрос для запуска программы|
|programm | Абсолютный путь до файла|
|console  |  Где запускать дебаг    |

#### 3. Написать простой проект (чтение файла, простой консольный калькулятор).

В `calculator.py` написал консольный калькулятор

#### 4. Написать тесты к проекту.


```python
import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.sum(5, 2), 7)
    
    def test_minus(self):
        self.assertEqual(calculator.minus(5, 2), 3)
    
    def test_div(self):
        self.assertEqual(calculator.div(6, 2), 3.0)
        self.assertRaises(ZeroDivisionError, calculator.div, 6, 0)
```


Запуск тестов `python3 -m unittest test.py`

#### 5. Изучить Visual Studio Code CLI: описать не менее 10 команд, используемых в данном интерфейсе.


|Команда  |Описание  |
|---------|---------|
|`code`     |     Запускает VSCode    |
|`code -h`   |     Открывает мануал по VSCode CLI    |
|`code --locale <locale>`    | Устанавливает язык интерфейса        |
|`code -r`     |   Открывает последий воркспейс    |
|`code file <file>`    |    Открывает файл    |
|`code folder  <folder>`  |   Открывает папку      |
|`code --list-extensions`     |    Список всех установленных расширений     |
|`code --install-extension <ext>`     |  Устанавливает расширение  |
|`code --uninstall-extension <ext>`     |     Удаляет расширение    |
|`code --disable-extensions`     |    Отключает все установленные расширения     |

#### 6. Написать 5 собственных Сниппетов

```json
{
    "while": {
        "scope": "python",
        "prefix": "while",
        "body": [
            "while $1:",
            "\t$2",
        ],
        "description": "while structure for python files"
    }
}
```


```json
{
    "Print to console": {
		"scope": "javascript,typescript",
		"prefix": "l",
		"body": [
			"console.log($1);",
			"$2",
		],
		"description": "Log output to console"
	}
}
```


```json
{
	"Interface": {
		"scope": "typescript",
		"prefix": "i",
		"body": [
			"interface $1 {",
			"\t$2",
			"}",
		],
		"description": "Interface structure for TS"
	}
}
```


```json
{
    "Vue component scructure": {
		"scope": "vue",
		"prefix": "t",
		"body": [
			"<template>",
			"\t",
			"</template>",
			"",
			"<script lang=\"ts\">",
			"import Vue from 'vue'",
			"",
			"</script>",
			"",
			"<style>",
			"\t",
			"</style>",
		],
		"description": "Default Vue component with TS"
	}
}
```


```json
{
	"Import structure": {
		"scope": "javascript,typescript",
		"prefix": "import",
		"body": [
			"import $2 from '$1'"
		],
		"description": "import something"
	}
}
```

#### 7. Изучить и описать наиболее распространённые HotKeys


|Команда  |Описание |
|---------|---------|
|`Cmd + F`  | Найти в текущем файле|
|`Shift + Cmd + F` | Найти в воркспейсе|
|`Cmd + J`    | Открыть терминал |
|`Cmd + /`     | Закоментировать код|
|`Cmd + Alt + ↑/↓` | Добавление курсора вверх/вниз|
|`Shift + Option` | Выделение столба|

#### 8. Задокументировать код с помощью расширения

Использовал другое расширение - PyDoc


```python
def sum(a, b):
    """ 
    Sum of 2 numbers

    :type a: any
    :param a: First num

    :type b: any
    :param b: Second num

    :raises: none

    :rtype: any
    """

    return a + b

def minus(a, b):
    """ 
    Difference of numbers

    :type a: any
    :param a: first number

    :type b: any
    :param b: second number

    :raises: none

    :rtype: any
    """
    return a - b

def div(a, b):
    """ 
    Division of 2 numbers

    :type a: any
    :param a: first number

    :type b: any
    :param b: second number

    :raises: ZeroDivisionError

    :rtype: float
    """
    if b == 0:
        raise ZeroDivisionError("Can not div by zero")
    
    return a / b
```


#### 9. Установить шрифт FiraCode.
Скачал шрифт и изменил `settings.json`

```json
"editor.fontFamily": "'Fira Code', Menlo, Monaco, 'Courier New', monospace",
"editor.fontLigatures": true,
```

#### 10. Установить расширение и показать, чего получилось.

Done ✅

#### 11. Отчет – Пошаговое руководство настройки проекта со скриншотами, исходники проекта.
 
You are reading it now 😎