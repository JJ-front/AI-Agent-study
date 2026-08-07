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
| 数字类型           | ==complex==      | 1+2j, 3-4j       | j表示$\sqrt{-1}$            |
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
```

# Python作用域

作用域（Scope）决定了程序中变量和名字的**可见范围**。理解作用域能帮助你预测代码的执行结果，避免变量名冲突。

---

## LEGB 规则

Python 查找变量时遵循 **LEGB** 规则，按以下优先级顺序搜索：

| 优先级 | 层级 | 说明 |
|--------|------|------|
| 1 | **L**ocal | 函数内部（局部作用域） |
| 2 | **E**nclosing | 嵌套函数的外层函数（闭包） |
| 3 | **G**lobal | 模块级别（全局作用域） |
| 4 | **B**uilt-in | Python 内置（如 `len`、`print`） |

```python
x = "global"          # G：全局作用域

def outer():
    x = "enclosing"   # E：外层函数作用域
    
    def inner():
        x = "local"   # L：局部作用域
        print(x)      # 按 L → E → G → B 查找
    
    inner()

outer()  # local
```

---

## 局部作用域（Local）

函数内部定义的变量，只在函数内部可见：

```python
def demo():
    local_var = 100   # 局部变量
    print(local_var)

demo()        # 100
# print(local_var)  # NameError！函数外部访问不到
```

**函数参数也是局部变量：**

```python
def greet(name):      # name 是局部变量
    message = f"Hello, {name}"  # message 也是局部变量
    print(message)

greet("Alice")
# print(name)     # NameError！
```

---

## 全局作用域（Global）

模块级别（文件最外层）定义的变量：

```python
count = 0             # 全局变量

def increment():
    print(count)      # 读取全局变量，OK

increment()  # 0
```

### 在函数内修改全局变量

直接赋值会创建局部变量，而非修改全局变量：

```python
count = 0

def wrong_increment():
    count += 1        # UnboundLocalError！

# wrong_increment()
```

使用 `global` 关键字声明：

```python
count = 0

def increment():
    global count      # 声明使用全局变量
    count += 1
    print(count)

increment()  # 1
increment()  # 2
print(count) # 2
```

---

## 闭包作用域（Enclosing）

嵌套函数中，内层函数可以访问外层函数的变量：

```python
def outer():
    x = "outer"       # 外层函数的局部变量
    
    def inner():
        print(x)      # 访问外层变量
    
    inner()

outer()  # outer
```

### 修改外层变量

内层函数不能直接修改外层变量：

```python
def counter():
    count = 0
    
    def increment():
        count += 1    # UnboundLocalError！
    
    increment()

# counter()
```

使用 `nonlocal` 关键字：

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count   # 声明使用外层变量
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

**`nonlocal` vs `global`：**

| 关键字 | 作用 |
|--------|------|
| `global` | 声明变量来自**全局**作用域 |
| `nonlocal` | 声明变量来自**外层函数**作用域 |

---

## 常见错误

### 错误 1：在函数内同时读写全局变量

```python
x = 10

def demo():
    print(x)      # 先读
    x = 20        # 再写 → 编译期就判定 x 是局部变量！

# demo()  # UnboundLocalError
```

**原因：** Python 在编译函数时就确定了变量作用域，一旦函数内有赋值语句，该变量就被视为局部变量。

**修正：**

```python
x = 10

def demo():
    global x
    print(x)
    x = 20

demo()  # 10
print(x)  # 20
```

### 错误 2：默认参数的陷阱

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] —— 意外！列表被共享了
```

默认参数在函数定义时求值，只创建一次。

**修正：**

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 作用域速查

```python
# 1. 简单函数
name = "global"

def func():
    name = "local"    # 局部变量，不影响全局
    print(name)       # local

func()
print(name)           # global

# 2. 嵌套函数

def outer():
    name = "outer"
    
    def inner():
        name = "inner"   # 自己的局部变量
        print(name)      # inner
    
    inner()
    print(name)          # outer

outer()

# 3. 使用 nonlocal
def outer():
    name = "outer"
    
    def inner():
        nonlocal name
        name = "modified"  # 修改外层变量
    
    inner()
    print(name)            # modified

outer()
```

---

## 作业(已完成)

### 作业一：作用域判断

阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

```python
x = 1

def func_a():
    x = 2
    
    def func_b():
        print(x)      # ?
    
    func_b()
    print(x)          # ?

func_a()
print(x)              # ?
```

### 作业二：global 与 nonlocal

阅读以下代码，预测输出结果：

```python
count = 0

def outer():
    count = 10
    
    def inner():
        global count
        count += 1
        print(count)  # ?
    
    inner()
    print(count)      # ?

outer()
print(count)          # ?
```

### 作业三：修复代码

以下代码用于统计函数调用次数，先读取全局计数器打印日志，再递增计数。但实际运行会报错，请修改使其正确运行：

```python
call_count = 0

def process_data(data):
  	result = sum(data)
    # 处理完成后递增计数器
    call_count += 1 
    return result

print(process_data([1, 2, 3]))
print(process_data([4, 5, 6]))
print(f"总共调用了 {call_count} 次")
```

### 作业四：闭包计数器

实现一个函数 `make_multiplier(n)`，返回一个函数。返回的函数接收一个参数 `x`，返回 `n * x`。

要求使用闭包实现，不要使用 `global`。

```python
triple = make_multiplier(3)
print(triple(5))   # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))   # 14
```

### 作业五：综合练习

实现一个函数 `create_account(initial_balance)`，返回两个函数：
- `deposit(amount)`: 存款，返回新余额
- `withdraw(amount)`: 取款，余额不足返回 `"余额不足"`，否则返回新余额

要求使用闭包保存余额状态，不要暴露余额变量。

```python
deposit, withdraw = create_account(100)
print(deposit(50))    # 150
print(withdraw(30))   # 120
print(withdraw(200))  # 余额不足
```
# Lambda表达式

Lambda表达式用于创建**匿名函数**——即没有名称的临时函数。当你需要一个简单函数且只用一次时，lambda能让代码更简洁。

---

## 基本语法

```python
lambda 参数1, 参数2, ... : 表达式
```

```python
# 普通函数
def add(x, y):
    return x + y

# 等价的lambda
add_lambda = lambda x, y: x + y

print(add(2, 3))         # 5
print(add_lambda(2, 3))  # 5
```

**特点：**

- 只能包含**一个表达式**，不能写多条语句
- 表达式的计算结果**自动返回**
- 通常不命名，即用即走

---

## Lambda vs 普通函数

| 特性 | Lambda | 普通函数 (`def`) |
|------|--------|------------------|
| 名称 | 匿名（通常无名字） | 有函数名 |
| 函数体 | 只能有一个表达式 | 可以有多条语句 |
| 返回值 | 自动返回表达式结果 | 需要显式 `return` |
| 适用场景 | 临时、简单的逻辑 | 复杂、复用的逻辑 |

**原则：** 逻辑简单且只用一次 → 用lambda；逻辑复杂或需要复用 → 用`def`。

---

## 应用场景：内置高阶函数

高阶函数是指接收函数作为参数的函数。这是lambda最经典的使用场景。

### `map()` — 映射

对可迭代对象的每个元素执行指定操作，返回结果的迭代器。

```python
numbers = [1, 2, 3, 4, 5]

# 普通写法
def square(x):
    return x ** 2

result = map(square, numbers)
print(list(result))  # [1, 4, 9, 16, 25]

# lambda写法——更简洁
result = map(lambda x: x ** 2, numbers)
print(list(result))  # [1, 4, 9, 16, 25]
```

**`map()` 相当于：** 对列表每个元素做"转换"。

```python
# 将字符串列表转为长度列表
names = ["Alice", "Bob", "Charlie"]
lengths = map(lambda s: len(s), names)
print(list(lengths))  # [5, 3, 7]

# 两个列表对应元素相加
a = [1, 2, 3]
b = [10, 20, 30]
sums = map(lambda x, y: x + y, a, b)
print(list(sums))  # [11, 22, 33]
```

---

### `filter()` — 过滤

根据条件筛选可迭代对象中的元素，保留满足条件的。

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8, 10]

# 筛选长度大于3的字符串
words = ["cat", "elephant", "dog", "butterfly"]
long_words = filter(lambda s: len(s) > 3, words)
print(list(long_words))  # ['elephant', 'butterfly']
```

**`filter()` 相当于：** 按条件"筛选"列表。

```python
# 筛选正数
nums = [-2, -1, 0, 1, 2]
positives = filter(lambda x: x > 0, nums)
print(list(positives))  # [1, 2]
```

---

### `sorted()` — 排序（指定key）

`sorted()` 和列表的 `.sort()` 都支持 `key` 参数，用于指定"按什么排序"。

```python
words = ["banana", "pie", "Washington", "book"]

# 按长度排序
sorted_by_len = sorted(words, key=lambda s: len(s))
print(sorted_by_len)  # ['pie', 'book', 'banana', 'Washington']

# 按最后一个字母排序
sorted_by_last = sorted(words, key=lambda s: s[-1])
print(sorted_by_last)  # ['banana', 'pie', 'book', 'Washington']

# 降序排序
sorted_desc = sorted(words, key=lambda s: len(s), reverse=True)
print(sorted_desc)  # ['Washington', 'banana', 'book', 'pie']
```

```python
# 按绝对值排序
nums = [-5, 2, -8, 1, -9]
sorted_by_abs = sorted(nums, key=lambda x: abs(x))
print(sorted_by_abs)  # [1, 2, -5, -8, -9]
```

---

### `max()` / `min()` — 极值（指定key）

```python
words = ["apple", "banana", "cherry"]

# 找出最长的单词
longest = max(words, key=lambda s: len(s))
print(longest)  # banana

