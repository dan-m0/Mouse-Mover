If you encounter an error, you will find the error code and a brief description in the log file.

Please see the below table for the full list and an explanation.

If the error code isn't here, please [report a bug][report-a-bug-url]

|Code   |Name   |Explanation   |Is this a problem?|
|---|---|---|---|
|0   |Log setup   |The logging file has been created in PWD/logging   | NO|
|1  |Undefined error   |An unexpected error occured, please [report this][bug-reporting]   |YES|
|2  |Installer aborted | You cancelled the installer when asked if you wanted to continue  |NO|
|3  |winget fails   |The Windows installer failed to automatically install winget - follow the prompt on screen   |  YES|
|4  |Python fails   |The Windows installer failed to automatically install python, this may be related to Code:2 - follow the prompt on screen   | YES|
|5   |Keyboard interrupt   |You pressed Ctrl+C to close the program   |NO|
|6   |Loop started   |The main program loop has started - the program will run until closed   |NO|
|7   |Loop stopped   |The loop stopped  |NO|
|8   |Cursor moved   |The cursor has been moved because you weren't using it, so you're probably not there   |NO|
|9   |Cursor not moved   |The cursor hasn't been moved, because you were using it, so you're probably there   |NO|
|10   |Cursor moved to new position   |Related to Code:8 - this indicates that the specific part of the code to move the mouse worked   |NO|
|11  |Cursor moved to last position   |Related to Code:8 - this indicates that the specific part of the code to move the mouse worked   |NO|
|12   |Variables set   |Part of the initial startup   |NO|
|13   |datetime formatting   |Part of the initial startup   |NO|
|14   |autogui import failure   |pyautogui isn't installed - this is essential for the program. Please see [the setup][setup] section   |YES|

If an item is marked as a problem, either [report it](https://nyxtryx.github.io/Mouse-Mover/guides/report-a-bug) or follow the installation instructions to resolve the problem.