# SLS-Kassa-Settings-Updater

**_Current version 1.5.1_**


## ToDo

Добавить проверку на идентичность параметров, и не перезаписывать параметры, если данные идентичны.

Добавить уведомление в TG об апгреде параметров, если параметры не совпадают.

Добавить защиту передаваемых данных.

Найти проблему с POST запросами на сервере.


## ChangeLog

**version 1.5.2**

Launch mode changed to hidden.

Режим запуска изменен на скрытый.


**version 1.5.1**

Fixed problem with script autorun during user authorization, a relative path was specified instead of a full 
path to the logs folder, which caused an error if the working folder was not the script folder.

Исправлена проблема с автозапуском скрипта при авторизации пользователя, был указан относительный путь вместо 
полного к папке логов, что вызывало ошибку, если рабочая папка не была папкой скрипта.


**version 1.4.1**

Fixed problem with dataclass(slots=True) in older versions of python for Windows 7, added dataslots() 
for compatibility.

Исправлена проблема с dataclass(slots=True) в старых версиях Python для Windows 7, добавлены dataslots() 
для совместимости.


**version 1.3.0**

Fixed problem with JSON errors in situations where JSON is not correct or the site did not return anything.

The logger settings are moved to a separate file.

Исправлена проблема с ошибками ДЖСОН, в ситуациях, если ДЖСОН не корректен или сайт не вернул ни чего.

Настройки логгера вынесены в отдельный файл.