# 找出最短的单词
shortest = min(words, key=lambda s: len(s))
print(shortest)  # apple
```

```python
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 找出分数最高的学生
top_student = max(students, key=lambda s: s["score"])
print(top_student)  # {'name': 'Bob', 'score': 92}
```

---

### `reduce()` — 累积计算

`reduce()` 在 `functools` 模块中，用于将序列逐个累积计算为一个值。

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 求和
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# 求积
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# 求最大值
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

---

## 作业（已完成）

基于下面的产品信息完成练习

```python
products = [
  {"name": "iPhone 15", "inc": "APPLE", "price": 5999, "stock": 3012},
  {"name": "MacBook Pro", "inc": "APPLE", "price": 14999, "stock": 580},
  {"name": "AirPods Pro", "inc": "APPLE", "price": 1899, "stock": 4500},
  {"name": "iPad Air", "inc": "APPLE", "price": 4799, "stock": 1200},
  {"name": "Apple Watch", "inc": "APPLE", "price": 2999, "stock": 2100},
  {"name": "Galaxy S24", "inc": "SAMSUNG", "price": 5499, "stock": 2800},
  {"name": "Galaxy Tab", "inc": "SAMSUNG", "price": 3999, "stock": 950},
  {"name": "Galaxy Buds", "inc": "SAMSUNG", "price": 899, "stock": 3200},
  {"name": "Galaxy Watch", "inc": "SAMSUNG", "price": 2199, "stock": 1500},
  {"name": "Mate 60 Pro", "inc": "HUAWEI", "price": 6999, "stock": 800},
  {"name": "MatePad Pro", "inc": "HUAWEI", "price": 4299, "stock": 1100},
  {"name": "FreeBuds", "inc": "HUAWEI", "price": 999, "stock": 2600},
  {"name": "MateBook", "inc": "HUAWEI", "price": 6999, "stock": 670},
  {"name": "Watch GT", "inc": "HUAWEI", "price": 1488, "stock": 1800},
  {"name": "Xiaomi 14", "inc": "XIAOMI", "price": 3999, "stock": 3500},
  {"name": "Redmi K70", "inc": "XIAOMI", "price": 2499, "stock": 4200},
  {"name": "Mi Pad 6", "inc": "XIAOMI", "price": 1999, "stock": 2000},
  {"name": "Mi Band 8", "inc": "XIAOMI", "price": 239, "stock": 8000},
  {"name": "Xiaomi Buds", "inc": "XIAOMI", "price": 499, "stock": 5000},
  {"name": "Xiaomi Book", "inc": "XIAOMI", "price": 4999, "stock": 890},
  {"name": "Pixel 8", "inc": "GOOGLE", "price": 4999, "stock": 600},
  {"name": "Pixel Buds", "inc": "GOOGLE", "price": 1299, "stock": 1500},
  {"name": "Pixel Watch", "inc": "GOOGLE", "price": 2599, "stock": 900},
  {"name": "Pixel Tablet", "inc": "GOOGLE", "price": 3499, "stock": 400},
  {"name": "ThinkPad X1", "inc": "LENOVO", "price": 9999, "stock": 720},
  {"name": "Legion Y9000", "inc": "LENOVO", "price": 8999, "stock": 1100},
  {"name": "Tab P12", "inc": "LENOVO", "price": 2499, "stock": 1300},
  {"name": "Dell XPS 13", "inc": "DELL", "price": 10999, "stock": 650},
  {"name": "Dell G15", "inc": "DELL", "price": 6999, "stock": 1400},
  {"name": "Surface Pro", "inc": "MICROSOFT", "price": 8999, "stock": 580},
  {"name": "Surface Laptop", "inc": "MICROSOFT", "price": 7999, "stock": 700},
  {"name": "Surface Go", "inc": "MICROSOFT", "price": 3999, "stock": 1200},
  {"name": "OnePlus 12", "inc": "ONEPLUS", "price": 4299, "stock": 1800},
  {"name": "OnePlus Buds", "inc": "ONEPLUS", "price": 599, "stock": 3000},
  {"name": "OnePlus Watch", "inc": "ONEPLUS", "price": 1499, "stock": 1600},
  {"name": "OPPO Find X7", "inc": "OPPO", "price": 3999, "stock": 2200},
  {"name": "OPPO Pad 2", "inc": "OPPO", "price": 2999, "stock": 1000},
  {"name": "OPPO Enco", "inc": "OPPO", "price": 499, "stock": 3500},
  {"name": "Vivo X100", "inc": "VIVO", "price": 3999, "stock": 2500},
  {"name": "Vivo Pad 2", "inc": "VIVO", "price": 2499, "stock": 900},
  {"name": "Vivo TWS", "inc": "VIVO", "price": 399, "stock": 4000},
]
```

充分利用本节课学习过的Lambda表达式和内置高阶函数，完成下面的练习

1. 按照价格升序排序

2. 按照价格降序排序

3. 按照库存总额升序排序（库存总额 = 价格 × 库存数量）

4. 找出XIAOMI的所有产品，得到一个字符串列表

5. 找出价格最高的产品所属的公司列表（字符串列表）

7. 得到每家公司产品的平均价格
   结果示例：

   ```python
   [
       {"inc": "HUAWEI", "avg_price": 4156.8},
       {"inc": "GOOGLE", "avg_price": 3099.0},
       {"inc": "MICROSOFT", "avg_price": 6999.0},
       {"inc": "ONEPLUS", "avg_price": 2132.3333333333335},
       {"inc": "VIVO", "avg_price": 2299.0},
       {"inc": "XIAOMI", "avg_price": 2372.3333333333335},
       {"inc": "SAMSUNG", "avg_price": 3149.0},
       {"inc": "OPPO", "avg_price": 2499.0},
       {"inc": "DELL", "avg_price": 8999.0},
       {"inc": "APPLE", "avg_price": 6139.0},
       {"inc": "LENOVO", "avg_price": 7165.666666666667},
   ]
   ```

# Python类和对象

Python 是一门**面向对象**的编程语言。类（Class）是创建对象的蓝图，而对象（Object）是类的具体实例。通过类和对象，可以将数据（属性）和行为（方法）封装在一起，使代码更具结构性和可复用性。

---

## 定义类

使用 `class` 关键字定义类：

```python
class Dog:
    pass

# 创建实例
my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>
```

### 使用 `type()` 动态定义类

类本身也是对象，`type()` 是创建类的内置函数。可以动态地创建类：

```python
# type(类名, (父类元组,), {属性字典})

# 定义方法
def bark(self):
    print(f"{self.name} says: Woof!")

# 动态创建 Dog 类
Dog = type('Dog', (), {'name': 'Buddy', 'bark': bark})

# 创建实例
my_dog = Dog()
print(my_dog.name)  # Buddy
my_dog.bark()       # Buddy says: Woof!
```

**参数说明：**

- 第一个参数：类名（字符串）
- 第二个参数：继承的父类元组
- 第三个参数：类属性和方法的字典

**实际应用场景：** 在 ORM 框架或需要根据配置动态生成类的场景中经常使用。

---

## 构造方法 `__init__`

`__init__` 是类的构造方法，在创建对象时自动调用，用于初始化对象的属性：

```python
class Dog:
    def __init__(this, name, age):
        this.name = name
        this.age = age

# 创建对象时传入参数
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Buddy
print(my_dog.age)   # 3
```

**注意：** `self` 代表对象本身，必须是第一个参数，但调用时不需要传。

---

## 实例属性与类属性

### 实例属性

每个对象独立的属性，通过 `self` 定义：

```python
class Dog:
    def __init__(self, name):
        self.name = name  # 实例属性

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)  # Buddy
print(dog2.name)  # Max
```
**注意：** 实例属性存放在实例的__dict__方法上，实例上的__class__属性指向类，因此可以通过实例访问到类属性。
### 类属性

所有对象共享的属性，在类内部直接定义：

```python
class Dog:
    species = "Canis familiaris"  # 类属性

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# 修改类属性（通过类名）
Dog.species = "Canis lupus"
print(dog1.species)  # Canis lupus
```
**注意：** 类属性存放在类的__dict__方法上。
**访问规则：** 实例属性通过 `self(实例)` 访问，类属性通过 `类名` 或 `self（实例）` 访问。

---
## 实例方法

定义在类中的函数，第一个参数必须是 `self`：

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

    def introduce(self):
        self.bark()  # 方法内调用其他方法
        print(f"My name is {self.name}")

my_dog = Dog("Buddy")
my_dog.bark()       # Buddy says: Woof!
my_dog.introduce()  # Buddy says: Woof! My name is Buddy
```
**注意：** 实例方法存放在类的__dict__方法上，不是在实例的__dict__上。实例方法可以通过类调用。

---

## 类方法与静态方法

### 类方法 `@classmethod`

第一个参数是 `cls`，代表类本身，可以访问或修改类属性：

```python
class Dog:
    count = 0  # 类属性：记录创建了多少只狗

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(Dog.get_count())  # 2
```

### 静态方法 `@staticmethod`

不接收 `self` 或 `cls`，与普通函数类似，只是组织在类中：

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.add(3, 5))      # 8
print(MathUtils.is_even(4))     # True
```

**对比：**

| 方法类型 | 装饰器          | 第一个参数 | 访问实例属性 | 访问类属性 |
| -------- | --------------- | ---------- | ------------ | ---------- |
| 实例方法 | 无              | `self`     | ✓            | ✓          |
| 类方法   | `@classmethod`  | `cls`      | ✗            | ✓          |
| 静态方法 | `@staticmethod` | 无         | ✗            | ✗          |

---
## 继承

子类继承父类的属性和方法，并可以扩展或重写：

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog 继承 Animal
    def speak(self):  # 重写父类方法
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy")
cat = Cat("Kitty")

dog.speak()  # Buddy says: Woof!
cat.speak()  # Kitty says: Meow!
```

### 调用父类方法

使用 `super()` 调用父类的方法：

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal init")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的 __init__
        self.breed = breed      # 扩展新属性
        print("Dog init")

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)   # Buddy
print(dog.breed)  # Golden Retriever
```

### 多继承

Python 支持一个子类同时继承多个父类：

```python
class Flyable:
    def fly(self):
        print("I can fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Duck(Flyable, Swimmable):  # 同时继承 Flyable 和 Swimmable
    pass

duck = Duck()
duck.fly()   # I can fly!
duck.swim()  # I can swim!
```
**注意：** 父类的获取通过类的__base__属性获取，多个父类通过__bases__属性获取，是否多继承可以看__bases__的数量来判断。

#### 方法解析顺序（MRO）

当多个父类有同名方法时，Python 按照 **MRO**（Method Resolution Order）顺序查找：

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):  # MRO: D -> B -> C -> A
    pass

d = D()
d.hello()  # Hello from B（先找到 B 的方法）

# 查看 MRO 顺序
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

#### `super()` 在多继承中的行为

`super()` 按照 MRO 顺序调用**下一个**类的方法，不一定是直接父类：

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()  # 调用 C 的 __init__，不是 A

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()  # 调用 A 的 __init__

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()  # 调用 B 的 __init__

D()
# 输出：
# D init
# B init
# C init
# A init
```

**注意：** 多继承虽然强大，但过度使用会使代码难以维护。通常优先考虑组合（Composition）代替多继承。

---

## 访问控制

Python 没有严格的私有/公有，但以下划线约定访问权限：

| 命名方式 | 含义             | 访问建议         |
| -------- | ---------------- | ---------------- |
| `name`   | 公有             | 可自由访问       |
| `_name`  | 保护（约定）     | 建议不直接访问   |
| `__name` | 私有（名称改写） | 外部难以直接访问 |

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # 公有
        self._balance = balance     # 保护
        self.__password = "123456"  # 私有（名称改写为 _BankAccount__password）

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)
print(account.owner)      # Alice
print(account._balance)   # 1000（可以访问，但不建议）
# print(account.__password)  # AttributeError！
print(account._BankAccount__password)  # 123456（强行访问）
```

**注意：** Python 的访问控制基于约定，不是强制。
## 常见操作

### 内置属性

Python 的类和对象有一些内置属性，用于获取元信息：

| 属性        | 说明                     |
| ----------- | ------------------------ |
| `__class__` | 对象所属的类             |
| `__bases__` | 类的所有直接父类（元组） |
| `__base__`  | 类的第一个直接父类       |
| `__dict__`  | 对象或类的属性字典       |

```python
class Animal:
    pass

class Dog(Animal):
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")

# __class__: 查看对象所属的类
print(dog.__class__)        # <class '__main__.Dog'>
print(dog.__class__.__name__)  # Dog

# __bases__: 查看类的所有直接父类
print(Dog.__bases__)        # (<class '__main__.Animal'>,)

# __base__: 查看类的第一个直接父类
print(Dog.__base__)         # <class '__main__.Animal'>

# __dict__: 查看对象的属性字典
print(dog.__dict__)         # {'name': 'Buddy'}

# __dict__: 查看类的属性字典（包含方法）
print(Dog.__dict__.keys())  # dict_keys([..., 'species', '__init__', ...])
```

---

### `type()`

返回对象的类型（对象是通过哪个类创建的：

```python
dog = Dog("Buddy")

print(type(dog))       # <class '__main__.Dog'>
print(type(Dog))       # <class 'type'>
print(type(123))       # <class 'int'>
print(type("hello"))   # <class 'str'>
```

---

### `isinstance()`

判断对象是否是指定类（或其子类）的实例：

```python
dog = Dog("Buddy")

print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True（Dog 继承 Animal）
print(isinstance(dog, str))      # False

# 支持元组形式，判断是否为多个类型之一
print(isinstance(dog, (Dog, Cat)))   # True
print(isinstance(123, (str, int)))   # True
```

**与 `type()` 的区别：** `isinstance()` 会考虑继承关系，`type()` 不会。

---

### `issubclass()`

判断一个类是否是另一个类的子类：

```python
print(issubclass(Dog, Animal))   # True
print(issubclass(Dog, Dog))      # True（类是自己的子类）
print(issubclass(Animal, Dog))   # False

