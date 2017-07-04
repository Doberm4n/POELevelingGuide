# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import QEvent
from PyQt4.QtCore import QObject
#import res.res
import sys
import re
import os
from json import load
from json import loads
import json

with open('guide_new.json') as data_file:
	jsonGuide = load(data_file)

# for key in  jsonGuide['guide']['tabs']:
# 	print key

print jsonGuide['guide']['tabs'][7]['name']

for i in range(10, -1, -1):
	print i