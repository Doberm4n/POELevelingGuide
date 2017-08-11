rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POE_leveling_guide.py -w --noupx --onedir --onefile --icon=res\todo-icon16.ico --version-file=version.txt