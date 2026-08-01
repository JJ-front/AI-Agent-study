# 认识Agent

## 开发语言层面

开发Agents目前主要有两种语言：`Python`和`TypeScript`

|      | Python    | TypeScript                        |
| ---- | --------- | --------------------------------- |
| AI生态 | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐                              |
| 学习内容 | ⭐⭐⭐⭐⭐     | ⭐⭐⭐                               |
| 优先场景 | 服务端       | 客户端                               |
| 应用举例 | Dify、Coze | claude code、codex等桌面应用、OpenClaw等等 |
| 市场情况 | 服务端产品居多   | 客户端产品较少                           |

职业建议：

- **前端工程师**：学习`TypeScript`开发`Agents`
- **Agents应用工程师**：学习`Python`开发`Agents`
- **AI 全栈工程师**：最好都学习

## Python学习内容（只为了会Agent）

Agents开发会用到的要学，比如：

- 语法规则
- 包管理
- 网络通信
- 文件 IO
- 高阶函数
- ...

## 如何学习？

学习任何技术只有一个目标：建立知识体系！

尤其是在AI时代。

具体的手段：

- “古法编程” : 为了熟悉代码熟悉语法（虽然是AI时代，但是必要的知识掌握还是需要古法编程来熟悉并掌握）
- 费曼学习法：每学习一章节内容，需要自己说出来（可以找朋友练习，模拟面试当前学完的章节内容）
- 场景训练：通过对每一章节的学习，根据对应的章节内容所需面对的场景提出问题并解决问题
- ...

# Python环境搭建

## 语言分类：

解释型：JavaScript、Python、PHP

- 什么叫解释形代码？
  - 一边运行，一边解释，运行环境一定有解释器
    - 例：javaScript
      - 运行环境浏览器（内置V8引擎作为解释器）
    - 例：python
      - 解释器就是安装环境需要的东西

编译型:C、C++、C#、Java

- 什么叫编译形代码？
  - 例：java (就是运行代码一定要经过编译，源代码对应一份编译结果)
    - *.java --> 编辑器 --> *.class

## Python安装包

Python安装包中包含以下核心组件：

- 解释器：默认为`CPython` （解释器用C语言写的）
- 包管理器：`pip`
- 标准库：`os、sys、urllib、pathlib、...`
- 交互式终端：`REPL`
  - 例如前端的交互式窗口，在终端输入node，进入的环境就是交互式终端
  - python也一样，在终端输入python后，进入的环境

### Python发行版

Python有很多的发行版，不同的发行版又有很多的版本

- **官方 Python (CPython)**：C 语言原生实现，Python 标准参考版本，带 GIL，生态最全，日常开发默认首选

- **ActivePython**：商业公司打包的 CPython 发行版，企业级稳定适配，预装常用依赖，偏商用场景

- **Anaconda**：面向数据科学的全家桶 CPython，内置海量数据分析、AI 库，体积大，适合数据分析一站式环境

- **Miniconda**：Anaconda 极简精简版，仅保留 Python+conda 包管理器，无多余预装库，轻量灵活

- **Miniforge**：开源免费 conda 发行版，无 Anaconda 商业版权限制，社区维护，替代 Miniconda 首选

- **Mambaforge**：基于 Miniforge，把 conda 替换为极速 mamba 包管理器，安装依赖速度远超原生 conda

- **Cinder**：Meta 自研优化版 CPython，针对长驻服务、低延迟做运行时与 GC 优化，内部业务专用，通用性差

- **Nogil**：Python 官方无 GIL 自由线程版本，去除全局解释器锁，支持多线程真并行，适合多核并发场景

- **PyPy**：带 JIT 即时编译的 Python 解释器，纯 Python 代码运行速度远超 CPython，C 扩展库兼容性一般

- **Jython**：运行在 JVM 虚拟机上的 Python，可无缝调用 Java 类库，无 GIL，不兼容 C 语言扩展包

- **IronPython**：运行在.NET 平台上的 Python，可直接调用 C#/.NET 生态库，多用于 Windows 桌面与.NET 集成

- **GraalPython/GraalPy**：基于 GraalVM 的高性能 Python，自带强 JIT 优化，支持与 Java 等多语言互通

- **Stackless Python**：CPython 分支，自研无栈微协程，支持超高并发轻量任务，适合游戏、高并发服务场景

- **MicroPython**：极简裁剪版 Python，专为单片机、嵌入式 IoT 设备设计，体积小、占用内存极低

基于上述问题，因此我们选择使用版本管理器来管理多个版本，可以类比前端的**NVM**

### Python版本管理器

#### pyenv

使用`pyenv`来管理多个`python`版本

##### mac 安装 pyenv

mac 建议使用 HomeBrew 安装 pyenv

```shell
# 安装构建python包的前置依赖项
brew install zstd openssl readline xz zlib
# 安装pyenv
brew install pyenv
# 测试
pyenv --version
```

配置镜像源

```shell
# ~/.zshrc
export PYTHON_BUILD_MIRROR_URL="https://mirrors.aliyun.com/python-release/source/"
```

##### win 安装 pyenv

以管理员身份打开`powershell`

```shell
# 解决权限问题
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# 运行安装命令
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
# 测试
pyenv --version
```

配置镜像源

1. 右键「此电脑」→「属性」→「高级系统设置」→「环境变量」。

