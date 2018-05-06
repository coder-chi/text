import os

base_path = 'data'

text_path = os.path.join(base_path, 'UTF-TEXT')
remove_file = os.path.join(base_path, 'remove.txt')


# 获取清理文件字符
def get_remove_list():
    with open(remove_file, 'r') as f:
        str = f.read()
    return str.split()

# 文件洗去字符
def file_remove_char(filename, li:list = get_remove_list()):
    filename = os.path.join(text_path, filename)
    with open(filename, 'r') as f:
        st = f.read()
    for ch in li:
        st = st.replace(ch, '')
        print(ch)
    with open(filename, 'w') as f:
        f.write(st)

# 文件夹洗去字符
def folder_remove_char():
    li = get_remove_list()

    for root, dirs, files in os.walk(text_path):
        for name in files:
            if '.txt' in name:
                print(name)
                file_remove_char(name, li)
            else:
                pass
