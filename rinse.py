import os

base_path = 'data'

text_path = os.path.join(base_path, 'UTF-TEXT')
oldfile = os.path.join(base_path, 'oldchar.txt')
newfile = os.path.join(base_path, 'newchar.txt')

# 打开单个文件
def file_open(filename):
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'r') as f:
        data = f.read()

    return data


# 构建替换字典
def make_displace_dice():
    old_list = []
    new_list = []
    n = int(input("请输入字符组数："))
    while n > 0:
        oc = input('请于此输入旧字符：')
        old_list.append(oc)
        nc = input('请于此输入新字符：')
        new_list.append(nc)
        n -= 1
    with open(oldfile, 'a') as f:
        for c in old_list:
            f.write(c + '\n')
    with open(newfile, 'a') as f:
        for c in new_list:
            f.write(c + '\n')

# 读取替换字典
def get_displace_dict():
    with open(oldfile, 'r') as f:
        old = f.read()
    with open(newfile, 'r') as f:
        new = f.read()
    old_list = old.split()
    new_list = new.split()
    displace_dic = dict(zip(old_list, new_list))
    return displace_dic

# 文件替换字符
def file_replace(filename, dic:dict = get_displace_dict()):
    filepath = os.path.join(text_path, filename)
    with open(filepath, 'r') as f:
        st = f.read()
    for key,value in dic.items():
        print(st.count(key))
        st = st.replace(key, value)
    with open(filepath, 'w') as f:
        f.write(st)

# 文件夹替换字符
def folder_replace_char():
    dic = get_displace_dict()
    for root, dirs, files in os.walk(text_path):
        for name in files:
            if '.txt' in name:
                print(name)
                file_replace(name, dic)
            else:
                pass