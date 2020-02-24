import os


path = '/home/judy/minotedata/'
image = []
suffix = set()

def list_all_file(path):
    msg = os.walk(path)
    filePath = []
    for i, j, k in msg:
        for name in j:
            filePath.append(os.path.join(i, name))
        for name in k:
            filePath.append(os.path.join(i, name))

    return filePath


def locate_image():
    j = 1
    for i in list_all_file(path):
        cmd = 'file ' + '"' + i + '"'
        print('(' + str(j) + '/' + str(len(list_all_file(path))) + ')' + cmd)
        msg = os.popen(cmd).read()
        #print(msg)
        if 'image' in msg:
            distinguish_suffix(i)
            image.append(i)
        j += 1

    for i in image:
        print(i)
    return image


def copy_image_to_new_directory():
    newPath = '/home/judy/minote_image'
    for i in image:
        cmd = 'pycp ' + i + ' ' + newPath
        msg = os.popen(cmd).read()
        print(msg)


def distinguish_suffix(file_name):
    tmp = file_name.split('.')
    #print(len(tmp))
    if len(tmp) > 1:
        suffix.add(tmp[-1])



locate_image()
copy_image_to_new_directory()

for i in suffix:
    print(i)