![a911aa22f25bf22fc48a83885299fb4f~tplv-a9rns2rl98-pc_smart_face_crop-v1_512_384](https://resource.duyiedu.com/yuanjin/202605111101231.webp)

2. 在**用户变量**（只影响当前用户）或**系统变量**（所有用户）里点「新建」：
   
   - 变量名：`PYTHON_BUILD_MIRROR_URL`
   
   - 变量值：填下面任意一个国内源
     
     ```
     https://mirrors.aliyun.com/python
     https://mirrors.tuna.tsinghua.edu.cn/python/
     https://mirrors.huaweicloud.com/python/
     https://registry.npmmirror.com/-/binary/python/
     ```

全部确定，**关闭旧 PowerShell，新开一个**即可。

### pyenv 使用

```shell
# 查看所有可安装的python版本
pyenv install --list
# 利用管道命令搜索
pyenv install --list | grep "^  3.14"
# 安装特定版本
pyenv install 3.14.1
# 卸载特定版本
pyenv uninstall 3.14.1
# 查看已安装的版本
pyenv versions
# 查看当前正在使用哪个版本
pyenv version

# 切换全局版本
pyenv global 3.14.1
# 切换本地版本
pyenv local 3.14.1
# 切换当前终端版本（临时生效）
pyenv shell 3.14.1
```

## IDE

* [PyCharm](https://www.jetbrains.com/pycharm/): Python 专属 IDE，开箱即用，专为 Python 设计，官方内置了 python 开发的诸多功能。
* [VSCode](https://code.visualstudio.com/download)： 通用代码编辑器，装插件才支持 Python，全能型。

选择哪个其实无所谓

本课程选择使用`VSCode`，理由：

1. 全栈开发**尽量**统一编辑器，减少心智负担
2. `VSCode`体系对`AI Coding`支持更友好
3. 轻量高效、启动速度快，低配电脑也能流畅使用

### VSCode插件

安装好`VSCode`后，依次安装以下插件

* **Python**
  * 作用：语法高亮、代码提示、运行调试、虚拟环境识别，**最核心**。
* **Code Runner**
  * 作用：方便调试代码,右键一键运行Python代码，不用敲命令，新手超好用。
* **Black Formatter**自动格式化代码，统一代码风格，不用手动排版。
* **Chinese**VSCode界面汉化，零基础友好。

### VSCode配置

code runner 配置

```json

    // code runner插件 不同语言配置的运行器位置 绝对路径
    "code-runner.executorMap": {
        // 这里要填写 python 的绝对路径
        "python": "C:\\Users\\xiaolei520\\.pyenv\\pyenv-win\\shims\\python",
    },
```

自动格式化配置

```json

    // 保存是否自动格式化
    "editor.formatOnSave": true,
    // python 格式化配置
    "[python]": {
        // 使用black-formatter插件格式化
        "editor.defaultFormatter": "ms-python.black-formatter",
        // 格式化缩进4个字符
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
    },
```

## 作业（已完成）

### hello world的py代码输出

# Python基本语法

## 语言基本特征

* **解释型**
  * 第二章已有解释
* **强类型**
  * 不同类型之间的变量不允许进行运算，否则报错
  * 数字类型之间可以运算，例如int和float之间，bool类型也是数字类型
* **动态类型**
  * 变量无需声明类型，直接赋值即可创建
  * 可以任意更改类型，在运行时才确定类型
* **面向对象**
  * python中所有数据均是对象
    * 例如：int类型（1，2，3），都是int类的实例（class）

## 注释

    # 这是单行注释
    
    """
    这是多行注释
    可以写多行
    """
    
    '''
    这也是多行注释
    可以写多行
    '''

## 数据类型

| 类别             | 类型名          | 字面量              | 说明                        |
| -------------- | ------------ | ---------------- | ------------------------- |
| 数字类型           | ==int==      | 1, 2, -3, 0      | 支持无限大小                    |
| 数字类型           | ==float==    | 1.5, -0.3, 2e10  | 64位双精度                    |
| 数字类型           | complex      | 1+2j, 3-4j       | j表示$\sqrt{-1}$            |
| 数字类型<br />布尔类型 | ==bool==     | True, False      | True是1的别名<br />False是0的别名 |
| 字符串            | ==str==      | "hello", 'world' |                           |
| 空值             | ==NoneType== | None             |                           |
| 容器类型           | 多种类型         | 后续介绍             | list/tuple/...            |

原子类型/基本内置类型/标量类型：int、float、complex、bool、str、NoneType

容器类型：list、tuple、...

```python
# 整数（多种进制）
print(42)       # 十进制
print(0b1010)   # 二进制 = 10 （0b开头）
print(0o52)     # 八进制 = 42 （0o开头）
print(0x2A)     # 十六进制 = 42 （0x开头）

# 浮点数（多种写法）
print(3.14)     # 小数形式
print(-0.5)     # 负数
print(2.5e10)   # 科学计数法 = 25000000000.0
print(1.2e-3)   # 负指数 = 0.0012

# 布尔值
print(True)     # 真
print(False)    # 假

# 字符串（单双引号等价）
print("hello")  # 双引号
print('world')  # 单引号
print('''Hello
world''')  # 多行字符串
print("""Hello
world""")  # 多行字符串

# 空值
print(None)     # 空值
```



## type函数

```python
# 整数
print(type(42))       # <class 'int'>
print(type(0b1010))   # <class 'int'>
print(type(0o52))     # <class 'int'>
print(type(0x2A))     # <class 'int'>

# 浮点数
print(type(3.14))     # <class 'float'>
print(type(-0.5))     # <class 'float'>
print(type(2.5e10))   # <class 'float'>
print(type(1.2e-3))   # <class 'float'>

# 布尔值
print(type(True))     # <class 'bool'>
print(type(False))    # <class 'bool'>

# 字符串
print(type("Hello"))  # <class 'str'>
print(type('World'))  # <class 'str'>

# 空值
print(type(None))     # <class 'NoneType'>
```

注意：`type`函数返回的不是字符串，而是类型对象

```python
print(type(42) == int) # True
```



## 变量

### 变量定义

Python是动态类型语言，变量无需声明类型，直接赋值即可创建。

```python
# 变量赋值
name = "Alice"      # 字符串
age = 25            # 整数
pi = 3.14159        # 浮点数
is_valid = True     # 布尔值
```

### 变量命名规则

| 规则            | 说明                     | 示例                     |
| ------------- | ---------------------- | ---------------------- |
| 字母/下划线开头      | 变量名必须以字母或下划线开头         | `name`, `_value`       |
| 区分大小写         | `Name` 和 `name` 是不同的变量 | `Name = 1`, `name = 2` |
| 不能是关键字        | 不能使用Python保留字          | `if`, `for`, `class` 等 |
| 只能包含字母/数字/下划线 | 不能包含空格或特殊字符            | `user_name`, `value2`  |

**关键字（不能作为变量名）：**

`False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield` 

```python
# 有效命名
user_name = "张三"
_age = 25
MAX_SIZE = 100
value2 = 3.14

# 无效命名（会报错）
# 2value = 10      # 数字开头
# user-name = "a"  # 包含连字符
# class = 5        # 关键
```

### 命名规范

| 类型                                   | 规范                     | 示例                         |
| ------------------------------------ | ---------------------- | -------------------------- |
| 变量名                                  | 小写字母，下划线分隔（snake_case） | `user_name`, `total_count` |
| 常量名(py实际不存在常量，只是命名上通过这样来区分，一种规范，软约束) | 全大写字母，下划线分隔            | `MAX_SIZE`, `PI`           |
| 类名                                   | 首字母大写的驼峰命名（PascalCase） | `UserInfo`, `DataModel`    |
| 私有变量                                 | 以下划线开头                 | `_internal`, `__private`   |

### 多重赋值

```python
# 同时赋值多个变量
a, b, c = 1, 2, 3

# 交换变量值
x, y = 10, 20
x, y = y, x  # x=20, y=10

# 相同值赋给多个变量
a = b = c = 0  # a=0, b=0, c=0
```



### 变量类型转换

```python
# 字符串转整数
age_str = "25"
age_int = int(age_str)      # 25

# 整数转字符串
num = 100
num_str = str(num)          # "100"

# 整数转浮点数
x = 5
x_float = float(x)          # 5.0

# 浮点数转整数（截断小数）
y = 3.9
y_int = int(y)              # 3（不是四舍五入）

# 转布尔值
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("hi"))   # True
```

## 字符串格式化（f-string）

Python 3.6+ 引入了 f-string（格式化字符串字面量），是最简洁、最常用的字符串格式化方式。

在字符串前加 `f` 或 `F`，在花括号 `{}` 中直接嵌入变量或表达式：

```python
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")  # 姓名: Alice, 年龄: 25

# 直接嵌入表达式
a, b = 3, 5
print(f"{a} + {b} = {a + b}")       # 3 + 5 = 8
```

## 运算符

### 算术运算符

| 运算符  | 名称  | int     | float   | str   | bool            | NoneType |
| ---- | --- | ------- | ------- | ----- | --------------- | -------- |
| `+`  | 加法  | 数值相加    | 数值相加    | 字符串拼接 | True=1, False=0 | 不支持      |
| `-`  | 减法  | 数值相减    | 数值相减    | 不支持   | True=1, False=0 | 不支持      |
| `*`  | 乘法  | 数值相乘    | 数值相乘    | 字符串重复 | True=1, False=0 | 不支持      |
| `/`  | 除法  | 返回float | 返回float | 不支持   | True=1, False=0 | 不支持      |
| `//` | 整除  | 整数除法    | 整数除法    | 不支持   | True=1, False=0 | 不支持      |
| `%`  | 取余  | 取余数     | 取余数     | 不支持   | True=1, False=0 | 不支持      |
| `**` | 幂运算 | 幂运算     | 幂运算     | 不支持   | True=1, False=0 | 不支持      |

```python
# int
print(5 + 3)        # 8
print(5 - 3)        # 2
print(5 * 3)        # 15
print(5 / 3)        # 1.666...
print(5 // 3)       # 1
print(5 % 3)        # 2
print(5 ** 3)       # 125

# float
print(5.0 + 3.0)    # 8.0
print(5.0 - 3.0)    # 2.0
print(5.0 * 3.0)    # 15.0
print(5.0 / 3.0)    # 1.666...
print(5.0 // 3.0)   # 1.0
print(5.0 % 3.0)    # 2.0
print(5.0 ** 3.0)   # 125.0

# str
print("Hello" + "World")  # "HelloWorld"
print("Hi" * 3)           # "HiHiHi"

# bool (True=1, False=0)
print(True + True)   # 2
print(True * 5)      # 5
print(False * 10)    # 0

# NoneType - 所有算术运算都会报错
# print(None + 1)   # TypeError
```

### 比较运算符

| 运算符  | 名称   | int  | float | str   | bool               | NoneType    |
| ---- | ---- | ---- | ----- | ----- | ------------------ | ----------- |
| `==` | 等于   | 数值比较 | 数值比较  | 内容比较  | True\==1, False==0 | None==None  |
| `!=` | 不等于  | 数值比较 | 数值比较  | 内容比较  | True!=0            | None!=非None |
| `<`  | 小于   | 数值比较 | 数值比较  | 字典序比较 | True=1, False=0    | 不支持         |
| `>`  | 大于   | 数值比较 | 数值比较  | 字典序比较 | True=1, False=0    | 不支持         |
| `<=` | 小于等于 | 数值比较 | 数值比较  | 字典序比较 | True=1, False=0    | 不支持         |
| `>=` | 大于等于 | 数值比较 | 数值比较  | 字典序比较 | True=1, False=0    | 不支持         |

```python
# int
print(5 == 5)       # True
print(5 != 3)       # True
print(5 > 3)        # True

# float
print(5.0 == 5.0)   # True
print(5.0 != 3.0)   # True
print(5.0 > 3.0)    # True

# str (按字典序/ASCII码比较)
print("abc" == "abc")     # True
print("abc" != "def")     # True
print("abc" < "def")      # True
print("A" < "a")          # True (A=65, a=97)

# bool
print(True == 1)          # True
print(False == 0)         # True
print(True > False)       # True

# NoneType
print(None == None)       # True
print(None != 0)          # True
print(None != False)      # True
# print(None > 0)         # TypeError
```

### 链式比较

Python 支持**链式比较**，可以像数学公式一样连续写比较运算符：

```python
x = 5

# 传统写法（其他语言）
print(x > 1 and x < 10)   # True

# Python 链式比较（更简洁）
print(1 < x < 10)         # True
print(1 < x <= 5)         # True
print(5 <= x < 10)        # True
print(1 < x < 3)          # False

# 甚至可以更复杂
print(1 < x < 10 < 100)   # True
```

**等价规则：** `a < b < c` 等价于 `a < b and b < c`，但**只计算一次** `b`。

### 赋值运算符

| 运算符   | 示例        | 等价于          | 适用类型            | 注意点（自己发现）                              |
| ----- | --------- | ------------ | --------------- | -------------------------------------- |
| `=`   | `a = 5`   | -            | 所有类型            |                                        |
| `+=`  | `a += 3`  | `a = a + 3`  | int, float, str |                                        |
| `-=`  | `a -= 3`  | `a = a - 3`  | int, float      |                                        |
| `*=`  | `a *= 3`  | `a = a * 3`  | int, float, str |                                        |
| `/=`  | `a /= 3`  | `a = a / 3`  | float           | 一定得到的是float类型，除尽的会补充.0  例如 1 / 1 = 1.0 |
| `//=` | `a //= 3` | `a = a // 3` | int, float      |                                        |
| `%=`  | `a %= 3`  | `a = a % 3`  | int, float      |                                        |
| `**=` | `a **= 3` | `a = a ** 3` | int, float      |                                        |

```python
# int
a = 10
a += 5    # a = 15
a -= 3    # a = 12
a *= 2    # a = 24
a /= 4    # a = 6.0 (注意：/= 结果变为float)

# str
s = "Hello"
s += " World"  # s = "Hello World"
s *= 2         # s = "Hello WorldHello World"
```

### 海象运算符（:=）

```python
# 传统写法：先赋值，再判断
line = input("输入: ")
while line != "quit":
    print(f"你输入了: {line}")
    line = input("输入: ")

# 使用海象运算符：赋值和判断合二为一
while (line := input("输入: ")) != "quit":
    print(f"你输入了: {line}")
```

**注意：** 海象运算符是 Python 3.8 的新特性，老版本不支持。

### 逻辑运算符

| 运算符   | 说明  | 返回值规则                   |
| ----- | --- | ----------------------- |
| `and` | 逻辑与 | 第一个为False则返回第一个，否则返回第二个 |
| `or`  | 逻辑或 | 第一个为True则返回第一个，否则返回第二个  |
| `not` | 逻辑非 | 返回True或False            |

**各类型真假值：**

* int: `0`为False，其他为True

* float: `0.0`为False，其他为True

* str: `""`为False，其他为True

* bool: `False`为False，`True`为True

* NoneType: `None`为False

* 容器类型没数据：[],{},()
  
  ```python
  # int
  print(0 and 5)        # 0 (0为False，返回0)
  print(3 and 5)        # 5 (3为True，返回5)
  print(0 or 5)         # 5 (0为False，返回5)
  print(3 or 5)         # 3 (3为True，返回3)
  print(not 0)          # True
  print(not 5)          # False
  
  # float
  print(0.0 and 5.0)    # 0.0
  print(3.0 and 5.0)    # 5.0
  print(not 0.0)        # True
  
  # str
  print("" and "hello") # "" (空字符串为False)
  print("hi" and "hello") # "hello"
  print(not "")         # True
  print(not "hello")    # False
  
  # bool
  print(True and False)  # False
  print(True or False)   # True
  print(not True)        # False
  
  # NoneType
  print(None and True)   # None
  print(None or True)    # True
  print(not None)        # True
  
  #容器
  ```

### 三元运算符（条件表达式）

Python 的三元运算符（条件表达式）是一种简洁的 `if-else` 写法，用于在一行中根据条件选择不同的值。

**语法：**

```python
结果 = 真值 if 条件 else 假值
```



```python
score = 85

# 传统写法
if score >= 60:
    result = "及格"
else:
    result = "不及格"

# 三元运算符（更简洁）
result = "及格" if score >= 60 else "不及格"
print(result)  # 及格

# 嵌套三元运算符（不推荐过度嵌套）
age = 25
category = "青年" if age < 40 else ("中年" if age < 60 else "老年")
```



## 输入输出

### print输出

```python
# 输出字符串
print("Hello, World!")

# 输出多个值，用空格分隔
print("年龄:", 25)

# 自定义分隔符
print("a", "b", "c", sep="-")  # a-b-c

# 自定义结束符（默认换行）
print("Hello", end=" ")
print("World")  # Hello World
```

### input输入

```python
# 接收用户输入，返回字符串类型
name = input("请输入你的名字: ")
print("你好,", name)

# input返回的是字符串
age_str = input("请输入年龄: ")
age = int(age_str)  # 需要转换为整数
print("明年你", age + 1, "岁")
```

## 流程控制

### 条件判断

| 语法         | 说明                       |
| ---------- | ------------------------ |
| `if 条件:`   | 条件为True时执行               |
| `elif 条件:` | 前一个条件为False且当前条件为True时执行 |
| `else:`    | 前面所有条件都为False时执行         |

```python
# 基本if-else
age = 18
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print(f"成绩等级: {grade}")

# 单行if-else（三元表达式）
result = "通过" if score >= 60 else "不及格"
```

**注意：** Python使用缩进（通常为4个空格）表示代码块，不使用花括号。

### pass占位符

`pass`是Python中的占位符语句，不执行任何操作，用于语法上需要语句但逻辑上暂时不需要的情况。

```python
# 空循环体
i = 0
while i < 5:
    pass  # 暂时不执行任何操作
    i += 1

# 空代码块（占位）
if True:
    pass  # 待实现
```

### 循环

#### while循环

```python
# 基本while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 带条件的while循环
user_input = ""
while user_input != "quit":
    user_input = input("输入'quit'退出: ")
    print(f"你输入了: {user_input}")
```

#### 循环控制语句

| 语句         | 作用             |
| ---------- | -------------- |
| `break`    | 立即终止整个循环       |
| `continue` | 跳过当前迭代，进入下一次循环 |

```python
# break - 找到第一个大于5的数就停止
num = 1
while num <= 10:
    if num > 5:
        print(f"找到大于5的数: {num}")
        break
    num += 1

# continue - 跳过奇数，只打印偶数
num = 0
while num < 10:
    if num % 2 != 0:
        num += 1
        continue
    print(num)  # 0, 2, 4, 6, 8
    num += 1
```

#### 循环else子句

循环可以带有一个`else`子句，当循环**正常结束**（没有被break中断）时执行。

```python
# while循环的else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("while循环正常完成")

# 典型用法：查找元素
num = 1
while num <= 9:
    if num == 4:
        print("找到: 4")
        break
    num += 2  # 模拟遍历奇数1, 3, 5, 7, 9
else:
    print("未找到: 4")  # 会执行，因为4不在奇数序列中
```



**重要区别：**

* 循环被`break`中断 → **不执行**else
* 循环正常结束（包括`continue`）→ **执行**else

## 作业(已完成)

### 作业一：代码输出结果预测

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
# 变量定义
a = 10
b = 3.5
c = "Python"
d = True
e = None

# 1. 数据类型与 type 函数
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(a) == int)

# 2. 变量类型转换
print(int(b))
print(float(a))
print(str(a) + c)
print(bool(0))
print(bool(""))
print(bool("hello"))

# 3. 算术运算符
print(a + 5)
print(a / 4)
print(a // 4)
print(a % 4)
print(a ** 2)
print(c * 2)

# 4. 字符串格式化（f-string）
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")
print(f"明年{age + 1}岁")
print(f"{a} + {5} = {a + 5}")

# 5. 比较运算符与链式比较
print(a > 5)
print(a == 10)
print(5 < a < 20)
print(c == "python")
print("A" < "a")

# 6. 逻辑运算符
print(True and False)
print(True or False)
print(not d)
print(0 and 5)
print(3 or 5)
print("" and "hello")
print("hi" or "hello")
print(not None)

# 7. 三元运算符
score = 85
result = "及格" if score >= 60 else "不及格"
print(result)
level = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(level)

# 8. 赋值运算符
x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 4
print(x)

s = "Hi"
s += " Python"
print(s)
s *= 2
print(s)
```

### 作业二：循环与判断代码输出预测

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
# 1. while 循环 + if-else
n = 1
result = 0
while n <= 5:
    if n % 2 == 0:
        result += n
    else:
        result -= n
    n += 1
print(result)

# 2. continue 和 break
num = 1
while num <= 10:
    if num == 3:
        num += 1
        continue
    if num == 7:
        break
    print(num)
    num += 1

# 3. 循环 else 子句
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("end")

# 4. 嵌套条件
x = 15
if x < 10:
    print("A")
elif x < 20:
    if x % 2 == 0:
        print("B")
    else:
        print("C")
else:
    print("D")

# 5. 综合练习
a = 1
b = 0
while a <= 5:
    if a == 3:
        b += 10
    elif a % 2 == 0:
        b += a * 2
    else:
        b += a
    a += 1
print(b)
```

### 作业三：BMI 计算器

编写一个 BMI 计算器程序，要求如下：

1. **用户输入**：通过 `input()` 函数获取用户的身高（单位：米）和体重（单位：千克）。

2. **计算 BMI**：使用公式 `BMI = 体重(kg) / 身高(m)²` 计算 BMI 值。

3. **判断分类**：根据 BMI 值判断身体状况（参考中国成人标准）：
   
   * BMI < 18.5：偏瘦
   * 18.5 ≤ BMI < 24：正常
   * 24 ≤ BMI < 28：超重
   * BMI ≥ 28：肥胖

4. **输出结果**：使用 f-string 格式化输出用户的 BMI 值和分类结果。

5. **健康建议**：根据分类结果给出相应的健康建议，例如：
   
   * 偏瘦：建议适当增加营养摄入，进行适量运动
   * 正常：保持良好的生活习惯
   * 超重/肥胖：建议控制饮食，增加运动量

**示例输出**：

```python
请输入您的身高（米）：1.75
请输入您的体重（千克）：70
您的 BMI 值为：22.86
身体状况：正常
建议：保持良好的生活习惯，继续保持！
```

### 作业四：素数筛选器

**素数（质数）** 是指在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数的数。例如：2、3、5、7、11 都是素数，而 4、6、8、9 则不是。

编写一个程序，要求如下：

1. **用户输入**：通过 `input()` 函数获取起始数字和结束数字。

2. **输入合法性检查**：
   
   * 输入必须是正整数（大于 0 的整数）
   * 结束数字必须大于起始数字
   * 如果输入不合法，给出相应提示并要求重新输入

3. **素数判断**：使用循环判断该范围内每个数字是否为素数。

4. **输出结果**：打印该范围内的所有素数，并统计素数的个数。

**示例输出**：

```python
请输入起始数字：10
请输入结束数字：50
10 到 50 之间的素数有：
11 13 17 19 23 29 31 37 41 43 47
共计 11 个素数
```

# Python容器类型

## 什么是容器类型

容器类型用于**存储多个数据**。Python中内置的容器类型包括：

| 类型      | 名称  | 是否可变 | 是否有序            | 元素是否可重复 | 示例                 | 备注                |
| ------- | --- | ---- | --------------- | ------- | ------------------ | ----------------- |
| `list`  | 列表  | 可变   | 有序              | 可重复     | `[1, 2, 2, 3]`     | 内部采用动态数组实现        |
| `tuple` | 元组  | 不可变  | 有序              | 可重复     | `(1, 2, 3)`        | 内部采用静态数组实现        |
| `dict`  | 字典  | 可变   | 有序（Python 3.7+） | 键不可重复   | `{"a": 1, "b": 2}` | 键值对，内部使用hashmap实现 |
| `set`   | 集合  | 可变   | 无序              | 不可重复    | `{1, 2, 3}`        | 内部使用hashset实现     |
| `str`   | 字符串 | 不可变  | 有序              | 可重复     | `"hello"`          |                   |

> **注意：** `str` 也可以视为一种不可变的有序字符序列，本节会穿插涉及。

## 列表（list）

列表是Python中最常用的**可变、有序**容器，可以存储任意类型的元素。

### 创建列表

```python
# 字面量创建
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []  # 空列表

# 通过list()函数创建
chars = list("abc")      # ['a', 'b', 'c']
nums2 = list((1, 2, 3))  # [1, 2, 3]
```

### 索引与切片

```python
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 索引访问（从0开始）
print(fruits[0])   # 苹果
print(fruits[-1])  # 西瓜（负数从末尾开始）

# 切片 [start:end:step] 注意：切片会产生新的列表
print(fruits[1:4])     # ['香蕉', '橙子', '葡萄'] —— 范围[1,4)
print(fruits[:3])      # ['苹果', '香蕉', '橙子'] —— 返回[0,3)
print(fruits[2:])      # ['橙子', '葡萄', '西瓜'] —— 从索引2到末尾
print(fruits[::2])     # ['苹果', '橙子', '西瓜'] —— 从头到尾，每隔一个取一个,步长为2
print(fruits[1:4:2])     # ['香蕉', '葡萄'] -- 范围[1,4)，步长为2
print(fruits[::-1])    # ['西瓜', '葡萄', '橙子', '香蕉', '苹果'] —— 从头到尾，步长为-1（倒序，即反转列表）
```

### 列表操作

```python
nums = [1, 2, 3]

# 添加元素
nums.append(4)        # [1, 2, 3, 4]      末尾添加
nums.insert(0, 0)     # [0, 1, 2, 3, 4]   指定位置插入
nums.extend([5, 6])   # [0, 1, 2, 3, 4, 5, 6]  批量添加

# 删除元素
nums.remove(0)        # [1, 2, 3, 4, 5, 6] 删除第一个匹配值
popped = nums.pop()   # 6, nums变为[1, 2, 3, 4, 5]  删除并返回末尾
popped = nums.pop(0)  # 1, nums变为[2, 3, 4, 5]    删除并返回指定位置
del nums[0]           # [3, 4, 5]  删除指定位置
nums.clear()          # []  清空列表

# 查找与统计
nums = [1, 2, 3, 2, 4]
print(nums.index(2))     # 1  第一个匹配的位置
print(nums.count(2))     # 2  出现次数

# 排序与反转
nums = [3, 1, 4, 1, 5]
nums.sort()              # [1, 1, 3, 4, 5]  原地排序
nums.sort(reverse=True)  # [5, 4, 3, 1, 1]  降序
nums.reverse()           # [1, 1, 3, 4, 5]  原地反转

# 排序但不修改原列表
nums = [3, 1, 4]
sorted_nums = sorted(nums)  # [1, 3, 4], nums不变

# 修改列表项
nums[0] = 10 # [10,3,4]
nums[4] = 10 # IndexError: list assignment index out of range
```

## 元组（tuple）

元组是**不可变**的有序序列，一旦创建就不能修改。

### 创建元组

```python
# 字面量创建（圆括号可省略）
point = (1, 2)
point = 1, 2       # 等价于 (1, 2)
single = (1,)      # 单元素必须加逗号！不是 (1)
empty = ()         # 空元组

# 通过tuple()函数创建
t = tuple([1, 2, 3])   # (1, 2, 3)
t = tuple("abc")       # ('a', 'b', 'c')
```

### 基本操作

```python
t = (1, 2, 3, 2, 4)

# 索引和切片（与list相同）
print(t[0])      # 1
print(t[-1])     # 4
print(t[1:4])    # (2, 3, 2)

# 查询（不能修改）
print(t.index(2))    # 1
print(t.count(2))    # 2
print(3 in t)        # True

# 不能修改！
# t[0] = 100       # TypeError: 'tuple' object does not support item assignment
# t.append(5)      # AttributeError
```

### 元组解包

```python
# 元组解包
coord = (3, 4)
x, y = coord
print(x, y)      # 3 4

# 扩展解包（Python 3+）
first, *rest = (1, 2, 3, 4)
print(first)     # 1
print(rest)      # [2, 3, 4]

*rest, last = (1, 2, 3, 4)
print(rest)      # [1, 2, 3]
print(last)      # 4

# 用于交换变量
a, b = 1, 2
a, b = b, a      # a=2, b=1
```

## 字典（dict）

字典是Python的**键值对**存储结构，通过键快速查找值。

### 创建字典

**注意：字段的键不可变，因此只要是不可变的数据结构，都可以作为键（例如：字符串，数字，元组）**

```python
# 字面量创建
person = {
    "name": "Alice",
    "age": 25,
    "city": "北京"
}
empty = {}      # 空字典

# 通过dict()函数创建
person = dict(name="Alice", age=25, city="北京")
person = dict([("name", "Alice"), ("age", 25)])

# 从键序列创建，值默认为None或指定
d = dict.fromkeys(["a", "b", "c"], 0)
# {'a': 0, 'b': 0, 'c': 0}
```

### 访问与修改

```python
person = {"name": "Alice", "age": 25}

# 访问
print(person["name"])       # Alice
# print(person["gender"])   # KeyError!

# 安全访问
print(person.get("gender"))         # None（不报错）
print(person.get("gender", "未知"))  # 未知（提供默认值）

# 添加/修改
person["gender"] = "女"      # 添加新键
person["age"] = 26           # 修改已有键

# 批量更新/合并
person.update({"phone": "123456", "age": 27})

# 删除
del person["phone"]          # 删除键值对
value = person.pop("age")    # 删除并返回值
last = person.popitem()      # 删除并返回最后插入的键值对（Python 3.7+）
person.clear()               # 清空
```

### 重要注意事项

```python
# 键必须是不可变类型（hashable）
valid = {
    "string": 1,      # str ✓
    42: 2,            # int ✓
    (1, 2): 3,        # tuple ✓
    # [1, 2]: 4,     # list ✗ 不可哈希！
}

# 字典的键是唯一的，重复赋值会覆盖
person = {"name": "Alice", "name": "Bob"}
print(person)  # {'name': 'Bob'}
```

## 集合（set）

集合是**无序、不重复**的元素集合，支持数学上的集合运算。

### 创建集合

```python
# 字面量创建
nums = {1, 2, 3, 3, 3}   # {1, 2, 3} —— 自动去重
empty = set()             # 空集合！不是 {}（那是空字典）

# 通过set()函数创建
nums = set([1, 2, 2, 3])  # {1, 2, 3}
chars = set("hello")      # {'h', 'e', 'l', 'o'}
```

### 集合操作

```python
s = {1, 2, 3}

# 添加/删除
s.add(4)          # {1, 2, 3, 4}
s.remove(2)       # {1, 3, 4} —— 不存在会报错
s.discard(10)     # 不报错，即使不存在
s.pop()           # 随机删除并返回一个元素
s.clear()         # set()

# 去重利器
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))   # [1, 2, 3]（顺序可能不同）
```

## 容器操作

### 通用操作函数

```python
# len() —— 获取元素个数
len([1, 2, 3])       # 3
len((1, 2, 3))       # 3
len({"a": 1, "b": 2}) # 2（键值对数量）
len("hello")         # 5

# max() / min() —— 最大/最小值
max([3, 1, 4, 1, 5])  # 5
min((3, 1, 4))        # 1
max("hello")          # 'o'（按字符编码）

# sum() —— 求和（元素必须是数字）
sum([1, 2, 3, 4])     # 10
sum((1, 2, 3))        # 6

# sorted() —— 排序，返回新列表
sorted([3, 1, 2])           # [1, 2, 3]
sorted((3, 1, 2))           # [1, 2, 3] —— 返回列表
sorted("cba")               # ['a', 'b', 'c']
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]

# reversed() —— 反转，返回迭代器
list(reversed([1, 2, 3]))   # [3, 2, 1]
list(reversed("abc"))       # ['c', 'b', 'a']
```

### 常用运算符

#### 成员运算符：`in` / `not in`

判断元素是否存在于容器中：

```python
# 列表
3 in [1, 2, 3]        # True
5 not in [1, 2, 3]    # True

# 元组
2 in (1, 2, 3)        # True

# 字符串
"he" in "hello"       # True —— 检查子串
"x" not in "hello"    # True

# 字典 —— 检查的是键，不是值
"name" in {"name": "Alice", "age": 25}   # True
"Alice" in {"name": "Alice", "age": 25}  # False

# 集合
2 in {1, 2, 3}        # True
```



#### 连接与重复运算符

```python
# + 连接（仅有序容器）
[1, 2] + [3, 4]       # [1, 2, 3, 4]
(1, 2) + (3, 4)       # (1, 2, 3, 4)
"hello " + "world"    # "hello world"
# {1, 2} + {3, 4}    # TypeError! 集合不支持

# * 重复（仅有序容器）
[1, 2] * 3            # [1, 2, 1, 2, 1, 2]
"-" * 10              # "----------"
```

#### 相等运算符：`==` / `!=`

`==` 比较的是两个容器的内容是否**相等**，而非它们是否是同一个对象。

**比较逻辑：**

1. **类型必须相同**：不同类型的容器即使内容看起来一样，也视为不相等。`[1, 2] == (1, 2)` 结果为 `False`。

2. **长度必须相同**：长度不同的容器一定不相等。

3. **逐元素比较**：从第一个元素开始，依次比较对应位置的元素。对于嵌套容器，会**递归**地进行逐元素比较。

4. **元素使用自身的 `==`**：容器本身不定义元素如何相等，而是调用元素自身的 `__eq__` 方法。因此 `[1, 2] == [1.0, 2.0]` 为 `True`。
   
   ```python
   # 基本比较
   [1, 2, 3] == [1, 2, 3]        # True，内容相同
   [1, 2, 3] == [1, 3, 2]        # False，顺序不同
   
   # 类型不同
   [1, 2] == (1, 2)              # False
   
   # 嵌套容器递归比较
   [[1, 2], [3, 4]] == [[1, 2], [3, 4]]  # True
   
   # 字典比较（键值对）
   {"a": 1, "b": 2} == {"b": 2, "a": 1}  # True，字典无序，键值对相同即可
   ```

> **注意**：`==` 比较的是**值相等**，不是**身份相同**（是否为内存中的同一个对象）。要判断身份，使用 `is`。

#### 身份运算符：`is` / `is not`

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b        # True，b 和 a 指向同一个列表对象
a is c        # False，c 是新创建的另一个对象，尽管内容相同
a == c        # True，内容相等

a is not c    # True
```

**常见使用场景：**

```python
# 判断是否为 None（Python 推荐写法）
value = None
if value is None:
    print("值为空")

# 判断单例对象
x = True
x is True     # True

# 小整数缓存（Python 优化）
a = 100
b = 100
a is b        # True（-5 到 256 的整数会被缓存复用）

x = 1000
y = 1000
x is y        # False（通常，取决于解释器实现）
```



> **重要区别**：
> 
> * `==` 问的是"你们长得一样吗？"（值相等）
> * `is` 问的是"你们就是同一个人吗？"（身份相同）
> * 比较 `None` 时，**永远使用 `is`**，而不是 `==`

#### 位运算符：`&`、`|`、`^`、`~`

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# & 交集（两个集合都有的元素）
s1 & s2       # {2, 3}

# | 并集（两个集合所有的元素，去重）
s1 | s2       # {1, 2, 3, 4}

# - 差集（在 s1 中但不在 s2 中的元素）
s1 - s2       # {1}
s2 - s1       # {4}

# ^ 对称差集（只在其中一个集合中的元素）
s1 ^ s2       # {1, 4}

# ~ 不适用于集合，用于整数的按位取反
```

> **注意**：位运算符只能用于**集合（set）**，不能用于 `list`、`tuple`、`dict` 等其他容器类型。

### 遍历容器

#### 基本 for 循环

```python
# 遍历列表
for item in [1, 2, 3]:
    print(item)

# 遍历元组
for char in ("a", "b", "c"):
    print(char)

# 遍历字符串
for ch in "hello":
    print(ch)  # h, e, l, l, o
```

#### 遍历字典

```python
person = {"name": "Alice", "age": 25, "city": "北京"}

# 遍历键（默认）
for key in person:
    print(key)

# 遍历键值对
for key, value in person.items():
    print(key, value)

# 仅遍历值
for value in person.values():
    print(value)

# 仅遍历键（显式）
for key in person.keys():
    print(key)
```

#### 遍历集合

```python
s = {1, 2, 3}
for item in s:
    print(item)
# 注意：集合是无序的，遍历顺序不固定
```

#### `enumerate()` 函数

遍历容器时，如果需要同时获取索引和值，使用 `enumerate()`：

```python
# 基本用法
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: 苹果
# 1: 香蕉
# 2: 橙子

# 指定起始索引
for i, v in enumerate(fruits, start=1):
    print(f"{i}. {v}")
# 1. 苹果
# 2. 香蕉
# 3. 橙子
```

#### `zip()` 函数

并行遍历多个容器，元素按位置一一配对：

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} 今年 {age} 岁，住在 {city}")

# zip 以最短容器为准
short = [1, 2]
long = ["a", "b", "c"]
for x, y in zip(short, long):
    print(x, y)
# 只输出两组：1 a 和 2 b
```

## 作业(已完成)

### 作业一：列表与身份运算符综合

```python
nums = [3, 1, 4, 1, 5]
copy = nums[:]
print(nums == copy, nums is copy)
nums[0] = 10

print(nums[0], copy[0])
print(nums == copy, nums is copy)
print(len(nums))

i = 0
count = 0
while i < len(nums):
    if nums[i] > 3:
        count += 1
    i += 1
print(count)
```

### 作业二：元组、集合与成员运算符综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
t = (5, 2, 8, 2)
first, *rest = t
print(first, rest)
print(sorted(t))
print(2 in t, 9 not in t)

s = set(t)
print(len(s))
s2 = {2, 8, 10}
print(s & s2, s | s2)
```

### 作业三：字典与遍历综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
d = {"x": 10, "y": 20}
d["z"] = 30
d.update({"x": 15})
print(len(d))
print("x" in d, 20 in d)
print(d.get("w", 0))

keys = []
for k in d:
    keys.append(k)
print(keys)

i = 0
while i < len(keys):
    k = keys[i]
    if d[k] > 15:
        print(k)
    i += 1
```



### 作业四：字符串操作与循环综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
s = "hello"
print(s[1:4])
print("el" in s, "x" not in s)
print(s + " world", s * 2)

i = 0
vowels = "aeiou"
count = 0
while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1
print(count)
print(f"length: {len(s)}")
```

### 作业五：enumerate、zip与多容器综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
names = ["Alice", "Bob"]
ages = (25, 30)

pairs = []
for name, age in zip(names, ages):
    pairs.append(f"{name}-{age}")
print(pairs)

for i, name in enumerate(names, 1):
    print(i, name)

d = {}
i = 0
while i < len(names):
    if ages[i] > 20:
        d[names[i]] = ages[i]
    i += 1
print(len(d))
print(d.get("Alice"))
print(d.get("Charlie", "not found"))
```

### 作业六：学生信息处理综合练习

以下是一个包含学生信息的列表，请根据要求编写代码完成各项任务。

**提示：** 以下所有任务请使用循环和条件判断完成，不要使用列表推导式。

```python
students = [
    {"id": 988985, "name": "梁平", "sex": "女", "age": 15, "address": "安徽省 淮南市", "tel": "12957961008"},
    {"id": 299422, "name": "邱杰", "sex": "男", "age": 25, "address": "辽宁省 本溪市", "tel": "12685726676"},
    {"id": 723972, "name": "王超", "sex": "女", "age": 14, "address": "新疆维吾尔自治区 阿克苏地区", "tel": "15277794541"},
    {"id": 723768, "name": "冯秀兰", "sex": "女", "age": 29, "address": "辽宁省 丹东市", "tel": "13014888148"},
    {"id": 536273, "name": "赖军", "sex": "男", "age": 19, "address": "重庆 重庆市", "tel": "15152658611"},
    {"id": 940136, "name": "顾强", "sex": "男", "age": 20, "address": "吉林省 松原市", "tel": "18562759588"},
    {"id": 489462, "name": "戴敏", "sex": "男", "age": 25, "address": "湖南省 长沙市", "tel": "11513562318"},
    {"id": 863594, "name": "吕涛", "sex": "女", "age": 16, "address": "湖北省 襄阳市", "tel": "16246419558"},
    {"id": 718313, "name": "冯静", "sex": "女", "age": 28, "address": "黑龙江省 牡丹江市", "tel": "18243767800"},
    {"id": 262068, "name": "蔡明", "sex": "男", "age": 20, "address": "黑龙江省 七台河市", "tel": "14185862227"},
    {"id": 900366, "name": "廖磊", "sex": "女", "age": 23, "address": "青海省 海南藏族自治州", "tel": "19469661693"},
    {"id": 316019, "name": "冯洋", "sex": "男", "age": 16, "address": "江西省 新余市", "tel": "18842832768"},
    {"id": 773536, "name": "韩杰", "sex": "男", "age": 23, "address": "云南省 丽江市", "tel": "18560747335"},
    {"id": 494398, "name": "江涛", "sex": "男", "age": 24, "address": "山西省 大同市", "tel": "12774658592"},
    {"id": 177459, "name": "文艳", "sex": "男", "age": 27, "address": "山东省 青岛市", "tel": "16233511417"},
    {"id": 979439, "name": "杜秀英", "sex": "男", "age": 22, "address": "甘肃省 张掖市", "tel": "14723781356"},
    {"id": 142762, "name": "丁艳", "sex": "男", "age": 28, "address": "澳门特别行政区 澳门半岛", "tel": "13157638539"},
    {"id": 157141, "name": "邓静", "sex": "女", "age": 19, "address": "海南省 三亚市", "tel": "17658672240"},
    {"id": 243063, "name": "江刚", "sex": "女", "age": 15, "address": "安徽省 六安市", "tel": "18205383748"},
    {"id": 351709, "name": "乔刚", "sex": "女", "age": 12, "address": "安徽省 蚌埠市", "tel": "14143838021"},
    {"id": 236140, "name": "史平", "sex": "男", "age": 24, "address": "广西壮族自治区 百色市", "tel": "11895866733"},
    {"id": 254260, "name": "康娜", "sex": "男", "age": 29, "address": "辽宁省 铁岭市", "tel": "18783219853"},
    {"id": 387769, "name": "袁磊", "sex": "男", "age": 28, "address": "重庆 重庆市", "tel": "15243676922"},
    {"id": 692436, "name": "龙秀英", "sex": "男", "age": 18, "address": "吉林省 延边朝鲜族自治州", "tel": "18667285569"},
    {"id": 304202, "name": "姚静", "sex": "男", "age": 21, "address": "吉林省 松原市", "tel": "17962179634"},
    {"id": 533032, "name": "潘娜", "sex": "男", "age": 13, "address": "湖北省 孝感市", "tel": "14132684173"},
    {"id": 773792, "name": "萧磊", "sex": "男", "age": 29, "address": "河南省 焦作市", "tel": "13865617456"},
    {"id": 171440, "name": "邵勇", "sex": "男", "age": 16, "address": "宁夏回族自治区 固原市", "tel": "19454444332"},
    {"id": 428587, "name": "李芳", "sex": "男", "age": 29, "address": "四川省 宜宾市", "tel": "14751601674"},
    {"id": 926156, "name": "谭芳", "sex": "女", "age": 27, "address": "湖南省 长沙市", "tel": "18683429563"},
    {"id": 171494, "name": "夏秀英", "sex": "男", "age": 14, "address": "陕西省 安康市", "tel": "17732967642"},
    {"id": 549517, "name": "程娜", "sex": "女", "age": 24, "address": "内蒙古自治区 锡林郭勒盟", "tel": "18927839708"},
    {"id": 999121, "name": "武杰", "sex": "女", "age": 21, "address": "新疆维吾尔自治区 博尔塔拉蒙古自治州", "tel": "15349698338"},
    {"id": 440785, "name": "崔军", "sex": "男", "age": 26, "address": "山西省 临汾市", "tel": "14863312346"},
    {"id": 113636, "name": "廖勇", "sex": "女", "age": 19, "address": "重庆 重庆市", "tel": "18152536541"},
    {"id": 109280, "name": "崔强", "sex": "女", "age": 25, "address": "河南省 安阳市", "tel": "12838860122"},
    {"id": 988885, "name": "康秀英", "sex": "女", "age": 29, "address": "广东省 佛山市", "tel": "12637161150"},
    {"id": 751542, "name": "余磊", "sex": "女", "age": 15, "address": "香港特别行政区 九龙", "tel": "16716667565"},
    {"id": 821693, "name": "邵勇", "sex": "女", "age": 27, "address": "内蒙古自治区 鄂尔多斯市", "tel": "11869733772"},
    {"id": 595152, "name": "贺涛", "sex": "女", "age": 12, "address": "吉林省 通化市", "tel": "18172684836"},
    {"id": 209059, "name": "万勇", "sex": "男", "age": 27, "address": "江苏省 淮安市", "tel": "13523350881"},
    {"id": 331199, "name": "江艳", "sex": "男", "age": 29, "address": "内蒙古自治区 包头市", "tel": "14357786637"},
    {"id": 597029, "name": "廖磊", "sex": "女", "age": 22, "address": "新疆维吾尔自治区 伊犁哈萨克自治州", "tel": "14343812715"},
    {"id": 243965, "name": "马芳", "sex": "女", "age": 29, "address": "湖南省 长沙市", "tel": "12226278003"},
    {"id": 796997, "name": "郝霞", "sex": "女", "age": 29, "address": "辽宁省 锦州市", "tel": "15734778439"},
    {"id": 735045, "name": "吴娜", "sex": "男", "age": 18, "address": "江西省 鹰潭市", "tel": "12550200851"},
    {"id": 858934, "name": "石秀英", "sex": "男", "age": 21, "address": "福建省 南平市", "tel": "14296454005"},
    {"id": 646003, "name": "苏静", "sex": "女", "age": 17, "address": "澳门特别行政区 澳门半岛", "tel": "11456865751"},
    {"id": 607537, "name": "于磊", "sex": "女", "age": 25, "address": "海南省 海口市", "tel": "14742847575"},
    {"id": 817410, "name": "胡超", "sex": "女", "age": 19, "address": "海外 海外", "tel": "16875962137"},
    {"id": 985064, "name": "任杰", "sex": "男", "age": 17, "address": "云南省 迪庆藏族自治州", "tel": "17548787335"},
    {"id": 644060, "name": "汪秀英", "sex": "男", "age": 19, "address": "香港特别行政区 九龙", "tel": "10278533538"},
    {"id": 755803, "name": "徐磊", "sex": "女", "age": 26, "address": "江苏省 徐州市", "tel": "18721465794"},
    {"id": 538130, "name": "熊洋", "sex": "男", "age": 13, "address": "吉林省 白城市", "tel": "13491345641"},
    {"id": 977696, "name": "孟磊", "sex": "男", "age": 24, "address": "香港特别行政区 香港岛", "tel": "10541964547"},
    {"id": 683438, "name": "赵霞", "sex": "男", "age": 28, "address": "重庆 重庆市", "tel": "13085741830"},
    {"id": 342123, "name": "曾芳", "sex": "女", "age": 15, "address": "湖南省 邵阳市", "tel": "11645124878"},
    {"id": 261733, "name": "马芳", "sex": "女", "age": 22, "address": "台湾 新北市", "tel": "10255722846"},
    {"id": 303578, "name": "姜杰", "sex": "女", "age": 17, "address": "黑龙江省 齐齐哈尔市", "tel": "12581543256"},
    {"id": 907392, "name": "熊杰", "sex": "男", "age": 16, "address": "广西壮族自治区 北海市", "tel": "18941398494"}
]
```



**任务列表：**

1. 遍历 `students` 列表，使用 f-string 格式化输出每个学生的姓名和年龄，格式为 `姓名: xxx, 年龄: xx`

2. 创建一个新列表 `female_students`，包含所有性别为"女"的学生（即 `sex` 键的值为 `"女"`）

3. 创建一个新列表 `young_females`，包含所有年龄小于 25 岁的女生

4. 创建一个新列表 `chen_students`，包含所有姓"陈"的学生（提示：`name[0]` 可以获取姓名的第一个字）

5. 创建一个新列表 `tel_end_with_1`，包含所有电话号码最后一位是 "1" 的学生（提示：字符串可以用索引访问最后一个字符，如 `tel[-1]`）

6. 创建一个新列表 `all_names`，包含所有学生的姓名

7. 创建一个新列表 `female_names`，包含所有女生的姓名

8. 创建一个新列表 `female_contacts`，其中每个元素是一个字典，只包含 `name` 和 `tel` 两个键，仅包含女生的信息

9. 计算并打印所有学生的年龄总和

10. 计算并打印所有学生的平均年龄（保留两位小数，使用 f-string 格式化）

11. 创建一个字典 `result`，包含两个键：`"names"` 对应的值是所有学生姓名的列表，`"ages"` 对应的值是所有学生年龄的列表

12. 找到 `id` 为 `796997` 的学生，打印其姓名和电话号码。如果找不到，打印 `"未找到"`

13. 判断是否包含年龄大于 28 岁的男生。如果存在，打印 `True` 并打印该学生的姓名；否则打印 `False`

14. 判断是否所有女生的年龄都在 28 岁以内（即没有超过 28 岁的女生）。如果是，打印 `True`；否则打印 `False`

# Python函数

函数是**可复用**的代码块，用于封装特定功能。通过定义函数，可以避免重复代码，提高程序的可读性和可维护性。

* * *

## 定义函数

使用 `def` 关键字定义函数：

```python
# 定义一个简单函数
def greet():
    print("Hello, World!")

# 调用函数
greet()  # Hello, World!
```



* * *

## 参数

### 位置参数

按照定义时的**顺序**传递参数：



```python
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 8
```

### 默认参数

为参数指定**默认值**，调用时可省略：

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
```

**注意：** 默认参数必须放在非默认参数后面。

```python
# 错误示例
# def greet(greeting="Hello", name):  # SyntaxError!
#     pass
```

### 关键字参数

通过**参数名**传递，顺序可以任意：

```python
def person_info(name, age, city):
    print(f"{name}, {age}岁, 来自{city}")

# 关键字参数，顺序无关
person_info(age=25, city="北京", name="Alice")
# Alice, 25岁, 来自北京
```

**混合使用：** 位置参数在前，关键字参数在后。

```python
person_info("Alice", age=25, city="北京")  # 正确
# person_info(name="Alice", 25, "北京")   # 错误！位置参数不能在关键字参数后
```

### 可变参数

#### `*args` —— 接收任意数量的位置参数

```python
\def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# 调用
print(sum_all(1, 2, 3))     # 6
print(sum_all(1, 2, 3, 4))  # 10
print(sum_all())            # 0
```

**`args` 的本质：** 函数内部是一个**元组**。

```python
def show_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)        # (1, 2, 3)

show_args(1, 2, 3)
```

#### `**kwargs` —— 接收任意数量的关键字参数

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用
print_info(name="Alice", age=25, city="北京")
# name: Alice
# age: 25
# city: 北京
```

**`kwargs` 的本质：** 函数内部是一个**字典**。

```python
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'name': 'Alice', 'age': 25}

show_kwargs(name="Alice", age=25)
```

### 参数顺序规则

定义函数时，参数必须按以下顺序：

```python
def func(位置参数, 默认参数, *args, **kwargs):
    pass

# 示例
def demo(a, b=2, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

demo(1, 3, 4, 5, x=10, y=20)
# a=1, b=3
# args=(4, 5)
# kwargs={'x': 10, 'y': 20}
```



* * *

## 返回值

### 使用 return

函数通过 `return` 返回结果：

```python
def square(x):
    return x ** 2
result = square(4) \
print(result) # 16
```

### 多返回值

Python 函数可以**同时返回多个值**（实际是返回元组）：

```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 1, 4, 1, 5])
print(minimum)  # 1
print(maximum)  # 5

