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
bk = "\\"
dest = "C:\\Users\\Admin\\Desktop\\pythoonnn\\bub"
desty = "C:\\Users\\Admin\\Desktop\\flask files"
destextfiles = "C:\\Users\\Admin\\Desktop\\Text files"
destcpp = "C:\\Users\\Admin\\Desktop\\cppfiles"
imgfilepath = "C:\\Users\\Admin\\Desktop\\images"
pdfilepath = "C:\\Users\\Admin\\Desktop\\pdf files"
ttfilepath = "C:\\Users\\Admin\\Desktop\\ttffiles"
javafilepath = "C:\\Users\\Admin\\Desktop\\javafiles"
output = render('Welcome back,Abhishek', colors=['red', 'blue'], align='center', font='chrome')
print(output)
countj, countcpp, counttxt, counttpdf, counttimg, countpy, countt = 0, 0, 0, 0, 0, 0, 0
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
# print("Welcome back,Abhishek.Your Desktop shall remain clean from now on.")

#output1 = render('No file transfer has taken place.', colors=['red', 'blue'], align='left', line_height=0, max_length=0, size=(30, 30))

if(countj == 0 and countcpp == 0 and counttxt == 0 and counttpdf == 0 and counttimg == 0 and countpy == 0 and countt == 0):
    print("No file transfer has taken place.")
else:
    print("No of python files moved:" + str(countpy))
    print("No of text files moved:" + str(counttxt))
    print("No of cpp files moved:" + str(countcpp))
    print("No of pdf files moved:" + str(counttpdf))
    print("No of image files moved:" + str(counttimg))
    print("No of font files moved:" + str(countt))
    print("No of Java files moved:" + str(countj))
