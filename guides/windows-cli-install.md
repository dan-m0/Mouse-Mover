To use the Windows command line tool follow these steps

1. Download [Download Windows folder][windows-cli-download-url] and save into your downloads folder

2. Run install_mouse_mover.ps1

    2.1. If the installer fails to run:

    2.2. Press and hold the Windows key at the same time, press R

    2.3. Paste this, then press enter: PowerShell.exe -ExecutionPolicy Bypass -File %USERPROFILE%\Downloads\windows\install_mouse_mover.ps1

    2.4. This will bypass any group policy preventing code execution, **only** for this file (ie it is not permanent)

3. Follow the installer prompts, it will tell you what to do next


## It didn't work!

If the installer doesn't work, [see here][windows-installer-issue]


If the program itself doesn't work, [see here][windows-cli-issue]

NB. Any issues created about this page which relate to the installer will be closed - please label such issues as "Windows>CLI-Installer"

[windows-cli-download-url]: https://github.com/nyxtryx/mouse-mover/blob/master/windows/ "Download Windows CLI"
[windows-installer-issue]: https://github.com/nyxtryx/mouse-mover/blob/guides/report-a-bug.md
[windows-cli-issue]: https://github.com/nyxtryx/mouse-mover/blob/guides/report-a-bug.md