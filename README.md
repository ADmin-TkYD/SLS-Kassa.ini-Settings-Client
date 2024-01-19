# SLS-Kassa-Settings-Updater

**_Current version 1.5.40_**


## ToDo

---

Add notification to TG about parameter upgrade if parameters do not match.

Add protection for transmitted data.

Find a problem with POST requests on the server (only accepts GET requests)..

Add reading and sending to the server, version of ```Kassa_W.exe``` from the file:
```C:\SoftLand Systems\SLS-Shared\SLS-Versions\Kassa_W.VER```

---

Добавить уведомление в TG об апгреде параметров, если параметры не совпадают.

Добавить защиту передаваемых данных.

Найти проблему с POST запросами на сервере (принимает только GET-запросы).

Добавить чтение и отправку на сервер, версии ```Kassa_W.exe``` из файла: 
```C:\SoftLand Systems\SLS-Shared\SLS-Versions\Kassa_W.VER```

---
## Installation

**PowerShell** *(Windows 10 and later)*:
```
[System.Console]::Title = hostname
winget install --id Git.Git -e --source winget ; 
winget install --id=Python.Python.3.12 -e --source winget ;
```

**cmd:**

```
title %computername%: %username%
mkdir "C:\SoftLand Systems\SLS-Scripts"
cd "C:\SoftLand Systems\SLS-Scripts"
git clone https://github.com/ADmin-TkYD/SLS-Kassa.ini-Settings-Client.git
cd SLS-Kassa.ini-Settings-Client
python.exe -m pip install --upgrade pip
python -m venv venv
venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

python main.py
deactivate
```

---
## ChangeLog

---
#### version 1.5.40

Error Fix: "StdErr: Fatal: ..." If there are problems connecting to git.

---
Исправление ошибок: "StdErr: Fatal: ..." При проблемах с подключением к git.

---
#### version 1.5.39

Error Fix: "fatal: not a git repository (or any of the parent directories)".

---
Исправление ошибки: "fatal: not a git repository (or any of the parent directories)".

---
#### version 1.5.38

Minor fixes

---
Мелкие исправления.


#### version 1.5.37

Minor fixes

---
Мелкие исправления.

---
#### version 1.5.36

Added termination of the cash register program process if it is already running.

Minor fixes.

---
Добавлено завершение процесса кассовой программы, если она уже запущена.

Мелкие исправления.

---
#### version 1.5.35

Generating json on the server side: Fixed a bug with json encoding (```$conn->set_charset("utf8");```). 
It is necessary to change the encoding of the entire database from latin1 to utf8.

Fixed a bug on the server with processing data about the type of PC, as the department to which 
the PC belongs.

Added sending data about the department to which the PC belongs 
(```'department_abbr': identity_pc.department_abbr```).

---
Формирование json на стороне сервера: Исправлена ошибка с кодировкой json 
(```$conn->set_charset("utf8");```). 
Необходимо сменить кодировку всей базы с latin1 на utf8.

Исправлена ошибка на сервере с обработкой данных о типе ПК, как подразделения, к которому относится ПК.

Добавлена отправка данных о подразделении, к которому относится ПК 
(```'department_abbr': identity_pc.department_abbr```).

---
#### version 1.5.34

Added github availability check.

Added additional data for sending.

Optimized code for sending data to the server.

---
Добавлена проверка доступности github.

Добавлены дополнительные данные для отправки.

Оптимизирован код для отправки данных на сервер.

---
#### version 1.5.29

Minor fixes

---
Мелкие исправления.

---
#### version 1.5.28

Minor fixes.

---
Мелкие исправления.

---
#### version 1.5.27

Minor fixes

---
Мелкие исправления.

---
#### version 1.5.26

Minor fixes.

---
Мелкие исправления.

---
#### version 1.5.25 

Minor fixes.

---
Мелкие исправления.

---
#### version 1.5.24