# 支持元组
print(issubclass(Dog, (Animal, str)))  # True
```

---

### `dir()`

返回对象的所有属性和方法列表（包括继承的）：

```python
dog = Dog("Buddy")

# 查看对象的所有属性和方法
print(dir(dog))
# ['__class__', '__delattr__', ..., 'name', 'species']

# 查看类的所有属性和方法
print(dir(Dog))

# 不带参数时，返回当前作用域的所有名称
print(dir())
```

---

### `vars()`

返回对象的 `__dict__` 属性，即对象的属性字典：

```python
dog = Dog("Buddy")

print(vars(dog))        # {'name': 'Buddy'}
print(vars(Dog))        # 类的 __dict__
print(dog.__dict__)     # 等同于 vars(dog)

# 不带参数时，等同于 locals()
print(vars())
```

---

### `getattr()`

获取对象的属性值，属性不存在时可返回默认值。**会沿着继承链查找属性（包括实例属性、类属性、父类属性）：**

```python
class Animal:
    species = "Animal"

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")

# 查找实例属性
print(getattr(dog, "name"))           # Buddy

# 查找类属性
print(getattr(dog, "species"))        # Animal（继承自父类）

# 查找父类方法
print(getattr(dog, "speak")())       # Some sound

# 属性不存在时，提供默认值
print(getattr(dog, "age", 3))         # 3（默认值）

# 等价于
dog.name
dog.species
dog.speak()
```

---

### `setattr()`

设置对象的属性值，属性不存在时会创建。**如果父类定义了描述符（如 `@property.setter`）或 `__setattr__` 方法，会遵循继承链上的这些机制：**

```python
dog = Dog("Buddy")

setattr(dog, "age", 3)
print(dog.age)            # 3

# 等价于
dog.age = 3

# 可以动态设置属性名
attr_name = "breed"
setattr(dog, attr_name, "Golden Retriever")
print(dog.breed)          # Golden Retriever
```

---

### `hasattr()`

判断对象是否有指定属性。**会检查继承链上的所有属性：**

```python
dog = Dog("Buddy")

# 实例属性
print(hasattr(dog, "name"))       # True

# 继承的类属性
print(hasattr(dog, "species"))    # True（继承自 Animal）

# 继承的方法
print(hasattr(dog, "speak"))      # True（继承自 Animal）

# 不存在的属性
print(hasattr(dog, "age"))        # False

# 常用于安全地访问属性前进行检查
if hasattr(dog, "name"):
    print(dog.name)
```

---

### `delattr()`

删除对象的属性：

```python
dog = Dog("Buddy")

# 添加一个属性
setattr(dog, "age", 3)
print(dog.age)            # 3

# 删除属性
delattr(dog, "age")
# print(dog.age)          # AttributeError!

# 等价于
del dog.age
```
## 作业(已完成)

### 一、腾讯面试题

说出下面代码的打印结果

```python
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super().__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super().__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super().__init__()
        print("leave C")

c = C()
```

### 二、综合预测题

说出下面代码的打印结果

```python
class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    count = 0

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        Dog.count += 1

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(type(dog1))
print(type(Dog))
print(isinstance(dog1, Animal))
print(isinstance(dog1, (int, Dog)))
print(issubclass(Dog, object))
print(dog1.__class__.__name__)
print(Dog.__base__.__name__)
print(hasattr(dog1, "kingdom"))
print(getattr(dog1, "age"))
print(getattr(dog2, "color", "brown"))
setattr(dog1, "color", "golden")
print(dog1.color)
print("bark" in dir(dog1))
print(vars(dog2))
delattr(dog1, "color")
print(hasattr(dog1, "color"))
print(Dog.count)
```

### 三、实现链表类

请实现一个单链表类 `LinkedList`，支持以下操作：

**需要实现的方法：**

| 方法                     | 说明                                                         |
| ------------------------ | ------------------------------------------------------------ |
| `__init__(data=None)`    | 初始化空链表；`data` 可以是列表、元组或集合，其中的值会被初始化为链表的节点 |
| `traverse(callback)`     | 遍历链表，对每个节点值调用 `callback(index, value)`          |
| `__str__()`              | 返回链表的字符串表示，如 `"1 -> 2 -> 3"`                     |
| `to_list()`              | 将链表转换为 Python 列表并返回                               |
| `append(value)`          | 在链表尾部添加一个新节点                                     |
| `prepend(value)`         | 在链表头部添加一个新节点                                     |
| `insert(index, value)`   | 在指定索引位置插入新节点，索引从 0 开始                      |
| `delete_by_value(value)` | 删除第一个值等于 `value` 的节点，返回是否删除成功            |
| `delete_by_index(index)` | 删除指定索引位置的节点，返回被删除的值，索引越界时返回 `None` |
| `find(value)`            | 查找值等于 `value` 的节点，返回其索引，不存在返回 -1         |
| `get(index)`             | 获取指定索引位置的值，索引越界时返回 `None`                  |
| `get_length()`           | 返回链表长度                                                 |
| `is_empty()`             | 判断链表是否为空                                             |

**提示：** 你可能需要先定义一个 `Node` 类来表示链表节点。
---

# 对象的类型

## 知识补充

### 使用 `type()` 动态定义类

类本身也是对象，`type()` 是创建类的内置函数。可以动态地创建类：

```python
# type(类名, (父类元组,), {属性字典})

# 定义方法
def bark(self):
    print(f"{self.name} says: Woof!")

# 动态创建 Dog 类
Dog = type('Dog', (), {'name': 'Buddy', 'bark': bark})

# 创建实例
my_dog = Dog()
print(my_dog.name)  # Buddy
my_dog.bark()       # Buddy says: Woof!
```

**参数说明：**

- 第一个参数：类名（字符串）
- 第二个参数：继承的父类元组
- 第三个参数：类属性和方法的字典

**实际应用场景：** 在 ORM 框架或需要根据配置动态生成类的场景中经常使用。

### MRO

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)  # (D, B, C, A)
print(D.mro())  # (D, B, C, A)  和 __mro__一样
print(D.__bases__)  # (B, C)
print(D.__base__)  # B，取__bases__第一个
```

### 类中的私有成员

```python
# 以下规则适用于所有成员


class A:
    _a = 1  # 约定私有成员，外部仍然可以访问，大部分情况用它
    __a = 2  # 严格私有成员，外部无法直接访问__a（实际上可以访问，被改名字了。变成了_A__a,依然存储在类的__dict__属性上）
    __a__ = 3  # 有特殊作用的成员，往往是系统内置的

    @classmethod
    def test(cls):
        print(cls._a, cls.__a, cls.__a__)  # 内部可以访问所有成员


A.test()  # 1 2 3
print(A._a, A.__a, A.__a__)  # __a访问不到，其他可以
```

## 对象的类型

所有的对象都是通过类创建的，创建对象的类，称之为该对象的类型（也有所属类的说法）

可以使用`type(对象)`得到某个对象的类型



