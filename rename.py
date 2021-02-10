import os

f = os.listdir('./')
f.remove('rename.py')
f.sort()
print(f)
print('--------length--------')
print(len(f))
print('--------item-------')
print(f)
print('--------开始改名--------')
n = 0
for i in f:
    oldname = f[n]
    newname = str(n) + '.png'
    os.rename(oldname, newname)
    print(oldname, '=======>', newname)
    n = n + 1