Minor fixes.

---
Мелкие исправления.

---
#### version 1.5.23

Fixed error that occurred when adding a non-existent key to the ini file.

---
Исправлена ошибка, возникавшая при добавлении несуществующего ключа в ini-файл.

---
#### version 1.5.22

---
#### version 1.5.21 *(for testing)*

Changed the **get_command_stdout()** function in the **get_update** module,
now the function returns errors, not just stdout.

---
Изменена функция **get_command_stdout()** в модуле **get_update**, теперь
функция возвращает ошибки, а не только стдаут.

---
#### version 1.5.20 *(for testing)*

Added transition to script folder.

Optimized code.

---
Добавлен переход в папку скрипта.

Оптимизирован код.

---
#### version 1.5.19 *(for testing)*

Added logging of some modules.

---
Добавлено логирование некоторых модулей.

---
#### version 1.5.17-1.5.18 *(for testing)*

Fixed minor bugs in the code.

---
Исправлены мелкие ошибки в коде.

---
#### version 1.5.15 *(for testing)*

Correct operation of the update script.

---
Корректная работа скрипта обновления.

---
#### version 1.5.9-1.5.14 *(for testing)*

Checking the correct operation of the update script.

---
Проверка корректной работы скрипта обновлений.

---
#### version 1.5.8 *(for testing)*

Added script update module via **git**, using `git pool`.

---
Добавлен модуль обновления скрипта через **git**, с помощью `git pool`.

---
#### version 1.5.7

Removed check, when sending confirmation that `is_update == true`,
now a message with the result of the script is always sent to the server.

---
Убрана проверка, при отправке подтверждения, что `is_update == true`, теперь
сообщение с результатом работы скрипта отправляется на сервер всегда.

---
#### version 1.5.6

**Debug mode** switched to **info** by default.

---
**Режим дебага** переключен на **info** по умолчанию.

---
#### version 1.5.5

Fixed error due to interpolation in configparser.

Fixed minor bugs in the code.

The server part has been improved, a table has been added with information
about the version and about changing the config on the PC.

---
Исправлены мелкие ошибки в коде.

Доработана серверная часть, добавлена таблица с информацией о версии и
об изменении конфига на ПК.

---
#### version 1.5.4

Fixed error due to interpolation in configparser.

**Error**: `raise ValueError("invalid interpolation syntax in %r at "
ValueError: invalid interpolation syntax in "abc%abcabc"`

**Fixed**: `configparser.ConfigParser(interpolation=None)`

---
Исправлена ошибка из-за интерполяции в configparser.

---
#### version 1.5.3

Added a check for the identity of the parameters, now the parameters
are not overwritten if the data is identical.

---
Добавлена проверка на идентичность параметров, теперь параметры
не перезаписываются, если данные идентичны.

---

#### version 1.5.2

Launch mode changed to hidden.

---
Режим запуска изменен на скрытый.

---
#### version 1.5.1

Fixed problem with script autorun during user authorization, 
a relative path was specified instead of a full path to the 
logs folder, which caused an error if the working folder was 
not the script folder.

---
Исправлена проблема с автозапуском скрипта при авторизации 
пользователя, был указан относительный путь вместо полного 
к папке логов, что вызывало ошибку, если рабочая папка 
не была папкой скрипта.

---
#### version 1.4.1

Fixed problem with dataclass(slots=True) in older versions of python for Windows 7, added dataslots()
for compatibility.

---
Исправлена проблема с dataclass(slots=True) в старых версиях Python для Windows 7, добавлены dataslots()
для совместимости.

---
#### version 1.3.0

Fixed problem with JSON errors in situations where JSON is not correct 
or the site did not return anything.

The logger settings are moved to a separate file.

---
Исправлена проблема с ошибками ДЖСОН, в ситуациях, если JSON не корректен или сайт не вернул ни чего.

Настройки логгера вынесены в отдельный файл.

---
