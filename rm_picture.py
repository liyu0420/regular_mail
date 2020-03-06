import os

def rmpicture():
    path=os.path.abspath('.')
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".png"):             #  填写规则
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))