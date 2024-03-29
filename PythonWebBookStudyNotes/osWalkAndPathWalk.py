#coding:utf-8
'''
函数声明：os.path.walk(top,func,arg)

(1)参数top表示需要遍历的目录路径

(2)参数func表示回调函数，即对遍历路径进行处理的函数。所谓回调函数，是作为某个函数的参数使用，当某个事件触发时，
程序将调用定义好的回调函数处理某个任务。
注意：walk的回调函数必须提供三个参数：
第1个参数为os.path.walk的参数arg，
第2个参数表示目录dirname，
第3个参数表示文件列表names。
注意：os.path.walk的回调函数中的文件列表不和os.walk()那样将子目录和文件分开，而是混为了一摊，需要在回调函数中判断是文件还是子目录。

(3)参数arg是传递给回调函数的元组，为回调函数提供处理参数，arg可以为空。回调函数的第1个参数就是用来接收这个传入的元组的。

过程：以top 为根的目录树中的每一个目录 (包含 top 自身，如果它是一个目录)，以参数 (arg, dirname, names)调用回调函数 funct。
参数 dirname 指定访问的目录，参数 names 列出在目录中的文件(从 os.listdir(dirname)中得到)。
回调函数可以修改 names 改变 dirname 下面访问的目录的设置，
例如，避免访问树的某一部分。(由 names 关连的对象必须在合适的位置被修改，使用 del 或 slice 指派。)
注意：符号连接到目录不被作为一个子目录处理，并且因此 walk()将不访问它们。访问连接的目录你必须以os.path.islink(file) 和 os.path.isdir(file)标识它们，并且必须调用walk()
'''

# 区别：os.path.walk()与os.walk()产生的文件名列表并不相同.
# os.walk()产生目录树下的目录路径和文件路径，
# 而os.path.walk()只产生文件路径（是子目录与文件的混合列表）。

import os

def listDir(arg,dirname,files):
    for file in files:
        print os.path.join(dirname, file)

if __name__ == "__main__":
    print "__file__:", __file__
    print "os.getcwd():", os.getcwd()
    print

    path = "d:\PythonWebBookStudyNotes"

    print "os.listdir('d:\PythonWebBookStudyNotes'):", os.listdir(path)
    print

    for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
        print root, dirs, files
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
        print "---" * 10
    print

    for root, dirs, files in os.walk(".", topdown=False):
        print root, dirs, files
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
        print "---" * 10
    print

    os.path.walk(path, listDir, ())