import os
import os.path
import shutil


class Traverse:
    def __init__(self,workdir):
        self.workdir = workdir

    def traversefile(self,workdir):
        count = 1
        for filename in os.listdir(workdir):
            file = os.path.join(workdir,filename)
            if os.path.isdir(file):
                print(file)
                count += self.traversefile(file)
            if os.path.isfile(file):
                shutil.move(file,workdir1)
        return count
workdir = r"E:\QQ文件\osshiyan"
workdir1 =r"E:\QQ文件\osshiyan\media"
traveres = Traverse(workdir)



