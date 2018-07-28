import os
import shutil
from pathlib import Path
from cfonts import render, say
os.chdir("C:\\Users\\Admin\\Desktop")
lst = [x for x in os.listdir(os.getcwd()) if x.endswith(".py")]
lstextf = [x for x in os.listdir(os.getcwd()) if x.endswith(".txt")]
cppfil = [x for x in os.listdir(os.getcwd()) if x.endswith(".cpp")]
imagefil = [x for x in os.listdir(os.getcwd()) if x.endswith(".PNG") or x.endswith(".jpg") or x.endswith(".png")]
pdffil = [x for x in os.listdir(os.getcwd()) if x.endswith(".pdf")]
ttffils = [x for x in os.listdir(os.getcwd()) if x.endswith(".ttf")]
javafils = [x for x in os.listdir(os.getcwd()) if x.endswith(".java")]
mp3files = [x for x in os.listdir(os.getcwd()) if x.endswith(".mp3")]
wordfiles = [x for x in os.listdir(os.getcwd()) if x.endswith(".docx")]
zipfiles = [x for x in os.listdir(os.getcwd()) if x.endswith(".zip")]
zipfiles.extend([x for x in os.listdir(os.getcwd()) if x.endswith(".zipx")])
zipfiles.extend([x for x in os.listdir(os.getcwd()) if x.endswith(".7z")])
zipfiles.extend([x for x in os.listdir(os.getcwd()) if x.endswith(".rar")])
bk = "\\"
dest = "C:\\Users\\Admin\\Desktop\\pythoonnn\\bub"
desty = "C:\\Users\\Admin\\Desktop\\flask files"
destextfiles = "C:\\Users\\Admin\\Desktop\\Text files"
destcpp = "C:\\Users\\Admin\\Desktop\\cppfiles"
imgfilepath = "C:\\Users\\Admin\\Desktop\\images"
pdfilepath = "C:\\Users\\Admin\\Desktop\\pdf files"
ttfilepath = "C:\\Users\\Admin\\Desktop\\ttffiles"
javafilepath = "C:\\Users\\Admin\\Desktop\\javafiles"
mp3filepath = "C:\\Users\\Admin\\Desktop\\songsss"
wordsfilepath = "C:\\Users\\Admin\\Desktop\\Word documents"
zipfilespath = "C:\\Users\\Admin\\Desktop\\Zipfiles"
output = render('Welcome back,Abhishek', colors=['red', 'blue'], align='center', font='chrome')
print(output)
countj, countcpp, counttxt, counttpdf, counttimg, countpy, countt, countmus, countword, countzips = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
# Pythonn files
for x in lst:
    name = x
    if name.startswith('flask'):
        countpy += 1
        shutil.move(os.getcwd() + bk[0] + name, desty)
        print("Flask related file detected and moved to seperate flask folder.")
    else:
        fcheckexist = Path(dest + bk[0] + name)
        if(fcheckexist.is_file()):
            os.remove(os.getcwd() + bk[0] + name)
        else:
            countpy += 1
            shutil.move(os.getcwd() + bk[0] + name, dest)
# zip files
os.chdir("C:\\Users\\Admin\\Desktop")
for t in zipfiles:
    val = t
    fcheckexist9 = Path(zipfilespath + bk[0] + val)
    if(fcheckexist9.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countzips += 1
        shutil.move(os.getcwd() + bk[0] + val, zipfilespath)
# Text files
os.chdir("C:\\Users\\Admin\\Desktop")
for t in lstextf:
    val = t
    fcheckexist1 = Path(destextfiles + bk[0] + val)
    if(fcheckexist1.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        counttxt += 1
        shutil.move(os.getcwd() + bk[0] + val, destextfiles)
# Word files
os.chdir("C:\\Users\\Admin\\Desktop")
for t in wordfiles:
    val = t
    fcheckexist1 = Path(wordsfilepath + bk[0] + val)
    if(fcheckexist1.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countword += 1
        shutil.move(os.getcwd() + bk[0] + val, wordsfilepath)
# cpp files
os.chdir("C:\\Users\\Admin\\Desktop")
for c in cppfil:
    val = c
    fcheckexist2 = Path(destcpp + bk[0] + val)
    if(fcheckexist2.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countcpp += 1
        shutil.move(os.getcwd() + bk[0] + val, destcpp)
# image files
os.chdir("C:\\Users\\Admin\\Desktop")
for i in imagefil:
    val = i
    fcheckexist3 = Path(imgfilepath + bk[0] + val)
    if(fcheckexist3.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        counttimg += 1
        shutil.move(os.getcwd() + bk[0] + val, imgfilepath)
# pdf files
os.chdir("C:\\Users\\Admin\\Desktop")
for p in pdffil:
    val = p
    fcheckexist4 = Path(pdfilepath + bk[0] + val)
    if(fcheckexist4.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        counttpdf += 1
        shutil.move(os.getcwd() + bk[0] + val, pdfilepath)
# ttf font files
os.chdir("C:\\Users\\Admin\\Desktop")
for t in ttffils:
    val = t
    fcheckexist5 = Path(ttfilepath + bk[0] + val)
    if(fcheckexist5.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countt += 1
        shutil.move(os.getcwd() + bk[0] + val, ttfilepath)
# java files
os.chdir("C:\\Users\\Admin\\Desktop")
for j in javafils:
    val = j
    fcheckexist6 = Path(javafilepath + bk[0] + val)
    if(fcheckexist6.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countj += 1
        shutil.move(os.getcwd() + bk[0] + val, javafilepath)
# music mp3 files
os.chdir("C:\\Users\\Admin\\Desktop")
for j in mp3files:
    val = j
    fcheckexist7 = Path(mp3filepath + bk[0] + val)
    if(fcheckexist7.is_file()):
        os.remove(os.getcwd() + bk[0] + val)
    else:
        countmus += 1
        shutil.move(os.getcwd() + bk[0] + val, mp3filepath)

if(countj == 0 and countcpp == 0 and counttxt == 0 and counttpdf == 0 and counttimg == 0 and countpy == 0 and countt == 0 and countmus == 0 and countword == 0 and countzips == 0):
    print("No file transfer has taken place.")
else:
    print("No of python files moved:" + str(countpy))
    print("No of text files moved:" + str(counttxt))
    print("No of cpp files moved:" + str(countcpp))
    print("No of pdf files moved:" + str(counttpdf))
    print("No of image files moved:" + str(counttimg))
    print("No of font files moved:" + str(countt))
    print("No of Java files moved:" + str(countj))
    print("No of mp3 files moved:" + str(countmus))
    print("No of word files moved:" + str(countword))
    print("No of zip files moved:" + str(countzips))