![基础类.excalidraw](https://resource.duyiedu.com/yuanjin/202605181745106.svg)

- 所有函数的类型是`function`（类的方法类型是method,method内部包装了一层function,所以还是认为是function）
- 所有类的类型是`type`
- **创建类的类，称之为元类（metaclass）**

> 见`demo1.py`的打印结果

## 成员的查找顺序

**类成员的查找顺序**

1. 查找自身的MRO链条
2. 查找元类的MRO链条



**其他实例的查找顺序**

1. 查找自身
2. 查找类型的MRO链条

## 作业(已完成)

### 使用费曼学习法，复述本节课内容

### 说出代码的查看结果

```python
function = type(lambda: None)

# type
print("type(type)", type(type))
print("isinstance(type, type)", isinstance(type, type))
print("isinstance(type, function)", isinstance(type, function))
print("isinstance(type, object)", isinstance(type, object))
print("\n")

# object
print("type(object)", type(object))
print("isinstance(object, type)", isinstance(object, type))
print("isinstance(object, function)", isinstance(object, function))
print("\n")

# function
print("type(function)", type(function))
print("isinstance(function, object)", isinstance(function, object))
print("isinstance(function, type)", isinstance(function, type))
print("isinstance(function, function)", isinstance(function, function))
print("\n")


# 普通对象和类
class A:
    pass


a = A()
print("type(a)", type(a))
print("type(A)", type(A))
print("isinstance(A, A)", isinstance(A, A))
print("isinstance(A, object)", isinstance(A, object))
print("isinstance(A, type)", isinstance(A, type))
print("isinstance(A, function)", isinstance(A, function))
print("isinstance(a, A)", isinstance(a, A))
print("isinstance(a, object)", isinstance(a, object))
print("isinstance(a, type)", isinstance(a, type))
print("isinstance(a, function)", isinstance(a, function))
print("\n")


# 普通函数
def func():
    pass


print("type(func)", type(func))
print("isinstance(func, object)", isinstance(func, object))
print("isinstance(func, type)", isinstance(func, type))
print("isinstance(func, function)", isinstance(func, function))
print("\n")
```

# 对象的创建过程

下面是对象创建的伪代码

```python
def create_object(cls, *args, **kwargs):
    # 1. 调用 __new__ 创建实例
    obj = cls.__new__(cls, *args, **kwargs)

    # 2. 类型检查：只有 obj 是 cls 的实例（或其子类的实例）时才调用 __init__
    if isinstance(obj, cls):
        obj.__init__(*args, **kwargs)

    # 3. 返回对象
    return obj


# 测试
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print(f"my name is {self.name}, I'm {self.age} years old")

p = create_object(Person, "shae", 5)
p.sayHi()
```

## 应用场景

理解对象的创建过程后，我们可以通过重写 `__new__` 和 `__init__` 来实现多种设计模式。

### 1. 单例模式

确保一个类只有一个实例：

```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 测试
conn1 = Database()
conn2 = Database()
print(conn1 is conn2)  # True，说明是同一个实例
```

### 2. 对象池/缓存

复用已有对象，避免重复创建：

```python
class ConnectionPool:
    _pool = {}

    def __new__(cls, conn_id):
        if conn_id not in cls._pool:
            obj = super().__new__(cls)
            cls._pool[conn_id] = obj
        return cls._pool[conn_id]

# 测试
pool1 = ConnectionPool("conn_1")
pool2 = ConnectionPool("conn_1")
pool3 = ConnectionPool("conn_2")
print(pool1 is pool2)  # True，相同 conn_id 返回同一个对象
print(pool1 is pool3)  # False，不同 conn_id 返回不同对象
```

### 3. 正整数（带默认值回退）

`__new__` 可以返回不同类型的对象。当返回的对象不是当前类的实例时，`__init__` 不会被执行：

```python
class PositiveInt:
    def __new__(cls, value):
        if value < 0:
            return 0  # 返回 int 类型的 0，不是 PositiveInt 的实例
        return super().__new__(cls)

    def __init__(self, value):
        print("PositiveInt.__init__ 被调用")
        self.value = value

# 测试
p = PositiveInt(5)
print(type(p))    # <class '__main__.PositiveInt'>
print(p.value)    # 5

n = PositiveInt(-3)
print(type(n))    # <class 'int'>
print(n)          # 0
```

## 作业（已完成）

自己写一遍：单例模式

# 可调用对象

在 Python 中，**可调用对象（Callable）**是指可以像函数一样使用括号 `()` 调用的对象。

## 如何判断对象是否可调用

使用内置函数 `callable()`：

```python
print(callable(len))        # True，内置函数
print(callable(int))        # True，类
print(callable([1, 2]))     # False，列表不可调用
print(callable(lambda: 1))  # True，lambda 表达式
```

函数是最常见的可调用对象：

```python
def greet(name):
    return f"Hello, {name}!"

print(callable(greet))  # True
print(greet("Alice"))   # Hello, Alice!
```

类也是可调用对象：

```python
class Dog:
    def __init__(self, name):
        self.name = name

print(callable(Dog))    # True
my_dog = Dog("Buddy")   # 调用类，创建实例
print(my_dog.name)      # Buddy
```

## 让对象变成可调用对象

在类中定义 `__call__` 方法，**实例**就变成了可调用对象：

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

add_5 = Adder(5)
print(callable(add_5))   # True
# add_5(10) 等效于 Adder.__call__(add_5, 10)
print(add_5(10))         # 15，像函数一样调用
print(add_5(100))        # 105
```

**关键理解：**

- `__call__` 让**实例**可以像函数一样被调用（因此上一章讲到的对象创建过程的伪代码，其实就是写到__call__方法中的）
- 调用实例时，传入的参数会传给 `__call__` 方法

## 实际应用场景

### 1. 实现可配置的函数对象

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
triple(5)   # 15
```

### 2. 实现状态保持的回调函数

```python
class Logger:
    def __init__(self, prefix):
        self.prefix = prefix
        self.log_count = 0

    def __call__(self, message):
        self.log_count += 1
        print(f"[{self.prefix}] #{self.log_count}: {message}")

error_log = Logger("ERROR")
error_log("文件未找到")     # [ERROR] #1: 文件未找到
error_log("网络连接失败")   # [ERROR] #2: 网络连接失败
```

## 作业（已完成）

### 一、实现一个计数器类

编写一个 `Counter` 类：

1. 初始化时指定起始值
2. 每次调用实例，计数器值加 1
3. 支持 `reset()` 方法重置为初始值
4. 支持 `get()` 方法获取当前值

```python
c = Counter(10)
print(c())      # 11
c()             # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10
```

### 二、思考题

下面代码的输出是什么？为什么？

```python
class A:
    def __call__(self):
        print("A called")

class B(A):
    def __call__(self):
        print("B called")
        super().__call__()

b = B()
b()
```
# 元类



## 类的创建过程

使用 `class` 关键字定义类时，Python 底层会调用元类来创建类：

```python
class Dog:
    pass


# 等效于
class Dog(metaclass=type):
    pass


# 等效于
Dog = type("Dog", (), {})

# 等效于
Dog = type.__call__(type, "Dog", (), {})
```

也就是说，`class` 关键字只是语法糖，底层仍然是通过 `type()` 创建类。

---

## 自定义元类

通过继承 `type`，可以自定义元类，控制类的创建过程。

```python
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"正在创建类: {name}")
        print(f"父类: {bases}")
        print(f"属性: {list(namespace.keys())}")

        # 必须调用 type.__new__ 来真正创建类
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


# 使用 metaclass 参数指定元类
class Dog(metaclass=MyMeta):
    species = "Canis familiaris"

    def bark(self):
        print("Woof!")


# 等效于
# def bark(self):
#     print("Woof!")


# Dog = type.__call__(MyMeta, "Dog", (), {"species": "Canis familiaris", "bark": bark})

# 输出：
# 正在创建类: Dog
# 父类: ()
# 属性: ['__module__', '__qualname__', 'species', 'bark']
```

**参数说明：**

- `mcs`：元类自身（类似类方法中的 `cls`）
- `name`：类名字符串
- `bases`：父类元组
- `namespace`：类属性的字典

## 深入：元类的查找顺序

子类会继承父类的元类：

```python
class MyMeta(type):
    pass

class Base(metaclass=MyMeta):
    pass

class Child(Base):  # 自动继承 MyMeta
    pass

print(type(Child))  # <class '__main__.MyMeta'>
```

如果父类元类不兼容，需要使用更通用的元类：

```python
class MetaA(type):
    pass

class MetaB(type):
    pass

class A(metaclass=MetaA):
    pass

class B(metaclass=MetaB):
    pass

# class C(A, B): pass  # TypeError! 元类冲突

# 解决方法：创建兼容的元类
class CommonMeta(MetaA, MetaB):
    pass

class C(A, B, metaclass=CommonMeta):  # 正常
    pass
```



## 总结

| 概念 | 说明 |
| ---- | ---- |
| 元类 | 创建类的类，默认是 `type` |
| `__new__` | 创建类，返回类对象 |
| `__init__` | 初始化类，无返回值 |
| `__call__` | 控制类的实例化过程 |
| 应用场景 | 命名检查、自动注册、方法增强、ORM 等 |

---

## 作业（已完成）

### 一、实现单例元类

编写一个元类 `SingletonMeta`，使得任何使用该元类的类都自动成为单例模式：

```python
class SingletonMeta(type):
    # 你的代码
    pass

class Database(metaclass=SingletonMeta):
    def __init__(self, host):
        self.host = host

db1 = Database("localhost")
db2 = Database("remote")
print(db1 is db2)  # 应该输出 True
print(db1.host)    # 应该输出 localhost
```

### 二、自动注册子类

编写一个元类 `PluginMeta`，使得任何继承自 `Plugin` 的子类都会被自动注册到 `PluginMeta.registry` 字典中（键为类名，值为类本身）：

```python
class PluginMeta(type):
    # 你的代码
    pass

class Plugin(metaclass=PluginMeta):
    pass

class ImagePlugin(Plugin):
    pass

class TextPlugin(Plugin):
    pass

print(PluginMeta.registry)
# 应该输出类似：{'ImagePlugin': <class '__main__.ImagePlugin'>, 'TextPlugin': <class '__main__.TextPlugin'>}
```

### 三、为所有方法添加日志

编写一个元类 `LogMeta`，自动为类中每个非私有方法（即不以 `_` 开头的方法）添加执行日志。调用方法时，先打印 `[LOG] 调用 {方法名}`，再执行原方法：

```python
class LogMeta(type):
    # 你的代码
    pass

class Calculator(metaclass=LogMeta):
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(3, 5))
print(calc.sub(10, 4))

# 应该输出：
# [LOG] 调用 add
# 8
# [LOG] 调用 sub
# 6
```

# 装饰器



## 装饰器的本质

装饰器本质上是一个接受函数作为参数并返回新函数的高阶函数：

```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

# 下面的代码
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)

# 等效于
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后
```



**装饰器是一个可调用对象，接收一个可调用对象，返回任意对象。但为了保证程序能正常运行，通常返回另一个可调用对象来替代原对象。**



## 多个装饰器叠加

可以同时使用多个装饰器，执行顺序为从下到上：

```python
@decorator_a
@decorator_b
def func():
    pass

# 等效于：
# func = decorator_a(decorator_b(func))
```

## 作业（已完成）

> **前置知识：** 本章作业中会用到 `time` 模块的两个功能：
> - `time.time()`：返回当前时间的时间戳（一个浮点数）
> - `time.sleep(seconds)`：让程序暂停执行指定的秒数
>
> 例如：
> ```python
> import time
>
> start = time.time()
> time.sleep(1)
> elapsed = time.time() - start
> print(f"耗时: {elapsed} 秒")
> ```

### 一、实现timer装饰器

```python
import time

def timer(func):
    # 你的代码
    pass

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
# 输出：slow_function 执行时间: 1.0012 秒
```



### 二、实现wraps装饰器

实现wraps装饰器，用于不改变函数的名称和注释

```python
# 实现wraps装饰器，用于不改变函数的名称和注释


def wraps(func):
    # 你的代码
    pass


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")

    return wrapper


@my_decorator
def say_hello():
    """打招呼"""
    print("Hello!")


say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后
print("name", say_hello.__name__)
print("doc", say_hello.__doc__)
```

### 三、实现repeat装饰器

```python
def repeat(n):
    # 你的代码
    pass


@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1
```

### 四、实现cache装饰器

编写一个装饰器 `cache`，缓存函数的计算结果。当使用相同的参数调用函数时，直接返回缓存的结果：

```python
def cache(func):
    # 你的代码
    pass

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))  # 应该快速返回结果
```

**提示：** 使用字典存储参数到结果的映射。



### 五、实现to_dict装饰器

编写一个类装饰器 `to_dict`，自动为类生成 `to_dict` 方法，该方法可以将对象转换为字典

```python
def to_dict(cls):
    # 你的代码
    pass

@to_dict
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.to_dict())  # 应该输出: {"x":3, "y":4}
```
# 魔术方法

魔术方法（Magic Methods）是 Python 中**以双下划线开头和结尾**的特殊方法，如 `__init__`、`__str__`。它们不需要显式调用，而是由 Python 在特定场景下**自动触发**。

## 字符串表示

当使用 `print()`、`str()` 或 `repr()` 时，Python 会自动调用对应的魔术方法：

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """面向用户，友好的可读格式"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """面向开发者，精确的重建格式"""
        return f"Point({self.x!r}, {self.y!r})"


p = Point(3, 4)
print(p)           # Point(3, 4) —— 调用 __str__
print(str(p))      # Point(3, 4) —— 调用 __str__
print(repr(p))     # Point(3, 4) —— 调用 __repr__

# 交互式环境中直接显示对象，调用 __repr__
# p  # Point(3, 4)
```

**建议：** 两个方法都实现。如果只实现 `__repr__`，`__str__` 会回退到使用它。

---

## 比较操作

通过实现比较魔术方法，可以让自定义对象支持 `==`、`<`、`>` 等操作：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """=="""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        """<"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __le__(self, other):
        """<="""
        return self < other or self == other

    def __gt__(self, other):
        """>"""
        return not self <= other

    def __ge__(self, other):
        """>="""
        return not self < other

    def __ne__(self, other):
        """!="""
        return not self == other

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"


alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice == bob)  # False   
print(alice > bob)   # True
print(alice <= bob)  # False

# 实现了比较方法后，可以使用 sorted
people = [bob, alice]
print(sorted(people))  # [Person('Bob', 25), Person('Alice', 30)]
```

**简化方案：** 使用 `@functools.total_ordering` 装饰器，只需实现 `__eq__` 和其中一个（如 `__lt__`），其余会自动推导：

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"
```

---

## 算术运算

让对象支持 `+`、`-`、`*`、`/` 等运算符：

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented  # 返回 NotImplemented，让 Python 尝试 other 的 __radd__

    def __sub__(self, other):
        """-"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """*，向量与标量相乘"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        """右乘：scalar * vector"""
        return self * scalar  # 复用 __mul__

    def __truediv__(self, scalar):
        """/"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    def __neg__(self):
        """负号：-vector"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """abs()"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)       # Vector(4, 6)
print(v2 - v1)       # Vector(2, 2)
print(v1 * 3)        # Vector(3, 6)
print(2 * v1)        # Vector(2, 4) —— 调用 __rmul__
print(-v1)           # Vector(-1, -2)
print(abs(v1))       # 2.236...
```

**常用算术魔术方法：**

| 运算符 | 魔术方法 | 说明 |
|--------|----------|------|
| `+` | `__add__` | 加法 |
| `-` | `__sub__` | 减法 |
| `*` | `__mul__` | 乘法 |
| `/` | `__truediv__` | 真除法 |
| `//` | `__floordiv__` | 整除 |
| `%` | `__mod__` | 取模 |
| `**` | `__pow__` | 幂运算 |
| `+a` | `__pos__` | 正号 |
| `-a` | `__neg__` | 负号 |
| `abs()` | `__abs__` | 绝对值 |

---

## 容器协议

实现容器协议，让自定义对象可以像 `list`、`dict` 一样使用 `[]`、 `len()`、`in` 等操作：

