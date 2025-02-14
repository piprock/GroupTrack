pyinstaller --onefile --noconsole --name GroupTrack src\main.py
xcopy src\database dist\database\ /E
copy README.md dist
copy LICENSE dist
set name=GroupTrack_v%1
rename dist "%name%"
tar -cf "%name%.zip" "%name%"
rmdir /S /Q build
rmdir /S /Q %name%
del GroupTrack.spec