# coding=utf-8
import os, shutil, sys, platform
from FileUtil import GetFileFromThisRootDir
# 目前只支持liunx和Windows
osSystem = platform.system().lower()
poFiles = GetFileFromThisRootDir("lang", "po")
startIndex = len(r"lang\lang_")
i18n = sys.prefix + os.sep + "Tools" + os.sep + "i18n" + os.sep + "msgfmt.py"
for pofile in poFiles:
    if osSystem == "linux":
        exeStr = "msgfmt " + pofile + " -o lang"+os.sep +"lang_" + pofile[startIndex:len(pofile) - 2] + "mo"
        os.system(exeStr)
    else:
        os.system("python "+i18n + " " + pofile)
# 移动所有mo到对应语言的目录
files = GetFileFromThisRootDir("lang", "mo")
for file in files:
    shutil.move(file, "locale" + os.sep + file[startIndex:][:2] + os.sep + "LC_MESSAGES\lang.mo")