```python
class ShoppingCart:
    def __init__(self):
        self._items = []

    def __len__(self):
        """len(cart)"""
        return len(self._items)

    def __getitem__(self, index):
        """cart[index]"""
        return self._items[index]

    def __setitem__(self, index, value):
        """cart[index] = value"""
        self._items[index] = value

    def __delitem__(self, index):
        """del cart[index]"""
        del self._items[index]

    def __contains__(self, item):
        """item in cart"""
        return item in self._items

    def __iter__(self):
        """for item in cart"""
        return iter(self._items)

    def append(self, item):
        self._items.append(item)

    def __repr__(self):
        return f"ShoppingCart({self._items!r})"


cart = ShoppingCart()
cart.append("apple")
cart.append("banana")
cart.append("orange")

print(len(cart))           # 3
print(cart[0])             # apple
print(cart[1:])            # ['banana', 'orange'] —— 支持切片
print("apple" in cart)     # True

for item in cart:
    print(item)
# apple
# banana
# orange
```

---

## 类型转换

实现类型转换魔术方法，让对象支持 `int()`、`float()`、`bool()` 等转换：

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __float__(self):
        return float(self.amount)

    def __bool__(self):
        return self.amount != 0

    def __repr__(self):
        return f"Money({self.amount})"


m = Money(100.5)
print(int(m))      # 100
print(float(m))    # 100.5
print(bool(m))     # True

m0 = Money(0)
print(bool(m0))    # False
```

---

## 属性访问拦截

通过实现属性访问相关的魔术方法，可以拦截对对象属性的**读取**、**设置**和**删除**操作：

```python
class Config:
    def __init__(self):
        # 必须用 object.__setattr__，否则会无限递归
        object.__setattr__(self, "_data", {})

    def __getattr__(self, name):
        """访问不存在的属性时触发"""
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' 对象没有属性 '{name}'")

    def __setattr__(self, name, value):
        """设置任意属性时触发"""
        if name.startswith("_"):
            # 内部属性直接设置，避免递归
            object.__setattr__(self, name, value)
        else:
            self._data[name] = value

    def __delattr__(self, name):
        """删除属性时触发"""
        if name in self._data:
            del self._data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' 对象没有属性 '{name}'")

    def __repr__(self):
        return f"Config({self._data!r})"


cfg = Config()
cfg.debug = True      # 调用 __setattr__
cfg.port = 8080       # 调用 __setattr__
print(cfg.debug)      # True —— 调用 __getattr__
print(cfg.port)       # 8080 —— 调用 __getattr__
del cfg.debug         # 调用 __delattr__
print(cfg)            # Config({'port': 8080})
```

**注意：** `__setattr__` 拦截**所有**属性设置。如果在其内部使用 `self.xxx = value` 的方式赋值，会再次触发 `__setattr__`，导致**无限递归**。应使用 `object.__setattr__(self, name, value)` 来绕过拦截。

---

### `__getattr__` vs `__getattribute__`

- `__getattr__`：**仅**在访问**不存在**的属性时触发
- `__getattribute__`：访问**任何**属性时都会触发（更底层，优先级更高）

```python
class Demo:
    def __init__(self):
        self.existing = 100

    def __getattribute__(self, name):
        """所有属性访问都会经过这里"""
        print(f"正在访问: {name}")
        # 必须用 object.__getattribute__，否则会无限递归
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        """只有访问不存在的属性时才到这里"""
        return f"'{name}' 不存在，返回默认值"


d = Demo()
print(d.existing)   # 先触发 __getattribute__，返回 100
print(d.missing)    # 先触发 __getattribute__，找不到，再触发 __getattr__
```

**⚠️ 警告：** 在 `__getattribute__` 中再次访问 `self.xxx` 也会触发自身，必须使用 `object.__getattribute__(self, name)`。

---

## 对象生命周期

除了 `__init__`，还有 `__del__` 在对象被销毁时调用：

```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        print(f"连接到数据库: {db_name}")

    def __del__(self):
        """对象被销毁时调用"""
        print(f"关闭数据库连接: {self.db_name}")


conn = DatabaseConnection("test_db")
del conn  # 关闭数据库连接: test_db
```

**注意：** `__del__` 的调用时机不确定（取决于垃圾回收），不应依赖它做关键清理。对于资源管理，应使用**上下文管理器**（后续课程讲）。

---

## 常用魔术方法速查

| 类别 | 方法 | 触发场景 |
|------|------|----------|
| 构造 | `__init__` | 创建对象后初始化 |
| 构造 | `__new__` | 创建对象（已讲过） |
| 字符串 | `__str__` | `print()`、`str()` |
| 字符串 | `__repr__` | `repr()`、交互式显示 |
| 比较 | `__eq__` | `==` |
| 比较 | `__lt__` | `<` |
| 比较 | `__gt__` | `>` |
| 比较 | `__le__` | `<=` |
| 比较 | `__ge__` | `>=` |
| 比较 | `__ne__` | `!=` |
| 算术 | `__add__` | `+` |
| 算术 | `__sub__` | `-` |
| 算术 | `__mul__` | `*` |
| 算术 | `__truediv__` | `/` |
| 容器 | `__len__` | `len()` |
| 容器 | `__getitem__` | `obj[key]` |
| 容器 | `__setitem__` | `obj[key] = value` |
| 容器 | `__delitem__` | `del obj[key]` |
| 容器 | `__contains__` | `in` |
| 容器 | `__iter__` | `for...in` |
| 转换 | `__int__` | `int()` |
| 转换 | `__float__` | `float()` |
| 转换 | `__bool__` | `bool()` |
| 可调用 | `__call__` | `obj()` |
| 属性 | `__getattr__` | 访问不存在的属性 |
| 属性 | `__getattribute__` | 访问任意属性 |
| 属性 | `__setattr__` | 设置属性 |
| 属性 | `__delattr__` | 删除属性 |
| 生命周期 | `__del__` | 对象销毁 |

---

## 作业（可使用AI、未实现，直接看的答案）

实现一个 `Fraction` 类，支持以下操作：

```python
f1 = Fraction(1, 2)   # 1/2
f2 = Fraction(1, 3)   # 1/3

print(f1 + f2)        # 5/6
print(f1 - f2)        # 1/6
print(f1 * f2)        # 1/6
print(f1 / f2)        # 3/2
print(f1 == f2)       # False
print(f1 > f2)        # True
print(float(f1))      # 0.5
print(str(f1))        # "1/2"
print(repr(f1))       # "Fraction(1, 2)"
```

**提示：**
- 实现 `__init__`、`__str__`、`__repr__`
- 实现 `__eq__`、`__lt__`、`__gt__`、`__le__`、`__ge__`、`__ne__`
- 实现 `__add__`、`__sub__`、`__mul__`、`__truediv__`
- 实现 `__float__`


# 描述符

## 问题

```python
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = radius**2 * math.pi
        self.diameter = radius * 2


c = Circle(5)
print(c.radius, c.area, c.diameter)  # 没问题

# 出现问题
# 1. 不符合逻辑的赋值
c.radius = -10

# 2. 数据不一致
c.radius = 10
print(c.radius, c.area, c.diameter)  # 数据不一致
```

## 描述符协议

### 认识术语

描述符协议规定，只要一个类，实现了`__get__`、`__set__`、`__delete__`任意一个实例方法：

- 该类称之为**描述符类**
- 该类的对象称之为**描述符对象**，也可以简称为**描述符**
  - 如果描述符类实现了`__set__`、`__delete__`任意一个
    它的对象又称之为**数据型描述符**（Data Descriptor）
  - 如果描述符类只实现了`__get__`
    它的对象又称为**非数据型描述符**（Non-Data Descriptor）
- 描述符对象只有是**类属性**时才有意义
  所以描述符通常又称为**属性描述符**

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    my_attr = MyDescriptor()  # 描述符、属性描述符、数据描述符
```

### 访问顺序

当访问实例成员时，按照以下优先级查找成员：

1. **数据型描述符**（类属性）
2. 实例属性（`instance.__dict__`）
3. 类属性（普通）
4. 父类...

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    my_attr = MyDescriptor()  # 描述符、属性描述符、数据描述符

    def __init__(self, value):
        self.my_attr = value  # 赋值的是类属性


ins = MyClass(10)
print(ins.__dict__)  # 不包含 my_attr
print(ins.my_attr)  # 访问的是类属性
```

### 读写删操作

描述符会拦截对它的读、写、删操作

```python
# 描述符类
class MyDescriptor:
    def __get__(self, instance, owner):
        print("__get__ called")
        pass

    def __set__(self, instance, value):
        print("__set__ called")
        pass

    def __delete__(self, instance):
        print("__delete__ called")
        pass


class MyClass:
    my_attr1 = MyDescriptor()  # 描述符、属性描述符、数据描述符
    my_attr2 = MyDescriptor()  # 描述符、属性描述符、数据描述符


ins = MyClass()
ins.my_attr1  # MyDescriptor.__get__(MyClass.my_attr, ins, MyClass)
ins.my_attr1 = 10  # MyDescriptor.__set__(MyClass.my_attr, ins, 10)
del ins.my_attr1  # MyDescriptor.__delete__(MyClass.my_attr, ins)


MyClass.my_attr2  # MyDescriptor.__get__(MyClass.my_attr, None, MyClass)
MyClass.my_attr2 = 20  # 直接覆盖 my_attr2，my_attr2 不再是描述符了
del MyClass.my_attr2  # 直接删除 my_attr2 属性，my_attr2 不再存在

```

**最佳实践：**

1. 绝大部分时候都使用**数据型描述符**
2. 对描述符的访问，永远通过实例去访问

### 钩子函数

目前，描述符类中仅提供了一个钩子函数`__set_name__`

> Python3.6版本加入

```python
# 描述符类
class MyDescriptor:
    def __set_name__(self, owner, name):
        print(f"__set_name__ called with owner={owner}, name={name}")

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class MyClass:
    # 这里会触发__set_name__
    # 时间点：完成赋值后
    # 作用：让描述符知道自己被赋值给了哪个类的哪个属性
    my_attr1 = MyDescriptor()
    my_attr2 = MyDescriptor()
```

## 解决最初的问题

```python
import math


class RadiusDescriptor:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        instance._radius = value

    def __get__(self, instance, owner):
        return instance._radius
    
    def __delete__(self, instance):
        raise AttributeError("radius 不能被删除")


class AreaDescriptor:

    def __get__(self, instance, owner):
        return instance.radius**2 * math.pi

    def __set__(self, instance, value):
        raise AttributeError("area 是只读属性，不能设置")
    
    def __delete__(self, instance):
        raise AttributeError("area 不能被删除")


class DiameterDescriptor:

    def __get__(self, instance, owner):
        return instance.radius * 2

    def __set__(self, instance, value):
        raise AttributeError("diameter 是只读属性，不能设置")
    
    def __delete__(self, instance):
        raise AttributeError("diameter 不能被删除")


class Circle:
    radius = RadiusDescriptor()
    area = AreaDescriptor()
    diameter = DiameterDescriptor()

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)  # 没问题
print(c1.radius)  # 输出 5
print(c1.area)  # 输出 78.53981633974483
print(c1.diameter)  # 输出 10
c1.radius = 10  # 没问题
print(c1.radius)  # 输出 10
print(c1.area)  # 输出 314.1592653589793
print(c1.diameter)  # 输出 20

c1.area = 100  # 报错
print(c1.area)

```



## @property 装饰器

`@property` 可以将方法变成**属性**，访问时像访问普通属性一样，不需要加括号：

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """获取半径"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """设置半径，带验证"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @radius.deleter
    def radius(self):
        """删除半径"""
        print("删除半径")
        del self._radius

    @property
    def area(self):
        """计算面积（只读属性）"""
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        """计算直径（只读属性）"""
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5 —— 调用 getter
print(c.area)       # 78.54... —— 自动计算
print(c.diameter)   # 10

c.radius = 10       # 调用 setter
print(c.area)       # 314.15...

# c.area = 100      # AttributeError! area 没有 setter
# c.radius = -5     # ValueError! 半径不能为负数

# del c.radius      # 调用 deleter
# print(c.radius)   # AttributeError!
```

