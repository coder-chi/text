import os
import chardet

# 说明：UTF兼容ISO8859-1和ASCII，GB18030兼容GBK，GBK兼容GB2312，GB2312兼容ASCII
CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5']
# UTF-8 BOM前缀字节
UTF_8_BOM = b'\xef\xbb\xbf'

base_dir = 'TEXT'

utf_dir = 'UTF-TEXT'

# 获取字符编码类型
def string_encoding(b: bytes):
    """
    使用charset 鉴定字符编码类型
    :param b: 字节数据
    :return str: 字符编码类型
    """
    d = chardet.detect(b)
    return d.get('encoding')

# 获取文件编码类型
def file_encoding(file_path):
    """
    获取文件编码类型
    :param file_path: 文件路径
    :return:
    """
    with open(file_path, 'rb') as f:
        return string_encoding(f.read())
def file_change(file_path):
    print(file_path)
    enc = file_encoding(file_path)
    write_path = os.path.join(utf_dir, file_path)
    with open(file_path, 'rb') as f:
        b = f.read()
        text = b.decode(enc)
    with open(write_path, 'w') as f:
        f.write(text)


def folder_change():
    for root, dirs, files in os.walk(base_dir):
        for name in files:
            if '.txt' in name:
                print(name)
                read_path = os.path.join(root, name)
                enc = file_encoding(read_path)
                write_path = os.path.join(utf_dir, name)
                with open(read_path, 'rb') as f:
                    b = f.read()
                    text = b.decode("GB18030")
                with open(write_path, 'w') as f:
                    f.write(text)
            else:
                pass


if __name__ == '__main__':
    folder_change()