"""
树形目录展示
编写一个函数 show_tree(dir_path: str, show_hidden: bool = False)，接收两个参数：

dir_path：目录路径，可以是绝对路径或相对路径（相对当前工作目录 CWD）

show_hidden：布尔类型，表示是否显示隐藏文件/目录

隐藏判断简单处理：文件或目录只要以.开头，则视为隐藏文件或目录，否则的话视为可视。

函数的功能是用树形递归的方式展示指定目录下的所有内容。效果类似于 Linux 的 tree 命令。

输出格式参考如下：

.
├── file1.txt
├── dir1
│   ├── file2.txt
│   └── file3.txt
└── file4.txt
"""

import os


def _is_hidden(filepath: str) -> bool:
    """判断文件或文件夹是否隐藏,判断规则是 是否以.开头的文件名字"""
    filepath = os.path.abspath(filepath)  # 始终转换为绝对路径
    if not os.path.exists(filepath): # 是否存在这个文件
        raise FileNotFoundError(f"路径不存在: {filepath}")
    basename = os.path.basename(filepath) #提取最后一级的目录名字或者文件名字 '/home/user/Documents/' -> Documents
    return basename.startswith(".")


def show_tree(dir_path: str, show_hidden: bool = False, _prefix: str = '') -> None:
    """以树形递归方式展示目录内容。"""
    path = os.path.abspath(dir_path)  # 始终转换为绝对路径

    entries = os.listdir(path) # 列出该目录下所有文件和子文件夹的名字 返回名字字符串列表 ['file1.txt', 'folder1', 'script.py', ...]
    if not show_hidden: # 是否需要隐藏 .开头的文件
        entries = [e for e in entries if not _is_hidden(os.path.join(path, e))] # 不隐藏的话就把.的文件和目录一起拼成列表

    entries.sort() # 对文件排序

    for i, entry in enumerate(entries): # 遍历文件列表
        entry_path = os.path.join(path, entry) # 拼接父目录
        is_last = i == len(entries) - 1 # 是否是最后一个文件

        connector = "└── " if is_last else "├── " 
        print(f"{_prefix}{connector}{entry}")

        if os.path.isdir(entry_path): # 是否是目录
            extension = "    " if is_last else "│   "
            show_tree(entry_path, show_hidden, _prefix + extension)
show_tree('../../AI作业')