**关键点：**
- `@property` 将方法变成**只读属性**
- `@属性名.setter` 定义可写属性（必须和 property 同名）
- `@属性名.deleter` 定义可删除属性

---



## 应用场景

### 1. 惰性计算

```python
class LazyProperty:
    """惰性加载属性：只在第一次访问时计算"""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        # 将结果缓存到实例的属性中
        setattr(instance, self.name, value)
        return value


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    @LazyProperty
    def data(self):
        print(f"正在加载文件: {self.file_path}")
        # 模拟耗时操作
        return [1, 2, 3, 4, 5]


loader = DataLoader("data.txt")
print(loader.data)  # 正在加载文件: data.txt
                    # [1, 2, 3, 4, 5]
print(loader.data)  # [1, 2, 3, 4, 5] —— 不再加载，直接从属性读取
```

### 2. 类型检查

```python
class Typed:
    """强制类型检查的描述符"""
    
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} 必须是 {self.expected_type.__name__} 类型，"
                f"而不是 {type(value).__name__}"
            )
        instance.__dict__[self.name] = value


class Student:
    name = Typed(str)
    age = Typed(int)
    score = Typed(float)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Alice", 20, 85.5)
# s.age = "20"      # TypeError! age 必须是 int 类型，而不是 str
```

---

## 作业（可使用AI，已看懂）

### 一、实现只读属性

编写一个类 `ImmutablePoint`，创建后不能修改坐标：

```python
p = ImmutablePoint(3, 4)
print(p.x)      # 3
print(p.y)      # 4

# p.x = 10      # AttributeError! 不能修改只读属性
```

**提示：** 使用 `@property` 但不提供 setter。

### 二、实现范围验证

编写一个 `Temperature` 类，温度必须在 -273.15（绝对零度）到 1000 之间：

```python
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0（只读属性，自动计算）
print(t.kelvin)       # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度
```

### 三、实现类属性计数器

编写一个描述符，记录某个类属性被访问和修改的次数：

```python
class AccessCounter:
    # 你的代码
    pass


class MyClass:
    value = AccessCounter(10)  # 初始值为 10


obj = MyClass()
print(obj.value)      # 10
print(obj.value)      # 10
obj.value = 20
print(obj.value)      # 20

# 查看访问和修改次数
print(AccessCounter.get_access_count())   # 3（被访问了 3 次）
print(AccessCounter.get_modify_count())   # 1（被修改了 1 次）
```

### 四、思考题

下面代码的输出是什么？为什么？

```python
class Descriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called, instance={instance}, owner={owner}")
        return 42

    def __set__(self, instance, value):
        print(f"__set__ called, instance={instance}, value={value}")


class A:
    x = Descriptor()


a = A()
print(a.x)
a.x = 100
a.__dict__["x"] = "instance"
print(a.x)
print(a.__dict__)
```
# 异常处理

## 异常的捕获

使用 `try...except` 捕获可能发生的异常

可以捕获多个异常，并获取异常对象：

```python
try:
    number = int("abc")
except ValueError as e:
    print(f"数值错误: {e}")
except TypeError as e:
    print(f"类型错误: {e}")
else:
    print("没有异常时执行")
finally:
    print("始终会执行")
```

```python
try:
    number = int("abc")
except ValueError as e:
    print(e.args)  # 获取异常信息
    print(e.__traceback__)  # 异常的堆栈跟踪对象
```

## 异常类型

Python 内置异常形成层次结构，捕获父类异常可以捕获其所有子类：

```
BaseException
 ├── SystemExit          # sys.exit() 引发
 ├── KeyboardInterrupt   # Ctrl+C 引发
 └── Exception           # 常规异常的基类
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      └── ...
```

```python
# 捕获 Exception 可以捕获几乎所有常规异常
try:
    # 可能引发各种异常的操作
    pass
except Exception as e:
    print(f"发生错误: {e}")

# 但不推荐捕获过于宽泛的异常，应尽量精确
```



## 主动抛出异常

使用 `raise` 主动抛出异常：

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("余额不足")
    if amount <= 0:
        raise ValueError("取款金额必须大于零")
    return balance - amount

try:
    withdraw(100, 200)
except ValueError as e:
    print(e)  # 余额不足
```

可以重新抛出当前异常：

```python
try:
    risky_operation()
except Exception:
    # 记录日志后继续抛出
    print("发生异常，准备抛出")
    raise  # 重新抛出
```

## 自定义异常

通过继承 `Exception` 或其子类创建自定义异常：

```python
class ValidationError(Exception):
    """参数验证失败"""
    pass

class NotFoundError(Exception):
    """资源不存在"""
    
    def __init__(self, resource, resource_id):
        self.resource = resource
        self.resource_id = resource_id
        super().__init__(f"{resource} (id={resource_id}) 不存在")


# 使用
def get_user(user_id):
    if user_id <= 0:
        raise ValidationError("用户ID必须大于零")
    if user_id not in user_database:
        raise NotFoundError("User", user_id)
    return user_database[user_id]
```



## 异常链

```python
def exception_chains1():
    # 方式1：直接抛出（无关联）
    try:
        raise ValueError("错误A")
    except ValueError:
        raise RuntimeError("错误B")  # 隐式关联，__context__ 有值


def exception_chains2():
    # 方式2：from 显式关联
    try:
        raise ValueError("错误A")
    except ValueError as e:
        raise RuntimeError("错误B") from e  # 显式关联，__cause__ 有值


# 查看区别
try:
    exception_chains1()
except RuntimeError as e:
    print("隐式关联:", e)
    print(f"  __cause__: {e.__cause__}")  # None
    print(f"  __context__: {e.__context__}")  # ValueError

try:
    exception_chains2()
except RuntimeError as e:
    print("\n显式关联:", e)
    print(f"  __cause__: {e.__cause__}")  # ValueError
    print(f"  __context__: {e.__context__}")  # None

```

## 作业（可使用AI，已看懂）

### 一、实现安全的除法函数

```python
def safe_divide(a, b):
    """
    安全除法，要求：
    1. 捕获 ZeroDivisionError，返回 0
    2. 捕获 TypeError，打印"参数类型错误"并返回 None
    """
    # 你的代码
    pass

print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # 0
print(safe_divide("10", 2))    # 参数类型错误，None
```

### 二、实现重试装饰器

```python
import time

def retry(max_attempts, delay=1):
    """
    失败重试装饰器
    如果函数抛出异常，等待 delay 秒后重试，最多重试 max_attempts 次
    """
    # 你的代码
    pass

@retry(max_attempts=3, delay=1)
def unstable_function():
    """模拟不稳定的操作"""
    import random
    if random.random() < 0.7:  # 70% 概率失败
        raise ConnectionError("连接失败")
    return "成功"

# 应该能处理失败并重试，最终返回"成功"或抛出最后一次异常
```

### 三、自定义异常与验证

```python
class InsufficientFundsError(Exception):
    """余额不足"""
    pass

class AccountFrozenError(Exception):
    """账户已冻结"""
    pass

class BankAccount:
    def __init__(self, balance=0, frozen=False):
        self.balance = balance
        self.frozen = frozen
    
    def withdraw(self, amount):
        """
        取款，要求：
        1. 如果 frozen=True，抛出 AccountFrozenError
        2. 如果 amount > balance，抛出 InsufficientFundsError
        3. 如果 amount <= 0，抛出 ValueError
        """
        # 你的代码
        pass
    
    def deposit(self, amount):
        """
        存款，要求：
        1. 如果 frozen=True，抛出 AccountFrozenError
        2. 如果 amount <= 0，抛出 ValueError
        """
        # 你的代码
        pass

# 测试
account = BankAccount(100)
account.deposit(50)           # balance = 150
account.withdraw(30)          # balance = 120

# account.withdraw(200)       # InsufficientFundsError
# account.deposit(-10)        # ValueError

frozen_account = BankAccount(100, frozen=True)
# frozen_account.withdraw(10)  # AccountFrozenError
```

### 四、异常转换

实现一个函数，将各种异常转换为统一的 APIException：

```python
class APIException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)

def call_api():
    """模拟API调用，可能抛出各种异常"""
    import random
    errors = [
        ValueError("参数错误"),
        ConnectionError("连接超时"),
        TimeoutError("请求超时"),
        RuntimeError("服务器内部错误")
    ]
    raise random.choice(errors)

def robust_api_call():
    """
    调用 call_api()，将各种异常转换为 APIException：
    - ValueError → APIException(400, "参数错误")
    - ConnectionError/TimeoutError → APIException(503, "服务不可用")
    - 其他异常 → APIException(500, "服务器内部错误")
    """
    # 你的代码
    pass
```

# 迭代器与生成器

## 迭代器(Iterator)

迭代器是实现了`__iter__`和`__next__`方法的对象

```python
class MyIterator:

    def __iter__(self):
        """
        要求：必须返回迭代器
        99.999999%的情况下，返回迭代器自身
        """
        return self

    def __next__(self):
        """返回下一个值"""
        pass
      
obj = MyIterator()  # obj 是一个迭代器
```



### 应用：无限序列

```python
class FibonacciIterator:
    """无限斐波那契数列迭代器"""

    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current


# 使用示例
fib = FibonacciIterator()

print(next(fib))  # 输出: 1  等效于 fib.__next__()
print(next(fib))  # 输出: 1
print(next(fib))  # 输出: 2
print(next(fib))  # 输出: 3
print(next(fib))  # 输出: 5
print(next(fib))  # 输出: 8

```



## 可迭代对象(Iterable)

**可迭代协议规定，只要一个对象实现了 `__iter__()` 方法，且返回一个迭代器，则它就是可迭代对象**

推理可知：**迭代器一定是可迭代对象**

> python中的容器类型都是可迭代对象

```python
my_list = [1, 2, 3]

# 调用 iter() 获取迭代器
iterator = iter(my_list)  # 等价于 my_list.__iter__()

print(type(iterator))     # <class 'list_iterator'>

# 使用 next() 逐个获取值
print(next(iterator))     # 1
print(next(iterator))     # 2
print(next(iterator))     # 3