# 本质上返回的是元组
result = min_max([3, 1, 4])
print(result)       # (1, 4)
print(type(result)) # <class 'tuple'>
```

### 没有 return

如果函数没有 `return`，默认返回 `None`：

```python
def say_hello():
    print("Hello")

result = say_hello()  # Hello
print(result)         # None
```

## 文档字符串（Docstring）

用三引号编写函数的说明文档：

```python
def calculate_bmi(weight, height):
    """
    计算 BMI 指数。

    参数:
        weight: 体重，单位千克
        height: 身高，单位米

    返回:
        BMI 值
    """
    return weight / (height ** 2)

# 查看文档
print(calculate_bmi.__doc__)
```

## 作业

### 作业一：函数参数与列表操作综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
def add_items(base, items=None, *tags):
    if items is None:
        items = []
   items.append(base)
    for tag in tags:
        items.append(tag)
    return items

result1 = add_items(10)
print(result1)

result2 = add_items(20, [1, 2], 30, 40)
print(result2)
```



### 作业二：关键字参数与字典操作综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
def merge_data(base, **extra):
    result = base.copy() # 浅拷贝
    for key, value in extra.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
data = {"a": 10, "b": [1, 2]}
merged = merge_data(data, a=5, b=[3], c="hello")
print(merged)
print(len(merged)) 
print(merged.get("d", "not found"))
```

### 作业三：多返回值与容器遍历综合

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
def split_data(data):
    mid = len(data) // 2
    return data[:mid], data[mid:]

nums = [1, 2, 3, 4, 5, 6]
first, second = split_data(nums)
print(first, second)

def find_indices(items, target):
    indices = []
    for i, item in enumerate(items):
        if item == target:
            indices.append(i)
    return indices

scores = [85, 92, 85, 78, 85]
positions = find_indices(scores, 85)
print(positions)

result = second + [len(positions)]
print(result)
```

