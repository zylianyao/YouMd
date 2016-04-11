# coding=utf-8
import os, shutil, sys, platform

# 目前只支持liunx和Windows
osSystem = platform.system().lower()


# 获取指定路径下所有指定后缀的文件
# dir 指定路径
# ext 指定后缀，链表&不需要带点 或者不指定。例子：['xml', 'java']
def GetFileFromThisRootDir(dir, ext=None):
    allfiles = []
    needExtFilter = (ext != None)
    for root, dirs, files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles


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
