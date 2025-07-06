
import os

def read_file(filename: str) -> str:
    """
    读取 test 目录下指定文件的内容
    :param filename: 文件名（不含路径）
    :return: 文件内容字符串
    """
    file_path = os.path.join('test', filename)
    if not os.path.isfile(file_path):
        return f"文件 {filename} 不存在。"
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def list_files() -> list:
    """
    列出 test 目录下的所有文件名
    :return: 文件名列表
    """
    test_dir = 'test'
    if not os.path.isdir(test_dir):
        return []
    return [f for f in os.listdir(test_dir) if os.path.isfile(os.path.join(test_dir, f))]

def rename_file(old_name: str, new_name: str) -> str:
    """
    重命名 test 目录下的文件
    :param old_name: 原文件名
    :param new_name: 新文件名
    :return: 操作结果字符串
    """
    old_path = os.path.join('test', old_name)
    new_path = os.path.join('test', new_name)
    if not os.path.isfile(old_path):
        return f"文件 {old_name} 不存在，无法重命名。"
    if os.path.exists(new_path):
        return f"目标文件名 {new_name} 已存在，无法重命名。"
    os.rename(old_path, new_path)
    return f"文件 {old_name} 已重命名为 {new_name}。"