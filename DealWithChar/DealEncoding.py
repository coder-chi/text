import os

# 说明：UTF兼容ISO8859-1和ASCII，GB18030兼容GBK，GBK兼容GB2312，GB2312兼容ASCII
CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5']
# UTF-8 BOM前缀字节
UTF_8_BOM = b'\xef\xbb\xbf'

base_dir = 'TEXT'

utf_dir = 'UTF-TEXT'

# 获取文件编码类型

# 获取字符编码类型
def string_encoding(b: bytes):
    """
    获取字符编码类型
    :param b: 字节数据
    :return:
    """
    for code in CODES:
        try:
            b.decode(encoding=code)
            if 'UTF-8' == code and b.startswith(UTF_8_BOM):
                return 'UTF-8-SIG'
            return code
        except Exception:
            continue
    return '未知的字符编码类型'


def file_encoding(file_path):
    """
    获取文件编码类型
    :param file_path: 文件路径
    :return:
    """
    with open(file_path, 'rb') as f:
        return string_encoding(f.read())

# 直接改变编码为utf-8
def file_change_encoding(file_path:str):
    read_path = os.path.join(base_dir, file_path)
    enc = file_encoding(read_path)
    write_path = os.path.join(utf_dir, file_path)
    with open(read_path, 'rb') as f:
        b = f.read()
        text = b.decode(enc)
    with open(write_path, 'w') as f:
        f.write(text)