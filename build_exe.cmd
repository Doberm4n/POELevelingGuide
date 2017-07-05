rmdir /Q /S build
rmdir /Q /S dist
pyinstaller POE_leveling_guide.py -w --version-file=version.txt