# print(next(iterator))   # StopIteration! 没有更多元素了
```

### 示例：倒数对象

```python
class Countdown:
    """可迭代对象：倒数"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """返回一个新的迭代器"""
        return CountdownIterator(self.start)


class CountdownIterator:
    """迭代器"""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num


cd = Countdown(5)

iterator = iter(cd)
print(next(iterator))  # 5
print(next(iterator))  # 4
print(next(iterator))  # 3
print(next(iterator))  # 2
print(next(iterator))  # 1
print(next(iterator))  # 0
# print(next(iterator))  # StopIteration!

```



### 消费者

#### 1. `for`循环

```python
# for 循环会自动调用 iter() 和 next()
for n in Countdown(3):
    print(n)  # 3 2 1 0
```

#### 2. **`list()`、`tuple()`、`set()` 等构造函数**

```python
print(list(Countdown(3)))  # [3, 2, 1, 0]
print(tuple(Countdown(3)))  # (3, 2, 1, 0)
print(set(Countdown(3)))  # {0, 1, 2, 3}
```

#### 3. **`*` 解包操作符**

```python
first, *rest = Countdown(3)
print(first)  # 3
print(rest)   # [2, 1, 0]

# 或用列表解包
values = [*Countdown(3)]
print(values)  # [3, 2, 1, 0]
```

#### 4. **`in` 成员判断**

```python
print(5 in Countdown(3))   # False
print(2 in Countdown(3))   # True
```

#### 5. **`sum()`、`max()`、`min()` 等内置函数**

```python
print(sum(Countdown(3)))  # 6
print(max(Countdown(3)))  # 3
print(min(Countdown(3)))  # 0
```

#### 6. **`zip()`、`map()`、`filter()` 等函数**

```python
# zip 合并多个可迭代对象
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
# Alice: 25
# Bob: 30
# Charlie: 35

# map 对元素进行转换
squares = map(lambda x: x**2, Countdown(3))
print(list(squares))  # [9, 4, 1, 0]

# filter 过滤元素
evens = filter(lambda x: x % 2 == 0, Countdown(3))
print(list(evens))  # [2, 0]
```

#### 7. **`any()`、`all()`**

```python
numbers = Countdown(3)
print(any(numbers))  # True (至少一个为真)
print(all(numbers))  # False (是否所有都为真)
```

### range函数

`range()` 是 Python 中最常用的可迭代对象之一，用于生成整数序列：

```python
# range(stop): 0 到 stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# range(start, stop): start 到 stop-1
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5

# range(start, stop, step): 指定步长
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8

# 负数步长（倒序）
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1
```

**重要特性：**

1. **惰性计算**：`range` 不会一次性生成所有数字，而是按需生成
2. **支持索引和切片**：与列表不同，`range` 支持随机访问

```python
r = range(0, 100, 2)

print(len(r))      # 50
print(r[5])        # 10
print(r[0:5])      # range(0, 10, 2)
print(10 in r)     # True
print(11 in r)     # False
```

3. **不是迭代器**：`range` 是可迭代对象，但不是迭代器（可以重复使用）

```python
r = range(3)

for i in r:
    print(i, end=" ")  # 0 1 2
print()

for i in r:
    print(i, end=" ")  # 0 1 2（可以再次遍历）
```

> `range` 对象在内存中只存储 `start`、`stop`、`step` 三个值，无论范围多大都占用固定内存

### 推导式

推导式(Comprehension)是一种简洁的语法，用于从一个可迭代对象创建新的列表、字典或集合。

#### 列表推导式

```python
# 基本语法：[表达式 for 变量 in 可迭代对象]
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 带条件过滤：[表达式 for 变量 in 可迭代对象 if 条件]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# 带 if-else 条件
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(5)]
print(labels)  # ['偶数', '奇数', '偶数', '奇数', '偶数']
```

#### 字典推导式

```python
# 基本语法：{键表达式: 值表达式 for 变量 in 可迭代对象}
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 带条件过滤
odd_squares = {x: x**2 for x in range(10) if x % 2 != 0}
print(odd_squares)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

#### 集合推导式

```python
# 基本语法：{表达式 for 变量 in 可迭代对象}
square_set = {x**2 for x in range(10)}
print(square_set)  # {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

# 带条件过滤
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

#### 嵌套推导式

```python
# 嵌套列表推导式：将二维列表展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 等价于：
# flat = []
# for row in matrix:
#     for x in row:
#         flat.append(x)

# 嵌套条件
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 只保留偶数
result = [x for row in matrix for x in row if x % 2 == 0]
print(result)  # [2, 4, 6, 8]
```

#### 元组推导式

Python中没有元组推导式。

#### 推导式 vs 循环

推导式通常比等效的 `for` 循环更快，也更简洁：

```python
# 推导式（推荐）
squares = [x**2 for x in range(10)]

# 等效的循环写法
squares = []
for x in range(10):
    squares.append(x**2)
```

> 注意：当逻辑过于复杂时，使用普通循环会更清晰易读

---

## 生成器(Generator)

### 生成器函数

```python
# Python识别到这个函数中包含yield的关键字，因此该函数是一个生成器函数。
def simple_generator():
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("结束")
    yield 3


g = simple_generator() # 生成器函数返回的是生成器，生成器是一个迭代器。
print(next(g))  # 开始
                # 1
print(next(g))  # 继续
                # 2
print(next(g))  # 结束
                # 3
# print(next(g))  # StopIteration!
```

可以利用生成器这种简易写法，快速完成迭代器的编写。

```python
def countdown(start):
    """生成器函数"""
    while start >= 0:
        yield start
        start -= 1


# 调用生成器函数，返回生成器
cd = countdown(5)
print(type(cd))       # <class 'generator'>

for n in cd:
    print(n, end=" ")  # 5 4 3 2 1 0
```

**生成器的特点：**

1. **惰性计算**：只在需要时生成值，不占用大量内存
2. **状态保存**：每次 `yield` 后暂停，下次从暂停处继续
3. **一次性**：和迭代器一样，只能遍历一次

### 链式调用

```python
def sub_generator():
    yield 1
    yield 2


def main_generator():
    yield "开始"
    for value in sub_generator():
        yield value
    yield "结束"


for value in main_generator():
    print(value)
# 开始
# 1
# 2
# 结束
```

可使用`yield from` 语法糖简化代码：

```python
def main_generator():
    yield "开始"
    yield from sub_generator()  # 委托给子生成器
    yield "结束"
```

### 发送数据

当调用生成器的`send`函数的时候，可以向生成器发送数据，该数据会导致`yield`的表达式返回对应的值。

```python
def calculator():
    total = 0
    while True:
        x = yield total  # yield 返回当前总数，并接收新值
        if x is None:
            break
        total += x

calc = calculator()
print(next(calc))      # 输出: 0 (启动)
print(calc.send(10))   # 输出: 10 (发送10，累加后返回)
print(calc.send(20))   # 输出: 30
print(calc.send(5))    # 输出: 35
```

### 生成器表达式

类似列表推导式，但使用圆括号，返回生成器：

```python
# 生成器表达式 —— 惰性计算，节省内存
squares_gen = (x**2 for x in range(1000000))

print(type(squares_gen))   # <class 'generator'>

# 按需获取值
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4
```

---



## itertools 简介

`itertools` 模块提供了许多高效的迭代器工具：

```python
import itertools

# count(start, step)：无限计数
counter = itertools.count(10, 2)
print(next(counter))  # 10
print(next(counter))  # 12
print(next(counter))  # 14

# cycle(iterable)：无限循环
cy = itertools.cycle(["A", "B", "C"])
print(next(cy))  # A
print(next(cy))  # B
print(next(cy))  # C
print(next(cy))  # A（重新开始）

# repeat(value, times)：重复值
times_three = list(itertools.repeat("x", 3))
print(times_three)  # ['x', 'x', 'x']

# chain(*iterables)：连接多个可迭代对象
combined = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(combined)  # [1, 2, 3, 4, 5, 6]

# islice(iterable, start, stop, step)：切片（支持无限迭代器）
first_five = list(itertools.islice(itertools.count(), 5))
print(first_five)  # [0, 1, 2, 3, 4]

# permutations(iterable, r)：排列
perms = list(itertools.permutations([1, 2, 3], 2))
print(perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations(iterable, r)：组合
combs = list(itertools.combinations([1, 2, 3, 4], 2))
print(combs)  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

---

## 作业(已完成)

先使用费曼学习法，复述迭代器、可迭代对象、生成器的概念和关系

### 一、实现扁平化迭代器

编写一个生成器函数 `flatten`，将嵌套的列表扁平化：

```python
def flatten(nested_list):
    # 你的代码
    pass


nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]
```

### 二、实现分页迭代器

编写一个生成器，模拟从数据库分页读取数据：

```python
def paginated_query(total_items, page_size):
    """
    模拟分页查询
    total_items: 总数据量
    page_size: 每页大小
    每次 yield 返回一页数据（列表）
    """
    # 你的代码
    pass


for page in paginated_query(25, 10):
    print(page)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
```

### 三、思考题

下面代码的输出是什么？为什么？

```python
def generator():
    print("准备 yield 1")
    yield 1
    print("准备 yield 2")
    yield 2
    print("准备 yield 3")
    yield 3
    print("生成器结束")


g = generator()
print("生成器已创建")
print(next(g))
print("---")
print(next(g))
print("---")
g.close()
print("生成器已关闭")
print(next(g))
```
# 上下文管理器

```python
with 表达式 as 变量名:
    代码块

# 等效于
变量名 = 表达式.__enter__()
try:
    代码块
except Exception as e:
    stopPropagation = 变量名.__exit__(type(e), e, e.__traceback__)
    if not stopPropagation:
        raise
else:
    变量名.__exit__(None, None, None)
```

带 `__enter__` 和 `__exit__` 方法的对象叫做**上下文管理器（Context Manager）**。

- **上下文管理器**是支持 `with` 语句的对象
- **必须同时实现**两个方法，否则 `with` 会报错

## 基本用法

```python
# 文件操作 —— 自动关闭文件
with open("data.txt", "r") as f:
    content = f.read()
    # 离开 with 块时，文件自动关闭

# 等价于
f = open("data.txt", "r")
try:
    content = f.read()
except Exception as e:
    stopPropagation = f.__exit__(type(e), e, e.__traceback__)
    if not stopPropagation:
        raise
else:
    f.__exit__(None, None, None)
```

## 自定义上下文管理器

实现 `__enter__` 和 `__exit__` 方法：

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connected = False

    def __enter__(self):
        """进入 with 块时调用，返回的对象赋值给 as 后的变量"""
        print(f"连接到数据库: {self.host}")
        self.connected = True
        return self  # 返回自身，供 with 块使用

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        离开 with 块时调用
        exc_type: 异常类型（无异常时为 None）
        exc_val: 异常值
        exc_tb: 异常追踪信息
        返回 True 表示异常已处理，不再向上传播
        """
        print(f"关闭数据库连接: {self.host}")
        self.connected = False
        return False  # 返回 False，不处理异常，让异常继续传播

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("未连接到数据库")
        print(f"执行查询: {sql}")
        return ["result1", "result2"]


# 使用上下文管理器
with DatabaseConnection("localhost") as conn:
    print(f"连接状态: {conn.connected}")  # True
    results = conn.query("SELECT * FROM users")
    print(results)

# 离开 with 块后
print(f"连接状态: {conn.connected}")  # False
```

## 异常处理

`__exit__` 方法可以处理或记录异常：

```python
class SuppressError:
    """忽略指定类型的异常"""
    
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            print(f"捕获并忽略异常: {exc_type.__name__}: {exc_val}")
            return True  # 返回 True，异常被处理，不再传播
        return False  # 不处理其他异常


# 使用
with SuppressError(ZeroDivisionError):
    result = 1 / 0  # 不会报错
    print("这行不会执行")

print("程序继续执行")  # 正常执行
```

---

## 使用 @contextmanager 装饰器

对于简单的上下文管理器，可以使用 `contextlib` 模块的 `@contextmanager` 装饰器，用生成器函数实现：

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    """用生成器实现上下文管理器"""
    print(f"获取资源: {name}")
    resource = {"name": name, "status": "active"}
    try:
        yield resource  # yield 之前的代码等价于 __enter__
    finally:
        print(f"释放资源: {name}")  # yield 之后的代码等价于 __exit__


# 使用
with managed_resource("database") as res:
    print(f"使用资源: {res}")
# 获取资源: database
# 使用资源: {'name': 'database', 'status': 'active'}
# 释放资源: database
```

**带异常处理的版本：**

```python
from contextlib import contextmanager

@contextmanager
def safe_file_write(file_path):
    """安全写入文件：先写入临时文件，成功后再替换原文件"""
    temp_path = file_path + ".tmp"
    try:
        f = open(temp_path, "w")
        yield f
        f.close()
        # 写入成功，替换原文件
        import os
        os.replace(temp_path, file_path)
        print("写入成功")
    except Exception as e:
        # 写入失败，清理临时文件
        f.close()
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"写入失败: {e}")
        raise  # 重新抛出异常


# 使用
with safe_file_write("data.txt") as f:
    f.write("Hello, World!\n")
```

---

## 多个上下文管理器

可以同时使用多个 `with`：

```python
# 嵌套写法
with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        fout.write(fin.read().upper())

# 简化写法（Python 3.1+）
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    fout.write(fin.read().upper())
```



## 作业（使用AI，已看懂）

### 一、实现代码块计时

