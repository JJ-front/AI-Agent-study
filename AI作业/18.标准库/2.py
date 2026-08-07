'''
Markdown 文件合并
编写一个函数 merge_markdown(files: list[str], output: str) -> None，接收两个参数：

files：Markdown 文件路径列表
output：合并后保存的目标文件路径
函数的作用是将多个 Markdown 文件合并为一个文件保存到目标路径。合并规则如下：

最终合并结果的一级标题固定为 # 合并结果
所有原始 Markdown 文件的标题需要降级：
一级标题 # → 二级标题 ##
二级标题 ## → 三级标题 ###
以此类推
六级标题 ###### → 正文，用 加粗 表示
非标题内容（正文、列表、代码块等）保持不变
'''
# 导入 re 模块，用于正则表达式操作
import re
# 导入 os 模块，用于文件路径操作
import os

# 编译正则表达式对象，用于匹配 Markdown 标题
# ^ 表示行首（配合 re.MULTILINE）
# (#{1,6}) 捕获组1：匹配 1-6 个 # 符号
# \s+ 至少一个空白字符（空格或制表符）
# (.+) 捕获组2：匹配标题内容（至少一个字符）
# $ 表示行尾
# re.MULTILINE 让 ^ 匹配每一行的开头，而不仅仅是整个字符串的开头
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


def _demote_heading(match: re.Match) -> str:
    """
    将匹配到的标题降级一级。
    
    参数:
        match: 正则匹配对象，包含标题的级别和内容
    
    返回:
        降级后的标题字符串
    """
    # 从匹配对象中提取捕获组
    # hashes: 如 "###" 或 "##"
    # content: 标题内容，如 "我的标题"
    hashes, content = match.group(1), match.group(2)
    
    # 计算标题级别（# 的数量）
    # level = 1 表示 H1, level = 2 表示 H2, 以此类推
    level = len(hashes)
    
    # 如果当前级别小于 6（即不是最深的 H6）
    if level < 6:
        # 在原级别基础上增加一个 #，实现降级
        # 例如: "# 标题" -> "## 标题"
        #       "## 标题" -> "### 标题"
        return f'{"#" * (level + 1)} {content}'
    else:
        # 如果已经是 H6（最深层级），无法再降级
        # 将标题加粗显示（**粗体**），作为替代方案
        return f"**{content}**"


def merge_markdown(files: list[str], output: str) -> None:
    """
    合并多个 Markdown 文件，所有标题降级一级。
    
    参数:
        files: 要合并的 Markdown 文件路径列表
        output: 输出文件的路径
    """
    # parts 列表用于存储最终输出的所有部分
    # 初始包含一个 H1 标题 "合并结果" 和一个空行
    parts: list[str] = ["# 合并结果", ""]

    # 遍历每个要合并的文件
    for filepath in files:
        # 将文件路径转换为绝对路径（确保路径正确）
        filepath = os.path.abspath(filepath)
        
        # 以 UTF-8 编码打开文件并读取全部内容
        # with 语句确保文件读取后自动关闭
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        # 使用正则表达式替换所有标题
        # HEADING_RE.sub() 会查找所有匹配的标题
        # 对每个匹配调用 _demote_heading 函数进行降级
        # 非标题内容保持不变
        demoted = HEADING_RE.sub(_demote_heading, content)
        
        # 将降级后的内容添加到 parts 列表
        # .strip() 去除首尾空白字符（避免多余空行）
        parts.append(demoted.strip())
        
        # 添加一个空行，分隔不同文件的内容
        parts.append("")

    # 将输出文件路径转换为绝对路径
    output = os.path.abspath(output)
    
    # 以 UTF-8 编码写入输出文件
    # with 语句确保文件写入后自动关闭
    with open(output, "w", encoding="utf-8") as f:
        # 使用换行符连接所有部分
        # .strip() 去除首尾空白字符
        # 最后添加一个换行符（符合文件结尾规范）
        f.write("\n".join(parts).strip() + "\n")