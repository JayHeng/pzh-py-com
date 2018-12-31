pyinstaller.exe pyinstaller_pack_fw.spec
copy .\dist\Jays-PyCOM.exe ..\bin
rd /q /s .\build
rd /q /s .\dist