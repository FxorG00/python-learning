import os
def test_os() :
    # dir:directory 文件夹
    print(os.listdir("D:/test")) # 列出该路径下的内容
    print(os.path.isdir('D:/test/a')) # 判断指定路径是不是文件夹
    print(os.path.exists('D:/test/d')) # 判断指定路径是否存在
def get_files(path) :
    """
    从指定的文件夹中利用递归，找出所有文件，并且以 list 的形式返回
    :param path: 当前路径
    :return: 当前这个path现在&往后找的所有文件list
    """
    # print('你好')
    if os.path.exists(path) :
        pass
    else :
        print(f'当前目录{path}不存在')
        return []
    nw=list()
    for f in os.listdir(path) :
        # 获取当前目录的所有文件
        # print(path+f'/{f}')
        if os.path.isdir(path+f'/{f}') :
            # 当前这个是文件夹
            nex=get_files(path+f'/{f}')
            nw.extend(nex)
        else :
            # 当前这个是文件
            nw.append(path+f'/{f}')
    return nw
if __name__=='__main__' :
    # test_os()
    result=get_files('D:/test')
    for x in result :
        print(x)