### 作业四：函数综合编程

请按照要求实现以下三个函数，并编写测试代码手动调用每个函数，验证功能是否正确。

**任务 1：列表扁平化**

实现函数 `flatten`，接收一个可能包含嵌套列表的列表（如 `[1, [2, 3], [[4], 5]]`），返回一个将所有元素展开后的一维列表（如 `[1, 2, 3, 4, 5]`）。

```python
nested1 = [1, [2, 3], [[4], 5]]
print(flatten(nested1))  # [1, 2, 3, 4, 5]

nested2 = [[[1]], 2, [3, [4, [5]]]]
print(flatten(nested2))  # [1, 2, 3, 4, 5]

print(flatten([]))       # []
print(flatten([1, 2, 3]))  # [1, 2, 3]
```



**任务 2：列表/元组转链表**

实现函数 `to_linked_list`，接收一个列表或元组，将其转换为一个链表结构并返回。

```python
linked1 = to_linked_list((1, 2, 3))
print(linked1)
# {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

linked2 = to_linked_list([10, 20])
print(linked2)
# {'value': 10, 'next': {'value': 20, 'next': None}}

print(to_linked_list([]))  # None
```

**任务 3：字典合并**

实现函数 `merge_dicts`，接收不定数量的字典参数，将它们合并为一个大字典。

合并规则：求并集，如果有相同的键，后传入的字典中的值覆盖先传入的字典中的值（浅合并即可）

```python
d1 = {"a": 1, "b": [1, 2]}
d2 = {"b": [3], "c": "hello"}
d3 = {"a": 10, "d": True}

merged = merge_dicts(d1, d2, d3)
print(merged)
# {'a': 10, 'b': [3], 'c': 'hello', 'd': True}

print(merge_dicts(d1))
# {'a': 1, 'b': [1, 2]}

print(merge_dicts())




