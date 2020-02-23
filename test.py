import os
import subprocess

path = '/home/judy/minotedata/DCIM/Facebook'


def listAllFile(path):
    msg = os.walk(path)
    filePath = [];
    for i, j, k in msg:
        for name in j:
            filePath.append(os.path.join(i, name))
        for name in k:
            filePath.append(os.path.join(i, name))

    return filePath


j = 1
image = []
for i in listAllFile(path):

    cmd = 'file ' + '"' + i + '"'
    print('(' + str(j) + '/' + str(len(listAllFile(path))) + ')' + cmd)
    msg = os.popen(cmd).read()
    print(msg)
    if 'image' in msg:
        image.append(i)
    j += 1


for i in image:
    print(i)


print(len(image))