```python
from contextlib import contextmanager

# 使用
with timer("数据处理"):
    import time
    time.sleep(1)
    print("处理完成")
# 处理完成
# 数据处理 耗时: 1.0012 秒
```



### 二、实现上下文管理器

编写一个 `TempDirectory` 上下文管理器，进入时创建临时目录，退出时自动删除：

```python
with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
```

**提示：** 使用 `tempfile` 模块创建临时目录，使用 `shutil.rmtree` 删除目录。

### ~~三、实现重试装饰器（结合上下文管理器思想）~~

~~编写一个上下文管理器 `retry`，在发生指定异常时自动重试：~~

==这道题有问题，上下文管理器无法实现retry功能，retry需要使用装饰器实现，见answers/p3-1.py==

### 四、思考题

下面代码的输出是什么？为什么？

```python
from contextlib import contextmanager

@contextmanager
def demo():
    print("进入")
    yield
    print("正常退出")


with demo():
    print("执行中")
    raise ValueError("出错了")
    print("这行不会执行")
```

如果改成下面的代码，输出会有什么不同？

```python
@contextmanager
def demo():
    print("进入")
    try:
        yield
    except Exception as e:
        print(f"捕获异常: {e}")
    finally:
        print("清理")


with demo():
    print("执行中")
    raise ValueError("出错了")
```

# 抽象类（Abstract Base Class）

抽象类是**不能被实例化**的类，用于定义子类**必须实现**的接口。Python 通过 `abc` 模块提供抽象类的支持。

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # 继承 ABC，表示这是一个抽象类
    @abstractmethod
    def speak(self):
        """子类必须实现这个方法"""
        pass

# animal = Animal()  # TypeError: 不能实例化抽象类

class Dog(Animal):
    def speak(self):  # 必须实现抽象方法
        print("Woof!")

dog = Dog()
dog.speak()  # Woof!
```

> 在vscode设置中，打开`python.analysis.typeCheckingMode`开关

## 定义抽象类

使用 `abc` 模块中的 `ABC` 类和 `@abstractmethod` 装饰器：

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算面积"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass

    def describe(self):
        """普通方法，子类可直接使用"""
        print(f"这是一个图形，面积: {self.area()}, 周长: {self.perimeter()}")
```

**要点：**

- 继承 `ABC` 表示这是一个抽象类
- `@abstractmethod` 标记的方法**必须**在子类中实现
- 抽象类可以包含普通方法（有默认实现）
- 抽象类**不能**被实例化

---

## 抽象属性

除了抽象方法，还可以定义抽象属性：

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        """子类必须实现 salary 属性"""
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self._monthly_salary = monthly_salary

    @property
    def salary(self):
        return self._monthly_salary

emp = FullTimeEmployee(10000)
print(emp.salary)  # 10000
```

**注意：** `@property` 和 `@abstractmethod` 的顺序**不能颠倒**。

---

## 子类必须实现所有抽象方法

如果子类没有实现所有抽象方法，它仍然是抽象类，不能被实例化：

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # 忘记实现 perimeter 方法

# rect = Rectangle(3, 4)  # TypeError: 不能实例化抽象类 Rectangle
```

---

## 实际应用场景

抽象类常用于定义**插件接口**或**框架扩展点**：

```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    """数据源抽象基类，所有数据源必须实现这些接口"""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def close(self):
        pass

class MySQLSource(DataSource):
    def connect(self):
        print("连接 MySQL")

    def read(self):
        return "MySQL 数据"

    def close(self):
        print("关闭 MySQL 连接")

class MongoDBSource(DataSource):
    def connect(self):
        print("连接 MongoDB")

    def read(self):
        return "MongoDB 数据"

    def close(self):
        print("关闭 MongoDB 连接")


def process_data(source: DataSource):
    """统一处理数据，不关心具体数据源"""
    source.connect()
    data = source.read()
    print(f"读取到: {data}")
    source.close()

# 使用不同的数据源
process_data(MySQLSource())
process_data(MongoDBSource())
```

---

## 作业（使用AI，已看懂）

### 一、实现抽象缓存类

编写一个抽象基类 `Cache`，定义缓存的基本接口，然后实现 `MemoryCache` 和 `FileCache`：

```python
from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

# 实现 MemoryCache（使用字典存储）
# 实现 FileCache（使用文件存储）
```

### 二、实现抽象序列类

编写一个抽象基类 `Sequence`，然后实现 `ListSequence` 和 `LinkedListSequence`：

```python
from abc import ABC, abstractmethod

class Sequence(ABC):
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_empty(self):
        return self.length() == 0

# 实现 ListSequence（基于 Python 列表）
# 实现 LinkedListSequence（基于链表）
```

### 三、思考题

下面代码的输出是什么？为什么？

```python
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def foo(self):
        pass

    def bar(self):
        print("A.bar")

class B(A):
    def foo(self):
        print("B.foo")

class C(B):
    pass

c = C()
c.foo()
c.bar()
```

如果改成下面的代码，会发生什么？

```python
class D(A):
    pass

d = D()
```

# 类型标注

> 现在开始，开启`python.analysis.typeCheckingMode`

## 为什么需要类型标注

```python
# 问题：参数类型不明确
def add(a, b):
    return a + b

# 调用者不知道应该传什么类型
add(1, 2)        # 3
add("1", "2")    # "12"  —— 这也是合法的，但可能不是预期行为
add([1], [2])    # [1, 2]  —— 同样合法

# 没有类型提示，难以在编码时发现错误
```

## 基础类型标注

### 变量类型标注

```python
# 声明变量的类型
name: str = "Alice"
age: int = 25
pi: float = 3.14
is_active: bool = True

# 没有初始值
value: int
value = 10

# Python 是动态语言，类型标注不会强制约束
x: int = "hello"  # 不会报错，但类型检查工具会提示
```

### 函数类型标注

```python
def greet(name: str, age: int) -> str:
    """函数参数和返回值的类型标注"""
    return f"{name} 今年 {age} 岁"


# 调用
greet("Alice", 25)        # 正确
greet("Alice", "25")      # 运行不会报错，但类型检查会警告
```

```python
from typing import NoReturn


def exit_program() -> NoReturn:
    """表示函数永远不会正常返回"""
    import sys
    sys.exit(1)
```

## 常用复合类型

### Optional 和 Union

```python
from typing import Optional, Union


# Optional：值可以是某个类型，也可以是 None
def find_user(user_id: int) -> Optional[str]:
    """返回用户名，找不到时返回 None"""
    if user_id <= 0:
        return None
    return f"User_{user_id}"


# Union：值可以是多种类型之一
def parse_value(value: str) -> Union[int, float, str]:
    """尝试将字符串转换为数字，失败则返回原字符串"""
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value
```

### 容器类型

```python
from typing import List, Dict, Tuple, Set


# 列表：元素类型
scores: List[int] = [85, 90, 78]
names: List[str] = ["Alice", "Bob", "Charlie"]


# 字典：键类型, 值类型
student_scores: Dict[str, int] = {
    "Alice": 85,
    "Bob": 90,
}


# 元组：固定长度，每个位置类型可不同
point: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Alice", 25, True)


# 集合：元素类型
tags: Set[str] = {"python", "typing", "type-hints"}
```

### Any 和 类型别名

```python
from typing import Any, TypeAlias


# Any：任意类型，相当于没有类型约束
def log_data(data: Any) -> None:
    print(f"数据: {data}")


# 类型别名，让复杂类型更易读
Vector: TypeAlias = List[float]
Matrix: TypeAlias = List[List[float]]


def dot_product(v1: Vector, v2: Vector) -> float:
    """计算两个向量的点积"""
    return sum(a * b for a, b in zip(v1, v2))
```

## 类与自定义类型

```python
from typing import Self


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float) -> Self:
        """返回移动后的新点"""
        return Point(self.x + dx, self.y + dy)

    def distance_to(self, other: "Point") -> float:
        """计算到另一个点的距离"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 使用
p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))  # 5.0
```

## 泛型

```python
from typing import TypeVar, Generic


T = TypeVar("T")


class Stack(Generic[T]):
    """泛型栈，可以存储任意类型的元素"""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("栈为空")
        return self._items.pop()

    def peek(self) -> T | None:
        if not self._items:
            return None
        return self._items[-1]


# 使用
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
# str_stack.push(123)  # 类型检查会警告
```

## Callable 和 回调函数

```python
from typing import Callable


def execute_callback(
    callback: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    """执行回调函数"""
    return callback(a, b)


# 使用
result = execute_callback(lambda x, y: x + y, 3, 5)
print(result)  # 8
```

## 应用场景

### 1. API 接口定义

```python
from typing import TypedDict


class UserResponse(TypedDict):
    """API 返回的用户数据结构"""
    id: int
    name: str
    email: str
    is_active: bool


def get_user(user_id: int) -> UserResponse:
    return {
        "id": user_id,
        "name": "Alice",
        "email": "alice@example.com",
        "is_active": True,
    }
```

### 2. 配合 IDE 获得智能提示

类型标注让 IDE 可以提供：
- 自动补全
- 参数提示
- 类型错误高亮

```python
class Database:
    def connect(self, host: str, port: int = 5432) -> "Connection":
        ...

    def query(self, sql: str) -> list[dict[str, Any]]:
        ...


db = Database()
conn = db.connect("localhost")  # IDE 会提示 port 参数
```

## 忽略类型检查

有时某些代码难以标注或不需要检查，可以使用 `# type: ignore` 忽略：

```python
# 忽略整行的类型检查
data = some_dynamic_library.load()  # type: ignore

# 有具体错误码时，可以指定忽略特定错误
x: int = "hello"  # type: ignore[assignment]
```

**注意：** 应该尽量少用，只在必要时使用

---

## 作业（可使用AI，已看懂）

### 一、为函数添加类型标注

为以下函数添加合适的类型标注：

```python
def calculate_bmi(weight, height):
    """计算 BMI 指数"""
    if height <= 0:
        raise ValueError("身高必须大于0")
    return weight / (height ** 2)


def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

### 二、实现泛型缓存

```python
from typing import TypeVar, Generic, Optional

K = TypeVar("K")
V = TypeVar("V")


class Cache(Generic[K, V]):
    """泛型缓存类"""
    
    def __init__(self) -> None:
        # 你的代码
        pass
    
    def set(self, key: K, value: V) -> None:
        """设置缓存"""
        # 你的代码
        pass
    
    def get(self, key: K) -> Optional[V]:
        """获取缓存，不存在返回 None"""
        # 你的代码
        pass
    
    def clear(self) -> None:
        """清空缓存"""
        # 你的代码
        pass


# 测试
cache: Cache[str, int] = Cache()
cache.set("a", 1)
cache.set("b", 2)
print(cache.get("a"))   # 1
print(cache.get("c"))   # None
cache.clear()
```

### 三、定义配置类

使用 `TypedDict` 定义应用配置结构：

```python
from typing import TypedDict, Optional


class DatabaseConfig(TypedDict):
    """数据库配置"""
    # 你的代码：包含 host(str), port(int), username(str), password(str), database(str)


class AppConfig(TypedDict):
    """应用配置"""
    # 你的代码：包含 app_name(str), debug(bool), db(DatabaseConfig)


def load_config() -> AppConfig:
    """加载默认配置"""
    return {
        "app_name": "MyApp",
        "debug": False,
        "db": {
            "host": "localhost",
            "port": 5432,
            "username": "admin",
            "password": "secret",
            "database": "mydb",
        }
    }
```

### 四、思考题

下面代码的类型标注是否正确？如果不正确，如何修改？

```python
from typing import List, Dict


def process_data(items: List) -> Dict:
    """处理数据项"""
    result = {}
    for item in items:
        result[item["id"]] = item["value"]
    return result


def find_max(a: int, b: int) -> int | None:
    """返回较大的数"""
    if a == b:
        return None
    return a if a > b else b
```



