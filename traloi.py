import subprocess as sub
from time import sleep

#38-686
f = open("C:/Users/phanc/Desktop/hqbm/mess.txt", "r", encoding='utf-8')
a = f.readlines()
f.close()
for i in range(len(a)):
    a[i] = a[i].replace("\n", "")
h = input()
while True:
    #sub.run("adb shell input tap 38 686")
    #sub.run("adb shell input tap 38 686")
    sub.run("adb shell input tap 250 1540;am broadcast -a ADB_INPUT_TEXT --es msg '%s';input tap 666 1481" %h)
    #sub.run("adMb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'" % h)
    #sub.run("adb shell input tap 666 1481")
    sleep(0.000001)