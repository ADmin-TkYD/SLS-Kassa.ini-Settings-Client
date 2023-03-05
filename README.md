# SLS-Kassa-Settings-Updater

**_Current version 1.5.16_**


## ToDo

---

Add notification to TG about parameter upgrade if parameters do not match.

Add protection for transmitted data.

Find a problem with POST requests on the server.

Add handling of situations in case the parameter is missing in the ini-file.

---

Добавить уведомление в TG об апгреде параметров, если параметры не совпадают.

Добавить защиту передаваемых данных.

Найти проблему с POST запросами на сервере.

Добавить обрабатку ситуаций, в случае отстутсвия параметра в ini-файле.

---

## ChangeLog

---

**version 1.5.17**

Fixed minor bugs in the code.

Исправлены мелкие ошибки в коде.

---

**version 1.5.15**

Correct operation of the update script.

Корректная работа скрипта обновления.

---

**version 1.5.9-1.5.14** *for testing*

Checking the correct operation of the update script.

Проверка корректной работы скрипта обновлений.

---

**version 1.5.8** *for testing*

Added script update module via **git**, using `git pool`.

Добавлен модуль обновления скрипта через **git**, с помощью `git pool`.

---

**version 1.5.7**

Removed check, when sending confirmation that `is_update == true`, now a message with the result of the script 
is always sent to the server.

Убрана проверка, при отправке подтверждения, что `is_update == true`, теперь сообщение с результатом работы скрипта 
отправляется на сервер всегда.

---

**version 1.5.6**

**Debug mode** switched to **info** by default.

**Режим дебага** переключен на **info** по умолчанию.

---

**version 1.5.5**

Fixed error due to interpolation in configparser.

Fixed minor bugs in the code.

The server part has been improved, a table has been added with information 
about the version and about changing the config on the PC.

Исправлены мелкие ошибки в коде.

Доработана серверная часть, добавлена таблица с информацией о версии и 
об изменении конфига на ПК.

---

**version 1.5.4**

Fixed error due to interpolation in configparser.

**Error**: `raise ValueError("invalid interpolation syntax in %r at " 
ValueError: invalid interpolation syntax in "abc%abcabc"`

**Fixed**: `configparser.ConfigParser(interpolation=None)`

Исправлена ошибка из-за интерполяции в configparser.

---

**version 1.5.3**

Added a check for the identity of the parameters, now the parameters are not overwritten if the data is identical.

Добавлена проверка на идентичность параметров, теперь параметры не перезаписываются, если данные идентичны.

---

**version 1.5.2**

Launch mode changed to hidden.

Режим запуска изменен на скрытый.

---

**version 1.5.1**

Fixed problem with script autorun during user authorization, a relative path was specified instead of a full 
path to the logs folder, which caused an error if the working folder was not the script folder.

Исправлена проблема с автозапуском скрипта при авторизации пользователя, был указан относительный путь вместо 
полного к папке логов, что вызывало ошибку, если рабочая папка не была папкой скрипта.

---

**version 1.4.1**

Fixed problem with dataclass(slots=True) in older versions of python for Windows 7, added dataslots() 
for compatibility.

Исправлена проблема с dataclass(slots=True) в старых версиях Python для Windows 7, добавлены dataslots() 
для совместимости.

---

**version 1.3.0**

Fixed problem with JSON errors in situations where JSON is not correct or the site did not return anything.

The logger settings are moved to a separate file.

Исправлена проблема с ошибками ДЖСОН, в ситуациях, если ДЖСОН не корректен или сайт не вернул ни чего.

Настройки логгера вынесены в отдельный файл.

---