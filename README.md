# SLS-Kassa-Settings-Updater

**_Current version 1.5.1_**

## ChangeLog
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