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
# Python基础
## Python环境搭建

### 语言分类：

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

### Python安装包

Python安装包中包含以下核心组件：

- 解释器：默认为`CPython` （解释器用C语言写的）
- 包管理器：`pip`
- 标准库：`os、sys、urllib、pathlib、...`
- 交互式终端：`REPL`
  - 例如前端的交互式窗口，在终端输入node，进入的环境就是交互式终端
  - python也一样，在终端输入python后，进入的环境

#### Python发行版

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

#### Python版本管理器

##### pyenv

使用`pyenv`来管理多个`python`版本

###### mac 安装 pyenv

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

###### win 安装 pyenv

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

#### pyenv 使用

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

### IDE

* [PyCharm](https://www.jetbrains.com/pycharm/): Python 专属 IDE，开箱即用，专为 Python 设计，官方内置了 python 开发的诸多功能。
* [VSCode](https://code.visualstudio.com/download)： 通用代码编辑器，装插件才支持 Python，全能型。

选择哪个其实无所谓

本课程选择使用`VSCode`，理由：

1. 全栈开发**尽量**统一编辑器，减少心智负担
2. `VSCode`体系对`AI Coding`支持更友好
3. 轻量高效、启动速度快，低配电脑也能流畅使用

#### VSCode插件

安装好`VSCode`后，依次安装以下插件

* **Python**
  * 作用：语法高亮、代码提示、运行调试、虚拟环境识别，**最核心**。
* **Code Runner**
  * 作用：方便调试代码,右键一键运行Python代码，不用敲命令，新手超好用。
* **Black Formatter**自动格式化代码，统一代码风格，不用手动排版。
* **Chinese**VSCode界面汉化，零基础友好。

#### VSCode配置

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

### 作业（已完成）

#### hello world的py代码输出

## Python基本语法

### 语言基本特征

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

### 注释

    # 这是单行注释
    
    """
    这是多行注释
    可以写多行
    """
    
    '''
    这也是多行注释
    可以写多行
    '''

### 数据类型

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



### type函数

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



### 变量

#### 变量定义

Python是动态类型语言，变量无需声明类型，直接赋值即可创建。

```python
# 变量赋值
name = "Alice"      # 字符串
age = 25            # 整数
pi = 3.14159        # 浮点数
is_valid = True     # 布尔值
```

#### 变量命名规则

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

#### 命名规范

| 类型                                   | 规范                     | 示例                         |
| ------------------------------------ | ---------------------- | -------------------------- |
| 变量名                                  | 小写字母，下划线分隔（snake_case） | `user_name`, `total_count` |
| 常量名(py实际不存在常量，只是命名上通过这样来区分，一种规范，软约束) | 全大写字母，下划线分隔            | `MAX_SIZE`, `PI`           |
| 类名                                   | 首字母大写的驼峰命名（PascalCase） | `UserInfo`, `DataModel`    |
| 私有变量                                 | 以下划线开头                 | `_internal`, `__private`   |

#### 多重赋值

```python
# 同时赋值多个变量
a, b, c = 1, 2, 3

# 交换变量值
x, y = 10, 20
x, y = y, x  # x=20, y=10

# 相同值赋给多个变量
a = b = c = 0  # a=0, b=0, c=0
```



#### 变量类型转换

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

### 字符串格式化（f-string）

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

### 运算符

#### 算术运算符

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

#### 比较运算符

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

#### 链式比较

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

#### 赋值运算符

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

#### 海象运算符（:=）

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

#### 逻辑运算符

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

#### 三元运算符（条件表达式）

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



### 输入输出

#### print输出

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

#### input输入

```python
# 接收用户输入，返回字符串类型
name = input("请输入你的名字: ")
print("你好,", name)

# input返回的是字符串
age_str = input("请输入年龄: ")
age = int(age_str)  # 需要转换为整数
print("明年你", age + 1, "岁")
```

### 流程控制

#### 条件判断

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

#### pass占位符

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

#### 循环

##### while循环

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

##### 循环控制语句

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

##### 循环else子句

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

### 作业(已完成)

#### 作业一：代码输出结果预测

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

#### 作业二：循环与判断代码输出预测

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

#### 作业三：BMI 计算器

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

#### 作业四：素数筛选器

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

## Python容器类型

### 什么是容器类型

容器类型用于**存储多个数据**。Python中内置的容器类型包括：

| 类型      | 名称  | 是否可变 | 是否有序            | 元素是否可重复 | 示例                 | 备注                |
| ------- | --- | ---- | --------------- | ------- | ------------------ | ----------------- |
| `list`  | 列表  | 可变   | 有序              | 可重复     | `[1, 2, 2, 3]`     | 内部采用动态数组实现        |
| `tuple` | 元组  | 不可变  | 有序              | 可重复     | `(1, 2, 3)`        | 内部采用静态数组实现        |
| `dict`  | 字典  | 可变   | 有序（Python 3.7+） | 键不可重复   | `{"a": 1, "b": 2}` | 键值对，内部使用hashmap实现 |
| `set`   | 集合  | 可变   | 无序              | 不可重复    | `{1, 2, 3}`        | 内部使用hashset实现     |
| `str`   | 字符串 | 不可变  | 有序              | 可重复     | `"hello"`          |                   |

> **注意：** `str` 也可以视为一种不可变的有序字符序列，本节会穿插涉及。

### 列表（list）

列表是Python中最常用的**可变、有序**容器，可以存储任意类型的元素。

#### 创建列表

```python
# 字面量创建
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
empty = []  # 空列表

# 通过list()函数创建
chars = list("abc")      # ['a', 'b', 'c']
nums2 = list((1, 2, 3))  # [1, 2, 3]
```

#### 索引与切片

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

#### 列表操作

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

### 元组（tuple）

元组是**不可变**的有序序列，一旦创建就不能修改。

#### 创建元组

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

#### 基本操作

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

#### 元组解包

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

### 字典（dict）

字典是Python的**键值对**存储结构，通过键快速查找值。

#### 创建字典

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

#### 访问与修改

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

#### 重要注意事项

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

### 集合（set）

集合是**无序、不重复**的元素集合，支持数学上的集合运算。

#### 创建集合

```python
# 字面量创建
nums = {1, 2, 3, 3, 3}   # {1, 2, 3} —— 自动去重
empty = set()             # 空集合！不是 {}（那是空字典）

# 通过set()函数创建
nums = set([1, 2, 2, 3])  # {1, 2, 3}
chars = set("hello")      # {'h', 'e', 'l', 'o'}
```

#### 集合操作

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

### 容器操作

#### 通用操作函数

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

#### 常用运算符

##### 成员运算符：`in` / `not in`

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



##### 连接与重复运算符

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

##### 相等运算符：`==` / `!=`

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

##### 身份运算符：`is` / `is not`

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

##### 位运算符：`&`、`|`、`^`、`~`

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

#### 遍历容器

##### 基本 for 循环

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

##### 遍历字典

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

##### 遍历集合

```python
s = {1, 2, 3}
for item in s:
    print(item)
# 注意：集合是无序的，遍历顺序不固定
```

##### `enumerate()` 函数

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

##### `zip()` 函数

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

### 作业(已完成)

#### 作业一：列表与身份运算符综合

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

#### 作业二：元组、集合与成员运算符综合

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

#### 作业三：字典与遍历综合

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



#### 作业四：字符串操作与循环综合

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

#### 作业五：enumerate、zip与多容器综合

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

#### 作业六：学生信息处理综合练习

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

## Python函数

函数是**可复用**的代码块，用于封装特定功能。通过定义函数，可以避免重复代码，提高程序的可读性和可维护性。

* * *

### 定义函数

使用 `def` 关键字定义函数：

```python
# 定义一个简单函数
def greet():
    print("Hello, World!")

# 调用函数
greet()  # Hello, World!
```



* * *

### 参数

#### 位置参数

按照定义时的**顺序**传递参数：



```python
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 8
```

#### 默认参数

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

#### 关键字参数

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

#### 可变参数

##### `*args` —— 接收任意数量的位置参数

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

##### `**kwargs` —— 接收任意数量的关键字参数

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

#### 参数顺序规则

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

### 返回值

#### 使用 return

函数通过 `return` 返回结果：

```python
def square(x):
    return x ** 2
result = square(4) \
print(result) # 16
```

#### 多返回值

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

#### 没有 return

如果函数没有 `return`，默认返回 `None`：

```python
def say_hello():
    print("Hello")

result = say_hello()  # Hello
print(result)         # None
```

### 文档字符串（Docstring）

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

### 作业

#### 作业一：函数参数与列表操作综合

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



#### 作业二：关键字参数与字典操作综合

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

#### 作业三：多返回值与容器遍历综合

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

#### 作业四：函数综合编程

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

## Python作用域

作用域（Scope）决定了程序中变量和名字的**可见范围**。理解作用域能帮助你预测代码的执行结果，避免变量名冲突。

---

### LEGB 规则

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

### 局部作用域（Local）

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

### 全局作用域（Global）

模块级别（文件最外层）定义的变量：

```python
count = 0             # 全局变量

def increment():
    print(count)      # 读取全局变量，OK

increment()  # 0
```

#### 在函数内修改全局变量

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

### 闭包作用域（Enclosing）

嵌套函数中，内层函数可以访问外层函数的变量：

```python
def outer():
    x = "outer"       # 外层函数的局部变量
    
    def inner():
        print(x)      # 访问外层变量
    
    inner()

outer()  # outer
```

#### 修改外层变量

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

### 常见错误

#### 错误 1：在函数内同时读写全局变量

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

#### 错误 2：默认参数的陷阱

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

### 作用域速查

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

### 作业(已完成)

#### 作业一：作用域判断

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

#### 作业二：global 与 nonlocal

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

#### 作业三：修复代码

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

#### 作业四：闭包计数器

实现一个函数 `make_multiplier(n)`，返回一个函数。返回的函数接收一个参数 `x`，返回 `n * x`。

要求使用闭包实现，不要使用 `global`。

```python
triple = make_multiplier(3)
print(triple(5))   # 15
print(triple(10))  # 30

double = make_multiplier(2)
print(double(7))   # 14
```

#### 作业五：综合练习

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
## Lambda表达式

Lambda表达式用于创建**匿名函数**——即没有名称的临时函数。当你需要一个简单函数且只用一次时，lambda能让代码更简洁。

---

### 基本语法

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

### Lambda vs 普通函数

| 特性 | Lambda | 普通函数 (`def`) |
|------|--------|------------------|
| 名称 | 匿名（通常无名字） | 有函数名 |
| 函数体 | 只能有一个表达式 | 可以有多条语句 |
| 返回值 | 自动返回表达式结果 | 需要显式 `return` |
| 适用场景 | 临时、简单的逻辑 | 复杂、复用的逻辑 |

**原则：** 逻辑简单且只用一次 → 用lambda；逻辑复杂或需要复用 → 用`def`。

---

### 应用场景：内置高阶函数

高阶函数是指接收函数作为参数的函数。这是lambda最经典的使用场景。

#### `map()` — 映射

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

#### `filter()` — 过滤

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

#### `sorted()` — 排序（指定key）

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

#### `max()` / `min()` — 极值（指定key）

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

#### `reduce()` — 累积计算

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

### 作业（已完成）

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

## Python类和对象

Python 是一门**面向对象**的编程语言。类（Class）是创建对象的蓝图，而对象（Object）是类的具体实例。通过类和对象，可以将数据（属性）和行为（方法）封装在一起，使代码更具结构性和可复用性。

---

### 定义类

使用 `class` 关键字定义类：

```python
class Dog:
    pass

# 创建实例
my_dog = Dog()
print(type(my_dog))  # <class '__main__.Dog'>
```

#### 使用 `type()` 动态定义类

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

### 构造方法 `__init__`

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

### 实例属性与类属性

#### 实例属性

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
#### 类属性

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
### 实例方法

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

### 类方法与静态方法

#### 类方法 `@classmethod`

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

#### 静态方法 `@staticmethod`

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
### 继承

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

#### 调用父类方法

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

#### 多继承

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

##### 方法解析顺序（MRO）

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

##### `super()` 在多继承中的行为

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

### 访问控制

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
### 常见操作

#### 内置属性

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

#### `type()`

返回对象的类型（对象是通过哪个类创建的：

```python
dog = Dog("Buddy")

print(type(dog))       # <class '__main__.Dog'>
print(type(Dog))       # <class 'type'>
print(type(123))       # <class 'int'>
print(type("hello"))   # <class 'str'>
```

---

#### `isinstance()`

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

#### `issubclass()`

判断一个类是否是另一个类的子类：

```python
print(issubclass(Dog, Animal))   # True
print(issubclass(Dog, Dog))      # True（类是自己的子类）
print(issubclass(Animal, Dog))   # False

# 支持元组
print(issubclass(Dog, (Animal, str)))  # True
```

---

#### `dir()`

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

#### `vars()`

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

#### `getattr()`

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

#### `setattr()`

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

#### `hasattr()`

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

#### `delattr()`

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
### 作业(已完成)

#### 一、腾讯面试题

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

#### 二、综合预测题

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

#### 三、实现链表类

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

## 对象的类型

### 知识补充

#### 使用 `type()` 动态定义类

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

#### MRO

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

#### 类中的私有成员

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

### 对象的类型

所有的对象都是通过类创建的，创建对象的类，称之为该对象的类型（也有所属类的说法）

可以使用`type(对象)`得到某个对象的类型



![基础类.excalidraw](https://resource.duyiedu.com/yuanjin/202605181745106.svg)

- 所有函数的类型是`function`（类的方法类型是method,method内部包装了一层function,所以还是认为是function）
- 所有类的类型是`type`
- **创建类的类，称之为元类（metaclass）**

> 见`demo1.py`的打印结果

### 成员的查找顺序

**类成员的查找顺序**

1. 查找自身的MRO链条
2. 查找元类的MRO链条



**其他实例的查找顺序**

1. 查找自身
2. 查找类型的MRO链条

### 作业(已完成)

#### 使用费曼学习法，复述本节课内容

#### 说出代码的查看结果

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

## 对象的创建过程

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

### 应用场景

理解对象的创建过程后，我们可以通过重写 `__new__` 和 `__init__` 来实现多种设计模式。

#### 1. 单例模式

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

#### 2. 对象池/缓存

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

#### 3. 正整数（带默认值回退）

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

### 作业（已完成）

自己写一遍：单例模式

## 可调用对象

在 Python 中，**可调用对象（Callable）**是指可以像函数一样使用括号 `()` 调用的对象。

### 如何判断对象是否可调用

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

### 让对象变成可调用对象

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

### 实际应用场景

#### 1. 实现可配置的函数对象

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

#### 2. 实现状态保持的回调函数

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

### 作业（已完成）

#### 一、实现一个计数器类

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

#### 二、思考题

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
## 元类



### 类的创建过程

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

### 自定义元类

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

### 深入：元类的查找顺序

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



### 总结

| 概念 | 说明 |
| ---- | ---- |
| 元类 | 创建类的类，默认是 `type` |
| `__new__` | 创建类，返回类对象 |
| `__init__` | 初始化类，无返回值 |
| `__call__` | 控制类的实例化过程 |
| 应用场景 | 命名检查、自动注册、方法增强、ORM 等 |

---

### 作业（已完成）

#### 一、实现单例元类

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

#### 二、自动注册子类

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

#### 三、为所有方法添加日志

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

## 装饰器



### 装饰器的本质

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



### 多个装饰器叠加

可以同时使用多个装饰器，执行顺序为从下到上：

```python
@decorator_a
@decorator_b
def func():
    pass

# 等效于：
# func = decorator_a(decorator_b(func))
```

### 作业（已完成）

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

#### 一、实现timer装饰器

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



#### 二、实现wraps装饰器

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

#### 三、实现repeat装饰器

```python
def repeat(n):
    # 你的代码
    pass


@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1
```

#### 四、实现cache装饰器

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



#### 五、实现to_dict装饰器

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
## 魔术方法

魔术方法（Magic Methods）是 Python 中**以双下划线开头和结尾**的特殊方法，如 `__init__`、`__str__`。它们不需要显式调用，而是由 Python 在特定场景下**自动触发**。

### 字符串表示

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

### 比较操作

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

### 算术运算

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

### 容器协议

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

### 类型转换

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

### 属性访问拦截

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

#### `__getattr__` vs `__getattribute__`

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

### 对象生命周期

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

### 常用魔术方法速查

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

### 作业（可使用AI、未实现，直接看的答案）

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


## 描述符

### 问题

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

### 描述符协议

#### 认识术语

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

#### 访问顺序

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

#### 读写删操作

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

#### 钩子函数

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

### 解决最初的问题

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



### @property 装饰器

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



### 应用场景

#### 1. 惰性计算

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

#### 2. 类型检查

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

### 作业（可使用AI，已看懂）

#### 一、实现只读属性

编写一个类 `ImmutablePoint`，创建后不能修改坐标：

```python
p = ImmutablePoint(3, 4)
print(p.x)      # 3
print(p.y)      # 4

# p.x = 10      # AttributeError! 不能修改只读属性
```

**提示：** 使用 `@property` 但不提供 setter。

#### 二、实现范围验证

编写一个 `Temperature` 类，温度必须在 -273.15（绝对零度）到 1000 之间：

```python
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0（只读属性，自动计算）
print(t.kelvin)       # 298.15（只读属性，自动计算）

# t.celsius = -300    # ValueError! 温度不能低于绝对零度
```

#### 三、实现类属性计数器

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

#### 四、思考题

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
## 异常处理

### 异常的捕获

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

### 异常类型

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



### 主动抛出异常

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

### 自定义异常

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



### 异常链

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

### 作业（可使用AI，已看懂）

#### 一、实现安全的除法函数

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

#### 二、实现重试装饰器

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

#### 三、自定义异常与验证

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

#### 四、异常转换

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

## 迭代器与生成器

### 迭代器(Iterator)

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



#### 应用：无限序列

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



### 可迭代对象(Iterable)

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

#### 示例：倒数对象

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



#### 消费者

##### 1. `for`循环

```python
# for 循环会自动调用 iter() 和 next()
for n in Countdown(3):
    print(n)  # 3 2 1 0
```

##### 2. **`list()`、`tuple()`、`set()` 等构造函数**

```python
print(list(Countdown(3)))  # [3, 2, 1, 0]
print(tuple(Countdown(3)))  # (3, 2, 1, 0)
print(set(Countdown(3)))  # {0, 1, 2, 3}
```

##### 3. **`*` 解包操作符**

```python
first, *rest = Countdown(3)
print(first)  # 3
print(rest)   # [2, 1, 0]

# 或用列表解包
values = [*Countdown(3)]
print(values)  # [3, 2, 1, 0]
```

##### 4. **`in` 成员判断**

```python
print(5 in Countdown(3))   # False
print(2 in Countdown(3))   # True
```

##### 5. **`sum()`、`max()`、`min()` 等内置函数**

```python
print(sum(Countdown(3)))  # 6
print(max(Countdown(3)))  # 3
print(min(Countdown(3)))  # 0
```

##### 6. **`zip()`、`map()`、`filter()` 等函数**

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

##### 7. **`any()`、`all()`**

```python
numbers = Countdown(3)
print(any(numbers))  # True (至少一个为真)
print(all(numbers))  # False (是否所有都为真)
```

#### range函数

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

#### 推导式

推导式(Comprehension)是一种简洁的语法，用于从一个可迭代对象创建新的列表、字典或集合。

##### 列表推导式

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

##### 字典推导式

```python
# 基本语法：{键表达式: 值表达式 for 变量 in 可迭代对象}
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 带条件过滤
odd_squares = {x: x**2 for x in range(10) if x % 2 != 0}
print(odd_squares)  # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

##### 集合推导式

```python
# 基本语法：{表达式 for 变量 in 可迭代对象}
square_set = {x**2 for x in range(10)}
print(square_set)  # {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

# 带条件过滤
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

##### 嵌套推导式

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

##### 元组推导式

Python中没有元组推导式。

##### 推导式 vs 循环

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

### 生成器(Generator)

#### 生成器函数

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

#### 链式调用

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

#### 发送数据

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

#### 生成器表达式

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



### itertools 简介

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

### 作业(已完成)

先使用费曼学习法，复述迭代器、可迭代对象、生成器的概念和关系

#### 一、实现扁平化迭代器

编写一个生成器函数 `flatten`，将嵌套的列表扁平化：

```python
def flatten(nested_list):
    # 你的代码
    pass


nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]
```

#### 二、实现分页迭代器

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

#### 三、思考题

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
## 上下文管理器

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

### 基本用法

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

### 自定义上下文管理器

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

### 异常处理

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

### 使用 @contextmanager 装饰器

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

### 多个上下文管理器

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



### 作业（使用AI，已看懂）

#### 一、实现代码块计时

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



#### 二、实现上下文管理器

编写一个 `TempDirectory` 上下文管理器，进入时创建临时目录，退出时自动删除：

```python
with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件
    # 离开 with 块时，目录及其内容自动删除

print("临时目录已清理")
```

**提示：** 使用 `tempfile` 模块创建临时目录，使用 `shutil.rmtree` 删除目录。

#### ~~三、实现重试装饰器（结合上下文管理器思想）~~

~~编写一个上下文管理器 `retry`，在发生指定异常时自动重试：~~

==这道题有问题，上下文管理器无法实现retry功能，retry需要使用装饰器实现，见answers/p3-1.py==

#### 四、思考题

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

## 抽象类（Abstract Base Class）

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

### 定义抽象类

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

### 抽象属性

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

### 子类必须实现所有抽象方法

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

### 实际应用场景

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

### 作业（使用AI，已看懂）

#### 一、实现抽象缓存类

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

#### 二、实现抽象序列类

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

#### 三、思考题

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

## 类型标注

> 现在开始，开启`python.analysis.typeCheckingMode`

### 为什么需要类型标注

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

### 基础类型标注

#### 变量类型标注

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

#### 函数类型标注

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

### 常用复合类型

#### Optional 和 Union

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

#### 容器类型

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

#### Any 和 类型别名

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

### 类与自定义类型

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

### 泛型

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

### Callable 和 回调函数

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

### 应用场景

#### 1. API 接口定义

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

#### 2. 配合 IDE 获得智能提示

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

### 忽略类型检查

有时某些代码难以标注或不需要检查，可以使用 `# type: ignore` 忽略：

```python
# 忽略整行的类型检查
data = some_dynamic_library.load()  # type: ignore

# 有具体错误码时，可以指定忽略特定错误
x: int = "hello"  # type: ignore[assignment]
```

**注意：** 应该尽量少用，只在必要时使用

---

### 作业（可使用AI，已看懂）

#### 一、为函数添加类型标注

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

#### 二、实现泛型缓存

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

#### 三、定义配置类

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

#### 四、思考题

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
## 模块化

### 包、模块、成员关系

![relation.excalidraw](https://resource.duyiedu.com/yuanjin/202605251100825.svg)

### 定义模块（导出）

创建一个 `.py` 文件，就是在**定义**一个模块。文件顶层的所有定义（变量、函数、类）就是这个模块**导出**的内容：

```python
# my_math.py —— 这就是一个模块，文件名叫 my_math.py，模块名就是 my_math

pi: float = 3.14159  # 导出变量


def add(a: int, b: int) -> int:  # 导出函数
    return a + b


class Calculator:  # 导出类
    def multiply(self, a: int, b: int) -> int:
        return a * b
```

**要点：**
- 文件名即模块名（去掉 `.py`）
- 文件顶层的**变量、函数、类**都是模块的导出成员
- 在函数/类**内部**定义的内容不是导出成员（外部无法访问）

#### 私有成员约定

Python 没有真正的私有机制，但用**下划线开头**表示"内部实现，外部不应直接使用"：

```python
# my_math.py

PI: float = 3.14159  # 公开


def add(a: int, b: int) -> int:  # 公开
    return a + b


def _internal_helper(a: int) -> int:  # "私有"——约定外部不应使用
    return a * 2
```

`from module import *` 时，下划线开头的成员**不会**被导入。

#### 使用 `__all__` 控制导出清单

`__all__` 明确指定哪些成员是公开 API：

```python
# my_math.py

__all__: list[str] = ["PI", "add"]  # 只导出 PI 和 add


PI: float = 3.14159
E: float = 2.71828  # 没有在 __all__ 中，from import * 不会导入


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:  # 不在 __all__ 中
    return a - b
```

**`__all__` 的作用：**
1. 控制 `from my_math import *` 导入哪些成员
2. **作为模块的"文档"，告诉使用者哪些是稳定 API**
3. 和一些其他工具配合

#### 模块的 `__name__` 与直接运行

每个模块都有一个内置属性 `__name__`：
- 直接运行时：`__name__ == "__main__"`
- 被导入时：`__name__ == 模块名`

利用这个特性，可以在模块中写测试代码，只有直接运行时才执行：

```python
# my_math.py

__all__: list[str] = ["PI", "add"]


PI: float = 3.14159


def add(a: int, b: int) -> int:
    return a + b


# 以下代码只有在 python my_math.py 直接运行时才执行
# 作为模块被导入时不会执行
if __name__ == "__main__":
    print(add(3, 5))  # 8
    print(add(-1, 1))  # 0
```

---

### 导入模块

Python在**运行时**动态导入

#### import 语句

```python
import my_math  # 导入整个模块

print(my_math.PI)  # 通过模块名访问
print(my_math.add(3, 5))

from my_math import PI, add  # 只导入需要的成员

print(PI)
print(add(3, 5))

from my_math import *  # 导入 __all__ 中列出的成员（谨慎使用）

print(PI)
print(add(3, 5))
# subtract 不在 __all__ 中，不会导入

import my_math as mm  # 模块别名
from my_math import add as my_add  # 成员别名

print(mm.PI)
print(my_add(3, 5))
```

#### 模块的动态导入

```python
import importlib

# 模块名来自变量
module_name = "math"
math = importlib.import_module(module_name)
print(math.sqrt(16))  # 4.0

# 来自用户输入
user_input = "json"
module = importlib.import_module(user_input)
data = module.dumps({"key": "value"})

# 动态导入子模块
submodule = importlib.import_module("os.path")
print(submodule.join("a", "b"))  # a/b
```



#### 模块的执行与缓存

模块在**首次导入**时**执行一次**，后续导入使用缓存，不会重复执行：

```python
import my_math  # 第一次导入：执行 my_math.py
import my_math  # 第二次导入：使用缓存，不执行
import my_math  # 第三次导入：使用缓存，不执行
```

缓存存储在 `sys.modules` 中：

```python
import sys

# 查看已加载的所有模块
print("math" in sys.modules)  # True（因为 math 已被导入）
print(my_math in sys.modules.values())  # True
```

---

### 包（Package）

只要一个目录中包含`__init__.py`模块，Python就会将该目录其视为一个包

#### `__init__.py` 的作用

`__init__.py` 是包的初始化文件，它在第一次导入该包的时候会自动运行，你可以：
1. **组织导出接口** —— 在包级别暴露子模块的成员
2. **包级别的初始化** —— 连接数据库、加载配置等

```python
# utils/__init__.py

__all__: list[str] = ["add", "subtract", "to_upper", "reverse"]

from .math_ops import add, subtract
from .string_ops import to_upper, reverse
```

---

### 相对导入

包内部的模块可以通过相对导入引用兄弟模块：

```
project/
├── main.py
└── utils/
    ├── __init__.py
    ├── math_ops.py
    └── string_ops.py
```

```python
# utils/string_ops.py
from .math_ops import add  # . 表示当前包（utils）


def add_and_reverse(a: int, b: int) -> str:
    result: int = add(a, b)
    return reverse(str(result))
```

相对导入符号：
- `.`  —— 当前包
- `..` —— 父包
- `...` —— 祖父包

**限制：** 相对导入**不能**用于直接运行的模块，只用于包内模块被导入时。

---

### 搜索路径

`import` 语句按以下顺序搜索模块：

1. 内置模块，如：`sys`
   ```python
   import sys
   
   print(sys.builtin_module_names) # 查看所有内置模块
   ```
2. `sys.path`

   1. 当前脚本所在目录
   2. `PYTHONPATH` 环境变量中的路径
   3. Python 内置模块
   4. 第三方包（`site-packages`）


```python
import sys

# 查看模块搜索路径
for path in sys.path:
    print(path)
```

---

### 循环导入问题

```python
# a.py
from b import bar

def foo() -> str:
    return bar()

# b.py —— 此时 a.py 还没执行完，foo 还不存在
from a import foo  # ImportError

def bar() -> str:
    return "bar"
```

**解决方案：**
1. 将公共代码抽到第三个模块
2. 延迟导入（在函数内部导入）

---

### 作业（已完成）

#### 复述

使用费曼学习法，复述：

1. 包、模块、成员关系
2. `__all__`的作用
3. `__init__.py`的作用
4. python对模块或包的搜索是怎样的

#### 学习`__slots__`

查询`python`中`__slots__`的作用
**总结：**
**1.限制类的实例去动态属性添加**
```python
class Person:
    __slots__ = ['name', 'age']  # 只允许 name 和 age
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
p.city = "NYC"  # ❌ AttributeError: 'Person' object has no attribute 'city'
```
**2.节省内存**
普通实例使用 __dict__ 字典存储属性，字典本身占用较大内存（哈希表）
__slots__ 使用固定大小的数组存储属性引用，内存占用显著减少
**3.提升访问速度**
由于不需要通过字典查找（没有__dict__属性了），__slots__ 的属性访问速度略快（约 10-15%）
**4.继承行为**
子类的__slot__会与父类的__slot__做合并
子类没有定义__slot__,父类有__slot__，则子类还是没有__slot__属性，可以动态添加
```python
class Parent:
    __slots__ = ['x']

class Child(Parent):
    __slots__ = ['y']  # 子类的 slots 会与父类合并
    
c = Child()
c.x = 1  # ✅ 允许
c.y = 2  # ✅ 允许
c.z = 3  # ❌ 不允许
```
## 标准库

官方手册：

- 按功能：https://docs.python.org/zh-cn/3.14/library/index.html
- 按名称：https://docs.python.org/zh-cn/3/py-modindex.html

包含：

- 内置API
- 内置模块
- 标准库

### 作业（使用AI，已看懂）

#### 作业一：树形目录展示

编写一个函数 `show_tree(dir_path: str, show_hidden: bool = False)`，接收两个参数：

- `dir_path`：目录路径，可以是绝对路径或相对路径（相对当前工作目录 CWD）
- `show_hidden`：布尔类型，表示是否显示隐藏文件/目录

  隐藏判断简单处理：文件或目录只要以`.`开头，则视为隐藏文件或目录，否则的话视为可视。

函数的功能是用树形递归的方式展示指定目录下的所有内容。效果类似于 Linux 的 `tree` 命令。

输出格式参考如下：
```
.
├── file1.txt
├── dir1
│   ├── file2.txt
│   └── file3.txt
└── file4.txt
```

#### 作业二：Markdown 文件合并

编写一个函数 `merge_markdown(files: list[str], output: str) -> None`，接收两个参数：

- `files`：Markdown 文件路径列表
- `output`：合并后保存的目标文件路径

函数的作用是将多个 Markdown 文件合并为一个文件保存到目标路径。合并规则如下：

1. 最终合并结果的一级标题固定为 `# 合并结果`
2. 所有原始 Markdown 文件的标题需要降级：
   - 一级标题 `#` → 二级标题 `##`
   - 二级标题 `##` → 三级标题 `###`
   - 以此类推
   - 六级标题 `######` → 正文，用 **加粗** 表示
3. 非标题内容（正文、列表、代码块等）保持不变

## 第三方库

Python 拥有庞大的第三方库生态，可以通过包管理工具 `pip` 来安装、升级、卸载和管理依赖。

### pip 概述

`pip` 是 Python 的官方包管理器，从 Python 3.4 开始自带。它从 **PyPI（Python Package Index）** 下载包，默认源为 `https://pypi.org`。

```bash
# 查看 pip 版本
pip --version

# 查看帮助
pip help
```

> 如果你同时安装了 Python 2 和 Python 3，可能需要用 `pip3` 代替 `pip`。或者使用 `python -m pip` 确保调用的是当前 Python 对应的 pip。

### 国内镜像源

由于网络原因，国内访问 PyPI 可能很慢，可以使用国内镜像：

```bash
# 临时使用阿里云镜像
pip install 包名 -i https://mirrors.aliyun.com/pypi/simple/

# 临时使用清华大学镜像
pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

配置默认镜像源（全局生效）：

```bash
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

常用国内镜像源：

| 镜像源       | URL                                                  |
| ------------ | ---------------------------------------------------- |
| 阿里云       | https://mirrors.aliyun.com/pypi/simple/              |
| 清华大学     | https://pypi.tuna.tsinghua.edu.cn/simple/            |
| 中国科技大学 | https://pypi.mirrors.ustc.edu.cn/simple/             |
| 华为云       | https://repo.huaweicloud.com/repository/pypi/simple/ |

### 安装第三方库
**注意**：
1.官方包管理器的安装：第三方库的安装位置与python版本绑定。安装的位置在site-packages（'C:\\Users\\xiaolei520\\.pyenv\\pyenv-win\\versions\\3.9.13\\lib\\site-packages'）
**带来的问题**：不同项目之间，可能使用相同的py版本，但是使用不同版本的第三方库，这样pip安装就有问题
**解决方案**：
1.使用虚拟环境（参考下面章节）
2.
#### 基础安装

```bash
# 安装最新版本
pip install 包名

# 实际例子
pip install requests
pip install flask
```

#### 指定版本

```bash
# 安装指定版本
pip install requests==2.31.0

# 安装高于某个版本
pip install "requests¡2.20"

# 安装某个范围内的版本
pip install "requests>=2.20,<3.0"
```

| 符号 | 作用             |
| ---- | ---------------- |
| `==` | 固定版本         |
| `>=` | 最低版本限制     |
| `>`  | 严格高于         |
| `<=` | 最高版本限制     |
| `<`  | 严格低于         |
| `~=` | 同系列小版本更新 |
| `,`  | 组合多条件       |
| `!=` | 排除指定版本     |
| `*`  | 通配补丁版本     |

#### 一次安装多个

```bash
pip install requests flask django
```

### 升级第三方库

```bash
# 升级到最新版本
pip install --upgrade 包名
# 或简写
pip install -U 包名

# 升级 pip 自身
pip install --upgrade pip
```

### 卸载第三方库

```bash
# 卸载包及其依赖
pip uninstall 包名

# 卸载多个
pip uninstall requests flask

# 注意：卸载操作会询问确认，加 -y 跳过确认
pip uninstall -y 包名
```

### 查看与管理包

```bash
# 列出所有已安装的包
pip list

# 查看过时的包（可升级的）
pip list --outdated

# 查看特定包的详细信息
pip show 包名

# 示例输出
pip show requests
# Name: requests
# Version: 2.31.0
# Summary: Python HTTP for Humans.
# Requires: certifi, charset-normalizer, idna, urllib3
# Required-by:  （哪些包依赖它）
```

### 依赖管理

#### requirements.txt

在项目中使用 `requirements.txt` 记录所有依赖：

```bash
# 生成当前环境的依赖列表
pip freeze > requirements.txt
```

`requirements.txt` 文件内容示例：

```
requests==2.31.0
flask==3.0.0
numpy>=1.24.0
```

从 `requirements.txt` 安装依赖：

```bash
pip install -r requirements.txt
```

### 虚拟环境

不同项目可能需要不同版本的依赖，使用虚拟环境可以隔离依赖：

```bash
# 创建虚拟环境（Python 3.3+）
python -m venv .venv (-m表示使用模块，venv是py的内置模块，可以想模块查找顺序)

# 激活虚拟环境
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# 激活后，pip 安装的包只在该环境中生效
pip install requests

# 退出虚拟环境
deactivate
```

#### 使用 venv 管理项目依赖

```bash
# 1. 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate

# 2. 安装项目依赖
pip install -r requirements.txt

# 3. 开发完成后冻结依赖
pip freeze > requirements.txt

# 4. 退出虚拟环境
deactivate
```

> 小知识：
>
> 1. `-m`表示python会按照模块的查找顺序查找模块运行
> 2. `venv`的前身是一个第三方库`virtualenv`，从Python 3.3开始，官方将 `venv` 作为其功能的“精简版”集成到了标准库中，这样我们就不需要额外安装，开箱即用了。

### 作业（使用AI，已看懂）

实现一个命令行工具，实现和AI的聊天

## 事件循环

### 同步代码的问题
**典型同步问题**：
1.I/O操作：网络请求，文件读写，控制台输入输出，UI交互
2.延时操作
```python
import requests

def task1():
  # 任务1
  requests.post(...) # 发送请求，阻塞线程

def task2():
  # 任务2
  pass

task1()	# task1的阻塞导致后续任务白白等待，浪费了CPU资源
task2()
```

### 什么是异步

异步是一种编程模式，当有多个任务需要在**一个线程**上执行时，这种模式可以让任务不会造成线程阻塞

![async_vs_sync](https://resource.duyiedu.com/yuanjin/202605271757205.svg)

### 异步 VS 多线程

运算密集型：多线程

I/O密集型：异步

### Python的事件循环

事件循环是实现异步的基础手段

#### AbstractEventLoop类

在`python`中，一个事件循环就是一个`AbstractEventLoop`类的对象

```python
import asyncio

# 创建一个新的事件循环对象
loop = asyncio.new_event_loop()

# 绑定事件循环到当前线程
asyncio.set_event_loop(loop)

# 获取当前线程的事件循环
current_loop = asyncio.get_event_loop()

print("当前事件循环:", current_loop)

# 移除事件循环绑定
asyncio.set_event_loop(None)

# 运行事件循环
# 陷入死循环，除非在循环中终止，否则后续代码永远无法得到运行
current_loop.run_forever()

# 停止事件循环
current_loop.stop()
```

#### run_forever方法

```python
def run_forever(self):
    """Run until stop() is called."""
    while True:
        self._run_once()
        if self._stopping:
            break
```

#### \_run\_once逻辑

`_run_once`方法的核心，就是调度事件循环中的队列

它要确保每次该方法运行，都能保证ready队列中的所有回调得到执行
**注意**：
1.延时“队列”数据结构实际是最小堆，内部延时操作排好顺序的，时间最早到的最前面
2.I/O"队列"数据结构实际是映射表

![队列.excalidraw](https://resource.duyiedu.com/yuanjin/202605271642589.svg)

> 核心逻辑：
> 1. 检查延时队列，加入ready
> 2. 计算等待时间 timeout
>    1. ready有东西，timeout = 0
>    2. 延时队列还有任务，timeout = 延时队列的队首 - 当前时间
>    3. 都没有任务，timeout = None（永远等待）
> 3. 用timeout的时间阻塞线程，等待I/O，期间有任何IO任务到达，马上加入ready
>    1. 如果timeout时间到达后还没有I/O任务，则重新处理一次延时队列
> 4. 复制ready队列
> 5. 执行复制的队列

试一试下面的代码

```python
import inspect
import asyncio

loop = asyncio.new_event_loop()


# 将函数直接放入ready队列
def my_ready_callback():
    print("这是一个直接进入ready队列的回调函数")


loop.call_soon(my_ready_callback)


# 将函数放入延迟队列，1秒后进入ready队列
def my_scheduled_callback():
    print("这是一个延迟1秒后进入ready队列的回调函数")
    loop.stop()  # 停止事件循环


loop.call_later(1, my_scheduled_callback)

loop.run_forever()

print("事件循环已停止")

```

### 作业

#### 一、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def task1():
    print("任务1")


def task2():
    print("任务2")


def task3():
    print("任务3")


loop.call_soon(task1)
print("task1 over")
loop.call_soon(task2)
print("task2 over")
loop.call_soon(task3)
print("task3 over")

loop.run_forever()
print("已结束")
```

#### 二、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def delayed():
    print(1)
    loop.call_later(0, lambda: print(2))
    loop.call_soon(lambda: print(3))


def soon():
    print(4)
    loop.call_soon(lambda: print(5))


loop.call_later(0, delayed)
loop.call_soon(soon)


loop.run_forever()
print("done")

```

#### 三、预测以下代码的输出结果

```python
import asyncio

loop = asyncio.new_event_loop()


def first():
    print(1)


def second():
    print(2)
    loop.call_soon(lambda: print(3))
    loop.stop()


def third():
    print(4)


loop.call_soon(first)
loop.call_soon(second)
loop.call_soon(third)

loop.run_forever()
print("循环已停止")

```


## Future类

在异步场景中，有很多任务开始后，只能在**将来**的某个时间点才能完成

为了表达这一逻辑，Python封装了`Future`类



`Future`类表达了一个在将来会完成的异步任务

每一个`Future`对象拥有两种状态：

- 未完成：表示任务还在等待
- 已完成：表示任务已有结果
  - 正常完成
  - 有错误
  - 被取消

开发者可以通过以下代码操作和检查状态

```python
import asyncio

loop = asyncio.new_event_loop()
fut = loop.create_future()  # 通过事件循环对象创建Future
# print(fut.done())  # False，未完成
# print(fut.result())  # 引发InvalidStateError异常

# 让fut完成
# fut.set_result("result")  # 设置完成结果的值
# print(fut.done(), fut.result())  # 是否完成、完成结果，打印：True result

# 发生异常
# fut.set_exception(TypeError("类型异常"))  # 设置异常
# print(fut.done(), fut.exception())
# print(fut.result())  # 此时获取result会引发异常

# 取消
# fut.cancel("不等了")  # 取消future
# print(fut.done(), fut.cancelled())  # 已完成、已取消
# print(fut.result())  # 获取结果会引发CancelledError异常
# print(fut.exception())  # 获取异常结果同样会引发CancelledError异常


# # 注册回调
# def on_done(f: asyncio.Future) -> None:
#     try:
#         print(f"Future完成，结果：{f.result()}")
#     except Exception as e:
#         print(f"Future完成，但发生异常：{e}")


# # 注册回调函数
# # 该回调函数会被放到事件循环的ready队列中，等待事件循环调度执行
# fut.add_done_callback(on_done)

```

### 作业（已看懂）

理解`25. Future/demo`目录中的两个`python`代码

## 协程 Coroutine

### 回调之痛

在之前的课程中，我们用 `Future` 把延时函数和网络请求封装成了异步模式，但使用者依然需要注册回调：

```python
async_delay(2).add_done_callback(lambda _: print("2秒后执行"))
```

如果请求之后还有请求，就会出现**回调地狱**：

```python
async_request("host1").add_done_callback(lambda r1:
    async_request("host2").add_done_callback(lambda r2:
        async_request("host3").add_done_callback(lambda r3:
            ...
        )
    )
)
```

代码横向增长，可读性急剧下降。

### 协程函数
简单理解：协程就是在一个单线程中制造了一个多线程的的感觉，类似生成器的使用

`Python` 中，使用 `async def` 定义一个**协程函数**。调用协程函数会得到一个**协程对象**。

```python
from async_delay import async_delay
from async_request import async_request
import asyncio


async def test():
    print("main begins")
    resp1 = await async_request("localhost", 5500, "/index.html")
    print("resp1", resp1[:9])
    await async_delay(1)
    print("delayed")
    resp2 = await async_request("localhost", 5500, "/index.html")
    print("resp2", resp2[:9])
    return "ok"
```

### 协程 VS 线程

| 对比维度        | 🧵 线程 (Thread)                                              | 🍃 协程 (Coroutine)                                           |
| :-------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **运行载体**    | 运行在操作系统内核态，受系统管理。                           | 完全运行在**用户态**，由事件循环（如 `asyncio`）管理。       |
| **资源开销**    | **较高** 每个线程需要独立的栈空间（通常数MB）和内核资源，创建和切换开销大。 | **极低** 协程栈空间很小（通常几KB），切换只需保存少量CPU寄存器上下文。 |
| **切换成本**    | **昂贵** 涉及用户态与内核态切换，需要数百个CPU时钟周期。     | **非常廉价** 纯用户态操作，仅需几十个时钟周期。              |
| **数据同步**    | 复杂且易出错 多线程共享内存，需要使用 `锁(Lock)`、`信号量(Semaphore)` 等机制，容易产生**死锁**、**竞态条件**。 | **相对安全** 单线程内运行，同一时刻只有一个协程在执行，天然避免了数据竞争。但使用多线程事件循环时仍需注意。 |
| **利用多核**    | ✅ **原生支持** 可将不同线程分配到不同CPU核心，实现并行计算（CPU密集型任务）。 | ❌ **单线程内不支持** 一个事件循环默认只运行在一个线程、一个核心上。需要配合 `asyncio` 的 `run_in_executor` 或多进程才能利用多核。 |
| **适用场景**    | **CPU密集型任务** 或 **对实时性要求高的I/O任务**（通过多线程掩盖阻塞） | **海量I/O密集型任务** 网络爬虫、Web服务器（如FastAPI）、聊天服务、高并发数据库访问等。可以轻松创建成千上万个协程。 |
| **代表库/语法** | `threading`, `concurrent.futures.ThreadPoolExecutor`         | `asyncio`, `async`/`await`, `trio`, `gevent` (基于协程的库)  |
| **典型数量级**  | 百级别（数百个线程开销已相当可观）                           | 万/十万级别（轻松创建数万个协程）                            |

### 驱动协程对象

```python

def main():
    coro = test()
    loop = asyncio.get_event_loop()
    f = loop.create_future()
    r = coro.send(None)

    def done_callback(fut):
        try:
            r = coro.send(fut.result())
            r.add_done_callback(done_callback)
        except StopIteration as e:
            f.set_result(e.value)

    r.add_done_callback(done_callback)
    return f


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def run():
    fut = main()

    def done_callback(fut):
        loop.stop()
        print(fut.result())

    fut.add_done_callback(done_callback)


loop.call_soon(run)
loop.run_forever()
print("over")
```

### Task

`Task`是`Future`的子类，它专门用于驱动协程对象的执行

```python
def main():
    coro = test()
    loop = asyncio.get_event_loop()
    f = loop.create_future()
    r = coro.send(None)

    def done_callback(fut):
        try:
            r = coro.send(fut.result())
            r.add_done_callback(done_callback)
        except StopIteration as e:
            f.set_result(e.value)

    r.add_done_callback(done_callback)
    return f


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def run():
    fut = main()

    def done_callback(fut):
        loop.stop()
        print(fut.result())

    fut.add_done_callback(done_callback)


loop.call_soon(run)
loop.run_forever()
print("over")

# 等效于
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def run():
    task = asyncio.create_task(test())  # 将协程包装成一个Task

    def done_callback(task):
        loop.stop()
        print(task.result())

    task.add_done_callback(done_callback)


loop.call_soon(run)
loop.run_forever()
print("over")
```



### asyncio.run

`asyncio.run`可以直接驱动一个协程对象，在内部会将其转换为`Task`

```python
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def run():
    task = asyncio.create_task(test())  # 将协程包装成一个Task

    def done_callback(task):
        loop.stop()
        print(task.result())

    task.add_done_callback(done_callback)


loop.call_soon(run)
loop.run_forever()
print("over")

# 等效于
result = asyncio.run(test())
print(result)
print("over")
```

### 深度总结

1. `async`修饰的函数称之为**协程函数/异步函数**，调用后返回**协程对象**
2. 协程对象可以通过`asyncio.create_task`包装成一个`Task`，用于驱动协程对象
   1. `Task`创建后，会立即启动协程对象的执行，执行放到ready队列中
   2. 协程对象执行结束，Task完成，完成的数据即是协程对象的返回值
3. `await`关键字可以等待一个`awaitable`对象
   1. `await`必须在协程函数中
   2. 常见的`awaitable`对象：**协程对象**、**Task**、**Future**

4. `asyncio.run`可接收一个协程对象，其在内部转换为`Task`



### 作业（已完成）

#### 一、实现 gather 函数

```python
import asyncio
from async_delay import async_delay
from typing import Coroutine


def gather(*aws: Coroutine) -> asyncio.Future:
    # 你的代码
    pass


async def coro(name: str, duration: int):
    await async_delay(duration)
    return f"{name} 完成"


async def main():
    results = await gather(
        coro("A", 2),
        coro("B", 1),
        coro("C", 3),
    )
    print(results)  # 预期: ['A 完成', 'B 完成', 'C 完成']


asyncio.run(main())

```

#### 二、实现 Event 类

```python
import asyncio
from async_delay import async_delay
from gather import gather


class Event:
    # 你的代码
    pass


async def test():
    event = Event()

    async def waiter():
        print("waiter: 开始等待")
        await event.wait()
        print("waiter: 被唤醒")

    async def setter():
        print("setter: 1秒后设置事件")
        await async_delay(1)
        event.set()
        print("setter: 事件已设置")

    await gather(waiter(), setter())


asyncio.run(test())

# 预期结果：
""" 
waiter: 开始等待
setter: 1秒后设置事件
setter: 事件已设置
waiter: 被唤醒 
"""
```

## 异步编程

前面三节课我们分别学习了事件循环、Future 和协程的底层原理。从这节课开始，我们不再自己造轮子，而是使用 Python 官方和社区给我们准备好的 API，高效地进行异步开发。

### 异步生成器与异步迭代器

在协程函数中使用 `yield`，就变成了**异步生成器**。它每次 `yield` 产出值时都可以 `await` 其他协程。

```python
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    # 必须用 async for 来遍历异步生成器
    async for item in async_generator():
        print(item)  # 每隔 1 秒打印一个数字


asyncio.run(main())
```

同样可以自定义**异步迭代器**，实现 `__aiter__` 和 `__anext__` 两个协议方法：

```python
class AsyncCounter:
    def __init__(self, limit: int):
        self._limit = limit
        self._count = 0

    def __aiter__(self):
        return self

    async def __anext__(self) -> int:
        self._count += 1
        if self._count > self._limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.5)
        return self._count


async def main():
    async for num in AsyncCounter(5):
        print(num)  # 每隔 0.5 秒打印 1 2 3 4 5
```

对比同步迭代协议：

| 同步                    | 异步                             |
| ----------------------- | -------------------------------- |
| `__iter__` / `__next__` | `__aiter__` / `__anext__`        |
| `for x in iterable`     | `async for x in async_iterable`  |
| `StopIteration`         | `StopAsyncIteration`             |
| 生成器 `yield`          | 异步生成器 `async def` + `yield` |

### 异步上下文管理器

`async with` 背后是 `__aenter__` 和 `__aexit__` 两个协议方法，和同步的 `with` 类似，只是都是异步的。

```python
class AsyncResource:
    async def __aenter__(self):
        print("获取资源")
        await asyncio.sleep(0.5)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")
        await asyncio.sleep(0.5)


async def main():
    async with AsyncResource() as res:
        print("使用资源")
```

对比同步上下文管理器：

| 同步                     | 异步                       |
| ------------------------ | -------------------------- |
| `__enter__` / `__exit__` | `__aenter__` / `__aexit__` |
| `with ctx`               | `async with ctx`           |

### 官方 asyncio 核心 API
**注意**
1.函数形参/和*符号
-     1.存在的话，/一定在*前面
-     2./和*都是分隔符，不需要传递
-     3./前面的参数是不定量参数
-     4./和*中的可以是不定量参数，也可以是字典不定量参数
-     5.*后面的是字典不定量参数
```python
run(x,y,/,a,b,c,*,d)
# x,y是不定量参数，需要这样传递run(1,2)
# a,b,c可以是不定量参数，也可以是字典不定量参数,需要这样传递run(1,2,3,4,5)或run(1,2,a=3,b=4,c=5)
# d是字典不定量参数,需要这样传递run(1,2,3,4,5,d=6)
```

#### sleep —— 非阻塞等待

回顾之前在 `async_delay.py` 中，我们自己用 `loop.call_later` + `Future` 实现的延时：

```python
def async_delay(duration: int):
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    loop.call_later(duration, future.set_result, None)
    return future
```

官方直接提供了 `asyncio.sleep`，用法完全相同：

```python
async def main():
    print("开始")
    await asyncio.sleep(1)  # 挂起当前协程 1 秒，事件循环去调度其他协程
    print("1秒后")
```

#### 创建与运行协程

```python
import asyncio


async def say_hello():
    await asyncio.sleep(1)
    return "Hello"


async def main():
    # 1. asyncio.run —— 最高层入口
    pass

result = asyncio.run(say_hello())
```

#### create_task —— 将协程包装成 Task 并调度执行

```python
async def main():
    # 创建 Task，协程会立即被调度到事件循环中执行
    task = asyncio.create_task(say_hello())
    # 这里可以做别的事，task 已经在后台运行
    result = await task  # 等待 task 完成
    print(result)
```

#### gather —— 并发执行多个协程

```python
async def fetch(url: str, delay: int) -> str:
    await asyncio.sleep(delay)
    return f"{url} 完成"


async def main():
    # 同时发起多个请求，等待所有完成
    results = await asyncio.gather(
        fetch("url1", 2),
        fetch("url2", 1),
        fetch("url3", 3),
    )
    print(results)  # ['url1 完成', 'url2 完成', 'url3 完成']


asyncio.run(main())
```

gather 的特点：

- 所有协程**并发**执行
- 返回结果顺序与传入顺序一致
- 任何一个协程抛出异常，gather 会立即传播异常（其他协程仍会继续运行）
- 可通过 `return_exceptions=True` 让异常以结果形式返回，不中断 gather

```python
async def fail() -> str:
    raise ValueError("出错了")


async def main():
    results = await asyncio.gather(
        fetch("ok", 1),
        fail(),
        return_exceptions=True,  # 将异常作为返回值，不抛出
    )
    print(results)  # ['ok 完成', ValueError('出错了')]
```

#### wait —— 更灵活的等待方式

```python
import asyncio
from typing import Coroutine


async def main():
    tasks = [
        asyncio.create_task(fetch("A", 2)),
        asyncio.create_task(fetch("B", 1)),
        asyncio.create_task(fetch("C", 3)),
    ]

    # FIRST_COMPLETED: 任一完成就返回
    # FIRST_EXCEPTION: 任一异常就返回
    # ALL_COMPLETED: 全部完成（默认）
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"已完成: {len(done)}, 待完成: {len(pending)}")

    # 还可以手动处理未完成的任务
    for task in pending:
        task.cancel()
```

#### as_completed —— 谁先完成谁先处理

```python
async def main():
    coros = [fetch("A", 2), fetch("B", 1), fetch("C", 3)]

    for coro in asyncio.as_completed(coros):
        result = await coro
        print(result)  # 按照完成的先后顺序打印
```

#### TaskGroup —— 结构化并发（Python 3.11+）

```python
async def main():
    # TaskGroup 保证所有子任务在退出前完成
    # 如果某个子任务异常，会取消组内所有其他任务
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch("A", 2))
        task2 = tg.create_task(fetch("B", 1))
        task3 = tg.create_task(fetch("C", 3))

    # 到这里所有任务都已安全完成
    print(task1.result(), task2.result(), task3.result())
```



#### Lock —— 互斥锁

多个协程可能竞争共享资源，Lock 保证同一时刻只有一个协程能访问

```python
import asyncio

shared_data: int = 0
lock = asyncio.Lock()


async def safe_increment():
    global shared_data
    async with lock:  # 获取锁，等锁释放前其他协程会在此等待
        temp = shared_data
        await asyncio.sleep(0)  # 模拟耗时操作，此时切换协程也不会出问题
        shared_data = temp + 1


async def main():
    await asyncio.gather(*[safe_increment() for _ in range(100)])
    print(shared_data)  # 100
```

#### Event —— 事件通知

一个协程等待另一个协程发出信号

```python
async def waiter(event: asyncio.Event):
    print("waiter: 开始等待")
    await event.wait()  # 等待事件被设置
    print("waiter: 被唤醒")


async def setter(event: asyncio.Event):
    print("setter: 1秒后设置事件")
    await asyncio.sleep(1)
    event.set()  # 设置事件，唤醒所有等待者


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))
```

#### Semaphore —— 限制并发数

```python
semaphore = asyncio.Semaphore(3)  # 同时最多 3 个


async def limited_fetch(url: str):
    async with semaphore:  # 超过并发限制时等待
        print(f"开始请求 {url}")
        await asyncio.sleep(1)
        print(f"完成请求 {url}")
        return url


async def main():
    urls = [f"url{i}" for i in range(10)]
    await asyncio.gather(*[limited_fetch(url) for url in urls])
```

#### Queue —— 异步队列

生产者-消费者模式的基石

```python
import random


async def producer(queue: asyncio.Queue):
    for i in range(10):
        item = f"item_{i}"
        await queue.put(item)
        print(f"生产: {item}")
        await asyncio.sleep(random.random())
    await queue.put(None)  # 发送结束信号


async def consumer(name: str, queue: asyncio.Queue):
    while True:
        item = await queue.get()
        if item is None:  # 收到结束信号
            queue.task_done()
            break
        print(f"{name} 消费: {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=5)
    await asyncio.gather(
        producer(queue),
        consumer("C1", queue),
        consumer("C2", queue),
    )
```

#### asyncio.wait_for

```python
async def slow_operation():
    await asyncio.sleep(10)
    return "完成"


async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
    except TimeoutError:
        print("操作超时了")
```

#### asyncio.timeout（Python 3.11+）

```python
async def main():
    try:
        async with asyncio.timeout(2):
            result = await slow_operation()
    except TimeoutError:
        print("操作超时了")
```

#### 在异步中运行同步代码

```python
import time


def blocking_io() -> str:
    time.sleep(0.5)  # 同步阻塞操作
    return "文件读取完成"


def cpu_intensive() -> int:
    return sum(i * i for i in range(10_000_000))


async def main():
    # to_thread：将同步阻塞函数放到线程池中执行
    result = await asyncio.to_thread(blocking_io)
    print(result)

    # run_in_executor：更底层，可以指定执行器
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, cpu_intensive)
    print(result)
```

### 第三方异步库

#### 网络请求

##### aiohttp（第三方最流行的异步 HTTP 库）

```python
import aiohttp


async def fetch_url(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    html = await fetch_url("https://example.com")
    print(len(html))
```

##### httpx（支持同步/异步双模式，API 更友好）

```python
import httpx


async def fetch_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def main():
    html = await fetch_url("https://example.com")
    print(len(html))
```

#### 文件 I/O

##### aiofiles（异步文件操作）

```python
import aiofiles


async def read_write_example():
    # 写文件
    async with aiofiles.open("example.txt", "w") as f:
        await f.write("Hello, 异步文件!\n")

    # 读文件
    async with aiofiles.open("example.txt", "r") as f:
        content = await f.read()
        print(content)
```

### 常见异步编程模式(面试题)

#### 并发批处理模式

```python
async def batch_process(urls: list[str]):
    """将一批任务并发执行，并收集结果"""
    async def process(url: str) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            return {"url": url, "status": resp.status_code}

    results = await asyncio.gather(*[process(url) for url in urls])
    return results
```

#### 限速器模式

```python
class RateLimiter:
    """限制单位时间内的请求数"""

    def __init__(self, max_rate: float, interval: float = 1.0):
        self._sem = asyncio.Semaphore(max_rate)
        self._interval = interval

    async def acquire(self):
        await self._sem.acquire()

        def release():
            self._sem.release()

        loop = asyncio.get_running_loop()
        loop.call_later(self._interval, release)

    async def __aenter__(self):
        await self.acquire()

    async def __aexit__(self, *args):
        pass


async def main():
    rate_limiter = RateLimiter(max_rate=2, interval=1.0)

    async def fetch(url: str) -> str:
        async with rate_limiter:
            await asyncio.sleep(0.3)
            return f"{url} done"

    results = await asyncio.gather(*[fetch(f"url{i}") for i in range(6)])
    print(results)  # 每秒最多完成 2 个请求


asyncio.run(main())
```

#### 重试模式

```python
async def retry(coro_factory, max_retries: int = 3, delay: float = 1.0):
    """为异步操作添加重试机制"""
    for attempt in range(max_retries):
        try:
            return await coro_factory()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"第 {attempt + 1} 次失败，{delay} 秒后重试...")
            await asyncio.sleep(delay)


async def main():
    n = 0

    async def unstable_request() -> str:
        nonlocal n
        n += 1
        if n < 3:
            raise ConnectionError(f"第 {n} 次请求失败")
        return "成功响应"

    result = await retry(unstable_request, max_retries=3, delay=0.5)
    print(result)  # 前 2 次失败，第 3 次成功


asyncio.run(main())
```

#### 优雅关闭模式

```python
import asyncio
import signal


class GracefulServer:
    def __init__(self):
        self._running = True

    async def serve(self):
        while self._running:
            try:
                await asyncio.sleep(1)  # 模拟处理请求
                print("正在处理请求...")
            except asyncio.CancelledError:
                print("收到取消信号，正在关闭...")
                break

    def shutdown(self):
        print("开始优雅关闭...")
        self._running = False

    async def run(self):
        loop = asyncio.get_running_loop()
        stop = loop.create_future()

        def signal_handler():
            stop.set_result(None)

        loop.add_signal_handler(signal.SIGINT, signal_handler)  # Ctrl+C
        loop.add_signal_handler(signal.SIGTERM, signal_handler)  # 终止信号

        task = asyncio.create_task(self.serve())
        await stop  # 等待关闭信号
        self.shutdown()
        task.cancel()
        await task


async def main():
    server = GracefulServer()
    await server.run()


# 按 Ctrl+C 触发 SIGINT，程序会优雅退出而非直接崩溃
asyncio.run(main())

```

### 最佳实践与注意事项

#### 1. 不要在协程中调用同步阻塞函数

```python
import time


async def bad():
    time.sleep(1)  # 错误！将阻塞整个事件循环


async def good():
    await asyncio.sleep(1)  # 正确！主动让出控制权


async def acceptable():
    await asyncio.to_thread(time.sleep, 1)  # 可行！让线程池去阻塞
```

#### 2. 始终使用 asyncio.run 作为入口

```python
# 错误：手动管理事件循环
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
task = loop.create_task(main())
loop.run_forever()

# 正确：asyncio.run 自动创建和关闭事件循环
asyncio.run(main())
```

#### 3. 小心协程对象未被 await

```python
async def main():
    # 错误：创建了协程但未 await，协程永远不会执行
    fetch("url", 1)

    # 正确
    await fetch("url", 1)

    # 或通过 gather
    await asyncio.gather(fetch("url1", 1), fetch("url2", 2))
```

#### 4. gather 异常处理

gather 默认任何协程异常都会立即传播，其他协程不会取消，但结果丢失

```python
async def main():
    # 方式一：使用 return_exceptions=True
    results = await asyncio.gather(
        risky_task(),
        safe_task(),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"某个任务失败: {r}")

    # 方式二：使用 TaskGroup（Python 3.11+）
    # 任一异常会取消组内所有任务
```

#### 5. 使用 debug 模式

asyncio 的 debug 模式可以帮助你发现异步代码中的常见问题，比如协程阻塞事件循环、忘记 await、回调执行时间过长等。

```python
# 开启 asyncio 调试模式
asyncio.run(main(), debug=True)

# 或通过环境变量
# PYTHONASYNCIODEBUG=1 python script.py
```
##### 检测长时间阻塞的协程

debug 模式下，事件循环会监控每个协程的执行时间。如果某个协程执行超过 0.1 秒（默认阈值），会在 stderr 输出警告：

```python
import time
import asyncio

async def blocking_coroutine():
    """模拟一个协程内部做了同步阻塞操作"""
    print("开始阻塞操作...")
    time.sleep(0.2)  # 同步阻塞，会阻塞整个事件循环
    print("阻塞操作结束")


async def main():
    await blocking_coroutine()


asyncio.run(main(), debug=True)
```

输出类似：
```
开始阻塞操作...
阻塞操作结束
Executor <TaskInfo name='Task-1' ...> running at (...)
    blocking_coroutine at demo.py:12
    main at demo.py:18
    ...
```

`time.sleep(0.2)` 是同步阻塞，但 debug 模式下检测到协程在同一个位置停留超过 0.1 秒，会打印出执行栈信息，精确定位阻塞的代码行。

##### 检测未 await 的协程对象

忘记 `await` 协程是新手最容易犯的错误，debug 模式会检测到协程对象被创建但从未被迭代：

```python
import asyncio


async def fetch_data(url: str) -> str:
    await asyncio.sleep(0.5)
    return f"{url} 数据"


async def main():
    # 忘记 await，协程对象永远不会执行
    fetch_data("https://example.com")

    await asyncio.sleep(1)


asyncio.run(main(), debug=True)

```

输出类似：
```
Coroutine 'fetch_data' was never awaited (at demo.py:12)
```

这个警告在你忘记 `await` 时非常有用，避免协程"静默丢失"。

##### 自定义慢操作阈值

通过 `loop.slow_callback_duration` 调整检测阈值：

```python
async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.5  # 改为 0.5 秒才报警

    def acceptable_callback():
        time.sleep(0.3)  # 0.3 秒，低于自定义阈值，不会报警

    loop.call_later(0.1, acceptable_callback)
    await asyncio.sleep(0.5)


asyncio.run(main(), debug=True)
```

#### 6. 避免全局事件循环

```python
# 错误：在模块级别获取事件循环
loop = asyncio.get_event_loop()  # 可能获取到错误的事件循环

# 正确：在协程内部获取当前事件循环
async def my_func():
    loop = asyncio.get_running_loop()
```

#### 7. CancelledError 的正确处理

```python
async def cleanup():
    try:
        await long_running_task()
    except asyncio.CancelledError:
        # 务必完成清理后再重新抛出
        await release_resources()
        raise  # 必须重新抛出
```

### 作业（使用AI,已看懂）

读懂`./answers`中的代码

## 多线程和多进程

之前的课程中我们一直在讲异步编程，它适用于 **I/O 密集型** 任务。但如果遇到 **CPU 密集型** 任务，或者需要调用同步阻塞的库，多线程就派上用场了。

### 进程 vs 线程 vs 协程

| 对比维度 | 🖥️ 进程 (Process) | 🧵 线程 (Thread) | 🍃 协程 (Coroutine) |
| :--- | :--- | :--- | :--- |
| **运行载体** | 操作系统内核态 | 操作系统内核态 | 用户态（事件循环） |
| **资源开销** | **极高** 独立地址空间、文件描述符等，创建需 fork/clone | **中等** 共享进程地址空间，独立栈空间（数 MB） | **极低** 共享线程栈，状态极小（几 KB） |
| **切换成本** | **最昂贵** 涉及 TLB 刷新、页表切换 | **昂贵** 内核态切换，数百 CPU 周期 | **非常廉价** 纯用户态，数十 CPU 周期 |
| **数据共享** | 需 IPC（管道、共享内存、socket 等） | 共享内存，**需同步机制** | 单线程天然安全，但需注意非原子操作 |
| **利用多核** | ✅ 原生支持 | ✅ 原生支持 | ❌ 单线程内不支持 |
| **适用场景** | 隔离性要求高的多任务 | CPU 密集型、同步阻塞 I/O | 海量 I/O 密集型 |
| **创建数量级** | 十级别 | 百/千级别 | 万/十万级别 |

### threading 模块

`threading` 是 Python 标准库中用于多线程编程的模块。

#### 创建线程

```python
import threading
import time


def worker(name: str, duration: int):
    print(f"线程 {name} 开始工作")
    time.sleep(duration)
    print(f"线程 {name} 工作完成")


# 创建线程
t = threading.Thread(target=worker, args=("A", 2))
t.start()  # 启动线程
print("主线程继续执行")
t.join()  # 等待线程结束
print("主线程等待结束")
```

输出：
```
线程 A 开始工作
主线程继续执行
...
线程 A 工作完成
主线程等待结束
```

#### 继承 Thread 类

```python
import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, name: str, duration: int):
        super().__init__(name=name)
        self._duration = duration

    def run(self) -> None:
        print(f"线程 {self.name} 开始，参数: {self._duration}")
        time.sleep(self._duration)
        print(f"线程 {self.name} 完成")


t = WorkerThread("B", 1)
t.start()
t.join()
```

#### 守护线程 (Daemon)

主线程退出时，**非守护线程**会阻止进程退出，**守护线程**会被强制终止。

```python
import threading
import time


def daemon_worker():
    while True:
        print("守护线程运行中...")
        time.sleep(1)


d = threading.Thread(target=daemon_worker, daemon=True)
d.start()

time.sleep(3)
print("主线程结束，守护线程被强制终止")
```

> 注意：守护线程中不应操作资源（如写文件），因为可能在操作过程中被强制终止。

### 线程安全与竞态条件

多个线程同时访问共享变量时，会出现**竞态条件 (Race Condition)**：

```python
import threading
import time


class BankAccount:
    def __init__(self, balance):
        self.balance = balance


def withdraw(account, amount, person_name):
    """取款函数 - 有竞态条件漏洞"""
    print(f"{person_name}: 查询余额，当前有 {account.balance} 元")

    # 关键漏洞：检查余额和扣款不是原子操作
    if account.balance >= amount:
        print(f"{person_name}: 余额充足，开始取款...")

        # 这个延迟让另一个线程有机会插进来
        time.sleep(0.1)  # 模拟输入密码、出钞等过程

        # 扣款
        account.balance -= amount
        print(f"{person_name}: ✓ 取款{amount}元成功！剩余 {account.balance} 元")
        return True
    else:
        print(f"{person_name}: ✗ 余额不足，取款失败")
        return False


# 创建一个账户，余额1000元
account = BankAccount(1000)

# 两个人同时取款800元
person1 = threading.Thread(target=withdraw, args=(account, 800, "张三"))
person2 = threading.Thread(target=withdraw, args=(account, 800, "李四"))

# 同时启动
print("=== 两个人同时开始取款 ===")
person1.start()
person2.start()

# 等待两人完成
person1.join()
person2.join()

print("\n=== 最终结果 ===")
print(f"账户余额: {account.balance} 元")
print(f"如果正常，应该只剩: {1000 - 800} = 200 元")
print(f"两人共取出了: {1600 - account.balance} 元")

```

> `account.balance -= amount` 并非原子操作，它对应三条 CPU 指令：`LOAD balance` → `SUB amount` → `STORE balance`。线程切换可能发生在任意两条指令之间。更关键的是，**检查余额和扣款这两个步骤之间**也存在时间窗口。

### Lock —— 互斥锁

`Lock` 确保同一时刻只有一个线程可以访问临界区，用锁修复上面的银行账户问题：

```python
import threading
import time


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self._lock = threading.Lock()


def withdraw(account: BankAccount, amount: int, person_name: str):
    """取款函数 - 使用锁保证线程安全"""
    with account._lock:  # 获取锁，同一时刻只有一个线程能进入
        print(f"{person_name}: 查询余额，当前有 {account.balance} 元")

        if account.balance >= amount:
            print(f"{person_name}: 余额充足，开始取款...")
            time.sleep(0.1)
            account.balance -= amount
            print(f"{person_name}: ✓ 取款{amount}元成功！剩余 {account.balance} 元")
            return True
        else:
            print(f"{person_name}: ✗ 余额不足，取款失败")
            return False


account = BankAccount(1000)

person1 = threading.Thread(target=withdraw, args=(account, 800, "张三"))
person2 = threading.Thread(target=withdraw, args=(account, 800, "李四"))

print("=== 两个人同时开始取款 ===")
person1.start()
person2.start()
person1.join()
person2.join()

print("\n=== 最终结果 ===")
print(f"账户余额: {account.balance} 元")
print(f"如果正常，应该只剩: {1000 - 800} = 200 元")
```

锁的常见问题：

```python
import threading


lock = threading.Lock()

# 同一个线程重复 acquire 会死锁
lock.acquire()
lock.acquire()  # 死锁！我锁我自己 —— 因为线程还没释放就再次申请
```

### RLock —— 可重入锁

`RLock` 允许同一个线程多次 acquire，内部维护一个计数器：

```python
import threading

lock = threading.RLock()


def recurse(n: int):
    with lock:
        if n > 0:
            print(f"Recursing with n={n}")
            recurse(n - 1)  # 同一个线程再次 acquire ✅


recurse(5)  # 正常运行

```

### Semaphore —— 限制并发数

```python
import threading
import time

semaphore = threading.Semaphore(3)


def limited_worker(n: int):
    with semaphore:
        print(f"线程 {n} 进入\n", end="")
        time.sleep(1)
        print(f"线程 {n} 离开\n", end="")


threads = [threading.Thread(target=limited_worker, args=(i,)) for i in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

```

### Event —— 线程间通知

```python
import threading
import time


event = threading.Event()


def waiter():
    print("waiter: 开始等待")
    event.wait()  # 等待事件被设置
    print("waiter: 被唤醒")


def setter():
    print("setter: 1秒后设置事件")
    time.sleep(1)
    event.set()
    print("setter: 事件已设置")


t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)
t1.start()
t2.start()
t1.join()
t2.join()
```

### Queue —— 线程安全的生产者消费者

```python
import queue
import random
import threading
import time


def producer(q: queue.Queue):
    for i in range(10):
        item = f"item_{i}"
        q.put(item)
        print(f"生产: {item}\n", end="")
        time.sleep(random.random())
    q.put(None)


def consumer(name: str, q: queue.Queue):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"{name} 消费: {item}\n", end="")
        q.task_done()


q = queue.Queue(maxsize=5)
threads = [
    threading.Thread(target=producer, args=(q,)),
    threading.Thread(target=consumer, args=("C1", q)),
    threading.Thread(target=consumer, args=("C2", q)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

```

> `queue.Queue` 内部已经实现了线程同步，无需额外加锁。

### ThreadPoolExecutor —— 线程池

频繁创建线程开销大，使用线程池复用线程：

```python
from concurrent.futures import ThreadPoolExecutor
import time


def fetch_url(url: str) -> str:
    time.sleep(1)  # 模拟网络请求
    return f"{url} 完成"


with ThreadPoolExecutor(max_workers=3) as executor:
    urls = ["url1", "url2", "url3", "url4", "url5"]

    # map 返回结果的顺序与传入顺序一致
    results = executor.map(fetch_url, urls)
    for r in results:
        print(r)

    # 也可以 submit 逐条提交
    futures = [executor.submit(fetch_url, url) for url in urls]
    for f in futures:
        print(f.result())
```

#### ThreadPoolExecutor 与 asyncio 配合

```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_io() -> str:
    time.sleep(0.5)  # 同步阻塞
    return "文件读取完成"


async def main():
    # to_thread 将同步阻塞函数放到线程池中执行
    result = await asyncio.to_thread(blocking_io)
    print(result)

    # 也可以手动指定执行器
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print(result)


asyncio.run(main())
```

### 线程局部数据 (Thread Local)

每个线程拥有独立的副本，互不干扰：

```python
import threading
import time


local_data = threading.local()


def worker(name: str):
    local_data.name = name  # 每个线程独立存储
    local_data.count = 0
    for _ in range(3):
        local_data.count += 1
        print(f"{local_data.name}: {local_data.count}")
        time.sleep(0.1)


threads = [
    threading.Thread(target=worker, args=("A",)),
    threading.Thread(target=worker, args=("B",)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()
```

### 多线程常见问题

#### GIL —— 全局解释器锁

CPython 中有一个 **GIL (Global Interpreter Lock)**，它保证同一时刻只有一个线程在执行 Python 字节码：

```python
import threading
import time


def cpu_intensive():
    total = 0
    for i in range(50_000_000):
        total += i * i
    return total


# 多线程 vs 单线程 —— 多线程不会更快！
t1 = threading.Thread(target=cpu_intensive)
t2 = threading.Thread(target=cpu_intensive)

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(f"多线程: {time.time() - start:.2f}s")

start = time.time()
cpu_intensive()
cpu_intensive()
print(f"单线程: {time.time() - start:.2f}s")
```

> GIL 的存在意味着：**Python 多线程无法利用多核 CPU 加速 CPU 密集型任务**。
>
> 那多线程的意义在哪？对于 **I/O 密集型** 任务，线程在等待 I/O 时会释放 GIL，其他线程可以继续执行，所以仍然有加速效果。

#### CPU 密集型 —— 应该用多进程

```python
from multiprocessing import Process


def cpu_intensive():
    total = 0
    for i in range(50_000_000):
        total += i * i
    return total


p1 = Process(target=cpu_intensive)
p2 = Process(target=cpu_intensive)
p1.start()
p2.start()
p1.join()
p2.join()
```

#### 死锁

```python
import threading
import time


lock_a = threading.Lock()
lock_b = threading.Lock()


def task_1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:  # 等待 lock_b
            print("task_1 完成")


def task_2():
    with lock_b:
        time.sleep(0.1)
        with lock_a:  # 等待 lock_a
            print("task_2 完成")


t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)
t1.start()
t2.start()
t1.join()
t2.join()
# 死锁！两个线程互相等待对方释放锁
```

解决死锁的原则：**固定锁的获取顺序**

```python
import threading
import time


lock_a = threading.Lock()
lock_b = threading.Lock()


def task_1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:
            print("task_1 完成")


def task_2():
    with lock_a:  # 与 task_1 获取锁的顺序一致
        time.sleep(0.1)
        with lock_b:
            print("task_2 完成")
```

### 何时用线程，何时用协程？

| 场景 | 推荐方案 |
| :--- | :--- |
| CPU 密集型 | `multiprocessing` / `ProcessPoolExecutor` |
| 同步 I/O 密集型（文件读写、数据库驱动阻塞） | `threading` / `ThreadPoolExecutor` |
| 异步 I/O 密集型（网络爬虫、Web 服务） | `asyncio` / 协程 |
| 调用第三方同步库 | 用 `asyncio.to_thread` 或 `run_in_executor` 包装 |


## 构建发布

### 库的开发流程

![image-20260601134020260](https://resource.duyiedu.com/yuanjin/202606011340298.png)

### 构建

> 构建协议：https://peps.python.org/pep-0517/
>
> 构建产物标准：https://peps.python.org/pep-0427/

```toml
# pyproject.toml

[build-system] # 构建系统配置，指定构建工具和依赖
requires = ["hatchling"] # 依赖的后端构建工具
build-backend = "hatchling.build" # 使用哪个工具的哪个模块来构建项目

[project] # 工程描述
name = "duyi-utils" # 发行版名称
version = "0.1.3" # 版本号，遵循语义化版本控制
description = "一个用于学习 Python 公共库构建和发布的示例工程" # 项目简介
requires-python = ">=3.14" # 指定支持的 Python 版本
readme = "README.md" # 指定项目的 README 文件路径
dependencies = [
    "python-dateutil>=2.8", # 依赖的第三方库，指定版本要求
    "Markdown>=3.5", # 另一个依赖
]

[tool.hatch.build.targets.sdist] # 配置源代码分发包
# 配置留空，表示它会默认包含所有项目文件

[tool.hatch.build.targets.wheel] # 配置 wheel 包
packages = ["src/duyi_utils"] # 配置 wheel 包的构建目标，指定包含的包路径
```

> 需要安装VSCode插件：even better toml

> 常用构建前端：`uv`、`Poetry`、`PDM`、...
>
> 常用构建后端：`hatchling`、`setuptools`、`PDM-backend`、`uv-build` `poetry-core`...

构建方式

```shell
# 1. 创建虚拟环境
python -m venv .venv

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 安装构建工具
pip install build

# 4. 运行构建
python -m build
```

构建产物放到了`./dist`中

**构建流程**
1.执行python -m build的过程

- 读取pyprojects.toml
- 安装配置文件中【build-system】中requires配置的后端构建工具，安装到隔离环境的，不影响当前虚拟环境和全局环境
- 按照配置的模块进行构建，即【build-backend】
- 读取构建后端所需要的额外配置，tool.xxx开头的
- 完成构建得到产物（sdist+wheel）

### 发布和安装

#### 发布前的准备

```shell
# 先构建（略）

# 安装官方的发布工具
pip install twine

# 【可选】验证构建产物的完整性
twine check dist/*
```

#### 发布到官方仓库

1. 注册账号：https://pypi.org/account/register/
2. 创建一个token：https://pypi.org/manage/account/token/
3. 复制token
4. 运行`twine upload dist/*`命令上传

---

安装：使用`pip install xxx`安装即可

#### 发布到私有仓库

通常使用云服务完成私有仓库的搭建

1. 创建阿里云效制品仓库
   https://packages.aliyun.com/
2. 按照仓库指南配置并上传包

---

安装：

1. 将制品仓库作为镜像源
   ```ini
   [global]
   index-url = 制品仓库地址
   extra-index-url = 镜像源地址
   trusted-host = packages.aliyun.com
   ```

2. 直接安装`pip install xxx`即可

### 可编辑依赖

> 可编辑安装（editable install）又称开发模式安装，通过 `pip install -e .` 将项目以链接形式安装到当前环境。

当项目被可编辑安装后，你对源码的任何修改都会**即时生效**，无需重新构建和重新安装。

这在日常开发中非常有用：

- 你可以在一个项目里开发公共库，同时在另一个项目里导入并实时测试
- 代码改动后不用反复执行 `pip install`，节约大量时间

```shell
# 在项目根目录执行
pip install -e 目标工程路径
```

其原理是在 `site-packages` 中创建一个指向项目源码的链接（ `.pth` 文件），而不是复制一份代码过去。

```python
# 执行后，可以在任意位置导入
from duyi_utils import some_func
# 修改源码后，下次调用自动生效
```



### 作业

1. 完整一个库的构建、私有发布、安装
2. 使用费曼学习法复述一个库整个的构建流程。

## 项目管理工具

从上一节我们知道，构建和发布一个 Python 项目需要依赖 `venv`、`pip`、`build`、`twine` 等一系列工具，流程繁琐且容易出错。

**UV** 就是为解决这些问题而生的现代项目管理工具。

> 官方文档：https://docs.astral.sh/uv/

### [可选]pyenv 卸载

之前我们使用 `pyenv` 来管理多版本 Python，现在 UV 集成了 Python 版本管理功能（`uv python install` / `uv python list` / `uv python pin`），不再需要 `pyenv`，可以将其卸载。

#### macOS（Homebrew 安装）

```shell
# 1. 卸载 pyenv
brew uninstall pyenv

# 2. 删除残留的 pyenv 目录和数据
rm -rf ~/.pyenv

# 3. 编辑 ~/.zshrc，移除以下内容：
#    - eval "$(pyenv init -)"
#    - export PYTHON_BUILD_MIRROR_URL="..."
#    然后执行 source ~/.zshrc 刷新
```

#### Windows（pyenv-win）

```shell
# 1. 删除安装目录（默认路径）
rm -r $env:USERPROFILE\.pyenv

# 2. 打开「系统环境变量」，删除：
#    - 用户变量中的 PYENV
#    - 用户变量中的 PYTHON_BUILD_MIRROR_URL
#    - Path 中的 %USERPROFILE%\.pyenv\pyenv-win\bin 和 %USERPROFILE%\.pyenv\pyenv-win\shims
```

#### 验证

```shell
pyenv --version
# 输出类似：command not found: pyenv
# 说明卸载成功
```

### UV 简介

UV 是用 Rust 编写的极速 Python 包和项目管理器，来自 Astral 公司。

它致力于替代以下工具：

| 被替代的工具 | UV 对应命令 | 说明 |
| :--- | :--- | :--- |
| `pip` | `uv pip` | 安装包 |
| `pip-tools` | `uv lock` / `uv sync` | 锁定依赖版本，同步环境 |
| `pipx` | `uv tool` | 运行/安装 CLI 工具 |
| `virtualenv` / `venv` | `uv venv` | 管理虚拟环境 |
| `pyenv` | `uv python` | 管理多版本 Python |
| `poetry` / `pdm` | `uv init` / `uv add` / `uv remove` | 项目初始化、依赖管理 |

它的最大亮点是**快** —— 比 pip 快 10–100 倍。



### 安装

```shell
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS 上也支持 brew
brew install uv
```

安装后确认：

```shell
uv --version
```

> UV 会自动将自身添加到 `PATH`。如果找不到命令，可以手动将 `~/.local/bin` 加入 `PATH`。

#### 配置镜像源（国内加速）

由于网络原因，国内用户建议配置 PyPI 镜像源来加速包下载。

编写文件`~/.config/uv/uv.toml`

```shell
[[index]] # 优先看第一个镜像仓库 找不到看第二个
name = "aliyun-private"
url = "阿里云私有源地址"
default = true

[[index]]
name = "tuna"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

#### VSCode Code Runner 配置

```json
"python": "uv run"
```



### Python 版本管理

UV 集成了 Python 版本管理功能，无需再使用 `pyenv`。

```python
# 查看所有可用的 Python 版本（可安装的）
uv python list

# 查看本地已安装的 Python 版本
uv python list --only-installed

# 安装特定 Python 版本（例如 3.12.3）
uv python install 3.12.3

# 安装最新稳定版 Python
uv python install

# 安装多个版本
uv python install 3.11.9 3.12.3

# 卸载特定 Python 版本
uv python uninstall 3.12.3

# 查看当前环境使用的 Python 路径
uv python find

# 为当前项目固定 Python 版本（会在目录下生成 .python-version 文件）
uv python pin 3.12

# 移除当前项目的 Python 版本固定（删除 .python-version 文件）
uv python pin --rm

# 查看当前项目固定了哪个 Python 版本
uv python pin

# 使用特定 Python 版本执行临时命令（不修改项目设置）
uv run --python 3.11 python --version

# 创建虚拟环境时指定 Python 版本
uv venv --python 3.12

# 查看所有已安装的 Python 版本及其路径
uv python list --only-installed --verbose
```



### 快速上手：创建一个项目

#### 初始化项目

```shell
# 创建目录并初始化
uv init my-project 
cd my-project

# 对当前目录初始化
uv init

# 不创建git仓库
uv init --vcs none

# 生成src layout结构的目录
uv init --lib
```

#### 配置脚本

`uv init` 生成的项目默认没有入口模块配置。要让项目可以通过 `uv run` 直接执行，或发布后提供命令行工具，需要在 `pyproject.toml` 中配置 `[project.scripts]`：

```toml
[project.scripts]
# 等号左边是命令名称，右边是 "模块路径:函数名"
my-cli = "my_project:main"
```

配置后：
- 项目内执行 `uv run my-cli` 即可调用 `my_project/__init__.py` 中的 `main()` 函数
- 发布到 PyPI 后，用户 `pip install` 安装即可在终端使用 `my-cli` 命令

如果项目入口不是命令行工具而是一个脚本（如 `main.py`），可以通过 `[tool.uv].default-run` 指定默认入口，让 `uv run`（不加参数）直接执行：

```toml
[tool.uv]
default-run = "main.py"
```

#### 安装依赖

```shell
# 添加依赖
uv add requests

# 添加开发依赖
uv add --dev pytest

# 指定版本
uv add "fastapi>=0.100.0"
```

执行 `uv add` 后，UV 会自动：

1. 解析依赖树，找到满足所有约束的最新版本
2. 安装到当前项目的虚拟环境
3. 更新 `pyproject.toml` 中的 `dependencies`
4. 生成/更新 `uv.lock` 锁定文件

```shell
# 查看当前依赖树（类似 pipdeptree）
uv tree
```

输出示例：

```
my-project v0.1.0
├── certifi v2024.2.2
├── charset-normalizer v3.3.2
├── idna v3.6
├── pytest v8.1.1
│   ├── iniconfig v2.0.0
│   ├── packaging v24.0
│   └── pluggy v1.4.0
└── requests v2.31.0
    ├── certifi v2024.2.2
    ├── charset-normalizer v3.3.2
    ├── idna v3.6
    └── urllib3 v2.2.1
```

#### 移除依赖

```shell
uv remove requests
```

#### 同步环境

如果别人拉取了你的代码，或者你想根据 `pyproject.toml` / `uv.lock` 重建环境：

```shell
uv sync
```

`uv sync` 会根据 `uv.lock`（如果有）或 `pyproject.toml` 安装所有依赖，确保环境与锁文件一致。

#### 运行项目

```shell
# 运行指定文件
uv run src/main.py

# 运行指定模块
uv run -m src.main
```

`uv run` 会自动激活虚拟环境并执行命令，无需手动 `source .venv/bin/activate`。

### 虚拟环境管理

UV 可以独立管理虚拟环境，而不必依赖项目。

#### 创建虚拟环境

```shell
# 在当前目录创建 .venv
uv venv

# 指定目录
uv venv my-env

# 指定 Python 版本
uv venv --python 3.11

# 指定 Python 版本范围
uv venv --python 3.10
```

#### 激活与退出

```shell
# 激活
source .venv/bin/activate

# 退出
deactivate
```

#### 查看环境信息

```shell
uv venv --list   # 显示所有管理的 venv（需要配合项目）
```

> UV 会在项目根目录创建 `.venv`，并在 `pyproject.toml` 中记录。你不需要手动管理 `venv` 的路径——`uv run` 会自动检测。

#### UV 的项目级 vs 全局级

| 模式 | 命令 | 说明 |
| :--- | :--- | :--- |
| 项目级 | `uv add` / `uv sync` / `uv run` | 关联 `pyproject.toml`，依赖写入项目 |
| 全局级 | `uv pip install` / `uv venv` | 独立于任何项目，像传统 pip 一样使用 |

> UV 的全局模式兼容 pip 的用法。如果你有现成的 `requirements.txt`：
>
> ```shell
> uv pip install -r requirements.txt
> ```
>
> 项目模式比全局模式更推荐使用。

#### 全局缓存

UV 使用全局缓存（`~/.cache/uv`）来存储下载的包，多个项目共享同一份缓存。

```shell
# 查看缓存信息
uv cache dir

# 清理缓存
uv cache clean
```

### Running Tools —— 无需安装即可运行

在开发中经常需要临时运行一些工具，比如 `black`、`ruff`、`pre-commit` 等。传统做法是先 `pip install`，用完再卸载。UV 提供了更优雅的方式：

#### uvx —— 一键运行

```shell
# 运行一个工具，无需安装
uvx ruff check .

# 等价于传统的
# pip install ruff && ruff check . && pip uninstall ruff

# 指定版本
uvx bandit@1.7.5 .

# 传递参数（跟在 `--` 后面）
uvx cowsay -- "Hello, UV!"
```

`uvx` 会：

1. 在临时虚拟环境中安装指定包
2. 运行对应命令
3. 结束后清理环境

#### uv tool —— 持久安装 CLI 工具

如果你想长期使用一个工具：

```shell
# 安装
uv tool install ruff

# 运行
ruff check .

# 查看所有安装的工具
uv tool list

# 更新
uv tool upgrade ruff

# 卸载
uv tool uninstall ruff
```



#### 在项目中添加工具依赖

```shell
# 将工具作为开发依赖添加到项目中
uv add --dev ruff black mypy
```

然后在项目中：

```shell
uv run ruff check .
uv run black .
uv run mypy src/
```

> 通过 `uv add --dev` 安装的工具，其他协作者执行 `uv sync` 后同样可用，这是团队协作推荐的方式。

### 构建与发布

UV 内置了构建和发布功能，完全替代了 `build` + `twine`。

#### 构建

```shell
# 构建 sdist 和 wheel
uv build

# 产物在 dist/ 目录下
ls dist/
# my_project-0.1.0.tar.gz
# my_project-0.1.0-py3-none-any.whl
```

> `uv build` 会读取 `pyproject.toml` 中的 `[build-system]` 配置，使用后端工具（如 `hatchling`）完成构建。

#### 发布

```shell
# 发布到 PyPI
uv publish

# 指定 token（推荐用环境变量）
UV_PUBLISH_TOKEN=pypi-xxxxx uv publish

# 发布到私有仓库
uv publish \
  --publish-url 私有仓库地址\
  --username 你的用户名\
  --password 你的密码\
  dist/*
```

> `uv publish` 直接替代了 `twine upload`。
>
> 首次发布需要先在 pypi.org 注册账号并创建 API token，UV 也支持使用 `.pypirc` 配置文件。



### Makefile —— 统一项目命令入口

> `make` 是 macOS 和 Linux 系统自带的工具，但 Windows 默认没有。Windows 用户可以按以下方式安装：
>
> ```shell
> # 方式一：Chocolatey（推荐）
> choco install make
>
> # 方式二：winget
> winget install GnuWin32.Make
>
> # 方式三：通过 Git Bash 安装（安装 Git 时勾选 Git Bash 即可）
> # 然后在 Git Bash 中运行 make，或将其加入 PATH
> ```
>
> 安装后验证：
>
> ```shell
> make --version
> ```

虽然 UV 提供了丰富的命令，但团队成员（或未来的你）仍需要记住 `uv run pytest`、`uv run ruff check`、`uv build` 等一串命令。**Makefile** 可以把常用操作封装成简短一致的名字。

#### 一个典型的 Python + UV 项目的 Makefile

```makefile
.PHONY: install test lint format build clean

# 安装依赖
install:
	uv sync

# 运行测试
test:
	uv run pytest

# 代码检查
lint:
	uv run ruff check .

# 自动格式化
format:
	uv run ruff format .

# 构建分发包
build:
	uv build

# 清理构建产物和缓存
clean:
	rm -rf dist/
	rm -rf .pytest_cache/
	uv cache clean
```

使用方式：

```shell
make install   # uv sync
make test      # uv run pytest
make lint      # uv run ruff check .
make format    # uv run ruff format .
make build     # uv build
make clean     # 清理
```

#### 带参数的目标

```makefile
.PHONY: publish

# 发布到指定仓库，用法: make publish REPO_URL=https://...
publish:
	uv publish --publish-url $(REPO_URL)
```

#### 串联多个任务

```makefile
.PHONY: ci

# CI 流程：检查 → 测试 → 构建
ci: 
	lint test build
```

```shell
make ci   # 依次执行 lint → test → build
```

> Makefile 的核心价值是**约定**：不管项目用什么工具链，新人只需 `make test` 就能跑测试，`make build` 就能构建。对于 CI/CD 也天然适配。

### 常用命令速查

| 命令 | 作用 |
| :--- | :--- |
| `uv init` | 初始化新项目 |
| `uv add` | 添加依赖 |
| `uv remove` | 移除依赖 |
| `uv sync` | 同步环境（安装/更新依赖） |
| `uv lock` | 更新锁定文件 |
| `uv run` | 在项目环境中运行命令 |
| `uv tree` | 查看依赖树 |
| `uv build` | 构建分发包 |
| `uv publish` | 发布到 PyPI |
| `uv venv` | 创建虚拟环境 |
| `uv python install` | 安装 Python 版本 |
| `uv python list` | 列出已安装的 Python |
| `uv python pin` | 锁定项目 Python 版本 |
| `uv tool install` | 安装 CLI 工具 |
| `uv tool run` / `uvx` | 临时运行 CLI 工具 |
| `uv cache clean` | 清理缓存 |

### 作业

1. 将`27. 异步编程`的代码改造成UV工程的格式。
2. 将`29. 构建发布`的代码使用uv发布到阿里云私有仓库

## Monorepo

### 什么是 Monorepo

**Monorepo**（单一仓库）是将多个相关的项目/包放在同一个代码仓库中管理的策略。

```
my-monorepo/
├── packages/
│   ├── utils/          # 公共工具库
│   ├── client-sdk/     # 客户端 SDK
│   └── web-app/        # Web 应用
├── pyproject.toml      # workspace 根配置
└── README.md
```

#### Multirepo VS Monorepo

| 对比维度 | MultiRepo | Monorepo |
| :--- | :--- | :--- |
| **代码共享** | 需要发版、发布 pip 包才能共享 | 源码级别直接引用，即时生效 |
| **原子提交** | 跨仓库改动需要多个 PR 协同 | 一次提交完成所有关联改动 |
| **工具规范** | 各仓库独立配置工具 | 统一的工具与规范 |
| **重构成本** | 跨仓库重构代价极高 | 工具链覆盖整个仓库，安全重构 |
| **CI/CD** | 多个 Pipeline 各自独立 | 统一 CI，可增量检测受影响的包 |
| **适用场景** | 团队独立、版本节奏不一致的项目 | 紧密协作的微服务、SDK 集合、工具链 |



### 搭建 Workspace

> uv workspace文档：https://docs.astral.sh/uv/concepts/projects/workspaces/#using-workspaces

#### 第一步：初始化根项目

```shell
mkdir my-monorepo && cd my-monorepo
uv init
```

根级 `pyproject.toml`：

```toml
# 添加 members
[tool.uv.workspace]
members = [
    "packages/*",
    "app/*",
]
```

`members` 支持 glob 模式：

| 模式 | 匹配范围 |
| :--- | :--- |
| `packages/*` | `packages/` 下的直接子目录 |
| `packages/**` | `packages/` 下的所有子目录（含嵌套） |
| `libs/*` | `libs/` 下的直接子目录 |
| `apps/*` | `apps/` 下的直接子目录 |

可以同时配置多个目录：

```toml
[tool.uv.workspace]
members = [
    "packages/*",
    "apps/*",
    "libs/*",
]
```

#### 第二步：创建成员包

```shell
uv init --lib packages/agents
uv init --lib packages/shared
uv init app/web-service
```

#### 第三步：成员包依赖

```toml
# packages/agents/pyproject.toml
dependencies = [
    "shared",
]

[tool.uv.sources]
shared = { workspace = true }

# app/web-service/pyproject.toml
dependencies = [
    "agents",
]

[tool.uv.sources]
agents = { workspace = true }
```

> **`[tool.uv.sources]`** 是 UV workspace 的**核心机制**。它告诉 UV：`utils` 依赖不从 PyPI 下载，而是从工作区内的同名成员包中链接。
>
> 如果某个包在 PyPI 和 workspace 中同名，workspace 优先。需要强制走 PyPI 时可以写成 `utils = { workspace = false }`。

#### [可选]第四步：同步安装

```shell
uv sync --all-packages
```

执行后：

1. UV 读取所有成员包的 `pyproject.toml`
2. 解析完整的依赖树（包括成员间的依赖）
3. 在根目录生成统一的 `uv.lock`
4. 在根目录创建 `.venv`，安装所有依赖

#### 第五步：运行

```shell
uv run --package web-service python app/web-service/main.py
```



#### [可选]使用Makefile

```makefile
.PHONY: run-web

run-web:
	uv run --package web-service python app/web-service/main.py
```

#### [可选]安装第三方依赖

```shell
# 给某个成员包添加依赖
uv add --package <成员包> <包名>

# 给项目根添加依赖
uv add --dev <包名>
```

#### [可选]构建

```shell
# 构建全部
uv build

# 构建指定包
uv build --package utils
```

#### [可选]查看依赖关系

```shell
# 查看 workspace 中某个包的依赖树
uv tree --package web-app

# 查看所有包的依赖树
uv tree
```

输出示例：

```
web-app v0.1.0
├── data-tools v0.1.0 (workspace)
│   └── pandas v2.1.0
│       ├── numpy v1.26.0
│       └── python-dateutil v2.8.2
└── utils v0.1.0 (workspace)
```

workspace 中的包会标记为 `(workspace)`，一目了然。

### 包间依赖的三种模式

#### 源码链接（workspace 模式）

```toml
[tool.uv.sources]
utils = { workspace = true }
```

- 本地直接引用源码，修改即时生效
- 无需 `pip install -e .` 或 `uv add` 重新安装
- 适合日常开发

#### 路径引用

```toml
[tool.uv.sources]
utils = { path = "../utils" }
```

- 引用工作区之外的本地包
- 路径可以是相对或绝对路径

#### Git 引用

```toml
[tool.uv.sources]
utils = { git = "https://github.com/org/utils.git", rev = "v0.1.0" }
```

- 引用 Git 仓库中的某个版本
- 可用于引用未发布到 PyPI 的依赖

### 作业

手工复现本节课工程，并将`shared`、`agents`发布到阿里云制品仓库

## 断点调试

### 调试组件

![image-20260603142319059](https://resource.duyiedu.com/yuanjin/202606031423132.png)

### 调试原理

待调试的文件

```python
# demo.py

def main():
    a = 1
    b = 2
    c = a + b
    return c


r = main()
print(r)
```

调试适配器的核心逻辑

```python
# debugpy

import os
import sys

# 获取当前代码文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "demo.py")

code = open(file_path, "r").read()


def my_tracer(frame, event, arg):
    print(f"事件: {event}, 行号: {frame.f_lineno}")
    return my_tracer


sys.settrace(my_tracer)
exec(code)
```

### 单文件调试

```json
{
  // 使用 IntelliSense 了解相关属性。
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python 调试程序: 当前文件", // 调试名称
      "type": "debugpy", // 调试器类型
      "request": "launch", // 调试请求类型
      "program": "${file}", // 要调试的程序，使用当前打开的文件
      "console": "integratedTerminal" // 在集成终端中运行调试程序
    }
  ]
}
```

### 工程调试

#### 一、配置

安装依赖

```shell
uv add --dev debugpy
```

配置调试器

```makefile
# Makefile
run-web-debug:
	uv run --package web-service python -m debugpy --listen 5678 --wait-for-client app/web-service/main.py
```

配置调试客户端

```json
{
  // 使用 IntelliSense 了解相关属性。
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to make run",
      "type": "debugpy",
      "request": "attach", // 使用附加模式
      "connect": {
        "host": "localhost",
        "port": 5678
      }
    }
  ]
}
```

#### 二、启动调试

1. 启动调试器

```shell
make run-web-debug
```

2. 启动调试客户端

### 作业

复现monorepo工程的调试
# python web框架
## Web服务框架

### Python Web服务框架对比

|     对比维度     | 🏢 Django                                                     | 🧰 Flask                                                      | 🚀 FastAPI                                                    |
| :--------------: | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
|   **官网链接**   | [Django](https://www.djangoproject.com/)                     | [Flask](https://flask.palletsprojects.com/en/stable/)        | [FastAPI](https://fastapi.tiangolo.com/)                     |
|   **诞生年份**   | 2005年                                                       | 2010年                                                       | 2018年                                                       |
|   **核心哲学**   | **开箱即用 (Batteries-included)** 内置ORM、后台管理、用户认证等几乎所有常用功能 | **微内核，可扩展 (Microframework)** 只提供最基础的核心功能，其他如数据库、表单等按需选择 | **高性能，现代化 (High-performance)** 利用类型注解和异步特性，专为API设计而生 |
| **性能 (速度)**  | **较慢** (约 5k req/s 对于Hello World)                       | **中等** (约 9k req/s 对于Hello World)                       | **极快** (约 30k req/s 对于Hello World)                      |
|   **学习曲线**   | **较陡**。功能多，概念多，需要学习的体量较大                 | **平缓**。设计简洁，核心API直观，非常适合初学者入门          | **中等**。性能优势明显，但需要理解类型注解和异步编程         |
| **最适合的场景** | • 大型、复杂的Web应用（如电商平台、CMS） <br />• 需要自带后台管理系统的项目 • 希望有统一解决方案的团队项目 | • 小型应用和快速原型开发 <br />• 简单的RESTful API <br />• 对组件有高度定制化需求的项目 | • 高性能的API服务 <br />• 微服务架构 <br />• 需要将AI/机器学习模型封装成API服务 |
|   **知名用户**   | Instagram, Pinterest, Disqus                                 | Airbnb, Netflix, Reddit (部分功能)                           | Uber, Netflix, Microsoft (部分内部项目)                      |

### 第一个FastAPI应用

#### 安装

```python
uv add --package web-service "fastapi[standard]==0.136.3"
```

`库名[额外安装名/可选安装名]==版本号`

```toml
# pyproject.toml
[project.optional-dependencies]
standard = [
    "fastapi-cli[standard] >=0.0.8",
    "fastar >= 0.9.0",
    # For the test client
    "httpx >=0.23.0,<1.0.0",
    # For templates
    "jinja2 >=3.1.5",
    # For forms and file uploads
    "python-multipart >=0.0.18",
    # To validate email fields
    "email-validator >=2.0.0",
    # Uvicorn with uvloop
    "uvicorn[standard] >=0.12.0",
    # # Settings management
    "pydantic-settings >=2.0.0",
    # # Extra Pydantic data types
    "pydantic-extra-types >=2.0.0",
]
```

#### 代码

```python
# apps/web-service/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

```

#### 启动

```shell
# Makefile

.PHONY: dev

dev:
	uv run --package web-service fastapi dev apps/web-service/main.py --port 8080

```

```shell
make dev
```

#### 访问

打开浏览器访问下面的地址:

- http://localhost:8080/
- http://localhost:8080/items/5?q=key_words
- http://localhost:8080/docs
- http://localhost:8080/redoc

### 核心概念

#### `WSGI` vs `ASGI`

`WSGI / ASGI`是一套`Python`的社区规范，主要为**Web服务器**和**Web应用程序**提供统一的交互标准

![image-20260605143504189](https://resource.duyiedu.com/yuanjin/202606051435295.png)

其中，`WSGI`是一个早期标准，用于**多线程**处理请求任务，`ASGI`是一个现代标准，用于**异步**处理请求任务。

理解`ASGI`关键是要理解：

1. `ASGI`服务器在做什么？
2. `ASGI`应用程序在做什么？
3. 服务器和应用程序如何对接？

##### ASGI服务器

主要负责：

- `socket`通信
  - 端口监听
  - 接受新的客户端连接
  - 从 socket 读取原始字节流
  - 将响应字节流写回 socket
- 报文解析
  - 解析 HTTP/1.1、HTTP/2、WebSocket 协议
  - 将原始字节（如 `b'GET /users/123 HTTP/1.1\r\n...'`）转换成结构化数据（如 method、path、headers）
  - 处理分块传输、Keep-Alive、管道化等协议细节
- 实现和启动事件循环
- 管理进程和线程
- ...

常见`ASGI`服务器

| 服务器         | 核心特点                                 | 协议支持                           | 适用场景                       |
| :------------- | :--------------------------------------- | :--------------------------------- | :----------------------------- |
| **Uvicorn**    | 基于 uvloop + httptools，性能极高        | HTTP/1、WebSocket（HTTP/2 实验性） | FastAPI/Starlette 首选，最流行 |
| **Hypercorn**  | 基于 sans-io 架构，协议支持最全          | HTTP/1、HTTP/2、HTTP/3、WebSocket  | 需要 HTTP/2/3 的场景           |
| **Daphne**     | Django Channels 官方服务器，Twisted 实现 | HTTP/1、HTTP/2、WebSocket          | Django 异步项目                |
| **Granian**    | Rust 实现，性能极致                      | HTTP/1、HTTP/2、WebSocket          | 追求极致性能的生产环境         |
| **Gunicorn**   | 传统 WSGI 服务器，通过 worker 支持 ASGI  | HTTP/1                             | 需要多进程 + ASGI 的混合部署   |
| **NGINX Unit** | 通用应用服务器，原生支持 ASGI            | HTTP/1、HTTP/2                     | 统一管理多语言应用的场景       |

##### ASGI应用程序

主要负责：业务逻辑

常见`ASGI`应用框架：`Django`、`FastAPI`、`starlette`、`...`

##### 如何对接

`ASGI`标准规定，`ASGI`应用程序必须通过`ASGI`服务器启动，启动时，`ASGI`应用程序必须对外暴露一个可调用对象：`app`

```python
# app规格
app(scope, receive, send) -> CoroutineType:
    """
    ASGI 应用程序的调用签名
    
    参数:
        scope (dict): 包含连接上下文信息的字典
                      - type: 连接类型，如 "http", "websocket", "lifespan"
                      - path: 请求路径 (http)
                      - method: 请求方法 (http)
                      - headers: 请求头列表
                      - ... 其他协议相关字段
    
        receive (callable): 异步无参数函数，用于接收消息
                            await receive() -> dict
                            用于获取请求体 (http) 或客户端消息 (websocket)
    
        send (callable): 异步单参数函数，用于发送消息
                         await send(message)
                        用于发送响应头/体 (http) 或服务端消息 (websocket)
    """
    # 应用程序逻辑
    pass
```

##### 完整流程

1. ASGI服务器监听端口
2. 请求到达ASGI服务器
   1. 处理字节流
   2. 构建scope字典
   3. 定义send函数
   4. 定义receive函数
   5. 调用`app`
3. 请求进入ASGI应用程序（期间调用`receive`和`send`）
   1. ASGI框架调用预定义的程序（路由）
   2. 处理业务逻辑
4. 控制权交给ASGI服务器
   1. 组装完整响应报文
   2. 发送响应给客户端

#### `Swagger UI` vs `Redoc`

OpenAPI规范指的是用一个标准的JSON格式来描述API接口

试试这个地址：http://localhost:8080/openapi.json

> `openapi.json` 遵循的标准是 **OpenAPI 规范 (OpenAPI Specification, OAS)**。
>
> 这个规范最初由 **Swagger** 工具集的创建者 **Tony Tam** 于 2010 年发起，当时被称为 **Swagger 规范**。为了让其成为行业通用标准，Swagger 规范的核心被捐赠给了 **Linux 基金会**，并于 2015 年成立了 **OpenAPI 倡议 (OpenAPI Initiative, OAI)** 来专门负责它的演进和管理。从 3.0 版本开始，这个规范正式更名为 **OpenAPI 规范**。

当首次启动时，`FastAPI`会自动生成`openapi.json`，并将其暴露到`/openapi.json`路由中

| 特性 (Feature)   | Swagger UI (`/docs`)                                         | ReDoc (`/redoc`)                                             |
| :--------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **核心功能**     | **交互式测试**                                               | **文档阅读**                                                 |
| **"Try it out"** | ✅ **支持**。可以直接在网页上填入参数并点击发送，实时测试 API 并查看返回结果。 | ❌ **不支持**。纯只读模式，专注于清晰展示信息。               |
| **界面风格**     | 功能全面，支持认证、请求头等复杂操作配置。                   | 视觉上更简洁美观，注重可读性，通过三栏式布局让 API 结构一目了然。 |
| **性能**         | 加载大型 API 文档时，初始渲染可能稍慢。                      | 采用**惰性加载**策略，滚动到哪就渲染到哪，在处理包含上百个接口的大型项目时，首屏加载速度更快，内存占用更低。 |
| **适用场景**     | **开发调试**阶段。方便后端开发者和测试人员快速验证接口逻辑。 | **对外发布**阶段。适合作为面向团队外部或公众的 API 参考文档，展示正式、稳定的接口规范。 |

你可以使用路由中的字典参数添加更多文档配置：

```python
@app.get("/", summary="Hello World", description="这是一个测试接口")
def read_root():
    return {"Hello": "World"}
```

> 更多的配置见：https://fastapi.tiangolo.com/zh/tutorial/path-operation-configuration/

你也可以禁用这些能力

```python
app = FastAPI(
    docs_url=None,      # 禁用 Swagger UI (/docs)
    redoc_url=None,     # 禁用 ReDoc (/redoc)
    openapi_url=None    # 禁用 openapi.json 端点
)
```

你也可以根据不同的环境决定是否禁用

```python
# 根据环境变量决定
import os
is_production = os.getenv("ENVIRONMENT") == "production"

app = FastAPI(
    docs_url=None if is_production else "/docs",
    redoc_url=None if is_production else "/redoc",
    openapi_url=None if is_production else "/openapi.json"
)
```

#### Pydantic

官方网站：https://pydantic.dev/

`Pydantic` 是一个全能的**数据建模与处理框架**，它的核心功能是实现数据校验和转换，从而确保数据的高可用

```python
from datetime import datetime
from pydantic import BaseModel


# 1. 定义数据模型（就像一个表单模板）
class User(BaseModel):
    id: int  # 要求必须是整数
    name: str = "John Doe"  # 字符串，且有默认值
    signup_ts: datetime | None = None  # 可以是日期时间或空
    friends: list[int] = []  # 整数列表


# 2. 输入外部数据（通常是 API 请求或文件读取）
# 注意：这里的 'id' 是字符串 '123'，'friends' 中包含了字符串和字节数据
external_data = {
    "id": "123abc",
    "signup_ts": "2024-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# 3. Pydantic 进行验证和转换
user = User(**external_data)

# 4. 打印结果
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2024, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123 (这里已经是整数类型，不再是字符串)
print(user.friends)
# > [1, 2, 3]

```

`Pydantic`集成到了`FastAPI`中，在请求和响应时会自动进行验证，验证失败会抛出`ValidationError`

`FastAPI`也会读取到`Pydantic`的模型，将其生成到`openapi.json`中

你可以精细的描述模型内部字段

```python
class Item(BaseModel):
    # ✅ 带默认值的可选字段
    item_id: int | None = Field(
        default=None,  # 默认值
        title="商品ID",  # 标题
        description="商品的唯一标识符，在创建商品时可忽略，系统会自动生成。",  # 描述
        ge=1,  # 大于等于1
        examples=[1, 2, 3],  # 示例值列表
    )

    # ✅ 必填字段的写法
    name: str = Field(
        ...,  # 三个点表示必填
        title="商品名称",
        description="商品的显示名称，长度必须在2到10个字符之间。",
        min_length=2,
        max_length=10,
        examples=["无线鼠标"],
    )

    # ✅ 带默认值的价格字段
    price: float = Field(
        default=0.0,  # 默认值
        title="商品价格",
        description="商品的销售价格，必须大于或等于0。",
        ge=0.0,
        examples=[19.99, 0.0, 100.5],  # 示例值列表
    )
```

### 作业(done)

1. 跟随课堂完成示例程序
2. 复述：
**什么是WSGI和ASGI？**
-  WSGI和ASGI都是web应用程序和web服务器之间的通行协议，WSGI是早期处理多线程的协议，而ASGI是现代处理异步的协议
**ASGI服务器和ASGI应用是如何协作的？**
- `ASGI`应用程序必须通过`ASGI`服务器启动，启动时，`ASGI`应用程序必须对外暴露一个可调用对象：`app`
**Uvicorn是什么？**
- 是ASGI服务器
**Starlette是什么？**
- 是一个ASGI框架，FastAPI 直接构建在 Starlette 之上，并添加了数据验证、依赖注入和自动 API 文档等高级功能
**OpenAPI是什么？**
- OpenAPI是一个规范：规定用一个标准的JSON格式来描述API接口
**Swagger UI是什么？Redoc是什么？**
- Swagger UI是一个交互式的OpenApi接口文档，可以直接在网页接口测试
- Redoc是一个仅阅读的OpenApi接口文档，不可测试
**Pydantic是什么？**
- 是一个全能的数据建模与处理框架，它的核心功能是实现数据校验和转换，从而确保数据的高可用

## 优化包结构

### 重组包结构

```
apps/web-service/
├── pyproject.toml
├── app/												 # web应用
│   ├── __init__.py
│   ├── main.py                  # FastAPI 应用入口
│   ├── core/                    # 核心基础设施
│   │   └── __init__.py
│   ├── api/                     # 路由层
│   │   └── __init__.py
│   └── schema/                 # Pydantic 请求/响应模型
│        └── __init__.py
├── test/											 # 测试脚本
     └──  __init__.py	
```

更新`Makefile`

```makefile
# Makefile

.PHONY: dev

dev:
	export PYTHONDONTWRITEBYTECODE=1; \
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080
```

### 使用环境变量

创建`.env`、`.env.example`文件

```yaml
# web服务配置
WEB_APP_NAME=渡一web服务
```

安装`pydantic-settings`

```shell
uv add --package web-service pydantic-settings==2.14.1
```

创建`core/config.py`

```python
from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    environment: str = "development"


class WebSettings(BaseSettings):
    app_name: str = "Web Service API"  # 实际读取 WEB_APP_NAME

    # 配置读取方式
    model_config = {
        "env_file": ".env",  # env文件的位置
        "env_prefix": "WEB_",  # 当前类中的字段使用的前缀
    }


common_settings = CommonSettings()
web_settings = WebSettings()

```

修改`main.py`

```python
# ...

from app.core.config import common_settings, web_settings

app = FastAPI(
    title=web_settings.app_name,
    docs_url=None if common_settings.environment == "production" else "/docs",
    redoc_url=None if common_settings.environment == "production" else "/redoc",
    openapi_url=(
        None if common_settings.environment == "production" else "/openapi.json"
    ),
)


# ...
```

访问：http://127.0.0.1:8080/docs 试一试

### 创建DTO
**DTO**:全称Data Transfer Object,数据传输对象，客户端与web服务器传输的数据结构

```python
# schema/item.py
from pydantic import BaseModel, Field


class Item(BaseModel):
    item_id: int | None = Field(
        default=None,
        title="商品ID",
        description="商品的唯一标识符，在创建商品时可忽略，系统会自动生成。",
        ge=1,
        examples=[1, 2, 3],
    )

    name: str = Field(
        ...,
        title="商品名称",
        description="商品的显示名称，长度必须在2到10个字符之间。",
        min_length=2,
        max_length=10,
        examples=["无线鼠标"],
    )

    price: float = Field(
        default=0.0,
        title="商品价格",
        description="商品的销售价格，必须大于或等于0。",
        ge=0.0,
        examples=[19.99, 0.0, 100.5],
    )

```

修改`main.py`

### 使用路由

`api/welcome.py`

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Hello World", description="这是一个测试接口")
async def read_root():
    return {"Hello": "World"}

```

`api/items.py`

```python
from fastapi import APIRouter

from app.schema.item import Item

router = APIRouter(prefix="/items")


@router.get("/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

```

`main.py`

```python
from fastapi import FastAPI
from app.core.config import common_settings, web_settings

app = FastAPI(
    title=web_settings.app_name,
    docs_url=None if common_settings.environment == "production" else "/docs",
    redoc_url=None if common_settings.environment == "production" else "/redoc",
    openapi_url=(
        None if common_settings.environment == "production" else "/openapi.json"
    ),
)


from app.api.welcome import router as welcome_router
from app.api.items import router as items_router

app.include_router(welcome_router)
app.include_router(items_router)

```



### FastAPI插件

安装`VSCode`的`FastAPI Extension`插件

### 断点调试

1. 使用`debugpy`启动`main.py`

```shell
# 安装 debugpy
uv add --dev debugpy
```

```makefile
# Makefile

.PHONY: dev debug

dev:
	export PYTHONDONTWRITEBYTECODE=1; \
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080

debug:
	export PYTHONDONTWRITEBYTECODE=1; \
	uv run --package web-service python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m fastapi dev apps/web-service/app/main.py --port 8000
```

```shell
# 启动调试服务器
make debug
```

2. 启动调试客户端

```json
{
  // 使用 IntelliSense 了解相关属性。
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to make run",
      "type": "debugpy",
      "request": "attach", // 使用附加模式
      "connect": {
        "host": "localhost",
        "port": 5678
      }
    }
  ]
}
```

## 初识 SQLAlchemy

官网地址：https://docs.sqlalchemy.org/en/20/index.html

### 创建数据库

启动数据库容器

```shell
docker run -d \
  --name duyi_pg_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=123123 \
  -p 5432:5432 \
  -v "你的目录绝对路径:/var/lib/postgresql/data" \
  postgres:16
```

创建数据库`duyi_db`

```shell
# 进入容器创建数据库
docker exec -it duyi_pg_db psql -U admin -c "CREATE DATABASE duyi_db;"
```

验证数据库是否创建成功：

```shell
docker exec -it duyi_pg_db psql -U admin -l
```

### 安装 SQLAlchemy

```shell
uv add --package web-service 'sqlalchemy[asyncio]==2.0.50' asyncpg==0.31.0
```

### 测试连接

```python
# model/main.py
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

# 异步连接字符串格式：postgresql+asyncpg://用户名:密码@主机:端口/数据库名
DATABASE_URL = "postgresql+asyncpg://admin:123123@localhost:5432/duyi_db"


async def test_connection():
    # 创建异步引擎
    config = {
        "pool_size": 10,  # 连接池维持的连接数
        "max_overflow": 20,  # 池满后额外可创建的连接数
        "pool_pre_ping": True,  # 每次连接前检查是否存活
        "echo": False,  # 是否打印 SQL 日志
    }
    engine = create_async_engine(DATABASE_URL, **config)

    try:
        # 测试连接：执行一个简单的查询
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            # 获取结果(第一行第一列)
            value = result.scalar()
            print(f"✅ 异步连接 PostgreSQL 成功！查询结果: {value}")
    except Exception as e:
        print(f"❌ 连接失败: {e}")
    finally:
        # 关闭引擎，释放资源
        await engine.dispose()


# 运行异步函数
if __name__ == "__main__":
    asyncio.run(test_connection())

```

### 认识概念（SQLAIchemy是啥？）

![image-20260615181032104](https://resource.duyiedu.com/yuanjin/202606151810206.png)

- SQLAlchemy（ORM框架）
  - engine
    - 管理连接池
        - 连接池是啥
            - 用来管理asyncpg驱动程序与数据库直接的连接
        - 连接池作用
            - 避免频繁建立关闭连接带来的性能开销
        - 池大小
            - 最大可以保留多少个连接
    - 处理不同数据库的差异
        - 例如使用不同数据库和不同驱动去连接数据库
- asyncpg：仅负责和PostgreSQL数据库通信

### 优化代码结构

`.env` + `.env.example`

```yaml
# web服务配置
WEB_APP_NAME=渡一web服务 # 站点名称，影响API文档标题

# 数据库配置
DB_HOST=localhost # 数据库主机
DB_PORT=5432 # 数据库端口
DB_NAME=duyi_db # 数据库名称
DB_USER=admin # 连接账号
DB_PASSWORD=123123 # 连接密码
```

`core/config.py`

```python
from pydantic_settings import BaseSettings


class _BaseSettingsWithEnv(BaseSettings):
    # 配置读取方式
    model_config = {"env_file": ".env"}  # env文件的位置


# 通用配置
class _CommonSettings(_BaseSettingsWithEnv):
    environment: str = "development"


# web服务配置
class _WebSettings(_BaseSettingsWithEnv):
    app_name: str = "Web Service API"  # 实际读取 WEB_APP_NAME

    # 配置读取方式
    model_config = {"env_prefix": "WEB_"}


# 数据库配置
class _DBSettings(_BaseSettingsWithEnv):
    host: str = ""
    port: str = ""
    name: str = ""
    user: str = ""
    password: str = ""

    model_config = {"env_prefix": "DB_"}


common_settings = _CommonSettings()
web_settings = _WebSettings()
db_settings = _DBSettings()

```

`model/engine.py`

```python
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.core.config import db_settings

_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine

    if _engine is None:
        url = f"postgresql+asyncpg://{db_settings.user}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}"
        _engine = create_async_engine(
            url,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,
            echo=False
        )

    return _engine

```

`model/main.py`

```python
import asyncio
from sqlalchemy import text
from app.model.engine import get_engine


async def test_connection():
    engine = get_engine()
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            value = result.scalar()
            print(f"✅ 异步连接 PostgreSQL 成功！查询结果: {value}")
    except Exception as e:
        print(f"❌ 连接失败: {e}")
    finally:
        await engine.dispose()


# 运行异步函数
if __name__ == "__main__":
    asyncio.run(test_connection())

```



### 作业

回答以下问题：

1. 连接池有什么用？
2. 连接池的连接是不是越多越好？
3. 数据库驱动是什么？
## ORM

> [!NOTE]
>
> 小贴士
>
> 快速删除所有表
>
> ```sql
> DROP SCHEMA public CASCADE;
> CREATE SCHEMA public;
> ```



### [补充]处理运行bug


`apps/web-service/pyproject.toml`

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["app/"]
```

```shell
uv sync --all-packages
```

`apps/web-service/app/core/config.py`

```python
class _BaseSettingsWithEnv(BaseSettings):
    # 配置读取方式
    model_config = {"env_file": ".env", "extra": "ignore"}  # env文件的位置
```

### 什么是ORM？

**ORM（Object Relational Mapping）** 将数据库中的"表"映射为 Python 中的"类"，将"一行记录"映射为"对象实例"；简单说：让你用操作对象的方式，来操作数据库里的表和行，而不用直接写 SQL。

先在 `model/` 下新建 `base.py`：

```python
# model/base.py
from datetime import datetime

from sqlalchemy import DateTime, Identity, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class IDMixin:
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

```

所有模型类继承这个 `Base`。

#### Category 模型

```python
# model/category.py
from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.association import product_category
from app.model.base import Base, IDMixin

if TYPE_CHECKING:
    from app.model.product import Product


class Category(Base, IDMixin):

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text, default="")

    products: Mapped[list["Product"]] = relationship(
        secondary=product_category, back_populates="categories"
    )

```

`relationship` 此时只是声明关系，不影响建表。建表只认 `mapped_column`。

#### Product 模型

```python
# model/product.py
from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.association import product_category
from app.model.base import Base, IDMixin, TimestampMixin

if TYPE_CHECKING:
    from app.model.category import Category
    from app.model.sku import Sku


class Product(Base, IDMixin, TimestampMixin):

    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    brand: Mapped[str | None] = mapped_column(String(100))

    categories: Mapped[list["Category"]] = relationship(
        secondary=product_category, back_populates="products"
    )
    skus: Mapped[list["Sku"]] = relationship(back_populates="product")

```

#### SKU 模型

```python
# model/sku.py
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model.base import Base, IDMixin

if TYPE_CHECKING:
    from app.model.product import Product


class Sku(Base, IDMixin):

    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE")
    )
    sku_code: Mapped[str] = mapped_column(String(50), unique=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(default=0)
    attrs: Mapped[dict] = mapped_column(JSONB)
    image_url: Mapped[str] = mapped_column(String)

    product: Mapped["Product"] = relationship(back_populates="skus")

```

#### product_category关系表

```python
# model/association/product_category.py
from sqlalchemy import Column, ForeignKey, Table

from app.model.base import Base

product_category = Table(
    "product_category",
    Base.metadata,
    Column("product_id", ForeignKey("product.id"), primary_key=True),
    Column("category_id", ForeignKey("category.id"), primary_key=True),
)

```

```python
# model/association/__init__.py
from app.model.association.product_category import product_category

__all__ = ["product_category"]
```



### 表结构同步

在 `model/main.py` 中写建表逻辑：

```python
# model/main.py
import asyncio
from sqlalchemy import text
from app.model.engine import get_engine
from app.model.base import Base
from app.model.category import Category   # noqa: F401
from app.model.product import Product     # noqa: F401
from app.model.sku import Sku             # noqa: F401


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def test_connection():
    engine = get_engine()
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            value = result.scalar()
            print(f"✅ 连接成功！查询结果: {value}")
    except Exception as e:
        print(f"❌ 连接失败: {e}")


async def main():
    await init_db()
    await test_connection()


if __name__ == "__main__":
    asyncio.run(main())
```

### ORM核心概念

![image-20260616141327046](https://resource.duyiedu.com/yuanjin/202606161413092.png)
**1.engine是啥？**
engine就是ORM框架，SQLAIchemy提供

**2.dialect模块的作用？**
1.记录py代码中的对数据的操作,翻译成sql语句记录（仅记录，暂未执行sql）
2.最后到特定代码执行的时候交给连接池的连接去执行sql

**3.pool的作用？**
1.管理数据库线程池的线程连接
### 作业

回答以下问题：

1. 如何处理多对多关系？什么时候使用模型？什么时候使用表？
1. ORM中，什么是dialect，它的作用是什么？它和连接有什么关系？
## 数据操作(CRUD)
C:即create，创建数据
R:即read,读数据
U:即update，更新数据
D:即Delete,删除数据

### Core

#### Raw SQL

```python
# model/main.py
import asyncio
from sqlalchemy import text
from app.model.engine import get_engine
from app.model.base import Base
import app.model.category  # noqa: F401
import app.model.product  # noqa: F401
import app.model.sku  # noqa: F401


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def raw_sql_insert():
    """直接用 SQL 字符串插入数据"""
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.execute(
            text(
                "INSERT INTO product (name, description, brand) VALUES ('iPhone 16', '最新款智能手机', 'Apple')"
            )
        )
        await conn.execute(
            text(
                "INSERT INTO product (name, description, brand) VALUES ('iPhone 15', '上一代旗舰', 'Apple')"
            )
        )
        await conn.execute(
            text(
                "INSERT INTO product (name, description, brand) VALUES ('Galaxy S25', '三星旗舰', 'Samsung')"
            )
        )
        await conn.execute(
            text(
                "INSERT INTO product (name, description, brand) VALUES ('Xiaomi 15', '性价比之选', 'Xiaomi')"
            )
        )
    print("✅ 数据插入完成")


async def search_products(keyword: str):
    """按关键字搜索商品——接受用户输入，拼接 SQL"""
    engine = get_engine()
    async with engine.connect() as conn:
        sql = f"SELECT * FROM product WHERE name LIKE '%{keyword}%'"
        result = await conn.execute(text(sql))
        rows = result.fetchall()
        for row in rows:
            print(f"  [{row.id}] {row.name} - {row.brand}")


async def delete_product_by_id(product_id: str):
    """按 ID 删除商品——接受用户输入，拼接 SQL"""
    engine = get_engine()
    async with engine.begin() as conn:
        sql = f"DELETE FROM product WHERE id = {product_id}"
        await conn.execute(text(sql))
    print(f"✅ 删除完成，id={product_id}")


async def main():
    await init_db()
    await raw_sql_insert()
    # 正常查询
    print("=== 搜索 'iPhone' ===")
    await search_products("iPhone")
    # 正常删除
    print("=== 删除 id=1 ===")
    await delete_product_by_id("1")
    print("=== 再次搜索 'iPhone' ===")
    await search_products("iPhone")


if __name__ == "__main__":
    asyncio.run(main())

```

运行后输出：

```
✅ 数据库表创建完成
✅ 数据插入完成
=== 搜索 'iPhone' ===
  [1] iPhone 16 - Apple
  [2] iPhone 15 - Apple
=== 删除 id=3 ===
✅ 删除完成，id=3
=== 再次搜索 'iPhone' ===
  [1] iPhone 16 - Apple
  [2] iPhone 15 - Apple
```

到这里，数据能插入、能查询、能按 ID 删除了，看起来一切正常。

##### SQL 注入

上面的 `search_products` 直接把用户输入拼进了 SQL 字符串。来验证一下：

```python
# 正常搜索
await search_products("iPhone")
```

输出符合预期：

```
=== 搜索 'iPhone' ===
  [1] iPhone 16 - Apple
  [2] iPhone 15 - Apple
```

现在换攻击者的输入：

```python
await search_products("%' OR 1=1 --")
```

拼接后的 SQL：

```sql
SELECT * FROM product WHERE name LIKE '%%' OR 1=1 -- %'
```

`OR 1=1` 永远为真，`--` 注释掉后续内容——**所有数据被暴露**：

```
  [1] iPhone 16 - Apple
  [2] iPhone 15 - Apple
  [3] Galaxy S25 - Samsung
  [4] Xiaomi 15 - Xiaomi
```

这还只是查询。同样的拼接方式在**按 ID 删除**里一样有效：

```python
# 正常删除，删掉 id=3（Galaxy S25）
await delete_product_by_id("3")
# 输出：✅ 删除完成，id=3
```

现在攻击者传入：

```python
await delete_product_by_id("1 OR 1=1")
```

拼接后的 SQL：

```sql
DELETE FROM product WHERE id = 1 OR 1=1
```

`WHERE id = 1 OR 1=1` 匹配**所有行**——整张表被清空：

```python
# 再查询，数据已经没了
await search_products("iPhone")
# 输出：（无结果，数据已被删光）
```

这就是经典的 **SQL 注入**——攻击者通过篡改输入改变 SQL 语句的意图，轻则偷数据，重则删库跑路。

##### 修复：参数化绑定

解决方案是：**SQL 结构与数据分离**。用 `:参数名` 作为占位符，通过字典传入值：

```python
async def search_products(keyword: str):
    """按关键字搜索商品——参数化绑定，安全"""
    engine = get_engine()
    async with engine.connect() as conn:
        result = await conn.execute(
            text("SELECT * FROM product WHERE name LIKE :keyword"),
            {"keyword": f"%{keyword}%"},
        )
        rows = result.fetchall()
        for row in rows:
            print(f"  [{row.id}] {row.name} - {row.brand}")
```

再用恶意输入试一次：

```python
await search_products("%' OR 1=1 --")
# 输出：（无结果，%' OR 1=1 -- 被当作普通字符串匹配，不会命中任何商品名）
```

原理：参数化绑定将 SQL 模板和参数值**分开发送**给数据库。数据库先解析 SQL 结构，再把参数值作为**纯数据**填入。无论攻击者输入什么，都不会被当作 SQL 指令执行。

手写 SQL 能跑，但两个核心问题摆在这里：一是注入风险，二是写字符串容易出错、没有 IDE 检查和补全。下一节引入 Core 表达式来解决这两个问题。

##### 总结

使用`RAW SQL`会带来以下问题：

1. 开发成本高
2. 易出错
3. 有注入风险
4. 无法适配不同数据库

但由于其高性能和极大的灵活性，仍然会有小概率用到

#### SQL表达式

SQLAlchemy Core 提供了一套 Pythonic 的 API 来构建 SQL 语句，底层自动完成参数化绑定，彻底杜绝注入风险。

```python
# model/main.py
import asyncio
from sqlalchemy import select, insert, update, delete
from app.model.engine import get_engine
from app.model.base import Base
from app.model.product import Product
from app.model.category import Category
import app.model.sku        # noqa: F401


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def core_insert():
    """Core 表达式插入"""
    engine = get_engine()
    async with engine.begin() as conn:
        # insert() 返回 Insert 对象，values() 设置列值
        stmt = insert(Product).values(
            name="iPhone 16",
            description="最新款智能手机",
            brand="Apple",
        )
        await conn.execute(stmt)

        stmt = insert(Product).values(
            name="iPhone 15",
            description="上一代旗舰",
            brand="Apple",
        )
        await conn.execute(stmt)

        stmt = insert(Category).values(
            name="手机", description="移动通信设备"
        )
        await conn.execute(stmt)
    print("✅ Core 插入完成")


async def core_query():
    """Core 表达式查询"""
    engine = get_engine()
    async with engine.connect() as conn:
        # select() 返回 Select 对象
        # where() 用 Python 表达式构建条件——Python 的 == 而非 SQL 的 =
        stmt = select(Product).where(
            Product.name.like("%iPhone%")
        )
        result = await conn.execute(stmt)
        for row in result:
            print(f"  [{row.id}] {row.name} - {row.brand}")


async def core_update():
    """Core 表达式更新"""
    engine = get_engine()
    async with engine.begin() as conn:
        stmt = (
            update(Product)
            .where(Product.id == 1)
            .values(name="iPhone 16 Pro")
        )
        await conn.execute(stmt)
    print("✅ Core 更新完成")


async def core_delete():
    """Core 表达式删除"""
    engine = get_engine()
    async with engine.begin() as conn:
        stmt = delete(Product).where(Product.id == 2)
        await conn.execute(stmt)
    print("✅ Core 删除完成")


async def main():
    await init_db()
    await core_insert()
    print("=== 查询 ===")
    await core_query()
    await core_update()
    print("=== 查询（更新后） ===")
    await core_query()
    await core_delete()
    print("=== 查询（删除后） ===")
    await core_query()


if __name__ == "__main__":
    asyncio.run(main())
```

##### 总结

使用SQL表达式有以下好处：

1. 类型化，不易出错
2. 无SQL注入风险
3. 适配不同方言



### 会话

```python
# model/main.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select, insert
from app.model.engine import get_engine
from app.model.base import Base
from app.model.product import Product
import app.model.category  # noqa: F401
import app.model.sku  # noqa: F401

session_factory = async_sessionmaker(
    get_engine(),
    class_=AsyncSession,  # 明确指定使用异步 Session
    expire_on_commit=False,
)


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def insert_with_session():
    session = session_factory()
    try:
        stmt = insert(Product).values(
            name="iPhone 16",
            description="最新款智能手机",
            brand="Apple",
        )
        await session.execute(stmt)
        await session.commit()
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
    print("✅ 提交完成")


async def insert_with_manual_commit():
    """手动提交"""
    async with session_factory() as session:
        try:
            stmt = insert(Product).values(
                name="iPhone 16",
                description="最新款智能手机",
                brand="Apple",
            )
            await session.execute(stmt)
            await session.commit()
        except:
            await session.rollback()
            raise
    print("✅ 手动提交完成")


async def insert_with_auto_commit():
    """自动提交"""
    async with session_factory.begin() as session:
        stmt = insert(Product).values(
            name="iPhone 15",
            description="上一代旗舰",
            brand="Apple",
        )
        await session.execute(stmt)
    print("✅ 自动提交完成")


async def main():
    await init_db()
    await insert_with_session()
    await insert_with_manual_commit()
    await insert_with_auto_commit()


if __name__ == "__main__":
    asyncio.run(main())

```

#### 优化代码结构

新建`core/database.py`
```python
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from app.core.config import db_settings

_engine: AsyncEngine | None = None


def get_engine() -> AsyncEngine:
    global _engine

    if _engine is None:
        url = f"postgresql+asyncpg://{db_settings.user}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}"
        _engine = create_async_engine(
            url, pool_size=10, max_overflow=20, pool_pre_ping=True, echo=False
        )

    return _engine


_session_factory: async_sessionmaker[AsyncSession] | None = None


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    global _session_factory

    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(),
            class_=AsyncSession,  # 明确指定使用异步 Session
            expire_on_commit=False,
        )

    return _session_factory

```

现在可以删除掉`model/engine.py`了

### ORM

前面两节无论是 Raw SQL 还是 Core 表达式，操作的都是**表**（Table）。而 ORM 的核心思想是：**操作的是 Python 对象，SQLAlchemy 负责把对象的变化同步到数据库**。

```python
# model/main.py
import asyncio
from sqlalchemy import select
from app.core.database import get_session_factory, get_engine
from app.model.base import Base
from app.model.product import Product
from app.model.category import Category
import app.model.sku        # noqa: F401

session_factory = get_session_factory()


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def orm_insert():
    """ORM 方式插入——创建对象，add 到 session"""
    async with session_factory.begin() as session:
        product = Product(
            name="iPhone 16",
            description="最新款智能手机",
            brand="Apple",
        )
        session.add(product)

        product2 = Product(
            name="iPhone 15",
            description="上一代旗舰",
            brand="Apple",
        )
        session.add(product2)

        category = Category(
            name="手机", description="移动通信设备"
        )
        session.add(category)
    print("✅ ORM 插入完成")


async def orm_query():
    """ORM 方式查询——execute + scalars() 拿到对象列表"""
    async with session_factory() as session:
        stmt = select(Product).where(
            Product.name.like("%iPhone%")
        )
        result = await session.execute(stmt)
        # scalars() 返回模型实例，可直接访问属性
        products = result.scalars().all()
        for p in products:
            print(f"  [{p.id}] {p.name} - {p.brand}")


async def orm_update():
    """ORM 方式更新——查出对象，改属性，自动同步"""
    async with session_factory.begin() as session:
        stmt = select(Product).where(Product.id == 1)
        result = await session.execute(stmt)
        product = result.scalar_one()
        # 直接修改 Python 对象属性，session 提交时自动生成 UPDATE
        product.name = "iPhone 16 Pro"
    print("✅ ORM 更新完成")


async def orm_delete():
    """ORM 方式删除——查出对象，调用 session.delete()"""
    async with session_factory.begin() as session:
        stmt = select(Product).where(Product.id == 2)
        result = await session.execute(stmt)
        product = result.scalar_one()
        await session.delete(product)
    print("✅ ORM 删除完成")


async def main():
    await init_db()
    await orm_insert()
    print("=== 查询 ===")
    await orm_query()
    await orm_update()
    print("=== 查询（更新后） ===")
    await orm_query()
    await orm_delete()
    print("=== 查询（删除后） ===")
    await orm_query()


if __name__ == "__main__":
    asyncio.run(main())
```

### 执行时机

session 在下面的情况下会触发执行 SQL

1. `session.flush()`，执行记录的操作，但不提交

2. `session.commit()`，先自动`flush`，再提交

3. `session.execute()`，执行传入的 SQL 语句，不提交

   - 当`autoflush=True`，则会先将 session 中 pending 的操作（即之前记录的操作） `flush` 到数据库，再执行传入的 SQL，这是默认值
   - 当`autoflush=False`，仅执行传入的 SQL，pending 操作保留在 session 中不动

4. `模型对象.字段`，当`expire_on_commit=True`时，可能会触发执行，不提交

   当 session 提交后，它会把 session 当中关联的模型对象的每一个字段都标记为过期，因为这些字段可能已经跟数据库不一样了。后续读取这些字段的时候，它会重新触发查询，将该对象的所有字段同步为数据库的字段值。

   这一切的前提条件是要开启`expire_on_commit=True`

   开启这个配置会损耗性能，同时会带来一些其他问题，所以说往往会关闭。

5. `session.refresh(模型对象)`，同步模型对象，不提交

   - 将数据库真实的值同步到模型对象。当`expire_on_commit=False`时，才可能需要使用该方法

### 总结

1. 简单 CRUD 用 ORM 更顺手，复杂查询（聚合、批量更新）可混用 Core 表达式，前两者都难以处理的情况下，可以考虑使用 RAW SQL，但要注意 SQL 注入问题
2. 耗时操作（比如I/O）尽量不要放到一次连接中
3. `session` 的能力总结：
   1. 模型结合
       2. 与连接的区别，连接需要手动执行excute sql
   3. 统一管理事务
   4. 记录操作、统一执行

### 作业

1. `SQLAlchemy`提供了几种操作数据的方式？分别适用于什么场景？
2. 什么是SQL注入？如何避免？
3. `SQLAlchemy`的会话功能有什么用？
4. `expire_on_commit`这个配置有什么用？
5. `flush`和`commit`有什么区别？
## 数据迁移

### 目前的问题

1. 如何才能保证过往数据不被删除？
2. 生产环境、测试环境、开发环境的数据库表结构如何同步？
3. 如何才能回滚到之前的表结构？

### 准备工作

删除数据库

```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

删除`model/main.py`

### 使用alembic

#### 安装

```shell
uv add --package web-service alembic==1.18.4 psycopg2-binary==2.9.12
```

#### 初始化

```shell
cd apps/web-service && uv run alembic init migrations
```

#### 配置

`app/model/__init__.py`

```python
from app.model import product  # noqa
from app.model import category  # noqa
from app.model import sku  # noqa
```

`apps/web-service/migrations/env.py`

```python
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# 从项目配置中读取数据库连接信息
from app.core.config import db_settings
# 导入模型（通过 __init__.py 触发所有模型注册到 Base.metadata）
from app.model.base import Base

# Alembic 配置对象，用于读取 alembic.ini
config = context.config

# 配置 Python 日志（读取 alembic.ini 中的 [loggers] 配置）
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 用项目配置覆盖 alembic.ini 中的 sqlalchemy.url
# 使用同步驱动 postgresql://（不需要 +asyncpg）
config.set_main_option("sqlalchemy.url",
    f"postgresql://{db_settings.user}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.name}")

# 告诉 Alembic 你的模型元数据，用于自动生成迁移
target_metadata = Base.metadata

# 其他配置项可通过 config.get_main_option() 获取


def run_migrations_offline() -> None:
    """离线模式执行迁移（只生成 SQL 脚本，不连接数据库）"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """在线模式执行迁移（直接连接数据库执行）"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

```



```makefile
# Makefile

.PHONY: dev debug db-migrate db-upgrade db-downgrade

dev:
	export PYTHONDONTWRITEBYTECODE=1; \
	uv run --package web-service fastapi dev apps/web-service/app/main.py --port 8080

debug:
	export PYTHONDONTWRITEBYTECODE=1; \
	uv run --package web-service python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m fastapi dev apps/web-service/app/main.py --port 8000

db-migrate:
	uv run --package web-service alembic -c apps/web-service/alembic.ini revision --autogenerate -m "$(message)"

db-upgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini upgrade head

db-downgrade:
	uv run --package web-service alembic -c apps/web-service/alembic.ini downgrade $(version)
```

#### 执行命令

```shell
# 生成迁移脚本
make db-migrate message="init"

# 执行迁移
make db-upgrade

# 执行回滚
make db-downgrade version=-1         # 回退一步
make db-downgrade version=abc123     # 回退到指定版本
```

### 最佳实践

#### 禁区

1. 手动修改数据库
2. 修改已执行过的迁移

记住：`迁移脚本执行完 == 本地数据库的最新状态 == 生产数据库的最新状态`



#### 日常开发

1. 改动模型
2. 生成迁移脚本
3. 审查迁移脚本（可使用AI）
   - 是否会导致数据丢失
   - 回滚和迁移是否互逆
4. 执行迁移



#### 常见问题

**如果发现某（几）次迁移有问题，同时这几次迁移已经执行过了，此时该怎么办？**

迁移有问题，同时迁移又执行过了，那说明目前的表结构就有问题。此时应该生成新的迁移脚本。让新的迁移适配现在的模型结构。审核过后，再重新执行迁移。

不建议修改和删除之前的迁移。

应该把迁移脚本看作是一个常量，一旦执行后，它就永远不可变更。



**如果某次迁移的执行失败了怎么办？**

根据错误信息查看是哪个脚本执行失败，修复它重新运行即可。



**什么时候我应该使用回滚？**

尽量不要使用回滚，因为回滚会造成数据库的表结构跟目前的模型结构不一致。可能解决了一个Bug，带来了更多的Bug。

如果确实需要回滚。一定要记得回滚过后，和当前的模型状态不一致的问题。你可以重新执行迁移，达到一致状态。或者是重新生成新的迁移，然后再执行。

始终记住，表结构和模型状态不一致，最多允许它是一个暂时状态，绝对不能允许它是一个长期状态。



### 作业

回答以下问题：

数据迁移解决了什么问题？
## 业务逻辑

<img src="https://resource.duyiedu.com/yuanjin/202606181041986.png" alt="image-20260618104106899" style="zoom:50%;" />

**图的处理过程**
1.客户端请求 -> DTO -> API -> DTO -> service -> model -> 数据处理/业务逻辑 -> DTO -> API -> DTO -> 响应给客户端

**三层架构作用**
1.职责分离
- API层：只负责接收HTTP请求、解析参数（如Header、Body、Query），并调用下一层。绝不包含任何业务判断或SQL语句
- Service层：负责处理核心业务逻辑
- model层：负责与数据库打交道。执行CRUD操作，并负责将数据库返回的原始数据转换为ORM对象

### 操作

复制本节课目录中的`duyi-service`下的所有文件，覆盖你的工程`apps/web-service`

### 核心关注点

1. 代码组织
   - 类模式还是函数模式？
   - 异常怎么处理？
2. 功能逻辑是否正确
   - 功能全不全？
   - 重要的验证做没做？
3. 边界是否清晰
   - 入参和返回的是什么？
   - 是否耦合了接口层的东西？

## 依赖注入（DI）

**IoC(控制反转)**：一种设计思想，旨在将某种**选择权**移交出去，从而避免与其耦合

- 解决的问题：某些情况某些函数内部确定选择了某种逻辑，导致在特殊情况下该函数失效不可用，而IOC通过参数将这种逻辑外抛来保证逻辑的通用从而解决该问题

**DI**：将IoC思想落地的一种手段

**IoC容器**：优化DI的工具，它负责交付依赖项
### 理解IoC、DI、IoC容器

`IoC`: **Inversion of Control，控制反转**

`DI`：**Dependency Injection，依赖注入**

```python
def check_permission(user: str):
    print(f"验证用户{user}权限")
    return True


def ali_oss_upload(user: str, file: str):
    if not check_permission(user):
        raise Exception("权限不足")
    print(f"阿里云，{file} 上传中...")


def upload_file(user: str, file: str):
    print("上传准备")
    ali_oss_upload(user, file)
    print("上传成功")


# 正常情况
upload_file("张三", "1.txt")

# 特殊情况：希望切换为腾讯云怎么办？？？
# 测试环境：希望使用假的oss上传怎么办？？？

```

```python
from typing import Callable


def check_permission(user: str) -> bool:
    print(f"验证用户{user}权限")
    return True


def ali_oss_upload(user: str, file: str, has_permission: Callable):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"阿里云，{file} 上传中...")


def upload_file(user: str, file: str, oss_upload: Callable, has_permission: Callable):
    print("上传准备")
    oss_upload(user, file, has_permission)  # 注意这里传入的是函数本身
    print("上传成功")


# 正常情况
upload_file("张三", "1.txt", ali_oss_upload, check_permission)


# 特殊情况：希望切换为腾讯云怎么办？？？
def tencent_oss_upload(user: str, file: str, has_permission: Callable):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"腾讯云，{file} 上传中...")


upload_file("张三", "1.txt", tencent_oss_upload, check_permission)


# 测试环境：希望使用假的oss上传怎么办？？？
def fake_upload(user: str, file: str, has_permission: Callable):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"模拟，{file} 上传中...")


def fake_check_permission(user: str) -> bool:
    print(f"模拟：验证用户{user}权限")
    return True


upload_file("张三", "1.txt", fake_upload, fake_check_permission)

```

```python
# Depends.py
from __future__ import annotations

from collections.abc import Callable
from typing import Any


class Depends:
    _overrides: dict[Callable[..., Any], Callable[..., Any]] = {}

    def __init__(self, func: Callable[..., Any]) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        actual = self._overrides.get(self.func, self.func)
        return actual(*args, **kwds)

    @classmethod
    def override(
        cls,
        original: Callable[..., Any],
        replacement: Callable[..., Any],
    ) -> None:
        cls._overrides[original] = replacement

    @classmethod
    def clear_override(cls, func: Callable[..., Any] | None = None) -> None:
        if func is not None:
            cls._overrides.pop(func, None)
        else:
            cls._overrides.clear()



 # main.py
from Depends import Depends


def check_permission(user: str) -> bool:
    print(f"验证用户{user}权限")
    return True


def ali_oss_upload(user: str, file: str, has_permission=Depends(check_permission)):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"阿里云，{file} 上传中...")


def upload_file(user: str, file: str, oss_upload=Depends(ali_oss_upload)):
    print("上传准备")
    oss_upload(user, file)  # 注意这里传入的是函数本身
    print("上传成功")


# 正常情况
upload_file("张三", "1.txt")


# 特殊情况：希望切换为腾讯云怎么办？？？
def tencent_oss_upload(user: str, file: str, has_permission=Depends(check_permission)):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"腾讯云，{file} 上传中...")


Depends.override(ali_oss_upload, tencent_oss_upload)
upload_file("张三", "2.txt")


# 测试环境：希望使用假的oss上传怎么办？？？
def fake_upload(user: str, file: str, has_permission=Depends(check_permission)):
    if not has_permission(user):
        raise Exception("权限不足")
    print(f"模拟，{file} 上传中...")


def fake_check_permission(user: str) -> bool:
    print(f"模拟：验证用户{user}权限")
    return True


Depends.clear_override()
Depends.override(ali_oss_upload, fake_upload)
Depends.override(check_permission, fake_check_permission)
upload_file("张三", "3.txt")

```




### 完善API层

#### 复制代码

复制当前目录的`duyi-service`下的内容到`apps/web-service/app`中

#### 该写get_db

```python
async def get_db():
    async with get_session_factory().begin() as session:
        yield session
```

## 统一异常处理
### 现存的问题（统一异常处理即解决了这些问题）

1. FastAPI 底层依赖 Starlette，当请求参数校验失败（如 pydantic.ValidationError）、数据库连接断开（如 SQLAlchemyError）或路径不存在时，框架会抛出特定的 Python 异常。
    - FastAPI无统一处理：默认返回 HTML 格式的 500 错误页面（含内部路径和代码片段），这在生产环境是严重的安全漏洞（信息泄露）
    - FastAPI有统一处理：捕获所有未被处理的 Exception，统一转化为 {"code": 500, "msg": "Internal Server Error"}，无法感知程序哪里有问题。
2. 错误相应格式不统一
3. 没有剥离“业务错误”和“系统错误”

### FastAPI默认异常处理情况
- 主动抛出的异常
  - `HTTPException`，在API接口中主动抛出，被`FastAPI`自动处理
  - `BusinessException`，在业务层主动抛出，被`FastAPI`当做`Exception`自动处理
- 系统自动抛出的异常
  - `RequestValidationError`，被`Pydantic`自动抛出，被`FastAPI`自动处理
  - `HTTPException`，被`FastAPI`自动抛出，被`FastAPI`自动处理
  - 其他未知异常，比如数据库、Python语言等无法预知的异常，被`FastAPI`当做`Exception`自动处理
### 异常处理的最佳实践

1. 对异常的自定义处理要收拢到统一代码位置
2. 请求-响应 链条中的异常不能中断服务器
3. 服务端的敏感信息不能暴露给响应
4. 通过设计，根据不同类型的异常响应不同的字段值
   - status code：HTTP响应码
   - code：错误业务码
   - message：错误消息
5. API文档中需要包含全局异常表

### 设计

![image-20260622111132511](https://resource.duyiedu.com/yuanjin/202606221111615.png)

### 完成代码

将本节课目录下`duyi-service`下边的文件和文件夹覆盖`apps/web-service/app`

### 作业

复述服务端异常处理的最佳实践
## 中间件
### 什么是中间件
中间件是一种架构设计模式，本质上就是一个函数。
### 中间件解决了什么问题
**解耦公共代码和业务代码**：主要解决了“横切关注点”的问题，也就是那些与核心业务逻辑无关，但又必须在很多甚至所有接口中处理的通用功能。它让我们能够将这类通用逻辑抽离出来，进行集中处理，避免在每个接口函数中重复编写相同的代码

### 中间件涉及的核心概念

- **横切关注点（Cross-Cutting Concerns）**：描述了跨越多个功能、可被横切的共同逻辑的现象
- **AOP（Aspect Oriented Programming）**：应该将那些跨域多个功能、可被横切的共同逻辑分离出去，不侵入功能本身
- **DI**：AOP的一种实现手段

### 理解中间件

FastAPI的中间件是AOP的一种实现手段

```python
async def my_middleware(request: Request, call_next):
  	# 操作...
    response = await call_next(request) # 传递给下一个中间件
    # 操作...
    return xxx
  
app.middleware("http")(my_middleware)
```

![image-20260622134925991](https://resource.duyiedu.com/yuanjin/202606221349147.png)

### 统一响应格式中间件

`apps/web-service/app/core/middleware/response.py`

```python
import json

from fastapi import Request
from fastapi.responses import JSONResponse


async def unified_response(request: Request, call_next):
    response = await call_next(request)

    if not request.url.path.startswith("/api/"):
        return response

    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    headers = dict(response.headers)
    headers.pop("content-length", None)

    if response.status_code >= 400:
        err = json.loads(body) if body else {}
        return JSONResponse(
            content={
                "code": err.get("code", str(response.status_code)),
                "data": None,
                "message": err.get("message", ""),
            },
            status_code=response.status_code,
            headers=headers,
        )

    data = json.loads(body) if body else None

    return JSONResponse(
        content={"code": "0", "data": data, "message": "success"},
        status_code=response.status_code,
        headers=headers,
    )


MIDDLEWARE = (unified_response, {})

```

`apps/web-service/app/core/middleware/__init__.py`

```python
import inspect

from fastapi import FastAPI

from app.core.middleware import response

MIDDLEWARES = [
    response.MIDDLEWARE
]


def register_middleware(app: FastAPI) -> None:
    for callable_obj, kwargs in MIDDLEWARES:
        if inspect.isclass(callable_obj):
            app.add_middleware(callable_obj, **kwargs)
        else:
            app.middleware("http")(callable_obj)

```

`apps/web-service/app/main.py`

```python
from app.core.middleware import register_middleware

register_middleware(app)
```

`apps/web-service/app/core/openapi.py`

```python
from fastapi import FastAPI


def _build_envelope_properties(data_schema: dict) -> dict:
    return {
        "code": {
            "type": "string",
            "description": "状态码，0 表示成功",
            "example": "0",
        },
        "data": data_schema,
        "message": {
            "type": "string",
            "description": "提示信息",
            "example": "success",
        },
    }


def _make_envelope(data_schema: dict) -> dict:
    return {
        "type": "object",
        "properties": _build_envelope_properties(data_schema),
        "required": ["code", "data", "message"],
    }


def _wrap_ref_schema(openapi_schema: dict, schema: dict) -> dict:
    ref_path: str = schema["$ref"]
    ref_name = ref_path.split("/")[-1]

    title = ref_name.replace("_", " ")
    wrapper_name = f"ApiResponse_{ref_name}"

    schemas = openapi_schema.setdefault("components", {}).setdefault("schemas", {})
    if wrapper_name not in schemas:
        schemas[wrapper_name] = {
            "title": f"ApiResponse[{title}]",
            "type": "object",
            "properties": _build_envelope_properties(schema),
            "required": ["code", "data", "message"],
        }

    return {"$ref": f"#/components/schemas/{wrapper_name}"}


def _wrap_array_schema(openapi_schema: dict, schema: dict) -> dict:
    items = schema.get("items")
    if isinstance(items, dict) and "$ref" in items:
        item_name = items["$ref"].split("/")[-1]
        title = f"List[{item_name.replace('_', ' ')}]"
        wrapper_name = f"ApiResponse_List_{item_name}"

        schemas = openapi_schema.setdefault("components", {}).setdefault("schemas", {})
        if wrapper_name not in schemas:
            schemas[wrapper_name] = {
                "title": f"ApiResponse[{title}]",
                "type": "object",
                "properties": _build_envelope_properties(schema),
                "required": ["code", "data", "message"],
            }

        return {"$ref": f"#/components/schemas/{wrapper_name}"}

    return _make_envelope(schema)


def setup_openapi(app: FastAPI) -> None:
    _original = app.openapi

    def _custom():
        if app.openapi_schema:
            return app.openapi_schema

        schema = _original()

        for path, path_item in schema.get("paths", {}).items():
            if not path.startswith("/api/"):
                continue

            for method in ("get", "post", "put", "delete", "patch"):
                operation = path_item.get(method)
                if operation is None:
                    continue

                responses = operation.get("responses", {})
                for status_code_str, response in list(responses.items()):
                    status_code = int(status_code_str)
                    if status_code not in (200, 201):
                        del responses[status_code_str]
                        continue

                    content = response.get("content", {})
                    json_content = content.get("application/json")
                    if json_content is None:
                        continue

                    original_schema = json_content.get("schema")
                    if original_schema is None:
                        continue

                    if "$ref" in original_schema:
                        wrapped = _wrap_ref_schema(schema, original_schema)
                    elif original_schema.get("type") == "array":
                        wrapped = _wrap_array_schema(schema, original_schema)
                    else:
                        wrapped = _make_envelope(original_schema)

                    json_content["schema"] = wrapped

        app.openapi_schema = schema
        return schema

    app.openapi = _custom

```

`apps/web-service/app/main.py`

```python
from app.core.openapi import setup_openapi

setup_openapi(app)
```

### 用于性能调试的中间件

`apps/web-service/app/core/middleware/process_time.py`

```python
import time

from fastapi import Request


async def process_time(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(round(time.perf_counter() - start, 4))
    return response


MIDDLEWARE = (process_time, {})

```

### 用于解决跨域的中间件

`.env.example / .env`

```python
# 其他配置
WEB_CORS_ORIGINS=* # 跨域白名单，多个来源用逗号分隔，* 表示允许所有
WEB_CORS_EXPOSE_HEADERS=X-Process-Time # 允许前端读取的响应头，多个用逗号分隔

# 其他配置
```

`apps/web-service/app/core/config.py`

```python
class _WebSettings(_BaseSettingsWithEnv):
    app_name: str = "Web Service API"  # 实际读取 WEB_APP_NAME
    cors_origins: str = ""  # 实际读取 WEB_CORS_ORIGINS，多个来源用逗号分隔
    cors_expose_headers: str = ""  # 实际读取 WEB_CORS_EXPOSE_HEADERS

    # 配置读取方式
    model_config = {"env_prefix": "WEB_"}
```

`apps/web-service/app/core/middleware/cors.py`

```python
from starlette.middleware.cors import CORSMiddleware

from app.core.config import web_settings

origins = [o.strip() for o in web_settings.cors_origins.split(",") if o.strip()]
expose_headers = [
    h.strip() for h in web_settings.cors_expose_headers.split(",") if h.strip()
]

MIDDLEWARE = (
    CORSMiddleware,
    {
        "allow_origins": origins,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
        "expose_headers": expose_headers,
    },
)

```

## 测试框架

### 为什么需要测试框架

1. **防回归**——改一处坏一片，没测试不敢重构。
2. **保契约**——契约即承诺，测试锁死预期输入输出。
3. **提效率**——验证十次，不如脚本跑一秒。

### 实现测试

安装必要库

```shell
uv add --package web-service --group dev httpx==0.28.1 pytest==9.1.1 pytest-asyncio==1.4.0
```

配置`web-service/pyproject.toml`
```toml

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["test"]
```

配置`Makefile`

```yaml
test:
	uv run pytest apps/web-service/test/integration/ -v
```

配置`.gitignore`

```yaml
# temp
/temp
/tmp
```
## 测试方案

> 测试无法覆盖所有情况

### 更新代码

安装覆盖率插件

```shell
uv add --package web-service --group dev pytest-cov==7.0.0
```

配置`apps/web-service/pyproject.toml`

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["test"]
markers = [
    "smoke: 标记为冒烟测试，验证核心流程是否正常",
]
```

配置`.gitignore`

```yaml
# test
.coverage
htmlcov/
```

覆盖课件中提供的代码

### 开发和测试的顺序

1. **TLD**：Test-Last Development，开发先行，测试后行
2. **TDD**：Test-Driven Development，测试先行，开发后行

#### 如何抉择TLD和TDD呢？
如果你追求更低的缺陷率和更高的代码质量，且团队有能力驾驭，TDD是更优选择；
如果你更看重短期的开发速度和较低的入门门槛，TLD则更实际
**历史经验（前公司流程）**：

- TLD和TDD混合
    - 开发完成后需冒烟测试，通过在给QA开始测试
    - 其中冒烟用例分未P0,P1,P2等优先级，一般QA只会给P0的核心流程给开发冒烟

### 测试选型

- **单元测试**：屏蔽外部，测试单函数、类

  目录建议：`unit/`

  适用场景：复杂或重要的函数、类

- **集成测试**：多模块、类、函数的交互

  目录建议：`integration/`

  适用场景：核心，达到测试覆盖率的核心手段

- **系统测试**：测试整个真实运行的系统

  目录建议：`e2e / system`

  适用场景：必做，通常是测试真实环境的启动是否会带来新问题，走一些happy path即可

- **e2e测试**：在系统测试的基础上，测试某个业务功能链（一个用例跑完整个功能链）

  目录建议：`e2e`

  适用场景：必做，主要业务功能链

- **冒烟测试**：系统的底线/红线/生命线，冒烟测试未通过可视为灾难性事故

  目录建议：`不限`

  适用场景：下面的情况满足任意一条，必须设置为冒烟测试
  - **如果这个功能挂了，用户立刻无法完成核心任务**

    登录挂了→用户进不来；下单挂了→收不到钱；支付回调挂了→钱付了但订单没更新

  - **这个功能被90%以上的用户每天使用**

    比如“查看商品详情”是电商的高频功能，而“修改收货地址”相对低频

  - **这个功能是其他所有功能的前置依赖**

    比如“获取用户Token”是所有需要登录接口的前提，如果它挂了，后面几十个接口都测不了

  - **这个功能一旦出错，会造成严重的数据损失或资损**

    比如“扣减库存”不能多扣，“退款”不能多退，这类功能哪怕使用频率不高也要加冒烟

  - **这个功能历史上经常出问题（痛点回归）**

    某个接口特别容易改坏（比如复杂的计算逻辑），即使它不算最核心，也可以加冒烟作为“保险”

  > [!IMPORTANT]
  >
  > 冒烟测试往往不针对新功能，而是已上线、稳定运行一段时间的旧功能

### 测试手段
不管是stub(桩)模式还是mock模式，其核心都是：在测试时，用一个"假的对象"替代真实的依赖，让测试能独立、可控地运行。

#### 为啥需要这个替身？
假设你在测一个订单服务：

```
text
OrderService → 依赖 → PaymentService（真实调用支付宝） → 依赖 → UserRepository（真实查数据库）
```

如果每次测 OrderService 都真的去调支付宝、真的连数据库，会有几个问题：

- 慢

- 不稳定（网络、第三方挂了）

- 无法构造异常场景（比如"支付超时"很难真实复现）

- 有副作用（真扣钱、真写库）

所以需要"替身"来隔离这些外部依赖。桩（Stub）和 Mock 就是两种最常见的替身。
#### Stub 模式
定义：桩是"预先设定好返回值"的假对象。 你只关心它"返回什么"，不关心它"被怎么调用"。
```python
# 假设这是你的业务代码（app/services/sms.py）
class SmsService:
    def send_verify_code(self, phone: str) -> dict:
        # 真实调用第三方短信接口
        return {"code": 123456, "success": True}

# app/routers/login.py
class login:

    @staticmethod
    def send_verify_code():
      	user = get_current_user()
        if not user:
           raise PermissionDenied()
        sms_serv = SmsService()
        sms_serv.send_verify_code(user.phone)
        # 后续其他逻辑
```

```python
# 定义一个 Stub（测试桩），替换真实短信服务
class SmsServiceStub:
    def send_verify_code(self, phone: str) -> dict:
        # 始终返回固定结果，不真正发短信
        return {"code": 999999, "success": True}


def test_login_with_stub(monkeypatch):
    # 用 Stub 替换真实的 SmsService
    monkeypatch.setattr("app.services.sms.SmsService", SmsServiceStub)

    # 现在调用登录接口，内部会用 Stub，不会真发短信
    from app.routers import login
    result = login.send_verify_code()

    assert result["code"] == 999999
    assert result["success"] is True
```

#### Mock 模式
定义：Mock 是"记录了调用行为"的假对象。 你不仅设定它的返回值，还校验它是否被正确调用（调用次数、参数、顺序等）。
```python
def test_login_with_mock(mocker):
    # 直接 patch 掉 SmsService 类
    mock_sms_class = mocker.patch("app.services.sms.SmsService")
    # 配置实例方法的返回值
    mock_sms_class.return_value.send_verify_code.return_value = {"code": 888888, "success": True}

    # 调用
    result = login.send_verify_code()

    assert result["code"] == 888888
    assert result["success"] is True

    # 验证：获取实例，再验证它的方法被调用了一次
    mock_sms_class.return_value.send_verify_code.assert_called_once()
```

Mock 比 Stub 多的功能

| 功能               | 说明                   | 代码示例                                          |
| :----------------- | :--------------------- | :------------------------------------------------ |
| **验证调用次数**   | 确保方法被调用了N次    | `mock.method.assert_called_once()`                |
| **验证调用参数**   | 检查传入了什么值       | `mock.method.assert_called_with(1, "a")`          |
| **验证调用顺序**   | 多个方法按预期顺序调用 | `mock.method1.assert_called_before(mock.method2)` |
| **动态返回不同值** | 每次调用返回不同结果   | `mock.method.side_effect = [1, 2, 3]`             |
| **抛出异常**       | 模拟异常场景           | `mock.method.side_effect = ValueError("错")`      |
| **记录所有调用**   | 查看历史调用记录       | `mock.method.call_args_list`                      |
| **重置调用记录**   | 清空历史，重新统计     | `mock.reset_mock()`                               |

**绝大部分情况下，Mock 可以平替 Stub**

#### 冒烟测试

```python
@pytest.mark.smoke  # ← 加这行即可
def test_login_success(client):
    response = client.post("/login", json={"email": "test@test.com", "password": "123456"})
    assert response.status_code == 200

def test_login_wrong_password(client):  # ← 没标记，不算冒烟
    response = client.post("/login", json={"email": "test@test.com", "password": "wrong"})
    assert response.status_code == 401
```

#### 测试覆盖率

测试覆盖率 = 运行所有测试用例执行到的代码 / 全量的代码

有些团队有硬性指标，比如测试覆盖率必须达到80%，否则无法PR

```shell
# 查看测试覆盖率
coverage report
# 生成HTML
coverage html
```

### 开发日常

1. 新功能选择 TLD 或 TDD
2. 确保新增或修改的测试脚本通过
3. 确保冒烟测试通过
4. 【可选】确保覆盖率达标
5. 提交PR
6. 后续进入流水线...[略]

## 三层架构

### 经典三层（MVC变体 = 三层架构 + 数据访问层）

<img src="https://resource.duyiedu.com/yuanjin/202606241104966.png" alt="image-20260624110412929" style="zoom:50%;" />

#### 为啥会有dao层
因为在ORM框架出现之前，是需要手动建表，然后在代码书写表 <-> 模型（model）之间的映射关系，执行sql语句，sql的执行又不能全放在service层，这样会导致代码冗余及其难维护，因此出现了dao层，负责存取。只跟数据库打交道，执行SQL。

#### 这个架构的作用

- 职责分离
    - API层（Controller/接口层）： 只负责接待。接收HTTP请求、校验参数、组装响应格式（JSON）。它不应该包含业务逻辑
    - Service层（业务逻辑层）： 负责干活。这是系统的核心，处理具体的业务规则（比如“转账”需要扣款、加款、记录流水，这是一个事务）。
    - DAO层（数据访问层）： 负责存取（原子CRUD操作）。只跟数据库打交道，执行SQL。
    - Model（模型）： 负责传输。定义数据结构（Entity、DTO、VO）


#### 这种模式带来的问题

-    耦合性强： 虽然分层了，但dao其实依赖service层，没有完全分出去
    -    例：原本dao层只应该提供原子操作（CRUD = 1（insert (新增)） + 3（findById (按ID查询) + findAll (查询所有) + count (统计总数)） + 1（update (更新)） + 1（deleteById (按ID删除)））查用户，但是登录需要验证账号密码，就把所有用户查出来，然后循环比较账号密码，出现了性能问题
        -    为了解决性能，应该dao层新增方法，根据账户密码去数据库查询，导致dao层多了很多业务相关的方法，从而导致dao层与service层职责不清晰
-    modle模型承担三层的职责：一对应数据库的模型载体，二是service层操作的逻辑载体，三是api层的传输载体

### 模型分化

<img src="https://resource.duyiedu.com/yuanjin/202606241105300.png" alt="image-20260624110548259" style="zoom:50%;" />

#### 解决了什么问题
解决了modle模型载体职责不明确的问题

示例：

```python
# model


class User:
    id: int
    username: str
    password_hash: str  # 存储加密后的密码
    email: str
    phone: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool  # 软删除标记


# BO
class UserIdentity:
    username: str
    password_hash: str

class UserInfo:
    email: str
    phone: str

class User:
    id: int
    identity: UserIdentity
    info: UserInfo
    created_at: datetime
    updated_at: datetime

# DTO
class User
    id: int
    username: str
    email: str
```



### 依赖倒置

<img src="https://resource.duyiedu.com/yuanjin/202606241128795.png" alt="image-20260624112836750" style="zoom:50%;" />

#### 解决了什么问题

- 因为最开始的三层架构说到dao层和service层的依赖关系耦合了，实际是dao层依赖service层，因此现在dao层就是为service服务，由service层声明需要哪些实现（IRepostory）由dao层提供，从而解决依赖混乱的问题
    - 一般都是框架通过依赖注入（DI）来实现的
    

### 当前的架构

<img src="https://resource.duyiedu.com/yuanjin/202606181041986.png" alt="image-20260618104106899" style="zoom:50%;" />

![上传模式](https://resource.duyiedu.com/yuanjin/202606261505481.svg)

阿里云的RAM用户权限的配置
```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "oss:PutObject",
                "oss:GetObject",
                "oss:DeleteObject"
            ],
            "Resource": [
                "acs:oss:*:*:your-bucket-name",
                "acs:oss:*:*:your-bucket-name/*"
            ]
        }
    ]
}
```
## 长短事务问题

### 什么是长事务
1.在接口处理函数中（service层，函数执行就会有一个数据库连接 session开启）
-   包含 操作数据库
-   **耗时**的I/O操作
-   再次操作数据库
**函数执行完成，最后才关闭session，此时因为耗时的I/O会导致连接长时间回不到线程池，造成性能问题**

2.回顾FastApi处理请求流程

- 运行钩子函数：lifespan,直到yeild
- 处理请求
- 找到第一个中间件，将其执行放入到try中
    - 当第一个中间件执行报错，进入异常处理
        - 根据注册的异常类型和对应处理函数执行
        - 相应异常函数处理结果
    - 第一个中间件未报错，则控制权移交下一个中间件，直到路由，然后执行路由表对应的函数处理
        - 路由函数注入参数（包含DI）
            - DI参数处理：运行DI依赖函数，得到生成器迭代的第一个（例如数据库session）
            - 将迭代结果给到DI参数
            - 路由函数执行（始终处于同一个事务中，这里就可能出现长短事务）
            - DI参数对象的生成器（数据库session）继续迭代，直到迭代完成(全部成功了自动提交数据库，有错误自动回滚，最后关闭事务)

### 长短事务优缺点
长事务优点：

- 强一致性：能保证数据一致性，由上第一例，先操作数据库，在长I/O，在操作数据库，在一个事务就保证了这2次操作数据库的数据一致性

长事务缺点：性能损耗高，线程池线程被长时间占用
**短事务与长事务相反**

### FastApi路由函数执行逻辑

- 进入路由函数处理
    - 调用service1处理xxx
    - ......
    - 调用service10处理xxxx
        - 只要在函数执行期间手动调用了session.commit,session.close等操作，则连接回线程池，后续在用session操作，都不用手动开启事务，会自动开启，因此耗时操作前可以手动关闭，结束后再操作数据库从而避免长事务(后续所有都是短事务，需要自行保证数据一致性 )
            - 前提路由的DI参数session不能是通过异步上下文管理器生成的，而需要手动处理，例：

```python
       session = get_session_factory()()
    session.begin()
    try:
        yield session
    except:
        await session.rollback()
        raise
    else:
        await session.commit()
    finally:
        await session.close()

    # async with get_session_factory().begin() as session:
    #     yield session
```

## 用户系统

### 涉及的问题

- 工程问题：测试脚本越来越多，如何仅运行受影响的测试？

- 业务问题

  - 模型层：简单没问题
  - 业务层：
    - 密码怎么保存才能防止泄露后造成灾难性后果？
        - 看下方密码学算法+哈希算法
    - 用户登录成功后颁发什么样的凭证才是可信的？
        - JWT
          - 用户凭证的过期时间在哪里设置？
              - 自行生成JWT的过程中设置，也可放服务端配置中设置
          - 用户凭证的密钥在哪里配置？
              - 放在服务端，一般放服务端环境变量
  - API层：
    - 如何知晓当前登录的用户？
        - 接口携带token
    - 如何限制接口必须登录后才能访问？
      - 验证token
    - 如何在API文档上直观的反映出需要认证的接口？
        - 加了token认证的接口（需要用FastApi官方的要求方式来验证token） 文档会显示锁

  

### 核心概念

#### 密码学算法

| 类别           | 有密钥吗      | 可逆吗 | 代表        |
| :------------- | :------------ | :----- | :---------- |
| ~~对称加密~~   | 有，同一密钥  | 可逆   | AES         |
| ~~非对称加密~~ | 有，公钥+私钥 | 可逆   | RSA、ECC    |
| 哈希算法       | 无密钥        | 不可逆 | SHA256、MD5 |
| 消息认证码     | 有，同一密钥  | 不可逆 | HMAC-SHA256 |

##### 哈希算法

**特点**：

输入任意数据，得到固定长度（通常是256位）的数据，过程不可逆，固定输入得到固定结果，不同输入得到不同结果



**场景**：

协商缓存：客户端请求服务器，询问当前缓存的结果是否过期

文件校验：下载文件时，官网会提供这个文件的Hash结果，下载到本地后，你可以重新计算Hash看结果和官网的是否一致

密码保存：服务器不关心用户的密码究竟是什么，只关心用户是否提供了正确的密码，用户注册时填写的密码用Hash保存，后续登录时填写的密码使用相同的算法进行Hash运算后比对两次密码是否一致



示例：

```python
import hashlib


def hash(password: str) -> str:
    """
    模拟"不加盐"的哈希运算（极度不安全，仅用于教学对比）
    特点：同样的密码永远得到同样的哈希值
    """
    # 直接对密码进行SHA256哈希（没有加任何随机盐）
    hash_bytes = hashlib.sha256(password.encode("utf-8")).digest()
    # 转成十六进制显示（64位字符串）
    return hash_bytes.hex()


# 测试：同样的密码，哈希值完全一样
pwd = "123456"
hash1 = hash(pwd)
hash2 = hash(pwd)

print(f"第一次哈希: {hash1}")
print(f"第二次哈希: {hash2}")
print(f"两次是否相同: {hash1 == hash2}")  # True

```



**🌈彩虹表**

预算Hash表，预先将常见字符进行Hash运算，得到结果，从可以倒推明文



**🧂加盐**：

方法1: 在计算Hash时，在明文前加入一段随机数据作为盐值，从而增加彩虹表逆向难度

方法2: 多轮计算（hash之后在多次hash），增加破解难度

现实中，两个方法往往结合使用



示例：

```python
import bcrypt


def hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


# 测试：同样的密码，哈希值完全不一样
pwd = "123456"
hash1 = hash(pwd)
hash2 = hash(pwd)

print(f"第一次哈希: {hash1}")
print(f"第二次哈希: {hash2}")
print(f"两次是否相同: {hash1 == hash2}")  # False

print(verify("123456", hash1))
print(verify("123456", hash2))

```



##### 消息认证码（JWT）

你可以简单认为：**消息认证码就是带密钥的哈希**

带密钥的目的，是**为了控制生成哈希的权力**

最常见的例子就是防止明文被篡改



示例：

```python
import uuid
from datetime import datetime, timedelta, timezone

import jwt


def create_token(
    data: dict,
    secret_key: str,
    *,
    algorithm: str = "HS256",
    expires_delta: timedelta | None = None,
) -> str:
    payload = data.copy()
    now = datetime.now(timezone.utc)
    payload.update(
        {
            "jti": str(uuid.uuid4()),
            "iat": now,
            "exp": now + (expires_delta or timedelta(hours=2)),
        }
    )
    return jwt.encode(payload, secret_key, algorithm=algorithm)


def decode_token(
    token: str,
    secret_key: str,
    *,
    algorithms: list[str] | None = None,
) -> dict:
    return jwt.decode(
        token,
        secret_key,
        algorithms=algorithms or ["HS256"],
    )


secret = "asdfasdfasdfasjfhkhjhasjsdfasdsdfsafdasd"

token = create_token({"id": 1}, secret)
print(token)

decode = decode_token(token, secret_key=secret)
print(decode)

```

思考：你觉得`JWT`需要加盐吗？
不需要。加盐是为了防止篡改

#### ContextVar 上下文变量

在不传递参数的情况下，让函数访问到"当前上下文"的数据，且每个并发任务互不干扰。

```python
import asyncio
from contextvars import ContextVar

# 声明一个上下文变量
name_var: ContextVar[str] = ContextVar("name", default="")


def say_hello() -> str:
    return f"你好，{name_var.get()}"


async def task(name: str, delay: float) -> None:
    name_var.set(name)           # 在当前上下文中设置值
    await asyncio.sleep(delay)   # 模拟耗时操作
    print(say_hello())           # say_hello 没有传参，但能拿到正确的值


async def main() -> None:
    await asyncio.gather(
        task("Alice", 0.2),
        task("Bob", 0.1),
    )


asyncio.run(main())
```

输出：

```
你好，Bob
你好，Alice
```

核心要点：

- **不传参也能拿到值**：`say_hello()` 无需参数，直接通过 `ContextVar` 读取上层设置的数据
- **并发隔离**：Bob 和 Alice 虽然在同一线程交替执行，但各自的上下文互不干扰
## 日志的核心问题

### 使用什么日志库？

在python中，通常使用`loguru`记录日志

```python
from loguru import logger
import sys

# 1. 移除默认的输出配置
logger.remove()

# 2. 配置控制台输出（彩色、格式化）
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{extra[request_id]}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="DEBUG",
    colorize=True,
)

# 3. 输出日志
logger.bind(request_id="abc-123", user="admin").info("开始处理请求")

```

- `logger.add`
  - 参数`1`：配置日志输出方式，通常为`sys.stdout`或文件路径
  - 参数`format`: 配置日志输出格式
  - 参数`level`: 配置日志级别
    - TRACE：跟踪级别
    - DEBUG：调试级别
    - INFO：信息级别
    - SUCCESS：操作成功级别
    - WARNING：警告级别
    - ERROR：错误级别
    - CRITICAL：严重错误级别
- `logger.bind`：绑定额外的自定义信息
- `logger.info`：输出`INFO`级别的消息

### 日志配置

#### 日志配置什么时候做？

在系统启动的时候完成配置，同时由于使用了日志系统，因此uvicorn的错误信息不再打印到控制台

#### 配置什么？

**生产环境：**

- 输出方式：固定为`stdout`，方便后期和云服务日志系统对接
- 输出级别：通过环境变量配置
- 输出格式：统一为`JSON`，方便云服务日志系统解析



**开发环境：**

- 输出方式：

  - 固定为`stdout`，打印到控制台

    对于错误日志，还要额外输出到文件

- 输出级别：通过环境变量配置

- 输出格式：统一为纯文本，方便人类阅读



### 日志输出

#### 输出什么？

**共同数据：**

- message：错误消息
- duration_ms：某个操作执行的时间（毫秒）



**差异数据：**

- 请求日志：method、path、status_code、client_ip
- 数据库日志：sql、params
- 业务日志：action、entity、entity_id



可以使用**类结构**约定字段

#### 在哪里输出？

##### 请求日志

使用请求中间件

1. 请求到达后：
   1. 记录请求id到上下文，使得该请求链条中的所有日志都可以拿到该id
   2. 创建请求日志对象
   3. 将日志对象放置到`request.state.request_log`中，方便其他地方获取日志对象
2. 请求成功：`log.success()`
3. 请求失败
   1. 进入`handler`的处理逻辑
   2. 该写`message`
   3. `500`错误输出`error`，其他错误输出`warning`

##### 数据库日志

注册`SQLAchemy`事件监听器，执行SQL前计时，执行后创建日志对象

对于一些慢查询（超过环境变量的阈值），输出`warning`级别的日志



##### 业务日志

通常不会全量的记录业务日志。

业务日志既可以统一处理，也可以灵活处理。



**统一处理：使用装饰器，见**`business_log.py:service_logger`

## 流式响应

### SSE模式

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务端

    C->>S: GET /events (EventSource)
    S-->>C: HTTP 200 + Content-Type: text/event-stream
    Note over C,S: 建立长连接，保持打开状态

    loop 服务端持续推送
        S->>C: data: 消息片段1\n\n
        S->>C: data: 消息片段2\n\n
        S->>C: data: 消息片段3\n\n
        S->>C: event: error\ndata: 消息片段3\n\n
    end

    C->>S: 关闭连接 / 网络断开
    Note over C,S: 连接终止
```

**关键特征**：
- 基于标准HTTP协议
- 单向通信：仅服务端→客户端推送
- 数据格式为`text/event-stream`，每条消息以双换行符(`\n\n`)结尾
- 适合新闻推送、股票行情、日志流等场景

Fast API 结合

| 项        | 信息                                                         |
| --------- | ------------------------------------------------------------ |
| 中间件    | 请求/响应会经过所有HTTP中间件<br />后续流式内容不经过中间件  |
| 异常处理  | 响应过程中的异常会经过异常处理函数<br />后续流式内容不经过异常处理函数 |
| 依赖注入  | 所有流式内容全部完成后才会迭代完成                           |
| token携带 | 原生`EventSource`只能将token放到query中<br />自定义或第三方库可以任意方式携带token |



### WebSocket模式



```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务端

    C->>S: GET /ws<br/>Connection: Upgrade<br/>Upgrade: websocket
    S-->>C: HTTP 101 Switching Protocols<br/>Upgrade: websocket
    Note over C,S: 协议升级完成，WebSocket连接建立

    C->>S: 发送文本/二进制帧
    S->>C: 推送文本/二进制帧
    C->>S: 发送文本/二进制帧
    S->>C: 推送文本/二进制帧
    Note over C,S: 全双工通信，任意一方可随时发送

    C->>S: Close帧 (主动关闭)
    S-->>C: Close确认帧
    Note over C,S: 连接优雅关闭
```

**关键特征**：
- 先通过HTTP握手，再升级为WebSocket独立协议（ws:// 或 wss://）
- 全双工通信：客户端和服务端均可主动发送消息
- 数据帧支持文本和二进制格式
- 适合在线聊天、多人协作、实时游戏等高频双向交互场景

Fast API 结合

| 项        | 信息                                         |
| --------- | -------------------------------------------- |
| 中间件    | 请求/响应都不会经过HTTP中间件                |
| 异常处理  | 不会经过异常处理函数                         |
| 依赖注入  | 连接断开后才会迭代结束                       |
| token携带 | 浏览器不支持自定义头，只能通过query携带token |



### SSE vs WebSocket 对比

| 特性 | SSE | WebSocket |
|------|-----|-----------|
| 通信方向 | 服务端→客户端（单向） | 全双工（双向） |
| 协议基础 | HTTP | 独立协议（基于HTTP握手） |
| 自动重连 | 原生支持 | 需手动实现 |
| 数据格式 | 文本（text/event-stream） | 文本或二进制 |
| 适用AI场景 | 简单的问答模式 | Agent 工作流<br />多人在线的AI协作 | 

## 部署-认识Docker



### 运行时的问题

你有一个从git拉取下来的FastAPI应用的全部源码。

如果你要在一个崭新的操作系统上启动它，需要做哪些事情？

<details> 
  <summary>📖 查看参考答案</summary> 
  <ol>
    <li>安装Python</li>
    <li>从镜像源安装uv</li>
    <li>设置uv镜像源</li>
    <li>安装运行时依赖：uv sync --frozen --no-dev --no-editable</li>
    <li>删除除.venv外的全部文件</li>
    <li>启动服务：uvicorn api.main:app --host 0.0.0.0 --port 8080</li>
  </ol> 
</details>



这些操作涉及到：

- 准备环境
- 准备必须的文件
- 启动命令



越是复杂的应用，需要安装的前置软件就越多，需要准备文件的过程就越复杂。



如果一台服务器中需要跑多个应用：

- 如何才能保证不同的应用环境互不干扰？
- 如何才能保证每一次在服务器端准备环境和文件的过程快捷而高效？
- 如何才能保证当应用更新过后，当环境和必须的文件发生变化过后，快速的更新？



这就是Docker要解决的问题。

### Docker

![image-20260702135701716](https://resource.duyiedu.com/yuanjin/202608012025285.png)

#### Dockerfile

一个配置文件，通过该文件产生一个镜像

```dockerfile
# 依赖轻量级python镜像，比完整镜像小90%，提升构建速度和构建产物的大小
FROM python:3.14-slim AS builder

# WORKDIR：设置工作目录，如果目录不存在则自动创建
WORKDIR /app

# RUN：安装 uv，RUN命令在镜像构建过程中执行
RUN pip install uv -i https://mirrors.aliyun.com/pypi/simple/
# 设置环境变量UV_INDEX_URL，后续uv使用该镜像源
ENV UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
# 以下两行是为了提升构建性能的，现在不用管它
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# 将当前目录下的所有文件复制到镜像的 /app 目录中
COPY . .

# --mount=type=cache,target=/root/.cache/uv 为了提升构建性能，可选，现在不管
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable


# ============================================================================
# 开启全新环境
FROM python:3.14-slim

WORKDIR /app

# 将 builder 阶段的 /app/.venv 目录复制到当前镜像的 /app/.venv 目录中
COPY --from=builder /app/.venv /app/.venv

# 将虚拟环境目录加入到PATH变量
ENV PATH="/app/.venv/bin:$PATH"

# 描述信息，可使用 docker image inspect <镜像名>:<tag> 查看
EXPOSE 8080

# CMD：将来启动镜像时需要执行的命令
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]

```

```shell
# 构建镜像
docker build -t <镜像名>:<tag> .

# 构建指定平台可用的镜像
docker --platform linux/amd64 build -t <镜像名>:<tag> .
```



#### 镜像

包含运行所需要的一切，比如`python`、`uv`、`.venv`

#### 容器

通过镜像启动，启动时会运行镜像中的`CMD`

```shell
docker run -d \
  --name my-app \
  -p 9090:8080 \
  -e environment=production \
  --restart unless-stopped \
  --memory=512m \
  --cpus=1 \
  <镜像名>:<tag>
```

- **`-d` (detach)**: **后台运行容器**。这是生产环境中最常用的参数，让容器在后台默默运行，并把容器ID返回给你。
- **`--name`**: **给容器起个名字**。如果不指定，Docker 会随机生成一个名字。
- **`-p 9090:8080` (publish)**: **端口映射**。将宿主机的 `9090` 端口，映射到容器内部的 `8080` 端口。
- `-e environment=production` 设置环境变量。
- **`--restart unless-stopped`**: **重启策略**。告诉 Docker 当容器意外退出或宿主机重启时，自动重新启动容器（除非你手动停止了它）。
- **`--memory=512m` / `--cpus=1`**: **资源限制**。限制容器最多只能使用 512MB 内存和 1 个 CPU 核心，防止单个容器耗尽宿主机所有资源。

### 为duyi-service构建镜像

1. 复制`Dockerfile`和`dockerignore`

2. 构建镜像

   ```shell
   docker build -t duyi-service:latest .
   ```

3. 准备好生产数据库：`duyi_prod_db`

4. 启动镜像

   ```shell
   docker run -d \
     --name duyi-service \
     -p 80:8080 \
     -e COMMON_ENVIRONMENT=production \
     -e WEB_APP_NAME=渡一API接口 \
     -e WEB_CORS_ORIGINS=www.duyi.com \
   	-e WEB_CORS_EXPOSE_HEADERS=X-Process-Time \
   	-e WEB_JWT_SECRET_KEY=8f231a2b3c4d5e6f444b9c0d1e2f3a4b \
   	-e DB_HOST=192.168.1.6 \
     -e DB_PORT=5432 \
     -e DB_NAME=duyi_prod_db \
     -e DB_USER=admin \
     -e DB_PASSWORD=123123 \
     -e LOG_LEVEL=INFO \
     -e LOG_SLOW_QUERY_THRESHOLD=200 \
     --restart unless-stopped \
     --memory=512m \
     --cpus=1 \
     duyi-service:latest
   ```

   

### 容器简易部署流程

1. 开发
2. 本地通过Dockerfile构建镜像
3. 将镜像传输给服务器
4. 服务器运行容器
## 云资产

> 本节课需要阿里云充值10元左右
>
> 同时需要你拥有一个域名

### 数字证书

1. 搜索ssl，进入数字证书服务

2. 购买个人测试证书

3. 到左侧的证书管理去申请证书：域名填：duyi-api.<你的域名>

4. 等待审核完成

### VPC

在阿里云搜索并创建vpc

注意选择地区，后续几乎所有云产品都要使用该地区

地区：自行选择

名称：duyi-vpc

ipv4：10.0.0.0/16

交换机：创建4个，每个可用区两个交换机

### OSS

至少有两个OSS，一个用作线上测试，一个用作生产，地域必须和VPC一致

### RDS

RDS PostgreSQL Serverless

1. 进入RDS的控制台。
2. 创建实例
3. 付费类型选Serverless。
4. 地域选VPC所在地域
5. PostgreSQL，选16版本。
6. 点击完成SLR 授权
7. RCU选0.5～1
8. VPC选你之前新建的VPC
9. 交换机选你之前新建的交换机
10. 存储空间选最小值20G
11. 其他默认
12. 立即购买

实例创建需要3～10分钟，创建好后

1. 管理
2. 账号管理：创建一个高权限账号
3. 数据库管理：创建一个数据库duyi_db，授权账号填刚才那个账号
4. 数据库连接：记录内网连接地址

### ACR

- 左侧菜单点「**实例列表**」→ 点「**创建个人版实例**」（如果已有默认实例就直接用）
- 地区必须和vpc相同
- 创建命名空间：duyiedu
- 创建镜像仓库：duyi-service
- 设置登录密码
- 得到公网地址

```shell
# 本地使用docker登录
docker login --username=<你的阿里云用户名> <你的镜像仓库公网地址>
# 构建镜像
docker build --platform linux/amd64 -t <你的镜像仓库公网地址>/<命名空间>/<仓库名>:<tag> .
# 推送镜像
docker push <你的镜像仓库公网地址>/<命名空间>/<仓库名>:<tag>
```
## k8s

K8s的全称是 **Kubernetes**。它是一个**用于自动部署、扩缩和管理容器化应用程序的开源系统**

![image-20260703205044579](https://resource.duyiedu.com/yuanjin/202607032050643.png)

### 创建ACS集群

1. 搜「ACS」，进入 容器计算服务 ACS 控制台
2. 开通服务：根据提示一步一步操作，全部默认
3. 创建集群：
   - 集群名称：duyi-cluster
   - 地域：vpc所在地域
   - 专有网络：使用已有，选两个交换机（带有pod名称的）
   - SNAT暂不勾选
   - 安全组：普通安全组
   - API Server：勾选EIP暴露API Server
   - ingress：暂不创建
   - 其他默认

等待集群建立完成（5～10分钟左右）

等待期间，你可以删除ACR的latest镜像，重新使用带有版本号标记的镜像

### 部署服务

1. 进入刚才创建的集群详情页，找到连接信息

2. 根据提示安装`kubectl`

3. 获取长期config，选公网访问

4. 按照提示，将复制的config保存到指定位置

5. 本地运行`kubectl get nodes`，看是否能看到节点

6. 配置`docker`的拉取地址和身份信息

   ```shell
   export ACR_PASSWORD='<acr的密码>'
   
   # 创建拉取凭证
   kubectl create secret docker-registry acr-registry-secret \
     --docker-server=<acr的内网地址> \
     --docker-username=<阿里云用户名> \
     --docker-password="$ACR_PASSWORD"
   ```

7. 安装 `VSCode` 插件 `Kubernetes` 和 `Kubernetes Templates`

8. 安装 `Helm`

   - Mac: `brew install helm`
   - windows: 使用windows的包管理工具，或者问AI

9. 应用配置
   ```shell
   export DB_PASSWORD='<数据库密码>'
   export JWT_SECRET_KEY='<jwt密钥>'
   
   helm upgrade --install duyi-service ./k8s \
     --set secret.dbPassword="$DB_PASSWORD" \
     --set secret.jwtSecretKey="$JWT_SECRET_KEY" \
   ```

10. 查看应用状态
    ```shell
    kubectl get pods
    ```

    

11. 配置ALB
    1. 阿里云搜索SLB，创建ALB
       1. 地域和VPC相同
       2. 选择公网
       3. 选择VPC
       4. 选择两个VPC的交换机所在的可用区
       5. 交换机选之前ACS集群没选过的（不带pod）
       6. 标准版
       7. 实例名称你看着取
    2. 为域名添加CNAME记录，指向ALB的DNS
    3. 安装ALB Ingress Controller
       1. 进入容器计算服务
       2. 组件管理：搜索ALB Ingress Controller
       3. 安装，选择已有的Ingress
       4. 等待安装完成
       5. 网络 / 路由
       6. 创建Ingress
       7. 名称自行填写
       8. 服务选择duyi-service
       9. 端口8080
    4. 监听：回到ALB
       1. 80端口：已自动创建好了，编辑规则转发规则，重定向到443
       2. 443端口

## CICD

CI/CD 的全称是 **持续集成**（**Continuous Integration**）和 **持续交付**（**Continuous Delivery**）。

### 创建CICD的镜像环境

下载镜像到本地

通过网盘分享的文件：python框架
链接: https://pan.baidu.com/s/1y_wrznlLD4AkmOwZANhT4A?pwd=t61z 提取码: t61z 
--来自百度网盘超级会员v7的分享

#### CI

1. ACR创建新的镜像仓库：duyi-service-ci

3. 推送镜像到仓库：
   
   ```shell
   # 到下载的镜像所在目录
   docker load -i duyi-service-ci.tar
   # 修改成你的tag
   docker tag duyi-service-ci:latest 复制仓库公网地址:latest
   # 推送
   docker push 复制仓库公网地址:latest
   ```

#### CD

1. ACR创建新的镜像仓库：duyi-service-cd

2. 推送镜像到仓库
   ```shell
   # 到下载的镜像所在目录
   docker load -i duyi-service-ci.tar
   # 修改成你的tag
   docker tag duyi-service-ci:latest 复制仓库公网地址:latest
   # 推送
   docker push 复制仓库公网地址:latest
   ```
   
   

#### python环境

1. ACR创建新的镜像仓库：python

2. 推送镜像
   ```shell
   docker buildx build --platform linux/amd64 \
     -t 复制仓库公网地址:3.14-slim \
     --push \
     - <<< 'FROM python:3.14-slim'
   ```

   

### 阿里云效

将你的仓库关联到阿里云效

```shell
git remote add origin <仓库SSH地址>
```

#### 创建CI流水线

1. 创建流水线

2. 触发方式选择：代码提交

3. 阶段1添加CI任务

   1. 使用自定义的镜像源

   2. 添加执行命令步骤
      ```shell
      uv sync --frozen --all-packages
      # make test
      # make test-e2e
      # make test-smoke
      make test-unit
      ```

   3. 添加通知插件

#### 创建CD流水线

听课堂上讲吧

环境变量：`${CI_COMMIT_REF_NAME}`

需要准备的环境变量：

- KUBECONFIG_BASE64：k8s config 的base64编码
  ```shell
  cat ~/.kube/config | base64
  ```

- ACR_USERNAME: 阿里云的账号

- ACR_PASSWORD：ACR密码

- DOCKER_SERVER：ACR的仓库专用网络地址

- DB_PASSWORD: 数据库密码

- JWT_SECRET_KEY：JWT密钥

CD执行的命令

```shell
# 写入 kubeconfig
echo "$KUBECONFIG_BASE64" | base64 -d > /tmp/kubeconfig

# 创建 ACR 拉取凭证
kubectl create secret docker-registry acr-registry-secret \
  --docker-server="$DOCKER_SERVER" \
  --docker-username="$ACR_USERNAME" \
  --docker-password="$ACR_PASSWORD" \
  --dry-run=client -o yaml \
  --kubeconfig /tmp/kubeconfig \
  --namespace default | \
kubectl apply -f - --kubeconfig /tmp/kubeconfig --namespace default

# Helm 部署
TAG=${CI_COMMIT_REF_NAME}
helm upgrade --install duyi-service ./k8s \
  --set image.tag=$TAG \
  --set secret.dbPassword="$DB_PASSWORD" \
  --set secret.jwtSecretKey="$JWT_SECRET_KEY" \
  --kubeconfig /tmp/kubeconfig \
  --namespace default
```
## 部署-总结

### CI / CD

![image-20260706192009861](https://resource.duyiedu.com/yuanjin/202607061920982.png)

### 服务器架构

![服务器架构](https://resource.duyiedu.com/yuanjin/202607061925447.svg)

### 面试要点

- 未亲自参与服务器部署
- 了解流程，对细节不太了解
  - 微服务架构：AI服务不直接对外
  - 通过ACK管理pod集群
  - 通过ALB路由服务
  - 和后端/运维配合编写Dockerfile
  - 使用ACR镜像仓库
  - 云效流水线的两个节点：PR、tag
  - ...
- 经过短时间的学习，自己搭建部署流水线没有问题

### 作业

回答面试问题：你在之前的企业中写好的AI服务是如何部署的？请讲一讲你们的部署流程。

## python收官检验

### 能力检验

**你是否能借助AI、课件、课程视频，可控的完成下面的事项？**



1. 你是否能使用`uv`管理项目？包括：管理依赖、搭建monorepo？
2. 你是否知道`ASGI服务器`和`ASGI应用程序`的关联？
3. 你是否知道`pydantic`是干什么的？
4. 你是否知道`pydantic-setting`是干什么的？
5. 你是否知道`openapi`是干什么的？
6. 你是否知道`swagger`是干什么的？
7. 给你生成了一组数据模型，你是否能用它生成到数据库表，同时完成数据迁移？
8. 你是否清楚SQL注入，并保证自己不会造成这样的漏洞？
9. 你是否能编写普通难度的业务层方法？
10. 给你任意一个函数，你是否能把它暴露成API接口？
11. 你是否理解`FastAPI`的依赖注入机制？
12. 你是否理解`FastAPI`的`Lifespan`？
13. 你是否理解中间件？同时理解哪些事情是应该在中间件中完成的？
14. 你是否能使用`loguru`记录日志，并理解`stdin / stdout`？
15. 你是否能对异常进行统一处理？
16. 你是否能使用`pytest`进行测试脚本的编写，并且知道单元测试、集成测试、e2e测试、冒烟测试的各自特点？
17. 在性能上，你是否能考虑到哪些地方要使用长事务，哪些地方使用短事务？
18. 你是否能实现云存储的直连上传？
19. 你是否清楚为什么密码要使用`hash`存储？为什么需要加盐？
20. 你是否清楚`JWT`的签名为什么无法被篡改？
21. 你是否清楚什么是模板引擎？
22. 你是否能使用断点调试，解决疑难杂症？
23. 给你一个异步生成器函数，你是否能把它暴露成一个`SSE`或`WebSocket`？
24. 你是否知晓`CI/CD`的流水线？
25. 你是否知道`k8s`集群？
26. 当你遇到其他web应用框架，比如`Flask`、`Django`，你是否有信心通过阅读其官方文档完成业务需求？
27. 对于一些没见过的API，你是否能借助AI快速理解它的含义？



以上问题，如果22个问题你的答案是肯定的，你就能：

1. 无障碍的学习后续AI课程
2. 超越绝大部分企业对你`python`能力的要求
3. 高质量完成企业工作任务



### Python的就业市场

#### AI岗位

大部分岗位，需要你：

- 专注于AI能力
- 通过API接口暴露AI能力
- 做好日志记录
- 能实现流式响应（SSE + WebSocket）
- 保存必要数据到数据库
- 做好必要的测试

#### 全栈岗位

大部分岗位，需要你：

- 实现普通业务的CRUD
- 避免严重的安全问题和性能问题
- 能理解现有的各个中间件的作用，以及它们产生的影响
- 能根据现有项目的异常处理模式，对异常进行统一归拢处理
- 能根据现有的测试模式，对增量需求进行相关测试处理
- 能对关键业务环节做好日志记录


# py数据科学包
## 课程内容简介

- `NumPy` & `Pandas`

  这两个库是数据分析和科学计算的基石，是Agent处理结构化数据的核心工具

- `Matplotlib` & `Seaborn`

  这两个库负责将枯燥的数据转化为直观的图表，是Agent“秀出”分析成果的关键

## Jupyter

安装`VSCode`插件：`Jupyter`

```shell
# 初始化一个uv工程
uv init .

# 安装 jupyter
uv add --dev jupyter
```

新建`ipynb`文件，选择虚拟环境中的`python`，试试效果

## NumPy 核心概念

NumPy 是 Python 科学计算的基石库，几乎所有数据科学生态（Pandas、PyTorch 等）都建立在 NumPy 之上。

它的底层是使用 `C` 和 `C++` 编写的，因此在处理大规模数据时具有极高的性能。

本节课只讲 NumPy 的核心概念——理解 ndarray 这个数据结构本身，后续课程再讲具体操作。

### ndarray

`ndarray`（N-dimensional array）是 NumPy 的核心数据结构，表示一个**多维数组**。

它与 Python 原生列表的关键区别：
- **同质化**：所有元素必须是相同类型（dtype）
- **连续内存**：数据存储在连续内存块中，访问效率高
- **向量化运算**：无需循环即可对整个数组执行运算

```python
# 从列表创建 ndarray
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"数组: {arr}")
print(f"类型: {type(arr)}")
print(f"形状: {arr.size}, 维度: {arr.ndim}, 数据类型: {arr.dtype}")
```

### 核心概念

理解 NumPy 的关键在于掌握以下几个概念，它们决定了数组的**形状**、**存储方式**和**运算规则**。

#### shape（形状）

`shape` 是一个元组，描述数组在每个维度上的大小。它是理解数组结构的起点。

- 1D 数组：`(n,)`
- 2D 数组：`(m, n)` —— 类似矩阵
- 3D 数组：`(a, m, n)` —— 类似多个矩阵堆叠

```python
# 不同维度的数组
a1 = np.array([1, 2, 3, 4])                    # 1D
a2 = np.array([[1, 2], [3, 4], [5, 6]])            # 2D
a3 = np.array([[[1], [2], [3]], [[4], [5], [6]]])    # 3D

# ndim 和 size
print(f"\n维度数 (ndim): {a3.ndim}")
print(f"元素总数 (size): {a3.size}")

# 形状
print(f"1D shape: {a1.shape}")
print(f"2D shape: {a2.shape}")
print(f"3D shape: {a3.shape}")
```

##### 💡**场景**

目前你正在训练「渡一大模型」，每个 Embedding 向量的维度是 768，你现在投入到训练的向量一共有 1000 个，那么这个ndarray的维度是？尺寸是？形状是？

#### dtype（数据类型）

`dtype` 指定数组中每个元素的数据类型。因为 ndarray 是同质的，所以 dtype 统一描述所有元素。

常见 dtype：
- `float64` / `float32`：浮点数（Embedding 常用 float32 来节省内存）
- `int64` / `int32` / `int8`：整数
- `bool`：布尔值
- `object`：Python 对象（尽量避免，会失去向量化优势）

dtype 本质上是把 **C 的类型系统**暴露给了 Python：

| NumPy dtype | C 类型 | 大小 |
|-------------|--------|------|
| `int64` | `int64_t` | 8 字节 |
| `int32` | `int32_t` | 4 字节 |
| `float64` | `double` | 8 字节 |
| `float32` | `float` | 4 字节 |

而 Python 的 `int` 是**不定长**对象，每个对象头就有 28+ 字节开销。ndarray 用 C 的固定类型，才能实现连续存储和向量化计算。

> **Agent 场景**：Embedding 向量通常用 `float32`，Token ID 用 `int64`，Mask 用 `bool`。

```python
# 不同 dtype 的数组
f_arr = np.array([1.0, 2.0, 3.0], dtype=np.float32)
i_arr = np.array([1, 2, 3], dtype=np.int64)
b_arr = np.array([True, False, True], dtype=np.bool_)

print(f"float32: {f_arr.dtype}, 每元素 {f_arr.itemsize} 字节")
print(f"int64:   {i_arr.dtype}, 每元素 {i_arr.itemsize} 字节")
print(f"bool:    {b_arr.dtype}, 每元素 {b_arr.itemsize} 字节")

# 内存占用的差距
print(f"\n100万 float64: {1_000_000 * 8 / 1024 / 1024:.2f} MB")
print(f"100万 float32: {1_000_000 * 4 / 1024 / 1024:.2f} MB")

# 最佳实践，禁止在同一个数组中混合不同类型的数据
try:
    arr = np.array([1, 2, "a"], dtype=np.int64)
    print(arr.dtype)
except Exception as e:
    print(f"\n指定 dtype 后报错: {e}")
```

#### strides（步幅）

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/stride.png)

`strides` 是一个元组，表示在每个维度上**前进一个元素需要跳过的字节数**。它决定了 NumPy 如何在内存中「行走」。

```python
# 理解 strides
arr = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=np.int64)

print(f"shape:   {arr.shape}")     # (2, 3)
print(f"strides: {arr.strides}")   # (24, 8) = (3*8, 1*8)
print(f"itemsize: {arr.itemsize} 字节")  # int64 = 8

# 行步幅 = 3 * 8 = 24（跳到下一行需跳过 24 字节）
# 列步幅 = 1 * 8 = 8（跳到下一列需跳过 8 字节）
```

```python
# strides 的实际影响：转置是零拷贝的
arr = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=np.int64)

t = arr.T
print(f"t: {t}")
print(f"转置 shape:   {t.shape}")     # (3, 2)
print(f"转置 strides: {t.strides}")   # (8, 24)——只是交换了步幅！

t[0, 0] = 99
print(f"修改转置后原数组:\n{arr}")  # 原数组也被修改了
```

#### 轴（axis）

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/axis.png)

axis 是一个整数，表示数组的维度索引。它用于指定操作沿哪个维度进行。

```python
# axis 的含义
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(f"数组:\n{arr}")
print(f"沿 axis=0 求和 (每列): {arr.sum(axis=0)}")  # [5, 7, 9]
print(f"沿 axis=1 求和 (每行): {arr.sum(axis=1)}")  # [6, 15]
```

## NumPy 数据操作

上一节课我们理解了 ndarray 的核心概念（shape、dtype、strides、axis），本节课聚焦于**如何操作数组中的数据**。

先说明一下，这节课我们只讲基础操作。以后讲到具体应用（模型推理、数据预处理等）时，涉及到的 NumPy 操作会再拿出来细讲，到时候理解起来也更具体。

### 数组创建

除了从列表直接创建，NumPy 提供了很多便捷的构造方法。

```python
# 导入 NumPy 库
import numpy as np
```

```python
# np.zeros: 创建全零数组
print('zeros(2,3):\n', np.zeros((2,3)), '\n')
# np.ones: 创建全一数组
print('ones(2,3):\n', np.ones((2,3), dtype=np.float32), '\n')
# np.eye: 创建单位矩阵
print('eye(3):\n', np.eye(3))
```

```
zeros(2,3):
 [[0. 0. 0.]
 [0. 0. 0.]] 

ones(2,3):
 [[1. 1. 1.]
 [1. 1. 1.]] 

eye(3):
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

```python
# np.arange: 创建等差数组
print('arange(0, 10, 2):', np.arange(0, 10, 2))
# np.linspace: 创建等间隔数组
print('linspace(0, 1, 5):', np.linspace(0, 1, 5))
# np.linspace: 创建等间隔数组
print('linspace(0, 1, 5, endpoint=False):', np.linspace(0, 1, 5, endpoint=False))
```

```
arange(0, 10, 2): [0 2 4 6 8]
linspace(0, 1, 5): [0.   0.25 0.5  0.75 1.  ]
linspace(0, 1, 5, endpoint=False): [0.  0.2 0.4 0.6 0.8]
```

```python
# default_rng: 创建随机数生成器
rng = np.random.default_rng(41)
# uniform: 生成均匀分布随机数
print('uniform(0, 1, (2,3)):\n', rng.uniform(0, 1, (2,3)), '\n')
# normal: 生成正态分布随机数
print('normal(0, 1, (2,3)):\n', rng.normal(0, 1, (2,3)), '\n')
# integers: 生成随机整数
print('integers(0, 10, (2,3)):\n', rng.integers(0, 10, (2,3)))
```

```
uniform(0, 1, (2,3)):
 [[0.9541511  0.76793209 0.12597075]
 [0.82698809 0.84907207 0.34978284]] 

normal(0, 1, (2,3)):
 [[  0.93754881 -11.70818076 -13.58240395]
 [-13.06564025  -7.17615282  11.85621358]] 

integers(0, 10, (2,3)):
 [[4 3 0]
 [4 2 5]]
```

##### 💡**场景**

快速造一批模拟数据来测试逻辑。比如模拟 10 个商品的价格和销量，测试排序或筛选功能。

```python
# default_rng: 创建随机数生成器
rng = np.random.default_rng(42)
# uniform: 生成均匀分布随机数
prices = rng.uniform(10, 100, 10).round(2)
# integers: 生成随机整数
sales = rng.integers(0, 1000, 10)
print('价格:', prices)
print('销量:', sales)
```

```
价格: [79.66 49.5  87.27 72.76 18.48 97.81 78.5  80.75 21.53 50.53]
销量: [500 370 182 926 781 643 402 822 545 443]
```

### 索引与切片

NumPy 的索引语法与 Python 列表类似，但支持多维操作。

#### 基本索引与切片

语法：`arr[start:stop:step]`，多维就用逗号分隔。

- start：起始索引，默认 0
- stop：结束索引（不包含），默认数组长度
- step：步长，默认 1

**注意：切片返回的是视图（view），不是拷贝**——改切片会影响原数组。

```python
# np.arange: 创建等差数组
arr = np.arange(12).reshape(3, 4)
print('原数组:\n', arr, '\n')
print('arr[0]:', arr[0])
print('arr[:, 1]:\n', arr[:, 1:])
print('arr[1:, 2:]:\n', arr[1:, 2:])
```

```
原数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 

arr[0]: [0 1 2 3]
arr[:, 1]:
 [[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]]
arr[1:, 2:]:
 [[ 6  7]
 [10 11]]
```

```python
view = arr[1:, 2:]
view[0, 0] = 99
print('修改视图后原数组:\n', arr)
# copy: 创建数组的副本
copy = arr[1:, 2:].copy()
```

```
修改视图后原数组:
 [[ 0  1  2  3]
 [ 4  5 99  7]
 [ 8  9 10 11]]
```

#### 花式索引（Fancy Indexing）

用整数数组选取不连续的行/列。**返回的是拷贝。**

```python
# np.arange: 创建等差数组
arr = np.arange(12).reshape(4, 3)
print('数组:\n', arr, '\n')
print('arr[[0, 2]]:\n', arr[[0, 2]], '\n')
rows = [0, 1, 3]
cols = [2, 1, 0]
print('arr[rows, cols]:', arr[rows, cols])
```

```
数组:
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]] 

arr[[0, 2]]:
 [[0 1 2]
 [6 7 8]] 

arr[rows, cols]: [2 4 9]
```

#### 布尔索引（Boolean Indexing）

用布尔数组作为掩码（mask），选取满足条件的元素。**返回的是拷贝。**

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([10, 25, 3, 47, 8, 19])
mask = arr > 15
print('mask:', mask)
print('arr[arr > 15]:', arr[mask])
print('arr[arr % 2 == 0]:', arr[arr % 2 == 0])
```

```
mask: [False  True False  True False  True]
arr[arr > 15]: [25 47 19]
arr[arr % 2 == 0]: [10  8]
```

```python
arr = np.array([5, 12, 18, 25, 30, 7, 42])
print('(>10) & (<30):', arr[(arr > 10) & (arr < 30)])
print('(<10) | (>30):', arr[(arr < 10) | (arr > 30)])
```

```
(>10) & (<30): [12 18 25]
(<10) | (>30): [ 5  7 42]
```

### 变形与重塑

改变数组的形状而不改数据。总元素数必须一致，用 `-1` 让 NumPy 自动算。

```python
# np.arange: 创建等差数组
arr = np.arange(12)
print('原始:', arr, '\n')
# reshape: 重塑数组形状
print('reshape(3, 4):\n', arr.reshape(3, 4), '\n')
# reshape: 重塑数组形状
print('reshape(2, -1):\n', arr.reshape(2, -1), '\n')
# reshape: 重塑数组形状
print('reshape(2, 2, 3):\n', arr.reshape(2, 2, 3))
```

```
原始: [ 0  1  2  3  4  5  6  7  8  9 10 11] 

reshape(3, 4):
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 

reshape(2, -1):
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]] 

reshape(2, 2, 3):
 [[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]
```

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([1, 2, 3, 4])
# np.resize: 改变数组大小（可重复填充）
print('np.resize(arr, (2, 3)):\n', np.resize(arr, (2, 3)))
# np.resize: 改变数组大小（可重复填充）
print('np.resize(arr, (2, 2)):\n', np.resize(arr, (2, 2)))
```

```
np.resize(arr, (2, 3)):
 [[1 2 3]
 [4 1 2]]
np.resize(arr, (2, 2)):
 [[1 2]
 [3 4]]
```

##### 💡**场景**

API 返回的数据是一维的，但你需要按行列组织成表格，用 reshape 搞定。

```python
# np.array: 从列表创建 NumPy 数组
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# reshape: 重塑数组形状
table = data.reshape(4, 3)
print('转换为 4行3列的表格:\n', table)
```

```
转换为 4行3列的表格:
 [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

### 数学运算

NumPy 的所有运算符都是**向量化**的——对整个数组一次性操作，不用写循环。

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([1, 2, 3, 4])
print('原数组:', arr)
print('arr + 10:', arr + 10)
print('arr * 2:', arr * 2)
print('arr ** 2:', arr ** 2)
print('arr > 2:', arr > 2)
```

```
原数组: [1 2 3 4]
arr + 10: [11 12 13 14]
arr * 2: [2 4 6 8]
arr ** 2: [ 1  4  9 16]
arr > 2: [False False  True  True]
```

```python
# np.array: 从列表创建 NumPy 数组
a = np.array([10, 20, 30])
# np.array: 从列表创建 NumPy 数组
b = np.array([1, 2, 3])
print('a + b:', a + b)
print('a - b:', a - b)
print('a * b:', a * b)
print('a / b:', a / b)
```

```
a + b: [11 22 33]
a - b: [ 9 18 27]
a * b: [10 40 90]
a / b: [10. 10. 10.]
```

##### 💡**场景**

对一批数据做批量转换。比如商品价格全部打八折，温度从摄氏度转华氏度。

```python
# np.array: 从列表创建 NumPy 数组
prices = np.array([99, 199, 299, 399], dtype=float)
discounted = prices * 0.8
print('原价:', prices)
print('打八折:', discounted)

# np.array: 从列表创建 NumPy 数组
celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9 / 5 + 32
print('摄氏:', celsius)
print('华氏:', fahrenheit)
```

```
原价: [ 99. 199. 299. 399.]
打八折: [ 79.2 159.2 239.2 319.2]
摄氏: [ 0 10 20 30 40]
华氏: [ 32.  50.  68.  86. 104.]
```

### 统计运算

对数组做聚合统计，可以用 `axis` 指定沿哪个方向算。

```python
# np.arange: 创建等差数组
arr = np.arange(12).reshape(3, 4).astype(float)
print('数组:\n', arr, '\n')
# sum: 计算所有元素之和
print('sum:', arr.sum())
# mean: 计算算术平均值
print('mean:', arr.mean())
# sum: 计算所有元素之和
print('sum(axis=0) 按列求和:', arr.sum(axis=0))
# sum: 计算所有元素之和
print('sum(axis=1) 按行求和:', arr.sum(axis=1))
# min: 找出最小值
print('min:', arr.min(), ', max:', arr.max())
# argmin: 找出最小值所在的索引
print('argmin:', arr.argmin(), ', argmax:', arr.argmax())
```

```
数组:
 [[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]] 

sum: 66.0
mean: 5.5
sum(axis=0) 按列求和: [12. 15. 18. 21.]
sum(axis=1) 按行求和: [ 6. 22. 38.]
min: 0.0 , max: 11.0
argmin: 0 , argmax: 11
```

##### 标准差

标准差（Standard Deviation）是统计学中衡量数据波动程度（即离散程度）最常用的指标。简单来说，它告诉你数据围绕平均值有多"散"。

标准差越小：说明数据越集中，平均值越有代表性（大家成绩都差不多）。

标准差越大：说明数据越分散，平均值越不靠谱（有人考100分，有人考0分）。

$$
\textbf{1. 总体标准差（Population Standard Deviation）}\\[1em]

\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}\\[2em]

\textbf{2. 样本标准差（Sample Standard Deviation）}\\[1em]

s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}\\[1em]
$$

```python
print("arr", arr)
print("mean", arr.mean())
# std: 计算总体标准差
print('std总体标准差:', arr.std())
# std: 计算样本标准差
print('std(ddof=1)样本标准差:', arr.std(ddof=1))
# 变异系数
print('变异系数CV:', arr.std() / arr.mean())
```

```
arr [[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]]
mean 5.5
std总体标准差: 3.452052529534663
std(ddof=1)样本标准差: 3.605551275463989
变异系数CV: 0.6276459144608478
```

| CV 范围       | 离散程度   | 直观感受                       | 典型场景举例                             |
| :------------ | :--------- | :----------------------------- | :--------------------------------------- |
| **< 10%**     | **非常小** | 数据极度集中，几乎一模一样     | 工厂自动化生产的零件尺寸、精密仪器读数   |
| **10% ~ 20%** | **较小**   | 有波动但很稳定，平均值可靠     | 成年人的身高、体重、日常气温             |
| **20% ~ 30%** | **中等**   | 正常波动范围，尚可接受         | 学生考试成绩、员工绩效评分               |
| **30% ~ 50%** | **较大**   | 数据比较分散，平均值代表性下降 | 城市房价、不同地区的薪资水平             |
| **> 50%**     | **非常大** | 极度分散，平均值几乎没意义     | 股票日收益率、创业公司估值、个人消费支出 |

### 条件筛选与 np.where

`np.where(condition, x, y)` —— 如果条件成立取 x 的值，否则取 y 的值。类似向量化的 if-else。

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([10, -5, 3, -8, 0, 15])
# np.where: 根据条件筛选或替换值
result = np.where(arr < 0, 0, arr)
print('原数组:', arr)
print('负数变 0:', result)
```

```
原数组: [10 -5  3 -8  0 15]
负数变 0: [10  0  3  0  0 15]
```

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([10, 20, 30, 40, 50])
# np.where: 根据条件筛选或替换值
indices = np.where(arr > 25)
print('arr > 25 的位置:', indices)
print('对应值:', arr[indices])
```

```
arr > 25 的位置: (array([2, 3, 4]),)
对应值: [30 40 50]
```

##### 💡**场景**

对数据进行分类处理。比如成绩单中，60 分以上标记为「通过」，否则为「不通过」。

```python
# np.array: 从列表创建 NumPy 数组
scores = np.array([85, 42, 73, 59, 90, 31, 68])
# np.where: 根据条件筛选或替换值
result = np.where(scores >= 60, '通过', '不通过')
print('成绩:', scores)
print('结果:', result)
```

```
成绩: [85 42 73 59 90 31 68]
结果: ['通过' '不通过' '通过' '不通过' '通过' '不通过' '通过']
```

### 拼接与分割

把多个数组合并，或把一个数组拆成多份。

```python
# np.array: 从列表创建 NumPy 数组
a = np.array([[1, 2], [3, 4]])
# np.array: 从列表创建 NumPy 数组
b = np.array([[5, 6]])
# np.vstack: 垂直堆叠数组
print('vstack (垂直拼):\n', np.vstack([a, b]), '\n')
# np.concatenate: 沿指定轴拼接数组
print('concatenate axis=0:\n', np.concatenate([a, b], axis=0))
```

```
vstack (垂直拼):
 [[1 2]
 [3 4]
 [5 6]] 

concatenate axis=0:
 [[1 2]
 [3 4]
 [5 6]]
```

```python
# np.array: 从列表创建 NumPy 数组
a = np.array([[1, 2], [3, 4]])
# np.array: 从列表创建 NumPy 数组
b = np.array([[5], [6]])
# np.hstack: 水平堆叠数组
print('hstack (水平拼):\n', np.hstack([a, b]), '\n')
# np.concatenate: 沿指定轴拼接数组
print('concatenate axis=1:\n', np.concatenate([a, b], axis=1))
```

```
hstack (水平拼):
 [[1 2 5]
 [3 4 6]] 

concatenate axis=1:
 [[1 2 5]
 [3 4 6]]
```

```python
# np.arange: 创建等差数组
arr = np.arange(16).reshape(4, 4)
print('数组:\n', arr, '\n')
# np.split: 沿行方向分割数组
first, second, rest = np.split(arr, [1, 3])
print('[:1]:\n', first, '\n')
print('[1:3]:\n', second, '\n')
print('[3:]:\n', rest)
```

```
数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]] 

[:1]:
 [[0 1 2 3]] 

[1:3]:
 [[ 4  5  6  7]
 [ 8  9 10 11]] 

[3:]:
 [[12 13 14 15]]
```

```python
# np.arange: 创建等差数组
arr = np.arange(12).reshape(3, 4)
print('数组:\n', arr, '\n')
# np.hsplit: 沿列方向分割数组
left, right = np.hsplit(arr, 2)
print('左:\n', left, '\n')
print('右:\n', right)
```

```
数组:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 

左:
 [[0 1]
 [4 5]
 [8 9]] 

右:
 [[ 2  3]
 [ 6  7]
 [10 11]]
```

### 排序

排序在很多场景中都会用到。

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print('原数组:', arr)
# np.sort: 返回排序后的数组
print('np.sort(arr):', np.sort(arr))
# np.argsort: 返回排序后的索引数组
print('np.argsort(arr):', np.argsort(arr))
# np.unique: 返回唯一值
print('np.unique(arr):', np.unique(arr))
```

```
原数组: [3 1 4 1 5 9 2 6]
np.sort(arr): [1 1 2 3 4 5 6 9]
np.argsort(arr): [1 3 6 0 2 4 7 5]
np.unique(arr): [1 2 3 4 5 6 9]
```

```python
# np.array: 从列表创建 NumPy 数组
matrix = np.array([[3, 1, 2], [6, 5, 4]])
print('矩阵:\n', matrix, '\n')
# np.sort: 返回排序后的数组
print('每行排序:\n', np.sort(matrix, axis=1))
# np.sort: 返回排序后的数组
print('每列排序:\n', np.sort(matrix, axis=0))
```

```
矩阵:
 [[3 1 2]
 [6 5 4]] 

每行排序:
 [[1 2 3]
 [4 5 6]]
每列排序:
 [[3 1 2]
 [6 5 4]]
```

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([3, 1, 4, 1, 5])
# sort: 原地排序数组
arr.sort()
# sort: 原地排序数组
print('arr.sort() 后:', arr)
```

```
arr.sort() 后: [1 1 3 4 5]
```

##### 💡**场景**

找出数据中最大/最小的前几个。比如找出销量最高的前 3 个商品。

```python
# np.array: 从列表创建 NumPy 数组
sales = np.array([230, 150, 890, 340, 560, 120, 670])
# np.argsort: 返回排序后的索引数组
top3_idx = np.argsort(sales)[::-1][:3]
print('销量:', sales)
print('前 3 名索引:', top3_idx)
print('前 3 名销量:', sales[top3_idx])
```

```
销量: [230 150 890 340 560 120 670]
前 3 名索引: [2 6 4]
前 3 名销量: [890 670 560]
```

### 广播（Broadcasting）

广播是 NumPy 的特色：**对不同形状的数组做运算时，NumPy 会自动把小数组「扩展」成和大数组一样的形状**，无需手动复制。

规则：从尾部维度开始比，维度相同或有一个是 1 就能广播。

```python
# np.array: 从列表创建 NumPy 数组
arr = np.array([1, 2, 3])
print('arr + 10:', arr + 10)
print('arr * 5:', arr * 5)
```

```
arr + 10: [11 12 13]
arr * 5: [ 5 10 15]
```

```python
# np.arange: 创建等差数组
matrix = np.arange(12).reshape(3, 4)
# np.array: 从列表创建 NumPy 数组
row = np.array([10, 20, 30, 40])
# np.array: 从列表创建 NumPy 数组
col = np.array([[100], [200], [300]])

print('matrix:\n', matrix, '\n')
print('matrix + row (行广播):\n', matrix + row, '\n')
# reshape: 重塑数组形状
print('matrix + col[:, None] (列广播):\n', matrix + col)
```

```
matrix:
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 

matrix + row (行广播):
 [[10 21 32 43]
 [14 25 36 47]
 [18 29 40 51]] 

matrix + col[:, None] (列广播):
 [[100 101 102 103]
 [204 205 206 207]
 [308 309 310 311]]
```

```python
# np.array: 从列表创建 NumPy 数组
a = np.array([[1], [2], [3]])
# np.array: 从列表创建 NumPy 数组
b = np.array([10, 20, 30, 40])
print('(3,1) + (4,) -> (3,4):\n', a + b)
```

```
(3,1) + (4,) -> (3,4):
 [[11 21 31 41]
 [12 22 32 42]
 [13 23 33 43]]
```

##### 💡**场景**

给一个二维表格的每一列加上不同的偏移量，或者每行乘以不同的系数。

```python
# np.array: 从列表创建 NumPy 数组
data = np.array([[80, 90, 85],
                 [70, 75, 80],
                 [60, 65, 70]])
# np.array: 从列表创建 NumPy 数组
bonus = np.array([5, 10, 3])
print('原始成绩:\n', data, '\n')
print('加上加分 (每人加的不同):\n', data + bonus)
```

```
原始成绩:
 [[80 90 85]
 [70 75 80]
 [60 65 70]] 

加上加分 (每人加的不同):
 [[ 85 100  88]
 [ 75  85  83]
 [ 65  75  73]]
```

### 总结

本节课覆盖了 NumPy 最常用的数据操作：

| 操作 | 常用方法 |
|------|----------|
| **创建** | `array`, `zeros`, `ones`, `arange`, `linspace`, `random` |
| **索引** | `arr[i]`, `arr[i:j]`, 花式索引, 布尔索引 |
| **变形** | `reshape`, `resize` |
| **数学运算** | `+`, `-`, `*`, `/`, `**`, `sin`, `cos`, `exp`, `sqrt` |
| **统计运算** | `sum`, `mean`, `std`, `min`, `max`, `cumsum` |
| **条件筛选** | `np.where`, 布尔掩码 |
| **拼接分割** | `concatenate`, `vstack`, `hstack`, `split` |
| **排序** | `sort`, `argsort`, `unique` |
| **广播** | 自动维度扩展 |

## Pandas 核心数据结构

其他竞品：Polars、Dask、DuckDB、Modin、FireDucks、Datatable

Pandas 是 Python 数据分析的核心库，它提供了两种核心数据结构：**Series** 和 **DataFrame**。

简单来说：
- **Series** → 一列带标签的数据（类似一个带索引的数组或 Excel 中的一列）
- **DataFrame** → 一个带标签的二维表格（类似 Excel 工作表或 SQL 表）

### Series

Series 可以理解为「带标签的一维数组」。它由两个核心部分组成：
- `values`：数据本身（类似 NumPy 数组）
- `index`：每个数据点的标签

```python
!uv add pandas==3.0.3 openpyxl==3.1.5
# 导入 Pandas 库
import pandas as pd
import numpy as np
```

```python
# pd.Series: 从列表创建 Series
pd.Series([10, 20, 30, 40])
```

```
0    10
1    20
2    30
3    40
dtype: int64
```

```python
# 从列表创建，指定索引
pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
```

```
a    10
b    20
c    30
d    40
dtype: int64
```

```python
# 从字典创建，key 自动成为索引
pd.Series({'a': 10, 'b': 20, 'c': 30})
```

```
a    10
b    20
c    30
dtype: int64
```

```python
# 核心属性
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print('values:', s.values, type(s.values))
print('index:', s.index, type(s.index))
print('dtype:', s.dtype)
print('shape:', s.shape)
```

```
values: [10 20 30 40] <class 'numpy.ndarray'>
index: Index(['a', 'b', 'c', 'd'], dtype='str') <class 'pandas.Index'>
dtype: int64
shape: (4,)
```

### DataFrame 创建

DataFrame 是一个二维表格结构，可以来自多种数据源。

```python
# pd.DataFrame: 从字典创建——key 是列名，value 是列数据
pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '薪资': [15000, 20000, 25000, 18000]
})
```

```
   姓名  年龄  城市     薪资
0  张三  25  北京  15000
1  李四  30  上海  20000
2  王五  35  广州  25000
3  赵六  28  深圳  18000
```

```python
# pd.DataFrame: 从嵌套列表创建——通过 columns 指定列名
pd.DataFrame([
    ['张三', 25, '北京', 15000],
    ['李四', 30, '上海', 20000],
    ['王五', 35, '广州', 25000],
], columns=['姓名', '年龄', '城市', '薪资'])
```

```
   姓名  年龄  城市     薪资
0  张三  25  北京  15000
1  李四  30  上海  20000
2  王五  35  广州  25000
```

```python
# pd.DataFrame: 从 NumPy 数组创建
arr = np.array([
    [25, 15000],
    [30, 20000],
    [35, 25000],
])
pd.DataFrame(arr, columns=['年龄', '薪资'])
```

```
   年龄     薪资
0  25  15000
1  30  20000
2  35  25000
```

#### 从文件读取

实际工作中数据很少手动输入，更多是从文件加载。Pandas 支持各种格式。

```python
# 从 CSV 文件读取（实际文件路径）——展示用法，不实际执行
df = pd.read_csv('../linking.csv')
df
# pd.read_csv 常用参数
# df = pd.read_csv('data.csv', encoding='utf-8')       # 指定编码
# df = pd.read_csv('data.csv', header=None)            # 无表头
# df = pd.read_csv('data.csv', index_col='id')         # 指定索引列
# df = pd.read_csv('data.csv', usecols=['a', 'b'])     # 只读指定列
# df = pd.read_csv('data.csv', nrows=100)              # 只读前 100 行
```

```
         昵称  学历  城市            经验                薪资  \
0       Map   本  北京          26应届                实习   
1    yanni*   本  杭州  6年前端\r\n2年转行  前端：20k\r\n转行：28k   
2       边牧*   本  长沙            5年                9k   
3       决堤*  本科  北京          25应届                9k   
4       月亮*   专  济南            3年                9k   
..      ...  ..  ..           ...               ...   
674     lh*  初中  上海            8年               18k   
675     微斯*   本  北京          3.5年               17k   
676     海盐*   专  北京          6.5年     25k->22k->18k   
677    wah*   专  上海            7年               20k   
678      渔*   本  武汉            2年                6k   

                               备注  
0                             NaN  
1          新能源企业前端-->产品-->销售-->售前  
2    离职，空窗期2年，北京17k，React，Flutter  
3                             被辞退  
4                             NaN  
..                            ...  
674                            前端  
675                           NaN  
676                            前端  
677                            前端  
678                            前端  

[679 rows x 6 columns]
```

```python
# pd.read_excel: 从 Excel 文件读取
df_xlx = pd.read_excel('../linking.xlsx', sheet_name='Sheet1')
df_xlx
# pd.read_json: 从 JSON 文件读取
# df = pd.read_json('data.json')
```

```
         昵称  学历  城市          经验              薪资                            备注
0       Map   本  北京        26应届              实习                           NaN
1    yanni*   本  杭州  6年前端\n2年转行  前端：20k\n转行：28k        新能源企业前端-->产品-->销售-->售前
2       边牧*   本  长沙          5年              9k  离职，空窗期2年，北京17k，React，Flutter
3       决堤*  本科  北京        25应届              9k                           被辞退
4       月亮*   专  济南          3年              9k                           NaN
..      ...  ..  ..         ...             ...                           ...
674     lh*  初中  上海          8年             18k                            前端
675     微斯*   本  北京        3.5年             17k                           NaN
676     海盐*   专  北京        6.5年   25k->22k->18k                            前端
677    wah*   专  上海          7年             20k                            前端
678      渔*   本  武汉          2年              6k                            前端

[679 rows x 6 columns]
```

#### 从数据库读取

Pandas 还可以直接读取 SQL 查询结果。这里以 Python 内置的 SQLite 为例。

```python
# pd.read_sql: 从数据库读取 SQL 查询结果
import sqlite3

# 创建内存数据库并写入数据
conn = sqlite3.connect(':memory:')
conn.execute('''
    CREATE TABLE employees (
        name TEXT, age INT, city TEXT, salary INT
    )
''')
conn.execute("INSERT INTO employees VALUES ('张三', 25, '北京', 15000)")
conn.execute("INSERT INTO employees VALUES ('李四', 30, '上海', 20000)")
conn.execute("INSERT INTO employees VALUES ('王五', 35, '广州', 25000)")
conn.execute("INSERT INTO employees VALUES ('赵六', 28, '深圳', 18000)")
conn.commit()

df = pd.read_sql('SELECT * FROM employees', conn)
conn.close()
df
```

```
  name  age city  salary
0   张三   25   北京   15000
1   李四   30   上海   20000
2   王五   35   广州   25000
3   赵六   28   深圳   18000
```

##### 💡**场景**

你的团队用 MySQL/PostgreSQL 存储业务数据，直接 `pd.read_sql('SELECT ...', connection)` 就能把数据拉到 DataFrame 里做分析，不用手动导出成 CSV。

### DataFrame 的组成结构

一个 DataFrame 内部由以下核心部分组成。理解它们，你就掌握了一半。

```python
df_xlx
```

```
         昵称  学历  城市          经验              薪资                            备注
0       Map   本  北京        26应届              实习                           NaN
1    yanni*   本  杭州  6年前端\n2年转行  前端：20k\n转行：28k        新能源企业前端-->产品-->销售-->售前
2       边牧*   本  长沙          5年              9k  离职，空窗期2年，北京17k，React，Flutter
3       决堤*  本科  北京        25应届              9k                           被辞退
4       月亮*   专  济南          3年              9k                           NaN
..      ...  ..  ..         ...             ...                           ...
674     lh*  初中  上海          8年             18k                            前端
675     微斯*   本  北京        3.5年             17k                           NaN
676     海盐*   专  北京        6.5年   25k->22k->18k                            前端
677    wah*   专  上海          7年             20k                            前端
678      渔*   本  武汉          2年              6k                            前端

[679 rows x 6 columns]
```

```python
# columns: 列名
print('columns:', df_xlx.columns)
print('类型:', type(df_xlx.columns))
```

```
columns: Index(['昵称', '学历', '城市', '经验', '薪资', '备注'], dtype='str')
类型: <class 'pandas.Index'>
```

```python
# index: 行索引
print('index:', df_xlx.index)
print('类型:', type(df_xlx.index))
```

```
index: RangeIndex(start=0, stop=679, step=1)
类型: <class 'pandas.RangeIndex'>
```

```python
# values: 核心数据（二维 NumPy 数组）
print('类型:', type(df_xlx.values))
print('values:')
df_xlx.to_numpy()
```

```
类型: <class 'numpy.ndarray'>
values:
array([['Map', '本', '北京', '26应届', '实习', nan],
       ['yanni*', '本', '杭州', '6年前端\n2年转行', '前端：20k\n转行：28k',
        '新能源企业前端-->产品-->销售-->售前'],
       ['边牧*', '本', '长沙', '5年', '9k', '离职，空窗期2年，北京17k，React，Flutter'],
       ...,
       ['海盐*', '专', '北京', '6.5年', '25k->22k->18k', '前端'],
       ['wah*', '专', '上海', '7年', '20k', '前端'],
       ['渔*', '本', '武汉', '2年', '6k', '前端']], shape=(679, 6), dtype=object)
```

```python
# dtypes: 每列的数据类型
print('dtypes:')
df.dtypes
```

```
dtypes:
name        str
age       int64
city        str
salary    int64
dtype: object
```

```python
# shape: 形状 (行数, 列数)
print('shape:', df.shape)
print('行数:', df.shape[0])
print('列数:', df.shape[1])
```

```
shape: (679, 6)
行数: 4
列数: 4
```

```python
# size: 元素总数
print('size:', df.size)
# ndim: 维度数
print('ndim:', df.ndim)
```

```
size: 16
ndim: 2
```
## Pandas 数据清洗

数据清洗是数据分析中最耗时但也最重要的环节。
真实世界的数据往往是「脏」的——类型不统一、格式不一致、缺失值、异常值……

本节课我们以一份真实的程序员薪资调查数据为例，动手做一次完整的数据清洗。

**核心目标**：统一各列数据类型，让数据「干净、可用」。

```python
import pandas as pd
import numpy as np
import re

df = pd.read_excel('../linking.xlsx')
```

```python
# loc: 按索引标签名定位（行名、列名）
# 语法: df.loc[行, 列]
# df.loc[0:5]  # 索引0到5的所有行
# df.loc[0:5, "城市"]  # 取前5行的城市列
# df["城市"] == "北京"
# df.loc[df["城市"] == "北京"]  # 条件筛选所有列

# # iloc: 按整数位置定位
# # 语法: df.iloc[行位置, 列位置]
# df.iloc[0:5]  # 前5行
# df.iloc[0:5, 0:3]  # 前5行、前3列
# df.iloc[0, 0]  # 第一行第一列的值
```

```
0    北京
1    杭州
2    长沙
3    北京
4    济南
Name: 城市, dtype: str
```

### 1. 数据初探

拿到一份新数据，先别急着动手——先「观察」。

`df.info()` 可以快速了解：数据量、各列类型、缺失情况。

```python
df.info()
```

```
<class 'pandas.DataFrame'>
RangeIndex: 679 entries, 0 to 678
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   昵称      676 non-null    object
 1   学历      677 non-null    str   
 2   城市      658 non-null    str   
 3   经验      662 non-null    object
 4   薪资      578 non-null    str   
 5   备注      222 non-null    object
dtypes: object(3), str(3)
memory usage: 32.0+ KB
```

`df.head()` 看一下前几行，对数据内容有个直观感受。

```python
df.head()
```

```
       昵称  学历  城市          经验              薪资                            备注
0     Map   本  北京        26应届              实习                           NaN
1  yanni*   本  杭州  6年前端\n2年转行  前端：20k\n转行：28k        新能源企业前端-->产品-->销售-->售前
2     边牧*   本  长沙          5年              9k  离职，空窗期2年，北京17k，React，Flutter
3     决堤*  本科  北京        25应届              9k                           被辞退
4     月亮*   专  济南          3年              9k                           NaN
```

再单独看看每列的类型和缺失值数量。

这里我们发现：虽然有 679 行，但很多列都有缺失值；而且**类型全是 object/str**——
数值型的字段（经验、薪资）被读成了字符串，这是我们今天要解决的核心问题。

```python
df.dtypes
```

```
昵称    object
学历       str
城市       str
经验    object
薪资       str
备注    object
dtype: object
```

```python
df.isna().sum()
```

```
昵称      3
学历      2
城市     21
经验     17
薪资    101
备注    457
dtype: int64
```

### 2. 应届信息提取

很多列都混入了「26应届」「25应届」这类值——它其实是「毕业年份」信息，不是该列的正常数据。
统一做法：把「X应届」提取为独立的一列「毕业年份」，原列留空（经验列写 0）。

先看看「应届」值分布在哪些列：

```python
col_name = '学历'
temp_mask = df[col_name].astype(str).str.contains('应届', na=False)
# temp_mask
df.loc[temp_mask, col_name].head(10)
# df[temp_mask][['城市','经验','薪资','学历']].head(10)
```

```
Series([], Name: 学历, dtype: str)
```

用 `str.extract()` 可以从字符串中提取正则匹配的部分。先试试一列：

```python
df.loc[temp_mask, '城市'].astype(str).str.extract(r'(\d+)\s*应届')
```

```
      0
51   26
171  26
191  29
197  26
198  26
199  27
202  27
203  25
207  27
263  26
377  27
381  26
382  27
416  26
658  26
```

拿到数字后加上 2000 就是真实的毕业年份。现在统一处理所有列：

```python
df['毕业年份'] = np.nan

for col in ['城市', '经验']:
    mask = df[col].astype(str).str.contains(r'应届', na=False)
    year = df.loc[mask, col].astype(str).str.extract(r'(\d+)\s*应届')
    if not year.empty:
        df.loc[mask, '毕业年份'] = 2000 + year[0].dropna().astype(int)
    if col == '经验':
        df.loc[mask, col] = 0.0
    else:
        df.loc[mask, col] = None
```

```python
df['毕业年份'].value_counts(dropna=False)
```

```
毕业年份
NaN       570
2026.0     62
2027.0     34
2025.0      8
2028.0      4
2029.0      1
Name: count, dtype: int64
```

```python
df['城市'].value_counts(dropna=False)
```

```
城市
北京      128
深圳       77
上海       68
成都       62
杭州       60
       ... 
广西柳州      1
河北        1
鄂州        1
江西        1
保定        1
Name: count, Length: 70, dtype: int64
```

```python
df['经验'].value_counts(dropna=False)
```

```
经验
0.0           99
3年            77
4年            68
5年            65
6年            39
7年            35
2年            32
1年            31
3.5年          30
1.5年          25
2.5年          23
0.5年          23
8年            18
4.5年          17
NaN           17
10年           16
9年            15
5.5年           8
11年            6
0年             5
7.5年           3
9.5年           2
13年            2
12年            2
-              2
<1年            2
6年前端\n2年转行     1
4个月            1
上海             1
14年            1
15年+           1
<3年            1
17年            1
大一             1
大三             1
23年毕业          1
10+年           1
8年+            1
3个月            1
创业9年           1
转行             1
读研             1
6.5年           1
Name: count, dtype: int64
```

```python
df
```

```
         昵称  学历  城市          经验              薪资                            备注  \
0       Map   本  北京         0.0              实习                           NaN   
1    yanni*   本  杭州  6年前端\n2年转行  前端：20k\n转行：28k        新能源企业前端-->产品-->销售-->售前   
2       边牧*   本  长沙          5年              9k  离职，空窗期2年，北京17k，React，Flutter   
3       决堤*  本科  北京         0.0              9k                           被辞退   
4       月亮*   专  济南          3年              9k                           NaN   
..      ...  ..  ..         ...             ...                           ...   
674     lh*  初中  上海          8年             18k                            前端   
675     微斯*   本  北京        3.5年             17k                           NaN   
676     海盐*   专  北京        6.5年   25k->22k->18k                            前端   
677    wah*   专  上海          7年             20k                            前端   
678      渔*   本  武汉          2年              6k                            前端   

       毕业年份  
0    2026.0  
1       NaN  
2       NaN  
3    2025.0  
4       NaN  
..      ...  
674     NaN  
675     NaN  
676     NaN  
677     NaN  
678     NaN  

[679 rows x 7 columns]
```

### 3. 学历清洗

先看「学历」列——它是分类数据，但写法很不统一。

```python
df['学历'].value_counts()
```

```
学历
本        374
专        207
硕         28
高中        14
本科         8
高          8
初          7
硕士         6
初中         5
本211       4
中专         4
中          2
985硕士      2
大专         2
小学         1
招人         1
高二         1
专科         1
留美         1
985本       1
Name: count, dtype: int64
```

问题很明显：
- 「本」「本科」「本211」「985本」本质都是「本科」
- 「专」「专科」「大专」本质都是「大专」
- 「硕」「硕士」「985硕士」本质都是「硕士」
- 「招人」「留美」等是异常值

我们用 `map()` 做**分类映射**，不认识的统一设为 `NaN`。

```python
edu_map = {
    '本': '本科', 
    '本科': '本科', 
    '本211': '本科', 
    '985本': '本科',
    '专': '大专', 
    '专科': '大专', 
    '大专': '大专',
    '硕': '硕士', 
    '硕士': '硕士', 
    '985硕士': '硕士',
    '高中': '高中', 
    '高': '高中', 
    '高二': '高中',
    '初': '初中', 
    '初中': '初中',
    '中专': '中专',
    '小学': '小学',
}
df['学历'] = df['学历'].map(edu_map)
```

```python
df['学历'].value_counts(dropna=False)
```

```
学历
本科     387
大专     210
硕士      36
高中      23
初中      12
NaN      6
中专       4
小学       1
Name: count, dtype: int64
```

清洗后类别清晰多了。还可以进一步把 `object` 转为 `category` 类型——
既节省内存，也明确这是分类数据。

```python
df['学历'] = df['学历'].astype('category')
df['学历'].dtype
```

```
CategoricalDtype(categories=['中专', '初中', '大专', '小学', '本科', '硕士', '高中'], ordered=False, categories_dtype=str)
```

### 4. 城市清洗

城市列的主要问题是**混入了不属于城市的数据**。

```python
df['城市'].value_counts()
```

```
城市
北京      128
深圳       77
上海       68
成都       62
杭州       60
       ... 
广西柳州      1
河北        1
鄂州        1
江西        1
保定        1
Name: count, Length: 69, dtype: int64
```

可以看到「焦虑型人格」「在读」「-」等明显不是城市名。

处理方法：先 `str.strip()` 去空格，再用布尔索引剔除非城市值。
（「应届」相关值已在上述预处理中提走，不会再出现在这里。）

```python
# 去空格
df['城市'] = df['城市'].str.strip()

# 省/市格式，保留斜杠后的城市名
# 如「湖南/株洲」→「株洲」
df['城市'] = df['城市'].str.split('/').str[-1].str.strip()

# 剔除异常值
not_cities = ['焦虑型人格', '在读', '-']
df.loc[df['城市'].isin(not_cities), '城市'] = None
df.loc[df['城市'] == '广西柳州', '城市'] = '柳州'
df['城市'].value_counts()
```

```
城市
北京    129
深圳     77
上海     68
成都     62
杭州     60
     ... 
柳州      1
河北      1
鄂州      1
江西      1
保定      1
Name: count, Length: 64, dtype: int64
```

### 5. 经验清洗

经验列的目标是转为**数值（年）**。但现有的值五花八门——

```python
df['经验'].value_counts()
```

```
经验
0.0           99
3年            77
4年            68
5年            65
6年            39
7年            35
2年            32
1年            31
3.5年          30
1.5年          25
2.5年          23
0.5年          23
8年            18
4.5年          17
10年           16
9年            15
5.5年           8
11年            6
0年             5
7.5年           3
9.5年           2
13年            2
12年            2
-              2
<1年            2
6年前端\n2年转行     1
4个月            1
上海             1
14年            1
15年+           1
<3年            1
17年            1
大一             1
大三             1
23年毕业          1
10+年           1
8年+            1
3个月            1
创业9年           1
转行             1
读研             1
6.5年           1
Name: count, dtype: int64
```

我们需要处理的情况：
- `「3年」「2.5年」` → 提取数字
- `「3个月」「4个月」` → 转为年
- （应届已在预处理中统一处理为 0）
- `「<1年」「<3年」` → 取中间值
- `「10+年」` → 取下限
- `「转行」「读研」「上海」` → 无法解析为经验值，设为 NaN

这些规则适合用 **自定义函数 + `apply()`** 来实现。

```python
def parse_experience(val):
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip()
    if s in ['-', '']:
        return np.nan
    if s in ['转行', '读研', '上海']:
        return np.nan
    if '应届' in s or '毕业' in s:
        return 0.0
    if s in ['大一', '大三']:
        return 0.0
    plus_match = re.search(r'(\d+(?:\.\d+)?)\s*\+\s*年', s)
    if plus_match:
        return float(plus_match.group(1))
    lt_match = re.search(r'<(\d+(?:\.\d+)?)\s*年', s)
    if lt_match:
        v = float(lt_match.group(1))
        return max(v - 0.5, 0)
    years = re.findall(r'(\d+(?:\.\d+)?)\s*年', s)
    if years:
        return sum(float(y) for y in years)
    months = re.findall(r'(\d+)\s*个月', s)
    if months:
        return round(sum(float(m) for m in months) / 12, 1)
    return np.nan

df['经验'] = df['经验'].apply(parse_experience)
```

```python
df['经验'].describe()
```

```
count    657.000000
mean       3.686454
std        2.935093
min        0.000000
25%        1.000000
50%        3.500000
75%        5.000000
max       17.000000
Name: 经验, dtype: float64
```

```python
df['经验'].value_counts(dropna=False)
```

```
经验
0.0     107
3.0      77
4.0      68
5.0      65
6.0      39
7.0      35
2.0      32
1.0      31
3.5      30
0.5      25
1.5      25
2.5      24
NaN      22
8.0      20
4.5      17
10.0     17
9.0      16
5.5       8
11.0      6
7.5       3
9.5       2
13.0      2
12.0      2
0.3       1
14.0      1
15.0      1
17.0      1
0.2       1
6.5       1
Name: count, dtype: int64
```

经验被成功转为了 `float64` 类型。

### 6. 薪资清洗

薪资是最复杂的一列——来看看它有多少种写法。

```python
df['薪资'].value_counts()
```

```
薪资
15k              52
12k              38
10k              37
14k              32
13k              30
                 ..
12.5k             1
3.5k              1
13k*15            1
49w/年             1
25k->22k->18k     1
Name: count, Length: 97, dtype: int64
```

薪资列的情况：
- `9k`、`10k` → 标准千元月薪
- `20w/年` → 年薪，需转月薪
- `13k*15` → 带月数，取基本月薪
- `30k+`、`25+k` → 带加号
- `前端：20k\n转行：28k` → 多行，取最后一行
- `25k->22k->18k` → 变动历史，取最新值
- `16k（广州）` → 带地点说明
- `50k~60k` → 薪资范围
- `实习`、`？？` → 异常值

还是用 **自定义函数 + `apply()`** 处理。

```python
def parse_salary(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip()
    if s in ['实习', '-', '？？', '']:
        return np.nan
    if '\n' in s:
        s = s.split('\n')[-1].strip()
    if '->' in s:
        s = s.split('->')[-1].strip()
    s = re.sub(r'[（(][^)）]*[)）]', '', s).strip()
    w_match = re.search(r'(\d+(?:\.\d+)?)\s*w', s, re.IGNORECASE)
    if w_match:
        return round(float(w_match.group(1)) * 10 / 12, 1)
    slash_match = re.search(r'(\d+(?:\.\d+)?)\s*k\s*/\s*(\d+(?:\.\d+)?)\s*k', s, re.IGNORECASE)
    if slash_match:
        return float(slash_match.group(2))
    k_match = re.search(r'(\d+(?:\.\d+)?)\s*\+?\s*k', s, re.IGNORECASE)
    if k_match:
        return float(k_match.group(1))
    return np.nan

df['薪资'] = df['薪资'].apply(parse_salary)
```

```python
df['薪资'].value_counts(dropna=False)
```

```
薪资
NaN     106
15.0     52
12.0     38
10.0     37
14.0     32
       ... 
18.3      1
4.5       1
12.5      1
3.5       1
40.8      1
Name: count, Length: 72, dtype: int64
```

```python
df['薪资'].describe()
```

```
count    573.000000
mean      16.479756
std       11.007336
min        2.000000
25%       10.000000
50%       15.000000
75%       20.000000
max      166.700000
Name: 薪资, dtype: float64
```

清洗后薪资变为 `float64`，单位统一为**千元/月**，可以正常做统计分析了。

（注：`200w/年` 等个例被正确转为月薪约 166.7k。个别极端值可根据业务需要后续处理。）

```python
df = df.rename(columns={'薪资': '薪资(k)', '经验': '经验(年)'})
```

### 7. 清洗结果验证

最后整体检查一遍清洗成果。

```python
df.info()
```

```
<class 'pandas.DataFrame'>
RangeIndex: 679 entries, 0 to 678
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype   
---  ------  --------------  -----   
 0   昵称      676 non-null    object  
 1   学历      673 non-null    category
 2   城市      638 non-null    object  
 3   经验(年)   657 non-null    float64 
 4   薪资(k)   573 non-null    float64 
 5   备注      222 non-null    object  
 6   毕业年份    109 non-null    float64 
dtypes: category(1), float64(3), object(3)
memory usage: 32.7+ KB
```

```python
df.dtypes
```

```
昵称         object
学历       category
城市         object
经验(年)     float64
薪资(k)     float64
备注         object
毕业年份      float64
dtype: object
```

```python
df.head()
```

```
       昵称  学历  城市  经验(年)  薪资(k)                            备注    毕业年份
0     Map  本科  北京    0.0    NaN                           NaN  2026.0
1  yanni*  本科  杭州    8.0   28.0        新能源企业前端-->产品-->销售-->售前     NaN
2     边牧*  本科  长沙    5.0    9.0  离职，空窗期2年，北京17k，React，Flutter     NaN
3     决堤*  本科  北京    0.0    9.0                           被辞退  2025.0
4     月亮*  大专  济南    3.0    9.0                           NaN     NaN
```

```python
df = df[['昵称', '学历', '城市', '经验(年)', '薪资(k)', '毕业年份', '备注']]
df['毕业年份'] = df['毕业年份'].astype('Int32')
# 保存到 Excel
df.to_excel('../linking_clean.xlsx', index=False)

# 保存到 CSV
df.to_csv('../linking_clean.csv', index=False, encoding='utf-8-sig')
```
## Matplotlib
```python
!uv add matplotlib ipympl
```

```python
# 启用交互式后端
%matplotlib widget
```

```python
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持（可选）
plt.rcParams.update({
    "font.sans-serif":["PingFang SC"],
    "axes.unicode_minus":False,
    "figure.dpi": 100
})
```



### Matplotlib 核心概念

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/核心概念.png)
Matplotlib 是整个 Python 数据可视化生态的基石。
无论你用 Seaborn、Plotly 还是其他高级库，底层都离不开 Matplotlib 的三层架构。

**本节课目标**：建立 Matplotlib 的概念体系——
搞懂 Figure、Axes、Artist 这三个核心对象及其关系。

---

#### 1. Figure — 画布

**Figure** 是最顶层的容器，相当于一张画布。
一个 Figure 可以包含一个或多个 Axes（绘图区）。

创建 Figure 最标准的方式：

```python
fig, ax = plt.subplots(figsize=(8, 4))  # 一张画布 + 一个绘图区
ax.plot([1, 2, 3], [1, 4, 9], marker="o")
```

##### 多个 Axes 的 Figure

```python
fig, axes = plt.subplots(2, 2, figsize=(8,6))

axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 1].bar([1, 2, 3], [3, 5, 2])
axes[1, 0].scatter([1, 2, 3], [1, 4, 9])
axes[1, 1].hist(np.random.randn(10000), bins=100)
```

##### 主题/样式

Figure 可以通过 `plt.style.use()` 切换整体视觉风格，
影响所有 Axes 的配色、网格、字体等。

```python
print(plt.style.available)
```

```python
plt.style.use('ggplot')
```

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3], [1, 4, 9])
ax.bar([1, 2, 3], [3, 5, 2], alpha=0.5)
```

```python
plt.style.use('default')  # 恢复默认
```

---

#### 2. Axes — 绘图区

**Axes** 是 Figure 内部的独立绘图区域，
数据实际被绘制在 Axes 上。
每个 Axes 有自己的坐标空间、坐标轴（Axis）、刻度、标签。

一个常见误区：Axes 不等于 Axis，一个 Axes 通常有 2 个 Axis（x轴、y轴）。

```python
fig, ax = plt.subplots(figsize=(8, 4))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin')
ax.plot(x, np.cos(x), label='cos')

ax.set_title('三角函数')
ax.set_xlabel('X 轴')
ax.set_ylabel('\n'.join('Y轴'), rotation = 0)
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.legend()
ax.grid(True, linestyle=':', alpha=0.5)
```

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 生成螺旋线数据
t = np.linspace(0, 20, 1000)
x = np.sin(t)
y = np.cos(t)
z = t

# 绘制3D线图
ax.plot(x, y, z, linewidth=2, color='red')

ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')
ax.set_title('3D螺旋线示例')
```

##### Spines（脊线）

Axes 的四条边框线称为 spines。
常见的「干净风格」就是隐藏上、右两条脊线。

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3], [1, 4, 9], linewidth=2)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('gray')
ax.spines['bottom'].set_linewidth(1.5)
```

##### 注解与图例

```python
fig, ax = plt.subplots(figsize=(8, 4))

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
ax.plot(x, y, marker='o')

ax.annotate('最大值', xy=(5, 25), xytext=(4, 23),
            arrowprops={
                "arrowstyle": "->",
                "color": "red"
            },
            fontsize=12)
ax.text(1, 20, '二次函数', fontsize=14, style='italic',
        bbox={
            "boxstyle": "round",
            "facecolor": "wheat",
            "alpha": 0.5
        }
)
```

---

#### 3. Artist — 绘制元素

**Artist** 是 Matplotlib 里「一切可见的东西」。
Figure、Axes、Axis、曲线、柱体、文字……都是 Artist。

我们平时画图时，就是在不断创建和配置 Artist 对象。

```python
fig, ax = plt.subplots(figsize=(8, 4))

ax.plot([1, 2, 3], [1, 4, 9], color='royalblue', linewidth=3, label='折线')
ax.bar([4, 5, 6], [3, 7, 5], color='tomato', edgecolor='black', alpha=0.7, label='柱状图')
ax.scatter([7, 8, 9], [8, 2, 6], color='green', s=100, label='散点')

ax.legend()
```

每个 Artist 都可以单独修改属性：

---

#### 总结：三层架构

```
Figure（画布）
  ├── Axes（绘图区1）
  │     ├── Axis（X轴）
  │     ├── Axis（Y轴）
  │     ├── Line2D（折线）
  │     ├── Rectangle（柱体）
  │     ├── Text（文字）
  │     ├── Legend（图例）
  │     └── ...
  ├── Axes（绘图区2）
  │     └── ...
  └── ...
```

**本节课的核心理念**：
- Figure 负责容器和全局配置（大小、样式、布局）
- Axes 负责数据和坐标（画什么、坐标范围、标签、图例）
- Artist 负责视觉表现（颜色、线型、透明度、大小）

掌握这套概念体系后，遇到新的图表需求，
你就能准确判断：这个问题应该去查 Figure 的 API、Axes 的 API，还是某个 Artist 的 API。



## Matplotlib 动画
```python
# 启用交互式后端
%matplotlib widget
```

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation
from IPython.display import HTML
from collections import deque

# 设置中文字体支持（可选）
plt.rcParams.update({
    "font.sans-serif":["PingFang SC"],
    "axes.unicode_minus":False,
    "figure.dpi": 100
})

def reset():
    old_ani = globals().pop("ani", None)

    if old_ani is not None:
        try:
            old_ani.event_source.stop()
        except Exception:
            pass

    plt.close("all")
```
动画是数据可视化的「升维」手段——
把静态图表变成动态过程，展示变化趋势、实时数据流或算法演化。

**本节课目标**：掌握 Matplotlib 动画的两大核心工具——
`FuncAnimation` 和 `ArtistAnimation`，并能够保存和展示动画。

---

### 1. FuncAnimation — 函数驱动动画

**FuncAnimation** 是最常用的动画方式：
你提供一个「更新函数」，动画循环每次调用它来更新图表。

核心三要素：
- `fig`：画布
- `update(frame)`：每帧调用的更新函数
- `frames`：帧总数（或可迭代对象）

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))

x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

ax.set_ylim(-1.5, 1.5)
ax.set_title('正弦波动画')

frames = 50

def update(frame):
    # 最后一帧相位 = 2π，和第一帧（相位 0）在视觉上相等
    phase = 2 * np.pi * frame / frames
    line.set_ydata(np.sin(x + phase))
    return line,

ani = FuncAnimation(fig, update, frames=range(frames + 1), interval=16, repeat=True)
```

#### 核心参数

| 参数 | 作用 |
|------|------|
| `frames` | 帧总数或可迭代对象（如 `range(100)`、`np.linspace(0, 10, 100)`）|
| `interval` | 每帧间隔（毫秒），默认 200 |
| `repeat` | 是否循环播放，默认 True |
| `blit` | 是否只更新变化部分（大幅提升性能）|
| `init_func` | 初始化函数，配合 blit 使用 |

```python
reset()

# 使用可迭代对象作为 frames


fig, ax = plt.subplots(figsize=(8, 4))

# 保存最近100个数据点
x_data = deque(maxlen=100)
y_data = deque(maxlen=100)

(line,) = ax.plot([], [], lw=2)

ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)


# -----------------------------
# 无限生成器（模拟实时数据流）
# -----------------------------
def data_stream():
    t = 0
    while True:
        yield t, np.sin(t * 0.1)
        t += 1


# -----------------------------
# 每收到一条数据就更新一次图像
# -----------------------------
def update(frame):
    x, y = frame

    x_data.append(x)
    y_data.append(y)

    line.set_data(x_data, y_data)

    # x轴跟着移动，形成滚动窗口
    if x >= 100:
        ax.set_xlim(x - 100, x)


ani = FuncAnimation(fig, update, frames=data_stream(), interval=30, cache_frame_data=False)  # 无限生成器
```

#### Blit 模式

`blit=True` 只重新绘制变化的 Artist，而不是整个 Axes。
建议配合 `init_func` 使用，先初始化所有 Artist，然后每帧只更新特定部分。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))

x = np.linspace(0, 2 * np.pi, 100)
(line,) = ax.plot([], [], lw=2)
(point,) = ax.plot([], [], "ro", ms=8)


def init():
    ax.set_xlim(0, 2 * np.pi + 5)
    ax.set_ylim(-1.5, 1.5)
    return line, point


def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_data(x, y)
    point.set_data([x[-1]], [y[-1]])
    return line, point


ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)
```

---

### 2. ArtistAnimation — 预生成帧

**ArtistAnimation** 适合你已经准备好每一帧所有 Artist 的情况。
它接受一个列表，每个元素是这一帧要显示的所有 Artist。

当你需要精确控制每一帧的内容时非常有用。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))

x = np.linspace(0, 2 * np.pi, 100)
frames = []

for phase in np.linspace(0, 2 * np.pi, 50):
    line, = ax.plot(x, np.sin(x + phase), color='royalblue')
    frames.append([line])

ani = ArtistAnimation(fig, frames, interval=50, repeat=True)
```

---

### 3. 保存动画

Matplotlib 支持将动画保存为 GIF、MP4、HTML 等格式。
- GIF：使用 `pillow` writer
- MP4：使用 `ffmpeg` writer（需安装 ffmpeg）
- HTML：使用 `ani.to_jshtml()` 嵌入 Notebook

```python
# 保存为 GIF（需要 pillow 库）
ani.save('sine_wave.gif', writer='pillow', fps=20)
print('已保存为 sine_wave.gif')
```

```python
# 在 Notebook 中嵌入 HTML 动画（无需额外播放器）
HTML(ani.to_jshtml())
```

```python
# 嵌入为 HTML5 视频（需要 ffmpeg）
# HTML(ani.to_html5_video())
```

```python
# 启用交互式后端
%matplotlib widget
```

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import (
    Slider, Button, CheckButtons, RadioButtons,
    TextBox
)

# 设置中文字体支持（可选）
plt.rcParams.update({
    "font.sans-serif": ["PingFang SC"],
    "axes.unicode_minus": False,
    "figure.dpi": 100
})

def reset():
    plt.close("all")
```

## Matplotlib 交互式组件

Matplotlib 自带一套基于 `matplotlib.widgets` 的交互式组件，
可以直接在图表中添加滑块、按钮、复选框等控件，让图表"活"起来。

**本节课目标**：掌握 Matplotlib 交互组件的使用模式——
学会将滑块、按钮、复选框、文本框、区间选择器等嵌入图表，并绑定回调函数。

---

### 1. Slider — 滑块

**Slider** 是最常用的交互组件，适合让用户通过拖动来调整连续数值。

基本用法：创建 Slider 对象，绑定 `on_changed` 回调。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))
fig.subplots_adjust(bottom=0.25)

x = np.linspace(0, 10, 500)
line, = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-1.5, 1.5)
ax.set_title('拖动滑块调整频率')

# 创建滑块 Axes 和 Slider 控件
slider_ax = fig.add_axes((0.2, 0.1, 0.6, 0.03))
slider = Slider(
    ax=slider_ax, label='频率', valmin=0.1, valmax=5.0,
    valinit=1.0, valstep=0.1
)

def update(freq):
    line.set_ydata(np.sin(freq * x))
    fig.canvas.draw_idle()

slider.on_changed(update)
```

多个滑块分别控制不同参数，实现多维度调整。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.3)

x = np.linspace(0, 10, 500)
line, = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-2, 2)

# 频率滑块
freq_slider_ax = fig.add_axes((0.2, 0.15, 0.6, 0.03))
freq_slider = Slider(freq_slider_ax, '频率', 0.1, 5.0, valinit=1.0)

# 振幅滑块
amp_slider_ax = fig.add_axes((0.2, 0.1, 0.6, 0.03))
amp_slider = Slider(amp_slider_ax, '振幅', 0.1, 2.0, valinit=1.0)

def update(_):
    line.set_ydata(amp_slider.val * np.sin(freq_slider.val * x))
    fig.canvas.draw_idle()

freq_slider.on_changed(update)
amp_slider.on_changed(update)
```

---

### 2. Button — 按钮

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))
fig.subplots_adjust(bottom=0.2)

x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.random.randn(100).cumsum(), lw=2)
ax.set_title('点击按钮重新生成数据')

button_ax = fig.add_axes((0.4, 0.05, 0.2, 0.075))
button = Button(button_ax, '重新生成', color='lightblue', hovercolor='skyblue')

def regenerate(event):
    line.set_ydata(np.random.randn(100).cumsum())
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

button.on_clicked(regenerate)
```

---

### 3. CheckButtons — 复选框

**CheckButtons** 允许用户切换多个独立开关，常用于控制多条曲线的显隐。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(left=0.3)

x = np.linspace(0, 10, 200)
lines = {}
colors = ['red', 'blue', 'green']
labels = ['sin(x)', 'cos(x)', 'sin(x)*cos(x)']
funcs = [np.sin, np.cos, lambda x: np.sin(x) * np.cos(x)]

for label, color, func in zip(labels, colors, funcs):
    line, = ax.plot(x, func(x), color=color, lw=2, label=label, visible=True)
    lines[label] = line

ax.legend(loc='upper right')
ax.set_title('复选框控制曲线显隐')

check_ax = fig.add_axes((0.05, 0.4, 0.15, 0.2))
check = CheckButtons(check_ax, labels, [True, True, True])

def toggle(label):
    lines[label].set_visible(not lines[label].get_visible())
    fig.canvas.draw_idle()

check.on_clicked(toggle)
```

---

### 4. RadioButtons — 单选按钮

**RadioButtons** 用于从一组互斥选项中选择一个，适合切换图表类型或数据源。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(left=0.3)

x = np.linspace(0, 10, 200)
line, = ax.plot(x, np.sin(x), lw=2, color='royalblue')
ax.set_ylim(-2, 2)
ax.set_title('单选按钮切换函数类型')

radio_ax = fig.add_axes((0.05, 0.4, 0.15, 0.2))
radio = RadioButtons(radio_ax, ('sin', 'cos', 'tan'))

func_map = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': lambda x: np.tan(x) * 0.5  # 缩放便于显示
}

def switch(label):
    line.set_ydata(func_map[label](x))
    fig.canvas.draw_idle()

radio.on_clicked(switch)
```

---

### 5. TextBox — 文本框

**TextBox** 获取用户输入的文本，适合需要精确数值或自定义表达式时使用。

```python
reset()
fig, ax = plt.subplots(figsize=(8, 4))
fig.subplots_adjust(bottom=0.2)

x = np.linspace(0, 10, 500)
line, = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-1.5, 1.5)
ax.set_title('输入频率值后按回车')

text_ax = fig.add_axes((0.2, 0.05, 0.6, 0.06))
text_box = TextBox(text_ax, '频率', initial='1.0')

def submit(text):
    try:
        freq = float(text)
        line.set_ydata(np.sin(freq * x))
        fig.canvas.draw_idle()
    except ValueError:
        pass

text_box.on_submit(submit)
```


## 用 Seaborn 分析前端开发者薪资数据
```python
# 启用交互式后端
%matplotlib widget
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体支持
plt.rcParams.update({
    "font.sans-serif": ["PingFang SC"],
    "axes.unicode_minus": False,
    "figure.dpi": 100
})

def reset():
    plt.close("all")

# Seaborn 全局样式
sns.set_theme(style="whitegrid", font="PingFang SC")

df = pd.read_csv("../linking_clean.csv")
df.head()

df_clean = df.dropna(subset=["薪资(k)"]).copy()
```

```
       昵称  学历  城市  经验(年)  薪资(k)    毕业年份                            备注
0     Map  本科  北京    0.0    NaN  2026.0                           NaN
1  yanni*  本科  杭州    8.0   28.0     NaN        新能源企业前端-->产品-->销售-->售前
2     边牧*  本科  长沙    5.0    9.0     NaN  离职，空窗期2年，北京17k，React，Flutter
3     决堤*  本科  北京    0.0    9.0  2025.0                           被辞退
4     月亮*  大专  济南    3.0    9.0     NaN                           NaN
```
本节课通过分析一份前端开发者的薪资调研数据，一边做分析一边熟悉 **Seaborn**。

Seaborn 是建立在 Matplotlib 之上的高级统计可视化库，
特点是**用简洁的代码就能生成美观且有统计意义的图表**。

**本节课目标**：掌握 Seaborn 的核心图类型——分布图、箱线图、散点图、
回归图、分类汇总图、热力图等，并能结合实际数据做探索性分析。

---

### 1. 薪资分布 — 单变量分析

先用 `histplot` 和 `kdeplot` 看薪资的整体分布形态。

`histplot` — 直方图，展示数据在各区间的频次。

`kdeplot` — 核密度估计，平滑地展示概率密度。

```python
reset()
fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# 直方图
sns.histplot(data=df_clean, x="薪资(k)", bins=30, ax=axes[0])
axes[0].set_title("薪资直方图")

# 核密度估计
sns.kdeplot(data=df_clean, x="薪资(k)", fill=True, ax=axes[1])
axes[1].set_title("薪资核密度估计")

# ax = axes[0]
# for patch in ax.patches:
#     height = patch.get_height()
#     if height > 0:  # 避免标注空柱子
#         ax.text(
#             patch.get_x() + patch.get_width()/2,  # X 坐标：柱子中间
#             height,                               # Y 坐标：柱子顶部
#             f'{int(height)}',                     # 显示内容
#             ha='center', va='bottom',             # 水平居中，垂直在底部上方
#             fontsize=8
#         )

plt.tight_layout()
```

```python
reset()
sns.displot(data=df_clean, x="薪资(k)",  kde=True, bins=30)
```

```
<seaborn.axisgrid.FacetGrid at 0x131ca8ec0>
```

---

### 2. 学历与薪资 — 分类对比

用 `boxplot` 和 `violinplot` 对比不同学历的薪资分布。

`boxplot` — 箱线图，展示中位数、四分位数、异常值。

`violinplot` — 小提琴图，在箱线图基础上叠加了分布形状。

```python
df['学历'].value_counts()
```

```
学历
本科    387
大专    210
硕士     36
高中     23
初中     12
中专      4
小学      1
Name: count, dtype: int64
```

```python
reset()
fig, axes = plt.subplots(1, 2, figsize=(8, 5))

# 箱线图
sns.boxplot(data=df_clean, x="学历", y="薪资(k)",
            order=["小学","中专", "初中", "高中", "大专", "本科", "硕士"], 
            ax=axes[0])
axes[0].set_title("学历 vs 薪资 — 箱线图")

# 小提琴图
sns.violinplot(data=df_clean, x="学历", y="薪资(k)",
               order=["小学","中专", "初中", "高中", "大专", "本科", "硕士"], 
               ax=axes[1])
axes[1].set_title("学历 vs 薪资 — 小提琴图")

fig.tight_layout()
```

```python
reset()
# barplot 默认显示均值 + 置信区间
sns.barplot(data=df_clean, x="学历", y="薪资(k)",
            order=["小学","中专", "初中", "高中", "大专", "本科", "硕士"])
plt.title("学历 vs 薪资均值")
```

```
Text(0.5, 1.0, '学历 vs 薪资均值')
```

---

### 3. 经验与薪资 — 回归分析

`scatterplot` 看散点分布，`regplot` 自动添加回归线，直观判断工作年限对薪资的影响。

```python
reset()
fig, axes = plt.subplots(1, 2, figsize=(8, 5))

# 散点图
sns.scatterplot(data=df_clean, x="经验(年)", y="薪资(k)", alpha=0.6, ax=axes[0])
axes[0].set_title("经验 vs 薪资 — 散点图")

# 添加回归线
sns.regplot(data=df_clean, x="经验(年)", y="薪资(k)",
            scatter_kws={"alpha": 0.5}, 
            line_kws={"color": "red", "linewidth": 2},
            ax=axes[1])
axes[1].set_title("经验 vs 薪资 — 回归图")

plt.tight_layout()
```
# Agent底层逻辑
## 必看导言

### AI岗位分布

| 岗位类型     | 岗位名称                                                     | 岗位需求 | 学习难度 | 薪资水平 | 核心知识                                                     |
| ------------ | ------------------------------------------------------------ | -------- | -------- | -------- | ------------------------------------------------------------ |
| **应用开发** | AI应用开发工程师<br />Agent应用开发工程师<br />大模型应用开发工程师<br /> | ★★★★★    | ★★★☆☆    | ★★★☆☆    | 编程思维<br />AI认知<br />应用框架<br />业务经验             |
| 推理部署     | 大模型部署工程师<br />LLM 推理优化工程师                     | ★★☆☆☆    | ★★★★★    | ★★★★★    | CUDA内核<br />GPU架构<br />算子融合<br />分布式推理<br />推理引擎<br />模型量化<br />显存优化 |
| 模型研发     | 大模型算法工程师<br />LLM 微调工程师<br />大模型训练工程师   | ★★☆☆☆    | ★★★★★    | ★★★★★    | 深度学习理论<br />算法创新<br />模型架构<br />分布式训练<br />数据处理<br />强化学习<br />论文复现<br />高等数学<br />线性代数<br />概率论<br />优化理论 |

### 课程安排

<img src="https://resource.duyiedu.com/yuanjin/202607141602641.png" alt="image-20260714160258565" style="zoom:50%;" />

## AI分类

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/AI的分类.jpg)

#@ 神经网络

神经网络是目前机器学习领域最常见、最重要的实现智能的手段

学习神经网络，一切要从神经元开始

## 神经元

<img src="https://resource.duyiedu.com/yuanjin/202607081415781.png" width="100%">

1943年，Warren McCulloch（神经科学家）和 Walter Pitts（逻辑学家）为神经元建立了数学模型。

经过几十年的发展，最终每个神经元的数学模型变成了下面的样子：

$y = \sigma(\sum_{i=1}^n w_i x_i + b) = \sigma(w_1 x_1 + w_2 x_2 + ... + w_n x_n + b)$

- **输入值**：$[x_1, x_2, ... x_n]$

  输入值中的每一个分量表示某一个维度的信息。

- **输出值/激活值**：一个标量
  
- **权重**：$[w_1, w_2, ... w_n]$

  没个权重表示该维度的信息的重要程度
  
- **偏置**：b

  改变被激活的阈值
  
- **参数**：权重和偏置的统称

- $\sigma$：激活函数

  激活函数决定了是否输出有效值

  经典激活函数 $ReLU(z)=max(0, z)$



### 总结

核心理解如下

- 单个神经元，接受一个向量，输出一个标量
- 激活函数是固定的
- 参数（权重和偏置）唯一的决定了该神经元的输出是否正确

## 神经元前向传播

神经网络：神经网络包含一个输入层，多个隐藏层，一个输出层
前向传播：就是从输入层经隐藏层最后到输出层的过程
![image](https://raw.githubusercontent.com/JJ-front/store-img/master/神经网络.png)

### 流程（前向传播）：

- 输入层不包含神经元，就是输入的值（向量），有多少个值需要设计
- 隐藏层有多少层和多少神经元不固定，隐藏层每一层的神经元的数量也可能不相等
- 输入层有多少个输入，则就会产生多少个输出传递到下一层
- 第N层隐藏层（包含输出层）的第N个神经元的输入就是单个神经元的计算方式
    - 其中x1来自上一层的第一个神经元的输出，w1随机
    - x2来自上一层的第二个神经元的输出，w2随机
    - 以此类推......
- 输出结果受神经网络的每一个神经元的权重和偏置的影响且唯一
- 输出层得到一堆结果，分析结果就可以得到哪个几率最大，但是此时结果很不靠谱，需要调参，看后面章节解决
$$
\begin{aligned}
& \textbf{单个神经元} \\
\\
& y = \sigma(\sum_{i=1}^n w_i x_i + b) \\
\end{aligned}
$$

---

$$
\begin{aligned}
& \textbf{神经网络中的单个神经元} \\
\\
& a^{L}_j = \sigma(\sum_{i=1}^n w_i a^{L-1}_i + b) \\
\\
& L: 第L层 \\
& j: 当前层第j行神经元
\end{aligned}
$$

---

$$
\begin{aligned}
& \textbf{神经网络中，某层的计算过程} \\
\\
& \text{完整矩阵形式：} \\
\\
& \begin{bmatrix}
  a_1^{(l)} \\
  a_2^{(l)} \\
  \vdots \\
  a_n^{(l)}
  \end{bmatrix}
  =
  \sigma\left(
  \begin{bmatrix}
  w_{11}^{(l)} & w_{12}^{(l)} & \cdots & w_{1m}^{(l)} \\
  w_{21}^{(l)} & w_{22}^{(l)} & \cdots & w_{2m}^{(l)} \\
  \vdots & \vdots & \ddots & \vdots \\
  w_{n1}^{(l)} & w_{n2}^{(l)} & \cdots & w_{nm}^{(l)}
  \end{bmatrix}
  \begin{bmatrix}
  a_1^{(l-1)} \\
  a_2^{(l-1)} \\
  \vdots \\
  a_m^{(l-1)}
  \end{bmatrix}
  +
  \begin{bmatrix}
  b_1^{(l)} \\
  b_2^{(l)} \\
  \vdots \\
  b_n^{(l)}
  \end{bmatrix}
  \right) \\[1.2em]
& \text{简写形式：} \\
\\
& \mathbf{a}^{(l)} = \sigma\left( \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)} \right) \\[1.2em]
& \text{其中：} \\
& \mathbf{a}^{(l)}: \text{第 } l \text{ 层的输出向量（大小为 } n \times 1 \text{）} \\
& \mathbf{a}^{(l-1)}: \text{第 } l-1 \text{ 层的输出向量（大小为 } m \times 1 \text{）} \\
& \mathbf{W}^{(l)}: \text{第 } l \text{ 层的权重矩阵（大小为 } n \times m \text{）} \\
& \mathbf{b}^{(l)}: \text{第 } l \text{ 层的偏置向量（大小为 } n \times 1 \text{）} \\
& \sigma(\cdot): \text{激活函数（如 Sigmoid、ReLU 等）}
\end{aligned}
$$



---

$$
\begin{aligned}
& \text{总参数量} = \sum_{l=1}^{L} \left( n_l \times n_{l-1} + n_l \right) \\[0.8em]
& = \left( n_1 \times n_0 + n_1 \right) + \left( n_2 \times n_1 + n_2 \right) + \cdots + \left( n_L \times n_{L-1} + n_L \right)
\end{aligned}
$$

公式总结：为啥要用矩阵运算，因为矩阵运算可以给GPU提速（批量运算），性能高

## 反向传播

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/反向传播期望.png)

反向传播就是实现梯度下降的手段
- 就是根据预测值和输出层结果算出期望（输出层与预测值的大小，输出层大于预测值，则期望下降，反之期望变大）
    - 调增期望就是改变输出层的结果
        - 影响输出的结果有：当前神经元的权重、偏置、和上一层的输出
            - 权重、偏置可以算出来具体结果（通过链式法则，具体不深究）
            - 上一层的输出无法算，因此对上层的输出还有期望
                - 但是可以看到输出层不同的神经元对上一层的期望不一样，因此需要把所有输出层对上一层同一个神经元的期望做加和在继续流程

### 一些概念

- 预测值（标签）：就是给输出层一个预测值，期望调整参数能够接近给的预测值
- 损失度：就是调参后和给的预测值会有一定的差异，这个就叫损失度
- 损失函数（代价函数）：就是用来算损失度的函数

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/反向传播.png)

$$
\begin{aligned}
& \textbf{损失函数示例} \\
\\
& L = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 \\
\end{aligned}
$$

    - 就是图中真实输出层与预测值之间相减求平方求和除以数量

### 什么在影响损失度？

- 最直观的就是输出层的结果
    - 输出层的结果又受参数影响，因此参数影响
        - 因此损失度和参数之间一定有某种关系，只是参数太庞大了，无法确定，故表示
            - y(损失度) = cost(参数) = C(参数)
                - cost是一个函数，C是简写
                - 损失度是大于0的

**目标**

- 如何改变参数，减小y
    - **梯度下降**
        -  沿着函数在当前点处**最速下降方向**（即负梯度方向，即函数的导数-斜率最大的）移动，使得函数的值逐步减少
        -  函数是无限的，只能找局部最优解

    - **学习率**
        - 梯度下降的幅度(就是参数移动的范围)

    - **学习/训练**
        - 是一个过程，在这个过程中，通过梯度下降的手段，让神经网络的参数逐步调整到最佳状态

## 训练模式和框架

### 梯度下降的训练模式

![mnist_100_digits](https://resource.duyiedu.com/yuanjin/202607161711415.png)

**Stochastic Gradient Descent (SGD) 随机梯度下降**

- 每一步**只取 1 个样本**算梯度更新参数
- 梯度噪声极大，收敛震荡；早年小数据集用，现代大模型基本不用
    - 单个样本的梯度 ≠ 全体样本的梯度，两者之间差了一个随机项，这个随机项就是“噪声”



**Full Batch Gradient Descent 全批量梯度下降**

- 每一轮更新参数：**使用全部训练集所有样本**计算损失与梯度，再更新权重
- 特点：梯度方向最稳定；大数据集显存 / 内存爆炸，迭代极慢，几乎不用于大模型训练



**Mini-Batch Gradient Descent 小批量梯度下降（大模型主流）**

- 每一步取固定数量样本（batch_size，如 32/128/1024）计算梯度更新
- 平衡稳定性与速度，显存可控，LLM、CV 模型全部默认使用



### 网络架构
就是指神经网络隐藏层多少层 每层多少个神经元怎么设计 神经元之间是全连接还是非全连接，这些决策会形成一个架构，就是神经网络架构，常见的有：

**卷积神经网络（CNN）—— 图像领域经典架构（现在不怎么用了，几乎都是下面这个）**

模仿人眼视觉：图像是局部关联的，不用一次性看整张图，只滑动小窗口（卷积核）提取局部纹理、边缘、色块。



**Transformer —— NLP 起家，现在通用全能架构**

后续讲解



### 深度学习框架

**TensorFlow**

现在已经不再流行，通常用于做一些边缘计算



**PyTorch**

现在的主力训练框架



### 模型

模型是训练的结果，通常以多个文件的形式存储，文件包含：

- **核心权重文件**：占99%体积（参数：权重+偏置）
- **配置文件**：模型的网络的架构、隐藏层维度、权重精度等信息

### 一些术语
**泛化**：模型训练集没有这个东西，但是模型依然认识，这个就叫泛化能力强
**过拟合**：泛化能力弱。只认识训练集的东西
**欠拟合**：训练集的东西都没认识完

## 词元（Token）

词元来自于 NLP 领域，它研究的话题是：

如何将文字序列转化为可被AI使用的数字序列

试一试：https://tiktokenizer.vercel.app/

转化过程称之为 **分词（Tokenize）**，转化的工具称之为 **分词器（Tokenizer）**，转化的结果序列称之为 **词元（Token）序列**，每一个数字称为为 **词元（Token）**。

### 字符编码

实现分词最简单的方式是将所有文字转化为UTF-8编码的数字

```python
# 示例1：中文+英文+符号测试
input_text = "你好Hello!123"
result = list(input_text.encode(encoding="utf-8"))
print(f"文本：{input_text}")
print(f"UTF-8：{result}")
```

为什么不直接将UTF-8的数字序列作为分词结果呢？主要有这几个原因：

- 长度膨胀：中文一个汉字 = 3 个 UTF-8 字节数字，导致将来的计算量、显存占用、训练速度全部恶化
- 信息浪费：模型每一层都要重复学习「228,189,160 = 你」这种固定组合，大量重复冗余学习
- 语义不明：模型很难学到词语、字的边界规律

如果能将每个有意义的字/词对应一个数字就好了，比如：
- 你好 -> 10000
- Hello -> 10001
- ! -> 10002
- 123 -> 10003

这样一来，只需要4个数字就可以表达这句话，同时每个数字对应着一个可以被学习的语义。

要实现这一点，就必须要建立一个"词典"，称之为 分词表（token vocabulary，Vocab）

### 词表的建立

通过统计大量的文字内容，建立词表。

词表中会合并那些高频出现的组合。

```python
import json
from collections import Counter

def bpe_train(text, target_vocab_size=400):
    """
    简易 BPE 算法

    将文本转为 UTF-8 字节序列后，不断合并高频相邻对，
    直到词表大小达到 target_vocab_size。
    """
    byte_seq = list(text.encode("utf-8"))
    # 初始词表：0~255 单字节
    vocab = {i: bytes([i]) for i in range(256)}
    seq = byte_seq.copy()

    print(f"文本: {len(text)} 字符")
    print(f"UTF-8 字节序列: {len(byte_seq)}（>> 初始词表 256）")
    print(f"目标词表大小: {target_vocab_size}")
    print()

    step = 0
    while len(vocab) < target_vocab_size:
        pair_counts = Counter()
        for i in range(len(seq) - 1):
            pair_counts[(seq[i], seq[i + 1])] += 1
        if not pair_counts:
            break

        best_pair, _ = pair_counts.most_common(1)[0]
        new_id = len(vocab)
        vocab[new_id] = vocab[best_pair[0]] + vocab[best_pair[1]]
        step += 1
        new_seq = []
        i = 0
        while i < len(seq):
            if i + 1 < len(seq) and seq[i] == best_pair[0] and seq[i + 1] == best_pair[1]:
                new_seq.append(new_id)
                i += 2
            else:
                new_seq.append(seq[i])
                i += 1
        seq = new_seq

    print(f"\n--- 合并结束 ---")
    print(f"合并次数: {step}")
    print(f"序列压缩: {len(byte_seq)} → {len(seq)}（{len(seq)/len(byte_seq)*100:.1f}%）")
    print(f"词表: 256 → {len(vocab)}")

    # 保存词表
    id_to_token = {}
    for tid in sorted(vocab.keys()):
        raw = vocab[tid]
        try:
            id_to_token[tid] = raw.decode("utf-8")
        except UnicodeDecodeError:
            id_to_token[tid] = raw.hex()

    with open("bpe_vocab.json", "w", encoding="utf-8") as f:
        json.dump(id_to_token, f, ensure_ascii=False, indent=2)



# ==================== 测试 ====================

with open("corpus.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

bpe_train(corpus, target_vocab_size=400)
```

### 分词

词表固定下来后，就不再改动了。

后续的分词动作，只需要读取词表进行匹配，就能高效完成分词。

```python
import json
import re

with open("bpe_vocab.json", "r", encoding="utf-8") as f:
    id_to_token = {int(k): v for k, v in json.load(f).items()}

def to_bytes(tid, s):
    if tid < 256:
        return bytes([tid])
    if re.fullmatch(r"(?:[0-9a-f]{2})+", s):
        raw = bytes.fromhex(s)
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError:
            return raw
    return s.encode("utf-8")

vocab_bytes = {tid: to_bytes(tid, s) for tid, s in id_to_token.items()}
bytes_to_id = {}
for tid in sorted(vocab_bytes):
    b = vocab_bytes[tid]
    if b not in bytes_to_id:
        bytes_to_id[b] = tid
max_len = max(len(b) for b in bytes_to_id)

def tokenize(text):
    data = text.encode("utf-8")
    ids = []
    i = 0
    while i < len(data):
        for length in range(min(max_len, len(data) - i), 0, -1):
            piece = data[i : i + length]
            if piece in bytes_to_id:
                ids.append(bytes_to_id[piece])
                i += length
                break
    return ids

test_text = "人工智能模型通过深度学习来理解自然语言。"
ids = tokenize(test_text)

print(f"测试文本: {test_text}")
print(f"UTF-8 字节数: {len(test_text.encode('utf-8'))}")
print(f"分词数量: {len(ids)}")
print()
decoded = []
for tid in ids:
    raw = vocab_bytes[tid]
    try:
        decoded.append(raw.decode("utf-8"))
    except UnicodeDecodeError:
        decoded.append(f"<字节 {raw.hex()}>")

print(ids)
print(decoded)
```

你会发现，某些单个汉字被拆分为了多个token，发生这种情况的原因有：

- 词表太小，有些词还未收录就已经达到了词表上限
- 训练的语料库中没有出现过该词

| 文本单元     | 海外模型              | 国产模型         |
| ------------ | --------------------- | ---------------- |
| 1 个汉字     | 1.3～1.5 token        | 0.8～1 token     |
| 1 个英文字母 | 平均 0.25～0.33 token | 0.25～0.33 token |
| 1 个英文单词 | 平均 1.3 token        | 平均 1.3 token   |

### 总结

通过分词表，可以高效的将文本序列转化为 token 序列。

不同的训练语料、不同的分词算法，得到不同的格式和内容的词表，从而得到不同的分词结果

## Token统计

Token 统计是指将一段文本序列转换为 Token 数量的过程

Token 统计分为事前统计和事后统计

**事后统计**：使用模型服务商的API接口会告知你本次token用量

**事前统计**

将文本发送给大模型之前进行统计，通常用于：

- **单轮输入长度拦截**

  用户粘贴 10 万字合同，事前算出超 100k token，直接弹窗 "文本过长，请分段上传"，不发起无效 API 调用。

- **用户额度 / 充值计费预校验**

  面向 C 端付费产品（AI 写作、AI 客服、知识库问答），调用前预计算本次请求预估总 token，若剩余额度不足，直接拦截，提示充值，不用等 API 返回才告知超限，提升体验；

- **企业预算前置审批**

  企业内部 AI 平台、员工 AI 工具：部门有月度 AI 成本预算。员工上传大文件跑分析前，本地算出预估 token，换算成人民币成本，超过阈值需走审批，再允许发起调用。

- **报价前置展示**

  SaaS AI 工具：用户上传文档 / 输入提示词，页面实时显示「本次预估消耗 XX token，约 XX 元」，让用户确认后再执行，减少客户对账单争议。

- ...

### API统计

某些大模型服务商提供API接口，可免费计算token用量

```python
!uv add requests==2.34.2 python-dotenv==1.2.2
```

```python
import requests
from dotenv import load_dotenv
import os

load_dotenv('../.env')

# 以 Moonshot AI（Kimi）为例，它提供了免费的 token 统计接口
# API Key 申请地址：https://platform.moonshot.cn
API_KEY = os.environ.get("MOONSHOT_API_KEY")  

url = "https://api.moonshot.cn/v1/tokenizers/estimate-token-count"

text = "人工智能正在深刻改变我们的生活，从智能助手到自动驾驶，AI 无处不在。"

response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        # "model": "moonshot-v1-8k",
        "model": "kimi-k3",
        "messages": [
            {"role": "user", "content": text},
        ],
    },
)

result = response.json()
print(f"接口返回：{result}")
print(f"文本：{text}")
print(f"文本长度：{len(text)}")
print(f"Token 数：{result['data']['total_tokens']}")
```

### SDK统计

某些模型服务商提供SDK，可在本地统计 token

```python
# 安装依赖（只需运行一次）
!uv add tiktoken==0.13.0
```

```python
import tiktoken

# tiktoken 是 OpenAI 官方的分词库
# 首次运行会联网下载词表并缓存，之后统计完全在本地进行，无需 API Key
encoding = tiktoken.encoding_for_model("gpt-4o")

text = "人工智能正在深刻改变我们的生活，从智能助手到自动驾驶，AI 无处不在。"

tokens = encoding.encode(text)
print(f"文本：{text}")
print(f"文本长度：{len(text)}")
print(f"Token 序列：{tokens}")
print(f"Token 数：{len(tokens)}")
```

### transformers库

开源模型可以使用 transformers 库进行统计

transformers库是 Hugging Face 的官方库，专门用于操作 transformers 模型。

Hugging Face 是一个开源平台，几乎所有的开源模型都会上传到该平台

官方网站：https://huggingface.co/

```python
# 安装依赖（只需运行一次）
!uv add transformers==5.14.1
```

```python
import os

# 国内访问 HuggingFace 需配置镜像（可直连的话删除这行即可）
os.environ["HF_ENDPOINT"] = "http://hf-mirror.com"

from transformers import AutoTokenizer

# 以开源模型 Qwen3 为例
# 首次运行会下载分词器文件（仅几 MB，不含模型权重），之后统计完全在本地进行
tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3")

text = "人工智能正在深刻改变我们的生活，从智能助手到自动驾驶，AI 无处不在。"

tokens = tokenizer.encode(text)
print(f"文本：{text}")
print(f"文本长度：{len(text)}")
print(f"Token 序列：{tokens}")
print(f"Token 数：{len(tokens)}")
```
## 神经网络本质

神经网络中的每一层，实际上做的是矩阵运算，并不存在所谓“神经元”。
$$
\begin{aligned}
& \textbf{神经网络中，某层的计算过程} \\
\\
& \text{完整矩阵形式：} \\
\\
& \begin{bmatrix}
  a_1^{(l)} \\
  a_2^{(l)} \\
  \vdots \\
  a_n^{(l)}
  \end{bmatrix}
  =
  \sigma\left(
  \begin{bmatrix}
  w_{11}^{(l)} & w_{12}^{(l)} & \cdots & w_{1m}^{(l)} \\
  w_{21}^{(l)} & w_{22}^{(l)} & \cdots & w_{2m}^{(l)} \\
  \vdots & \vdots & \ddots & \vdots \\
  w_{n1}^{(l)} & w_{n2}^{(l)} & \cdots & w_{nm}^{(l)}
  \end{bmatrix}
  \begin{bmatrix}
  a_1^{(l-1)} \\
  a_2^{(l-1)} \\
  \vdots \\
  a_m^{(l-1)}
  \end{bmatrix}
  +
  \begin{bmatrix}
  b_1^{(l)} \\
  b_2^{(l)} \\
  \vdots \\
  b_n^{(l)}
  \end{bmatrix}
  \right) \\[1.2em]
& \text{简写形式：} \\
\\
& \mathbf{a}^{(l)} = \sigma\left( \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)} \right) \\[1.2em]
& \text{其中：} \\
& \mathbf{a}^{(l)}: \text{第 } l \text{ 层的输出向量（大小为 } n \times 1 \text{）} \\
& \mathbf{a}^{(l-1)}: \text{第 } l-1 \text{ 层的输出向量（大小为 } m \times 1 \text{）} \\
& \mathbf{W}^{(l)}: \text{第 } l \text{ 层的权重矩阵（大小为 } n \times m \text{）} \\
& \mathbf{b}^{(l)}: \text{第 } l \text{ 层的偏置向量（大小为 } n \times 1 \text{）} \\
& \sigma(\cdot): \text{激活函数（如 Sigmoid、ReLU 等）}
\end{aligned}
$$

### 矩阵相加
要求相加的矩阵行、列长度相同
$$
c_{ij}=(a_{ij}+b_{ij})
$$


$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
+
\begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1n} \\
b_{21} & b_{22} & \cdots & b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
b_{m1} & b_{m2} & \cdots & b_{mn}
\end{bmatrix}
=
\begin{bmatrix}
a_{11}+b_{11} & a_{12}+b_{12} & \cdots & a_{1n}+b_{1n} \\
a_{21}+b_{21} & a_{22}+b_{22} & \cdots & a_{2n}+b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}+b_{m1} & a_{m2}+b_{m2} & \cdots & a_{mn}+b_{mn}
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
+
\begin{bmatrix}
7 & 8 & 9 \\
10 & 11 & 12
\end{bmatrix}
=
\begin{bmatrix}
1+7 & 2+8 & 3+9 \\
4+10 & 5+11 & 6+12
\end{bmatrix}
=
\begin{bmatrix}
8 & 10 & 12 \\
14 & 16 & 18
\end{bmatrix}
$$
$A_{(m\times n)} + B_{(m\times n)} = AB_{(m\times n)}$

### 矩阵的点乘
要求相乘的2个矩阵，前一个矩阵的行长度等于后一个矩阵的列长度，前一个的列长度等于后一个的行长度
$$
c_{ij}=\sum_{k=1}^{n} a_{ik}b_{kj}
$$

$$
AB=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
\cdot
\begin{bmatrix}
b_{11} & b_{12} & \cdots & b_{1p} \\
b_{21} & b_{22} & \cdots & b_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
b_{n1} & b_{n2} & \cdots & b_{np}
\end{bmatrix}
=
\begin{bmatrix}
c_{11} & c_{12} & \cdots & c_{1p} \\
c_{21} & c_{22} & \cdots & c_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
c_{m1} & c_{m2} & \cdots & c_{mp}
\end{bmatrix}
$$


$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\cdot
\begin{bmatrix}
7 & 8 \\
9 & 10 \\
11 & 12
\end{bmatrix}
=
\begin{bmatrix}
1\cdot7+2\cdot9+3\cdot11 & 1\cdot8+2\cdot10+3\cdot12 \\
4\cdot7+5\cdot9+6\cdot11 & 4\cdot8+5\cdot10+6\cdot12
\end{bmatrix}
=
\begin{bmatrix}
7+18+33 & 8+20+36 \\
28+45+66 & 32+50+72
\end{bmatrix}
=
\begin{bmatrix}
58 & 64 \\
139 & 154
\end{bmatrix}
$$


$A_{(m\times n)} \cdot B_{(n\times p)} = AB_{(m\times p)}$

### 矩阵的转置

$$
A=
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
\\
\\
A^T=
\begin{bmatrix}
a_{11} & a_{21} & \cdots & a_{m1} \\
a_{12} & a_{22} & \cdots & a_{m2} \\
\vdots & \vdots & \ddots & \vdots \\
a_{1n} & a_{2n} & \cdots & a_{mn}
\end{bmatrix}
$$

如果原矩阵 $A$ 是 $m×n$，转置后 $A^T$ 就是 $n×m$。

### 向量矩阵

向量可以和矩阵进行运算，运算时，可以把向量看作是$n×1$的矩阵，也可以看作是$1×n$的矩阵，如何看待根据算法而不同。

$A_{(m\times n)} \cdot x_{(n\times 1)} = y_{(m\times 1)}$

$A_{(m\times n)} \cdot x_{(1\times n)} = error$

$x_{(1\times n)} \cdot y_{(n\times 1)} = 标量_{(1\times 1)}$
$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
\cdot
\begin{bmatrix}
7 \\
8 \\
9
\end{bmatrix}
=
\begin{bmatrix}
1\cdot7+2\cdot8+3\cdot9 \\
4\cdot7+5\cdot8+6\cdot9
\end{bmatrix}
=
\begin{bmatrix}
7+16+27 \\
28+40+54
\end{bmatrix}
=
\begin{bmatrix}
50 \\
122
\end{bmatrix}
$$

### 张量
0维张量：标量（数字）
1维张量：向量
2维张量：矩阵
3维张量：多维矩阵

## 词嵌入 word embedding

> 词嵌入是 transformer 架构前向传播的第一个阶段

### Token的问题

在预处理阶段，通过分词器，拿到了一个Token ID的序列

但Token ID序列是不能直接拿来进行训练的。

问题的根源在于：

- **Token ID 无法表示语义**

  Token ID 只是表示一个文字符号。仅靠单个符号无法表示它背后丰富的语义。

  比如：你知道某个Token 对应的文字 `كِتاب` 是什么含义吗

- **Token ID 无法表达语义之间的数学关系**

  假设"吃苹果"，对应的 Token 序列是 `[33256, 11789]`

  请问`33256 + 11789`是什么含义？

因此我们需要**更多的维度**来描述一个token。

### 使用向量描述 Token

比如，**苹果**这个词，可以描述为：

- 一种食物
- 和科技有关系
- 昂贵的

如果数字化来表示，可以表示为3个维度：

- 维度1（可被食用的程度）：0.9
- 维度2（科技程度）：0.6
- 维度3（消费水平）：0.5

此时如果有另一个Token，它被描述为：

- 维度1（可被食用的程度）：0.7
- 维度2（科技程度）：0.8
- 维度3（消费水平）：0.3

如果把这个维度的值放到一个三维空间中，可以想象，这两个token在空间中是比较接近的。

> 向量可视化：https://projector.tensorflow.org/

当我们把Token转换成多个维度的数字来表达后，它们之间就可以形成一些有趣的数学关系，比如：

- $苹果\approx Apple$
- $国王 - 王后 \approx 男人 - 女人$
- $男人+医生\approx男医生$
- $2×开心≈狂喜$
- ...

把一个token转换成多个维度的数字向量，这一过程称之为**词嵌入 word embedding**

> 嵌入（Embedding）这个词的本意，就是把低维离散对象，“镶嵌、植入” 到一个连续高维几何空间里。

但问题是，我们应该规定每个token有多少个维度呢？每个维度又表达什么含义呢？每个维度的值又是什么呢？

**在深度学习中，我们只规定学习方法，永远不要告诉机器答案**

因此，我们仅规定有多少维度即可，让机器在训练的过程中，为每一个Token的每一个维度填写具体的值。

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/词嵌入.png)

### 额外的术语

- **上下文长度**：传入到 transformer 神经网络的 Token 数量。
- **上下文窗口长度**：transformer 神经网络能容纳的最大 Token 数量。

## 注意力机制

> Google 2017年论文：[《Attention Is All You Need》](https://arxiv.org/pdf/1706.03762)
>
> 
>
> 目前大模型使用的架构仅是其中一部分
>
> ![transformer_decoder](https://resource.duyiedu.com/yuanjin/202607201528441.svg)

> 接下来的所有讨论都基于**训练**的前向传播过程，而非推理

假设现在已经得到了一个 $4 × 6$ 的矩阵，该矩阵来自于 Embedding 的输出结果

### Embedding的问题

Embedding层为单独的每一个词编码了它的语义。

但实际上，同一个词在不同的上下文中，它的含义是会变化的。

比如：

- 他一把把把把住了
- “你这是什么意思？” 
  “没什么意思，就是意思意思” 
  “你这就不够意思了” 
  “小意思小意思”
  “你这人真有意思”
  “其实也没有别的意思”
  “那我就不好意思了”
  “是我不好意思”
- “请问你要几等座？”
  “你们有几等”
  “一等、二等、特等等等，特等要多等等”
  “我看一下，等一等”
- “衣服上除了校徽，不要别别的”
  “别啊，我就喜欢别别的”
  “那你就别别了！”
- ......

### 注意力机制要解决的问题

输入一个 $4 × 6$ 的矩阵，输出一个 $4 × 6$ 的矩阵，输出的矩阵要表达：

**每个token受到上下文的影响后，该如何调整自身的值**
结果为：
![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制.png)
**详细流程：**
- **第一步**：
    - Q:表示当前token关心什么东西，哪些东西会对当前token产生影响
    - K:其他token怎么知道我影响他
    - V:知道别的token对我的影响后，我怎么施加影响能改变，从而调整自身的值
    ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制2.png)
- **第二步**：
    - 切分矩阵，防止信息量过大（即多头注意力）
    ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制3.png)
- **第三步**：
    - GPU并行计算切分后的矩阵
    ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制4.png)
- **第四步**
    - 如何算呢？先用Q、K矩阵计算，K倒置和Q相乘，然后除以根号K
    - 结果（注意力得分）什么意思呢
        - 第一行第一个表示，自己对自己的影响多大
        - 第一行第二个表示，下一个词对自己的影响多大
        ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制5.png)
- **第五步**
    - 给右上角的得分做掩码（变为负无穷，表示没有影响，值越小表示影响越小）
    - 为啥？
        - 因为这部分表示后面的词对前面的词的影响
            - 因为大模型是预测下一个词，因此不能受后面的影响
            ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制6.png)
- **第六步**
    - 归一化（softmax函数执行），将所有数字转化为0-1之间的数
    ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制7.png)
- **第七步**
    - 加权输出
        - 归一化的结果*V
        ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制8.png)
- **第八步**
    - 多头拼接
    ![image](https://raw.githubusercontent.com/JJ-front/store-img/master/注意力机制9.png)

## Transformer的完整训练流程

<img src="https://resource.duyiedu.com/yuanjin/202607201528441.svg" alt="transformer_decoder" style="zoom:60%;" />

### Transformer Block

Transformer Block 层包含以下几个阶段：

1. **多头注意力**

   现代的大模型还会在多头注意力阶段注入`token`位置信息

   使用的算法是旋转位置编码 (RoPE)，针对的矩阵是Q和K，时机是多头切分之后、注意力得分计算之前

2. **残差连接（Add）**

   将多头注意力阶段得到的“残差”，和它的输入相加，得到 $4×6$ 的矩阵

3. **归一化（Norm）**

   通过 RMSNorm（均方根归一化），将大部分数据归一化到 $[-3,3]$ 之间

   这一步主要是为了防止梯度爆炸和梯度消失

   得到 $4×6$ 的矩阵

4. **前馈网络Feed Forward Network (FFN)**

   这一层主要是为了提升模型的复杂度，会引入一些非线性激活函数。

   FFN的权重矩阵里，不同行（神经元）相当于存储了不同的“知识片段”或“模式模板”。当模型看到一个特定的上下文时，相关的FFN神经元会被激活，输出对应的知识。

   不同的大模型在这一层设计的不一样，比如 DeepSeek V4 Pro 在这一层设计了 MoE（混合专家模型）。

   得到 $4×6$ 的矩阵（该矩阵仍然表达的是一个残差）

5. **残差连接（Add）**

   将FNN阶段得到的“残差”，和它的输入相加，得到 $4×6$ 的矩阵

6. **归一化（Norm）**

   通过 RMSNorm（均方根归一化），将大部分数据归一化到 $[-3,3]$ 之间

   这一步主要是为了防止梯度爆炸和梯度消失

   得到 $4×6$ 的矩阵
   
   

**✅单个 Transformer Block 全部完成**



对于单个Transformer block，它接收一个4×6的矩阵，输出一个4×6的矩阵。经过中间的大量运算，它可以让输出结果的矩阵每一行都包含了大量的上下文信息。



然后将这样的信息再传输给下一个block，循环往复。

> DeepSeek v4 pro 拥有 61 个 Transformer Block



**‼️最终最后一个block的输出，它的每一行都表达了一个完整的上下文‼️**

### 线性变换层

大多数模型的线性变换层，就是一个单层的全连接的神经网络。

通过该网络，它可以把一个 $4 × 6（表示token的维度）$ 的矩阵，变成一个 $4 × 120000（120000是指词汇表的大小）$ 的矩阵

> 请思考，该层的神经网络的权重矩阵应该是什么形状？

该层输出的每一行表达了对于当前上下文，下一个token的可能性，数值越大，可能性越高。

线性变换后，再经过Softmax进行归一化，就可以得到下一个Token的概率分布。

### 反向传播

程序通过读取原始语料，拿到每一个上下文对应的下一个token作为标签，进行反向传播，从而调整整个Transformer架构里边的所有参数。

## 推理机制

> transformer推理可视化：
>
> 
>
> https://poloclub.github.io/transformer-explainer/



理解:
以下是推理阶段比训练阶段多的步骤
- 预填充 Prefill
    - 这里是值用户开始输入时的上下文token需要按照训练过程走一次（这次开启k、v缓存）

- K-V 缓存
    - 同训练过程的，只是注意力机制的每个头的K、V矩阵被缓存
        - 这样就提高了性能，下一次推理只需要前一个词进入神经网络

- 采样策略（指最后取值不是固定取概率最高的，而是像轮盘一样，都有被取到的概率，只是概率高的越容易被取到而已）

  - **温度 Temperature**

    控制输出概率分布的“锐利”或“平滑”程度。

    在Softmax之前，将所有Logits除以温度值 `T`

    **T = 1**：标准概率分布，不作干预。

    **T < 1**（如0.5）：分布变得更尖锐，高概率的词概率更高，低概率的词概率更低。文本更稳定、保守、确定。

    **T > 1**（如1.5）：分布变得更平滑，各词之间的概率差距缩小。文本更具随机性、多样性、创造力。

  - **Top-K 采样**

    只从概率最高的 **K** 个词中随机抽取，其余词的采样概率直接被置零。比如设置 `K = 50`，模型会先选出概率最高的50个词，过滤掉剩余海量词汇，然后在这50个词中按新的概率分布采样。

  - **Top-P（核采样，Nucleus Sampling）**

    从累积概率达到 **P** 的最小词集合中采样。

    比如设置 `P = 0.9`，模型会按概率从高到低累加词，直到累积概率超过0.9，然后仅从这个动态的“核心”词汇子集中采样。

    这是目前最主流、效果最好的采样方式之一。它比Top-K更灵活，因为K是固定的，而P是动态的：当概率分布很集中时，采样集很小，输出更确定；当分布很分散时，采样集很大，输出更多样。
    
    # 训练阶段

![image-20260721163657184](https://resource.duyiedu.com/yuanjin/202607211636290.png)
## 训练机制
### 预训练特点

- **耗时最长（通常占总计算时间的90%以上）**

- **自监督学习**

- **算力是主要成本**

- **通过预训练，模型具备了以下能力：**

  - 理解人类语言的语法规律

  - 能感知上下文语境，能识别不同语境下词语含义的变化

  - 知晓世界的基本事实

    *太阳系有几大行星、第二次世界大战是哪一年结束的、Python语言的创始人是谁*

  - 拥有基础的推理能力

    *凡人均有一死，苏格拉底是人，所以苏哥拉底会死*

  - 拥有基础的模式识别能力

    *2, 4, 6, 8, ?*

  - 拥有基础的上下文学习能力

    *你是一个智能客服，请在回答问题的时候称用户为“宝宝”。用户的问题是：还有货吗？*

### 后训练特点

- **耗时很短（几小时、几天、几个月）**

- **让模型学会对话格式**

  ```
  输入：
  <|im_start|>system<|im_sep|>你是一个AI聊天助手，你的名字叫袁大炮<|im_end|><|im_start|>user<|im_sep|>你好，你是谁？<|im_end|><|im_start|>assistant<|im_sep|>
  
  输出：
  我是袁大炮<|im_end|>
  ```

  模型学会：对话格式、对话中的角色身份、对话语气、...

- **竖立价值观**

  什么回答是安全的、有用的、诚实的。通过人类标注的“好/坏”回答对比，训练奖励模型，再用强化学习让模型趋利避害。

- **能力校准**

  加入大量“承认无知”的问答对，比如：

  *用户：“你知道明天会发生什么吗？” → 助手：“作为AI，我无法预测未来，很抱歉无法回答这个问题。*

  这个过程能有效降低AI幻觉问题。

- **思维链 CoT**

  思维链（Chain of Thought, CoT）就是通过训练和引导，让模型在给出最终答案之前，先把内部的推理步骤“说出来”，即先输出思考过程，再输出最终回答。

  ```
  输入：
  <|im_start|>user<|im_sep|>小明有10个苹果，他给了小红3个，又买了5个，现在他有多少个苹果？<|im_end|>
  <|im_start|>assistant<|im_sep|>
  <think>
  
  输出：
  开始有10个。给了小红3个，还剩 10 - 3 = 7 个。又买了5个，现在有 7 + 5 = 12 个。所以，答案是12个。
  </think>
  最终答案是 12。<|im_end|>
  ```

- **专业领域知识**

- **后训练阶段主要依靠监督学习、强化学习**

- **数据与人力是主要成本**

### 持续学习

**“持续学习（Continual Learning）”**或**“增量学习（Incremental Learning）”**，是指现在的很多大模型厂商会把AI和用户之间的对话内容作为语料，持续对大模型进行训练。

## Ollama（模型使用）

### 本地模型

- `Pytorch + Transformers`：主要是用于本地训练、微调，也可以进行本地推理，但需要自行适配硬件加速
- `Ollama`：一键部署和运行开源大模型的命令行工具，内置量化支持和 GPU 加速
- `llama.cpp`：高性能 C/C++ 推理引擎，主打 CPU 推理和多种量化方案
- `vLLM`：高吞吐量推理框架，基于 PagedAttention 技术，适用于生产环境部署
- `MLX`：Apple 官方 ML 框架，专为 Apple Silicon 设计的本地推理方案
- `LM Studio`：带图形界面的桌面应用，支持一键下载和运行本地开源模型
- `LocalAI`：提供 OpenAI 兼容 API 的本地推理服务，方便现有应用无缝切换

### 下载安装

自行下载安装：https://ollama.com/

```shell
ollama -v
```

Ollama官方仓库：https://ollama.com/library

设置环境变量：`OLLAMA_MODEL_SERVER="https://mirror.ollama.com"`

```shell
# 拉取模型到本地
ollama pull qwen3-vl
# 查看已下载的模型
ollama list
# 删除模型
ollama rm <模型名称>
# 查看模型信息
ollama show <模型名称>
# 运行模型
ollama run <模型名称>
# 查看目前的服务
ollama ps
```

访问：http://localhost:11434/ ，查看服务是否正在运行



测试接口：

```shell
# 模型列表
curl http://localhost:11434/v1/models

# 聊天接口
curl -X POST http://localhost:11434/v1/chat/completions -H "Content-Type: application/json" -d "{\"model\": \"qwen3-vl\", \"messages\": [{\"role\": \"user\", \"content\": \"你好，请介绍一下自己\"}], \"stream\": false}"
```

### 大模型 API 接口形式

- OpenAI Chat Completions 兼容度最高 事实标准
- OpenAI Response
- Authropic

### 代码使用
使用OpenAI SDK完成，因为他封装了一些能力，兼容OpenAI Chat Completions这套接口形式

```python
!uv add openai==1.74.0 python-dotenv==1.2.2
```

```python
from utils import config
from openai import OpenAI, AsyncOpenAI

client = OpenAI()
```

```python
# 获取模型列表
list = client.models.list()
print(list.to_json())
```

```python
# 基本对话
response = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[
        {"role":"user", "content":"你是谁"}
    ]
)
print(response.to_json())
```

```python
# 关闭思维链
response = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[
        {"role":"user", "content":"你是谁"}
    ],
    extra_body={
        "thinking": {
            "type": "disabled" # qwen3-vl无法直接关闭思考模式
        }
    }
)
print(response.to_json())
```

```python
# 流式响应
import sys

stream = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[
        {"role":"system", "content":"少思考，简洁回答"},
        {"role":"user", "content":"从1数到10"}
    ],
    stream=True
)

for chunk in stream:
    print(chunk)
    sys.stdout.flush()
```

```python
# 流式响应提取
from utils.stream_print import print_stream
import sys

stream = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[
        {"role":"system", "content":"少思考，简洁回答"},
        {"role":"user", "content":"从1数到10"}
    ],
    stream=True
)
print_stream(stream)
```

```python
# 使用视觉能力
from utils.stream_print import print_stream
from utils.img_base64 import to_dataurl

# 读取本地图片并转换为 Base64
dataurl = to_dataurl("menu.png")
stream = client.chat.completions.create(
    model=config.OPENAI_MODEL,
    messages=[{
            "role":"user", 
            "content":[
                {"type": "text", "text": "请描述这张图片的内容"},
                {"type": "image_url","image_url": {"url": dataurl} }
            ]
        }
    ],
    stream=True
)
print_stream(stream)
```
## 系统提示词
### 二次封装（上一节的工具函数）

```python
!uv add pydantic-settings==2.14.1
```

```python
from agent.model import Model
from agent.printer import print_response, print_stream, PrinterConfig
from agent.message import SystemMessage, UserMessage, AssistantMessage

model = Model()
```

```python
resp = model.invoke_stream([
    SystemMessage("当用户向你打招呼时，你仅需回答你好即可"),
    UserMessage("你好")
])
print_stream(resp)
```

### 系统提示词

系统提示词往往出现在所有消息的最前面，大模型在训练的过程中，会重点关注系统提示词。

编写系统提示词的核心原则是：

- **精简**

  能不说就不说，能少说就少说，绝对避免无病呻吟。

  > **反面案例：**
  >
  > 
  >
  > 你现在要充当一名专业代码顾问，接下来我会向你提出各种各样和编程相关的问题。希望你认真仔细地阅读我每一次发送过来的内容，充分理解我的诉求之后，再进行回答。回答的时候尽量清晰易懂，方便我进行理解。如果遇到不清楚的内容，千万不要随意编造答案。
  >
  > 
  >
  > **正面案例**
  >
  > 
  >
  > 你是代码顾问。精准解答编程问题，不懂直接说明，禁止编造信息。

- **自洽**

  提示词不能自我矛盾。

  > **反面案例：**
  >
  > 
  >
  > 你是数据分析助手。回答务必详尽，多角度展开说明；同时所有回复控制在 30 字以内。
  >
  > 
  >
  > **正面案例**
  >
  > 
  >
  > 你是数据分析助手。回答简洁，整体控制在 30 字以内。

- **全局约束**

  系统提示词内所有规则作用于整条对话的每一轮交互。

  > **反面案例：**
  >
  > 
  >
  > 当用户要求你写数据分析类代码的时候，你应该使用Python来编写。
  >
  > 
  >
  > **正面案例**
  >
  > 
  >
  > <空>

- **保持静态**

  系统提示词内容应当**尽量**固定不变。

  > **反面案例：**
  >
  > 
  >
  > 当前用户是：<动态内容>，时间是：<动态内容>
  >
  > 
  >
  > **正面案例**
  >
  > 
  >
  > <空>

- **结构化**

  系统提示词采用 Markdown / XML（或二者混用）进行分层排版；核心指令、硬性约束、输出规范使用标记进行隔离，便于模型区分层级、识别关键规则，避免文本扁平化造成理解偏差。

  > **反面案例：**
  >
  > 
  >
  > 你是技术助手。回答必须精简，不能编造信息。输出答案尽量条理清晰。如果信息不足直接说明。禁止额外多余话术。
  >
  > 
  >
  > **正面案例：**
  >
  > 
  >
  > ```markdown
  > # 角色
  > 技术助手
  > ## 硬性规则
  > 1. 回答精简，严禁编造信息
  > 2. 信息不足直接说明，不强行作答
  > ## 输出要求
  > 条理清晰，无多余开场白与结束语
  > ```

```python
!uv add jinja2==3.1.6
```

```python
# 获取所需信息
import os
import platform
import subprocess


def get_cwd() -> str:
    return os.getcwd()


def get_is_git() -> bool:
    result = subprocess.run(
        ['git', 'rev-parse', '--is-inside-work-tree'],
        capture_output=True, text=True, timeout=5
    )
    return result.returncode == 0 and result.stdout.strip() == 'true'


def get_language() -> str:
    system = platform.system()
    if system == 'Darwin':
        result = subprocess.run(
            ['defaults', 'read', '-g', 'AppleLocale'],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip()
    elif system == 'Windows':
        import ctypes
        lcid = ctypes.windll.kernel32.GetUserDefaultLCID() # type: ignore
        buf = ctypes.create_unicode_buffer(256)
        ctypes.windll.kernel32.GetLocaleInfoW(lcid, 0x5C, buf, 256) # type: ignore
        return buf.value
    return ''


print(f"cwd: {get_cwd()}")
print(f"is_git: {get_is_git()}")
print(f"language: {get_language()}")
```

```python
# 模板渲染
from jinja2 import Environment, FileSystemLoader


def render_system_prompt() -> str:
    template_dir = os.path.join(os.getcwd(), 'agent/prompt')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('system.j2')
    return template.render(
        language=get_language(),
        cwd=get_cwd(),
        is_git=get_is_git(),
    )


print(render_system_prompt())
```

```python
# 使用封装后的结果
from agent.prompt import render_prompt

print(render_prompt("system"))
```

```python
# 使用系统提示词

from agent.prompt import render_prompt

resp = model.invoke_stream([
    SystemMessage(render_prompt("system")),
    UserMessage("目前在哪个目录？")
])
print_stream(resp)
```

## 会话
```python
from agent.model import Model
from agent.printer import print_response, print_stream, PrinterConfig
from agent.prompt import render_prompt

model = Model()
```

```python
# 第1次调用
resp = model.invoke_stream([
    {"role": "system", "content": render_prompt("system")},
    {"role": "user", "content": "uv是什么？"}
])

print_stream(resp)
```

```python
# 第2次调用
resp = model.invoke_stream([
    {"role": "system", "content": render_prompt("system")},
    {"role": "user", "content": "如何安装？"}
])

print_stream(resp)
```

```python
from agent.session import Session

session = Session()
session.add_message({"role": "system", "content": render_prompt("system")})
session.add_message({"role": "user", "content": "uv是什么？"})
# 第一次调用
resp = model.invoke_stream(session)

print_stream(resp)
```

```python
# 查看会话内容
import json

print(session.id)
print(json.dumps(session.messages, ensure_ascii=False, indent=2))
```

```python
session.add_message({"role":"user", "content": "如何安装？"})
# 第2词调用
resp = model.invoke_stream(session)

print_stream(resp)
```

```python
# 查看会话内容
import json

print(session.id)
print(json.dumps(session.messages, ensure_ascii=False, indent=2))
```

```python
# 保存会话内容
session.save()
```

### 最佳实践

在使用会话功能的时候，不管以何种方式实现，应该遵循以下法则：

- **历史上下文不可修改**
    - 不满足此条，会导致难以命中模型服务商的 prompt cache（命中缓存，token收费会低很多）
        - 一次请求内：K、V缓存
        - 第二次请求，会把上次的k、v缓存读出来做匹配，叫做prompt 缓存
- **上下文中应保留思维链**

  不满足此条，会导致推理上下文丢失，从而导致模型回复质量下降

## Tool Calling

大模型只能处理输入得到输出，没有任何其他功能。

而在Agent应用中，经常会出现希望：

- 大模型读取或写入一个文件
- 执行一段命令
- 联网搜索一些资料
- ...

这些功能大模型都无法直接处理。

如果需要大模型去完成一些除了文本输出之外的功能的时候，就需要借助`Tool Calling`

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/tools.png)


### 定义工具函数

```python
def read_file(filepath: str) -> str:
    """读取文件内容并以字符串形式返回"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


# 测试：读取当前课件文件的前 200 个字符
content = read_file("./agent/prompt/system.j2")
print(content[:200])
```

```python
def write_file(filepath: str, content: str) -> None:
    """将内容写入文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# 测试：写入测试文件
write_file("test_write.txt", "Hello, this is a test file.\n这是测试文件。")
print(read_file("test_write.txt"))
```

### 绑定工具到上下文

https://api-docs.deepseek.com/zh-cn/api/create-chat-completion

```python
session.tools = [
    # 工具1: 读文件
    {
        # 固定: function
        "type": "function",
        "function": {
            # 工具名称，会影响模型输出结果，通常为函数名
            "name": "read_file",
            # 自然语言描述函数功能，模型能理解 
            "description": "读取文件",
            # 参数的schema描述"
            "parameters": {
                "type": "object", # 固定为 object
                "properties": {
                    # 描述参数 filepath
                    "filepath":{
                        "type": "string",
                        "description": "文件的绝对路径，或相对于cwd的路径",
                    }
                },
                # 必填参数
                "required": ["filepath"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "写入文件",
            "parameters": {
                "type": "object", 
                "properties": {
                    "filepath":{
                        "type": "string",
                        "description": "文件的绝对路径，或相对于cwd的路径",
                    },
                    "content": {
                        "type": "string",
                        "description": "要写入的内容，该内容会完全覆盖文件原本内容"
                    }
                },
                "required": ["filepath", "content"]
            }
        }
    }
]
```

```python
# 查看上下文
session.print()
```

### 调用模型

大模型厂商通常会将你传递的工具放到系统上下文的末尾，比如：

```markdown
<|im_start|>system<|im_sep|>
系统提示词
# Tools

## functions

namespace functions {
    // 读取文件
    type read_file = ({
        // 文件的绝对路径，或相对于cwd的路径
        file_path: string
    }) => any;
    // 写入文件
    type write_file = ({
        // 文件的绝对路径，或相对于cwd的路径
        file_path: string;
        // 待写入的内容
        content: string
    }) => any;
}
<|im_end|>
<|im_start|>user<|im_sep|>
用户消息
<|im_end|>
<|im_start|>assistant<|im_sep|>
 thinking
```

模型会返回：

```
思考内容
 response
<tool_call>
{"name": "write_file", "arguments": {"file_path": "..."}}
</tool_call>
<|im_end|>
```

```python
listener.listening = False # 暂时不监听流式输出

session.add_message({"role": "user", "content": "请在当前目录新建一个`uv.md`文件，写入UV的安装教程。直接新建就好"})
resp = model.invoke(session)
print(resp.print_raw())
```

```python
session.save()
```

### 执行工具

```python
msg = session.messages[-1]
msg
```

```python
import json

tool_calls = msg["tool_calls"][0]
tool_id = tool_calls["id"]
tool_name = tool_calls["function"]["name"]
arguments = json.loads(tool_calls["function"]["arguments"])

print("tool id", tool_id)
print("tool name", tool_name)
print("arguments", arguments)
```

```python
func = globals().get(tool_name)
if callable(func):
    func(**arguments)
```

## 封装 Tool Calling

Tool Calling 完整流程：定义函数 → 手动拼 JSON Schema → 绑定到 session.tools → 调用模型 → 执行工具。
主要解决**手动拼 JSON Schema**和**调用模型** 这个重复且可抽离的动作
```python
from agent.model import Model
from agent.printer import ModelPrinterListener
from agent.prompt import render_prompt
from agent.session import Session
import json
import os

session = Session()
model = Model()
listener = ModelPrinterListener(model)
session.add_message({"role": "system", "content": render_prompt("system")})
print("环境准备完成")
```
```python
# 先定义两个工具函数（跟上节课一样）
def read_file(filepath: str) -> str:
    """读取文件内容并以字符串形式返回"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    """将内容写入文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


# 测试一下
print(read_file("./agent/prompt/system.j2")[:100])
```

封装的目标是希望在代码层面更加简洁优雅地完成这条流水线。

### 再次认识 Pydantic

```python
!uv add pydantic==2.13.4
```

```python
from pydantic import BaseModel, Field

class Counter(BaseModel):
    n: int = Field(description="计数值", default=0)

# 自动适配默认值
# Counter()

# 自动转换类型
# Counter(n="123")

# 无法转换则报错
# Counter(n=[1,2,3])

# 转换为字典格式
# Counter().model_dump()

# 获取 schema
schema = Counter.model_json_schema()
# schema
print(json.dumps(schema, indent=2, ensure_ascii=False))
```

**我们期望可以通过 Pydantic 的模型来校验参数，并且得到参数列表的 Schema。**

类似于

```python
param_model = create_params_model(write_file, param_descriptions={
  "filepath": "文件的绝对路径或相对于cwd的路径",
  "content": "待写入的文件内容"
})
write_file_param_model = param_model(filepath="./uv.md") # 校验参数
param_model.model_json_schema() # 获取 schema
```

```python
# 动态创建模型
from pydantic import create_model

param_model = create_model(
    "dynamic_model", 
    filepath = (str, Field(description="文件的绝对路径或相对于cwd的路径")),
    content = (str, Field(description="待写入的文件内容"))
)

# write_file_param_model = param_model(filepath="./uv.md") # 校验参数
schema = param_model.model_json_schema() # 获取 schema
print(json.dumps(schema, indent=2, ensure_ascii=False))
```

```python
# 实现 create_params_model 函数
import inspect
from typing import Any

def create_params_model(func, param_descriptions = {}):
    model_name = f"{func.__name__}_params"
    args = {}
    sig = inspect.signature(func)
    for pname, param in sig.parameters.items():
        py_type = (
            param.annotation if param.annotation is not param.empty else Any
        )
        desc = param_descriptions.get(pname, "")

        if param.default is param.empty:
            # 必填参数：不设默认值
            args[pname] = (py_type, Field(description=desc))
        else:
            # 可选参数：设置默认值
            args[pname] = (
                py_type,
                Field(default=param.default, description=desc),
            )

    return create_model(model_name, **args)

param_model = create_params_model(write_file, param_descriptions={
  "filepath": "文件的绝对路径或相对于cwd的路径",
  "content": "待写入的文件内容"
})
# write_file_param_model = param_model(filepath="./uv.md") # 校验参数
schema = param_model.model_json_schema() # 获取 schema
print(json.dumps(schema, indent=2, ensure_ascii=False))
```

### 封装 Tool 类

我们期望，`Tool` 类能够实现下面的操作。

```python
# 1. Tool可以包装一个函数，并指定每个参数的描述

tool = Tool(
  read_file, 
  param_descriptions={"filepath": "文件路径"}
)

# 2. 调用 tool 和调用原函数行为一致
tool("./uv.md")

# 3. 可以轻松获取 schema
tool.schema # {"type":"function", "function": {...}}

```

```python
# 创建 Tool 类
import inspect
from typing import Callable


class Tool:

    def __init__(
        self,
        func: Callable,
        param_descriptions: dict = {},
    ):
        self.func = func
        self.name = func.__name__
        self.description = inspect.getdoc(func) or ""
        self.param_descriptions = param_descriptions or {}
        self.param_model = create_params_model(func, param_descriptions)

tool = Tool(
  read_file, 
  param_descriptions={"filepath": "文件路径"}
)
```

```python
# 实现 schema
def schema(self) -> dict:
    param_schema = self.param_model.model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    name: {
                        "type": prop.get("type", "string"),
                        "description": prop.get("description", ""),
                    }
                    for name, prop in param_schema.get("properties", {}).items()
                },
                "required": param_schema.get("required", []),
            },
        },
    }

setattr(Tool, "schema", schema)

# print(json.dumps(tool.schema(), indent=2, ensure_ascii=False))
```

```python
# 实现可调用
import traceback
def __call__(self, **kwargs) -> Any:
    result = ""
    try:
        # 验证参数
        validated = self.param_model(**kwargs)
        result = str(self.func(**validated.model_dump())) # 将结果转换为字符串
    except Exception as e:
        # 完整堆栈字符串
        result = "".join(traceback.format_exception(type(e), e, e.__traceback__))

    return result

setattr(Tool, "__call__", __call__)
# tool(filepath = "./agent/prompt/system.j")
```

```python
# 使用封装好的类
from agent.tool.core.tool import Tool

tool = Tool(write_file, param_descriptions={
    "filepath": "文件的绝对路径或相对于cwd的路径",
    "content": "待写入的文件内容"
})

# tool(filepath="uv.md", content="123123123")
tool.schema()
```

### 实现装饰器

我们希望对函数的描述能够聚合到函数所在的位置。

```python
@tool(filepath="文件的绝对路径或相对于cwd的路径", content="待写入的文件内容")
def write_file(filepath: str, content: str) -> None:
    """将内容写入文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
```

```python
# 实现 tool 装饰器

def tool(**args):
    """装饰器：将普通函数包装为 Tool 对象"""
    def decorator(func):
        return Tool(func, param_descriptions=args)
    return decorator
```

```python
@tool(filepath = "文件绝对路径或相对于cwd的路径")
def read_file(filepath: str) -> str:
    """读取文件内容并以字符串形式返回"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

@tool(filepath = "文件绝对路径或相对于cwd的路径", content="待写入的内容")
def write_file(filepath: str, content: str) -> None:
    """将内容写入文件"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
```

### 封装工具调度中心

现在我们已经可以定义工具了，但是从工具到session之间，以及从session到调用工具之间，还有一点距离。工具调度中心就是为了弥补这个距离。

```python
session.tools = registry.schema()
resp = model.invoke(session)
result = registry.invoke(resp.messages[-1])
result # 工具调用结果，None表示此次无须调用工具
```

```python
class _ToolRegistry:
    _tools: dict[str, Tool] = {}

    def register(self, tool: Tool):
        """注册一个工具"""
        self._tools[tool.name] = tool

    def schemas(self) -> list[dict]:
        """返回所有工具的 Schema 列表，可直接赋值给 session.tools"""
        return [t.schema() for t in self._tools.values()]

    def invoke(self, message: dict) -> list[dict] | None:
        """从模型返回的消息中提取 tool_calls 并逐一执行"""
        tool_calls = message.get("tool_calls", [])
        if not tool_calls:
            return None
        results = []
        for tc in message.get("tool_calls", []):
            id = tc["id"]
            name = tc["function"]["name"]
            args = json.loads(tc["function"]["arguments"])
            tool = self._tools[name]
            result = ""
            if not tool:
                result = "无此工具，请仔细检查你传递的工具名称是否正确"
            else:
                result = tool(**args)
            results.append({
                "role": "tool",
                "tool_call_id": id,
                "name": name,
                "content": result,
            })
        return results

registry = _ToolRegistry()
registry.register(read_file)
registry.register(write_file)
```

### 完整流程测试

```python
# 注册工具

from agent.tool import registry

session.tools = registry.schemas()

session.print()
```

```python
# 发起对话
session.add_message({"role": "user", "content": "请在当前目录新建一个`uv.md`文件，写入UV的安装教程。直接新建就好"})

resp = model.invoke_stream(session)
```

```python
session.print()
```

```python
call_msg = registry.invoke(session.messages[-1])
print(call_msg)
```

```python
# 追加工具结果到上下文
if call_msg:
    session.messages += call_msg

session.print()
```

```python
# 告知模型结果

model.invoke_stream(session)
```


## ReAct
本次代码变动：

- 新增了`tool/bash_command.py`，提供了执行`bash`命令的工具
- 在系统提示词中注入了当前操作系统的信息
- 新建 `Session` 时自动注入工具和提示词
- 将打印格式进行了简洁化处理

```python
from agent.model import Model
from agent.printer import ModelPrinterListener
from agent.session import Session
from agent.tool import registry
import json
import os

session = Session()
model = Model()
listener = ModelPrinterListener(model)
session.print()
```

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/ReAct.png)


```python
def query(q: str, session: Session, model: Model):
    "根据用户提问进行处理"
    session.add_message({"role": "user", "content": q})
    # ReAct Loop
    while True:
        model.invoke_stream(session)
        call_msg = registry.invoke(session.messages[-1])
        if call_msg is None:
            break
        else:
            session.messages += call_msg

query("请帮我分析./agent目录中的核心实现逻辑，将结果放到当前目录的 分析.md 中", session, model)
```

```python
session.save()
```

## Agent

AI Agent（智能体）：通过自主规划、调用工具、持续观察反馈并迭代行动，独立推进复杂任务直至目标达成的人工智能运行单元。

课前修改：

- 修改了系统提示词，现在系统提示词更加简洁
- 封装了`agent.py`
- 封装了抽象的监听器
- 新增了`session`的简洁打印方法`print_friendly`

```python
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)
```

```python
agent.invoke("请帮我分析./agent目录中的核心实现逻辑，将结果放到当前目录的 分析.md 中")
```

```python
agent.session.print_friendly()
```

### 概念
轮次：用户输入 -> agent（loop） -> 结果

## Agent 搜索引擎

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/AI%20Search.png)

问题的关键是，`web_search` 工具应该返回给 AI 什么调用结果？

如何使用传统的搜索引擎，内容被大量的标签、样式、JS代码污染，会遇到以下问题：

- 更多的 token 消耗
- 注意力被分散
- 很多 CSR 的页面无法得到内容
- 包含大量无关信息，比如广告图片、菜单、banner等等
- 深层链接无法一次性获取
- ...

这些问题，都使得我们需要一个更加适合 Agent 调用的搜索引擎

- **Firecrawl**：https://www.firecrawl.dev/

- **Tavily**：https://www.tavily.com/

- **AnySearch**：http://www.anysearch.com/

- **Brave**：https://brave.com/

- **Exa**: https://exa.ai/

### 获取 API-KEY

https://www.tavily.com/

将获取到的 API KEY 保存到环境变量

### 使用 Tavily

```python
!uv add tavily-python==0.7.26
```

```python
from tavily import TavilyClient, TavilyKeylessLimitError
from agent.config import tavily_settings

client = TavilyClient(api_key=tavily_settings.api_key)
```

#### 基本搜索功能

```python
import json
response = client.search(query="可控核聚变最新研究进展")
print(json.dumps(response, indent=2, ensure_ascii=False))
```

#### 网页提取功能

```python
response = client.extract(
    urls=[
        "https://baike.baidu.com/item/Tavily/67277807",
        "https://baike.baidu.com/item/Firecrawl"
    ], 
    include_images=True)

print(json.dumps(response, indent=2, ensure_ascii=False))
```

#### 爬虫功能

```python
response = client.crawl(
    url="https://www.yuanjin.tech/",
    max_depth=3,
    limit=50,
    instructions="找到所有和网络相关的知识"
)

print(json.dumps(response, indent=2, ensure_ascii=False))
```

#### 更多功能

https://github.com/tavily-ai/tavily-python

### 集成到 Agent

```python
# 新增 tools
from agent.tool import registry
from agent.tool.core import tool
from tavily import TavilyClient, TavilyKeylessLimitError
from agent.config import tavily_settings



@tool(query="搜索关键字")
def web_search(query:str):
    "根据关键字进行网络搜索，返回结构化的搜索结果"
    client = TavilyClient(api_key=tavily_settings.api_key)
    response = client.search(query=query)
    return json.dumps(response, ensure_ascii=False)

@tool(urls="要抓取的url链接数组")
def fetch_url(urls: list[str]):
    "根据提供的url数组，抓取网页内容，返回结构化的搜索结果"
    client = TavilyClient(api_key=tavily_settings.api_key)
    response = client.extract(
    urls=urls, 
    include_images=False)

    return json.dumps(response, ensure_ascii=False)

registry.register(web_search)
registry.register(fetch_url)
```

```python
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)

agent.invoke("帮我查一查苹果最新发布了哪些产品？")
```

```python
agent.session.print_friendly()
```

## Skill

接下来要聚焦提示词的问题。

考虑下面的场景，提示词该如何编排？

- 在`SaaS`系统中，用户**有时候**需要对销售数据分析，数据分析时，需要告诉模型：
  - 从哪里获取销售数据？
  - 数据有哪些字段，每个字段是什么含义？
  - 有哪些常见的分析方式？
  - 如何根据用户的需求选择合适的分析方式？
  - 分析结果用哪种形式展现？
  - ...
- 在智能客服系统中，用户会**经常**询问关于产品的信息，则需要告诉模型：
  - 我们有哪些产品
  - 每个产品的参数、特点、用法、注意事项、价格、活动、购买链接、建议组合...



如果在系统提示词中，完整地塞入这些内容，会导致严重的提示词膨胀。

而实际上，像这些提示词只有在某些场景下才会触发。因此，我们可以用更加优雅的方式完成提示词的注入。

<img src="./assets/skill.svg">

### 编写 SKILL

编写 `agent/.agents/skills/no-permission/SKILL.md`

### 注入系统提示词和工具

```python
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)
```

```python
agent.session.print_friendly()
```

```python
agent.session.tools
```

```python
# 测试
agent.invoke("最近天气如何？")
```

```python
agent.session.save()
```

### 安装公共 SKILL

请先安装 node：https://nodejs.org/zh-cn/

查询公共skill: 

https://www.skills.sh/

```shell
# 安装 skill
npx skills add https://github.com/anthropics/skills --skill frontend-design
```

```python
agent.invoke("帮我在 ./demo 中创建一个 html 页面，创建一个漂亮的分页表格，请使用 frontend-design skill")
```

```python
agent.session.save()
```

## MCP 协议

MCP 定义了 **Agent** 和 **外部工具** 的 **通信标准** 

https://modelcontextprotocol.io/
### MCP解决什么问题

- 如何让你的tools可以跨项目、跨语言、跨框架使用呢？

### 协议内核

标准中包含：

- 通信角色

  - 客户端 MCP Client：通常是 Agent
  - 服务端 MCP Server：工具提供者
- 通信方式

  - stdio：通过 stdin、stdout 在本地进程间通信
  - http：通过 http 协议通信
- 通信格式：JSON‑RPC 2.0

  ```json
  // json-rpc 示例
  {
    "jsonrpc": "2.0",
    "id": "req-123",
    "method": "tools/call",
    "params": { ... }
  }
  ```
  
### 客户端

任何匹配 MCP 协议的程序都可以作为 MCP Client

本节课使用 `@modelcontextprotocol/inspector` 充当 MCP Client 客户端，它通常用于调试 MCP Server，可以清楚的看到通信内容

```shell
npx -y @modelcontextprotocol/inspector@1.0.0
```

### 服务端

MCP 聚合站包含了海量 MCP 服务器，常见聚合站：

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [mcp.so](https://mcp.so/zh)
- [smithery.ai](https://smithery.ai/servers)
- [glama.ai](https://glama.ai/)
- ...

建议:

- 官方的测试服务器 [time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)

  `uvx mcp-server-time`

- 微软官方文档 `Microsoft Learn`

  `https://learn.microsoft.com/api/mcp`

### 通信内容

| 内容       | 备注         |
| ---------- | ------------ |
| initialize | 初始化       |
| tools/list | 发现工具列表 |
| tools/call | 调用工具     |

## MCP Client

```python
# https://github.com/modelcontextprotocol/python-sdk/tree/v1.28.1
!uv add mcp==1.28.1
```

### Stdio

#### 定义服务器连接参数

```python
from mcp import StdioServerParameters

server_params = StdioServerParameters(
    command="uvx",  # Using uv to run the server
    args=["mcp-server-time"]
)
```

#### 工具列表

```python
from mcp.client.stdio import stdio_client
from mcp import ClientSession

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        # initialize
        await session.initialize()

        # tools/list
        tools = await session.list_tools()
        print(tools.model_dump_json(indent=2, ensure_ascii=False))
```

#### 调用工具

```python
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        # 初始化
        await session.initialize()

        # tools/call
        tools = await session.call_tool(
            name="get_current_time", 
            arguments={
                "timezone": "Asia/shanghai"
            })
        print(tools.model_dump_json(indent=2, ensure_ascii=False))
```

### HTTP

#### 工具列表

```python
from mcp.client.streamable_http import streamable_http_client
from mcp import ClientSession

async with streamable_http_client("https://learn.microsoft.com/api/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
    async with ClientSession(read_stream, write_stream) as session:
        # initialize
        await session.initialize()  # http请求1

        # tools/list
        tools = await session.list_tools() # http请求2
        print(tools.model_dump_json(indent=2, ensure_ascii=False))
```

#### 调用工具

```python
async with streamable_http_client("https://learn.microsoft.com/api/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
    async with ClientSession(read_stream, write_stream) as session:
        # initialize
        await session.initialize()

        # tools/call
        tools = await session.call_tool(
            name="microsoft_docs_search", 
            arguments={
                "query": "c#如何解析excel"
            })
        print(tools.model_dump_json(indent=2, ensure_ascii=False))
```

### 封装

#### MCP 配置

```python
mcp = {
  "servers": {
    "time": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-server-time"
      ]
    },
    "microsoft-learn": {
        "type": "http",
        "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

#### 导入

```python
import asyncio
from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client
from contextlib import asynccontextmanager
```

#### 封装连接逻辑

用 `@asynccontextmanager` 将连接和初始化逻辑封装为一个异步上下文管理器，根据配置中的 `type` 字段自动选择 stdio 或 http 传输方式。

```python
@asynccontextmanager
async def connect_mcp(server_config: dict):
    """根据配置连接 MCP 服务器，返回已初始化的 ClientSession"""
    if server_config["type"] == "stdio":
        params = StdioServerParameters(
            command=server_config["command"],
            args=server_config.get("args", [])
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session
    elif server_config["type"] == "http":
        async with streamable_http_client(server_config["url"]) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session
    else:
        raise ValueError(f"不支持的服务器类型: {server_config['type']}")
```

#### 封装单个服务器操作

有了 `connect_mcp`，获取工具列表和调用工具变得非常简洁——只需 `async with` 进入上下文，拿到 session 后直接调用对应方法即可。

```python
async def list_server_tools(server_config: dict):
    """获取单个 MCP 服务器的工具列表"""
    async with connect_mcp(server_config) as session:
        return await session.list_tools()


async def call_server_tool(server_config: dict, tool_name: str, arguments: dict | None = None):
    """调用单个 MCP 服务器上的工具"""
    async with connect_mcp(server_config) as session:
        return await session.call_tool(tool_name, arguments or {})
```

验证一下——用 time 服务器测试：

```python
tools = await list_server_tools(mcp["servers"]["time"])
print(tools.model_dump_json(indent=2, ensure_ascii=False))
```

```python
result = await call_server_tool(mcp["servers"]["time"], "get_current_time", {"timezone": "Asia/Shanghai"})
print(result.model_dump_json(indent=2, ensure_ascii=False))
```

#### 构建 MCPClient 管理多个服务器

上面的函数已经能处理单个服务器了，但每次都要手动传递 `mcp["servers"]["xxx"]` 仍然不够便捷。我们创建一个 `MCPClient` 类，在初始化时接收完整的 MCP 配置字典，然后提供遍历所有服务器的方法。

先写出异步版本的 `alist_tools` 和 `acall_tool`：

```python
class MCPClient:
    def __init__(self, config: dict):
        self.servers = config["servers"]

    async def alist_tools(self) -> list:
        """异步获取所有服务器的工具列表"""
        results = []
        for name, config in self.servers.items():
            async with connect_mcp(config) as session:
                tools = await session.list_tools()
                results.append({
                    "server": name,
                    "tools": tools
                })
        return results

    async def acall_tool(self, server_name: str, tool_name: str, arguments: dict | None = None):
        """异步调用指定服务器上的工具"""
        config = self.servers[server_name]
        async with connect_mcp(config) as session:
            return await session.call_tool(tool_name, arguments or {})
```

异步版已经可以工作了（在 Jupyter 中用 `await` 直接调用）：

```python
client = MCPClient(mcp)

all_tools = await client.alist_tools()
for item in all_tools:
    print(f"\n===== {item['server']} =====")
    print(item["tools"].model_dump_json(indent=2, ensure_ascii=False))
```

```python
result = await client.acall_tool("time", "get_current_time", {"timezone": "Asia/Shanghai"})
print(result.model_dump_json(indent=2, ensure_ascii=False))
```

#### 同步封装

现在到了最后一步——将异步方法包装为**真正的同步函数**。

`asyncio.run()` 可以直接运行异步协程并返回结果，但它要求在调用时没有其他事件循环在运行。Jupyter 自身维护了一个事件循环，直接调用会报错。

解决方法：利用 `threading` 在**独立线程**中运行异步代码。每个线程拥有自己的事件循环，互不干扰——新线程中调用 `asyncio.run()` 是安全的，因为它不走 Jupyter 的主循环。

```python
import threading

def run_async(coro):
    """在独立线程中运行异步协程，同步等待并返回结果"""
    result = None
    error = None

    def _run():
        nonlocal result, error
        try:
            result = asyncio.run(coro)
        except Exception as e:
            error = e

    t = threading.Thread(target=_run)
    t.start()
    t.join()

    if error:
        raise error
    return result
```

现在为 `MCPClient` 添加同步方法，内部调用 `run_async`：

```python
class MCPClient:
    def __init__(self, config: dict):
        self.servers = config["servers"]

    async def alist_tools(self) -> list:
        """异步：获取所有服务器的工具列表"""
        results = []
        for name, config in self.servers.items():
            async with connect_mcp(config) as session:
                tools = await session.list_tools()
                results.append({
                    "server": name,
                    "tools": tools
                })
        return results

    async def acall_tool(self, server_name: str, tool_name: str, arguments: dict | None = None):
        """异步：调用指定服务器上的工具"""
        config = self.servers[server_name]
        async with connect_mcp(config) as session:
            return await session.call_tool(tool_name, arguments or {})

    def list_tools(self) -> list:
        """同步：获取所有 MCP 服务器的工具列表"""
        return run_async(self.alist_tools()) # type: ignore

    def call_tool(self, server_name: str, tool_name: str, arguments: dict | None = None):
        """同步：调用指定服务器上的工具"""
        return run_async(self.acall_tool(server_name, tool_name, arguments))
```

#### 使用最终封装

##### 发现工具列表

`list_tools()` 返回一个列表，每个元素对应一个 MCP 服务器，包含服务器名称和该服务器的所有工具：

```python
client = MCPClient(mcp)

all_tools = client.list_tools()
for item in all_tools:
    print(f"\n===== {item['server']} =====")
    print(item["tools"].model_dump_json(indent=2, ensure_ascii=False))
```

##### 调用工具

`call_tool()` 接收服务器名称、工具名称和参数，返回工具执行结果：

```python
result = client.call_tool("time", "get_current_time", {"timezone": "Asia/Shanghai"})
print(result.model_dump_json(indent=2, ensure_ascii=False)) # type: ignore
```

```python
result = client.call_tool("microsoft-learn", "microsoft_docs_search", {"query": "Python async"})
print(result.model_dump_json(indent=2, ensure_ascii=False)) # type: ignore
```

## Agent 接入 MCP

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/mcp.png)


to do list:

- `mcp` 独立配置
- 进一步封装描述和工具
- 注册工具
- 修改系统提示词模板和注入

```python
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)
```

```python
agent.session.print_friendly()
```

```python
agent.invoke("当前时间是？")
```

```python
agent.session.save()
```

## 实现MCP服务器

```python
# https://github.com/modelcontextprotocol/python-sdk/tree/v1.28.1
!uv add mcp==1.28.1
```

```python
from mcp.server.fastmcp import FastMCP
```

### 定义MCP服务器

```python
mcp = FastMCP(
    "Weather Service",
    json_response=True,
)
```

### 定义工具函数

```python
# https://www.juhe.cn/ 聚合数据有一些免费API接口，有兴趣的同学自行使用
@mcp.tool()
async def get_weather(city: str = "成都") -> dict[str, str]:
    """Get weather data for a city"""
    return {
        "city": city,
        "temperature": "22",
        "condition": "多云",
        "humidity": "65%",
    }
```

### 运行服务

```python
# mcp库底层使用 starlette + uvicorn 启动 http 服务
mcp.run(transport="streamable-http")
```

```python
# for jupyter

import threading

def run():
    """在独立线程中运行服务器"""
    mcp.run(transport="streamable-http")

t = threading.Thread(target=run)
t.start()
```

### 测试服务

```python
!npx -y @modelcontextprotocol/inspector@1.0.0
```

## SKILL VS MCP

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/skill.png)

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/mcp.png)


Skill 和 MCP 完全是两个东西，它们之所以放到一起讨论，是因为在使用感官上，它们有一些共同点。

### 共同点

#### 标准化

无论是 Skill 还是 MCP，它们都有各自的事实标准。

由于有标准，就容易形成社区和聚合站。我们通过社区或聚合站，能使用到大量现成的 SKILL 和 MCP 工具。

#### 功能体验重叠

以获取某个城市的天气为例，它既可以用Skill来实现，也可以使用 MCP 来实现。

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/agent对比skill.png)


### 差异点

定位差异：MCP 告诉模型谁来做，Skill 告诉模型怎么做

|                      | Skill | MCP                       |
| -------------------- | ----- | ------------------------- |
| 上下文消耗（未命中） | 低    | 高 *可通过渐进式披露解决* |
| 上下文消耗（命中）   | 高    | 低                        |
| 接入成本             | 低    | 高                        |
| 可扩展性             | 高    | 低                        |
| 贡献人群             | 广    | 窄                        |
| 确定性               | 低    | 高                        |
| 通用工具依赖         | 高    | 低                        |
| 越权风险             | 高    | 低                        |

### 最佳实践

MCP 定义底层工具，Skill 定义业务流程

MCP 负责实现底层工具：

- 文件读写
- 命令执行
- 网络搜索
- 接口搜索、调用
- 代码执行
- 其他对确定性、安全性要求高的操作

Skill 负责定义业务流程：

- 机票怎么定，行程怎么规划
- 退货能不能退，怎么退
- 怎么介绍产品
- 怎么成交
- 其他对灵活性、专业性要求高的流程
## 子代理 Sub Agent

考虑这么一种场景，你需要完成一个业务功能开发，并将其暴露为FastAPI的接口，如果让一个Agent单独的去完成，在一个轮次中，它会经历以下流程：

- reasoning：需求分析、方案设计
- 一个超级庞大的ReAct循环
  - 建立ORM数据层
  - 实现数据迁移
  - 执行迁移命令
  - 创建DTO
  - 创建Service
  - 创建接口
  - 创建多个测试脚本
  - 运行测试脚本
  - 解决错误（循环）

你最终会得到一个超级庞大的上下文，这会带来诸多问题，例如：

- ReAct循环往复导致上下文太大，导致skill和tools命中率下降
    - 实际中间某些过程我们只需要结果，主代理不需要ReAct产生的某些上下文，则可使用子代理解决

可以使用子代理来解决这个问题

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/子代理.png)


刚才的例子，更友好的设计是：

- reasoning：仅宏观需求分析、方案设计
- ReAct循环
  - 子代理：实现数据层
  - 子代理：实现DTO
  - 子代理：实现接口
  - 子代理：完成测试
  - 等待所有子代理完成，汇总结果

### 代码实现

#### 实现 tool: create_agent

```python
# 测试
from agent.tool.create_agent import create_agent

resp = create_agent(agent_config=[
    {
        "name": "sub-agent-1",
        "query": "这是一个测试，请说：你好！"
    },
    {
        "name": "sub-agent-2",
        "query": "this is a test, reply: Hello!"
    }
]) 
print(resp)
```

#### 启动子代理

```python
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)
```

```python
agent.invoke("请开启多个子代理，创建两个页面，分别画小猪佩奇和海绵宝宝。")
```

```python
agent.session.save()
```

## Prompt Engeering

https://github.com/dair-ai/Prompt-Engineering-Guide

![image-20260729151654925](https://resource.duyiedu.com/yuanjin/202607291516036.png)

## Context Engeering

> 2025年6月，Shopify的CEO Tobi Lütke 在社交媒体上表示，他更喜欢用“上下文工程”这个词来替代“提示词工程”，因为它更准确地描述了为LLM提供充分信息以完成任务的核心技能

<img src="https://resource.duyiedu.com/yuanjin/202607301034894.png" alt="image-20260730103412811" style="zoom:50%;" />



**上下文唯一的影响着模型的输出质量**

上下文具有**注意力偏差（Attention Bias）**的特点

- **长度稀释**

  上下文越长，注意力就被分散到更多token上，关键信息的权重被摊薄，模型更容易漏掉信息

- 长度**分布外（OOD，Out-of-Distribution）**

  当上下文长度超过训练语料常见长度后，模型回复的置信度会有明显下降

- **信噪比问题**

  噪声信息越多，越会挤占模型对关键信息的注意力预算

- **首尾强化**

  模型对开头（系统提示词）和结尾（最近输入）的关注度天然高于中间（位置偏差/Positional Bias）



上下文工程的关注点：

- **编排**

  提示词、用户问题、工具、MCP、Skill 等内容在上下文中如何排列？什么时间加入什么内容？

- **治理**

  如何确保上下文的内容安全可信？

  如何在持续的循环中，管理和优化不断膨胀的上下文？



<img src="https://resource.duyiedu.com/yuanjin/202607301128877.png" alt="image-20260730112820794" style="zoom:33%;" />

## Harness Engeering

https://mitchellh.com/writing/my-ai-adoption-journey

https://openai.com/index/harness-engineering/

Harness一词，意为马具。

> 马具对骑乘的影响非常大。

原作者的意思是，在任务落地的时候，我们应该把更多的注意力从选择什么马（模型）转移到选择什么样的马具身上（如何驾驭模型）

因此，该词也被翻译为"驾驭工程" / "缰绳工程"

Harness Engineering 的核心关注点：

- **情境与状态管理**

  确保AI在复杂、长周期的任务中，能获得正确的上下文信息，并记住任务状态，避免“失忆”和“跑偏”
  强调 召回 -> 规划 -> 行动

- **护栏**
  
  像给系统设置权限一样，严格管理AI能调用哪些工具、访问哪些数据。核心理念是 最小权限原则 ——只给AI完成当前任务所必须的权限，以防误操作或恶意利用
  
- **可观测**
  
  需要做详细的设计，保证模型知晓是否完成了任务？判断的依据是什么？从哪里获取判断需要的信息？





![Agent model and harness components diagram](https://resource.duyiedu.com/yuanjin/202607301241831.svg)

<img src="https://resource.duyiedu.com/yuanjin/202607301247290.png" alt="image-20260730124725225" style="zoom:33%;" />

## Loop Engeering

https://x.com/addyosmani/status/2064127981161959567

Loop Engineering 关注的是如何让 Agent 自我推动，最终完成一个可交付的产品。

它的实现方式是循环，在循环中：

- 自主发现还未完成的任务
- 驱动多个子代理并行任务，并使用工作树隔离
- 自主沉淀知识
- 自主接入工具
- 不同的子代理分工

<img src="https://resource.duyiedu.com/yuanjin/202607301319760.png" alt="image-20260730131916647" style="zoom: 33%;" />

## Graph Engeering
<img src="https://resource.duyiedu.com/yuanjin/202607301340988.png" alt="image-20260730134041913" style="zoom:50%;" />

# AI 应用框架
## 课程导言

### 为什么需要AI应用框架

- 问题
    - 大模型的接口调用有3种规范，不同的规范调用接口方式不同，我们如何抹平这些差异？
        - 3种规范
            - OpenAI Chat Complition
            - OpenAI Response
            - Anthropic
        - 调用大模型的接口的方式有3种：
            - 直接使用py的request、httpx库
                - 存在的问题？
                    - 请求/响应结构需要手动处理
                        - 不同厂商字段名不同（messages vs input），解析路径各异，容易写错
                    - 流式（SSE）解析要自己实现
                        - 不同厂商格式不统一（Anthropic 的 event 类型完全不同）
                    - 出错重连、断流处理都要自己写
                        - 500/503 → 重试
                        - timeout → 超时重试
                    - 多模态 / 工具调用（tool Calling）组装繁琐
                        - 图片 base64 编码、URL 格式
                        - tool schema 定义、tool_call 结果回传
                        - 各家格式差异大（OpenAI tool_calls vs Anthropic tool_use）
                    -  厂商差异要自己抹平
                        -  想切换 OpenAI / Claude / 通义 / DeepSeek，请求体、鉴权头、响应结构全要改，代码里到处是 if provider == ...
            - 使用OpenAI的SDK、Anthropic的SDK
                - 存在的问题？
                    - 厂商锁定
                        - 切换到 Anthropic 要重写调用代码，SDK 之间不兼容
                    - 版本迭代快，破坏性变更
                        - OpenAI SDK v0.x → v1.x 是完全重写
                        - 升级 SDK 可能大面积改代码
                    - 对国内模型支持弱
                        - 想调用 DeepSeek、Qwen、GLM、本地 vLLM，OpenAI SDK 虽然兼容但部分特性不支持（如特定字段、特殊鉴权）
                        - Anthropic SDK 基本只能调 Claude
            - 使用AI应用框架
                - AI应用框架的出现就是为了解决上面存在的问题
                    - 统一抽象：ChatOpenAI / ChatAnthropic 同一接口
                    - 流式/工具/多模态统一封装
                    - 重试、限流、fallback 内置
                    - 可观测性（LangSmith 等）
                    - 多模型路由、负载均衡

### 学习顺序调整

<img src="https://resource.duyiedu.com/yuanjin/202607301431254.png" alt="image-20260730143144179" style="zoom:50%;" />

### langchain全家桶

<img src="https://resource.duyiedu.com/yuanjin/202608052258029.png" alt="image-20260805225830903" style="zoom:50%;" />

- langchain-core: 底层数据结构约束
- langgraph：流程引擎
- langchain：模型能力
- deepagent：Agent范式

### 资料交付方式调整

获取每节课资料的方式见根目录下的 `README.md`
## langgraph 核心概念

### 安装

```python
!uv add langgraph=="1.2.10"
```

### 第一个 langgraph 程序

```python
from langgraph_python.graph.my_first_graph import workflow

graph = workflow.compile()

graph.invoke({})
```

```python
from langchain_core.runnables import Runnable
print(isinstance(graph, Runnable))
```

### 核心概念

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/图.png)


#### 三个阶段

定义 -> 编译 -> 运行

1. **定义**

   - 节点
       - 可变化、可被调用的对象
       - 节点的输入是最新的图状态，输出是改变图状态
   - 边
       - 表达了上一个节点运行完成，我去哪儿运行下一个节点
   - 图状态结构

2. **编译**

   定义好的图是不可运行的，它只是一个描述。

   若要运行图，需要进行编译

   编译好的图，节点和边会固定下来，不能动态变化。

3. **运行**

   编译结果可以运行。

   > langgraph 底层使用 Pregel 系统运行图
   >
   > Pregel来自2010年的谷歌论文，论文中详细阐述了图的执行。
   >
   > https://dl.acm.org/doi/10.1145/1807167.1807184

4. **执行过程数据变化**

- 初始状态：图状态值都为空（str类型：则对象不存在该字段，int类型：为0，其他对象类型：都是空值（例如空数组））
- start节点后，图状态的值变成执行（invoke函数的参数）后的值
- 依次运行节点，更新图状态

#### 节点

节点可以接收以下类型：
- 可调用对象：实现了`__call__`的对象
- Runnable对象：`Runnable`是`langchain_core`中定义的类型

```python
from langchain_core.runnables import Runnable

print(hasattr(Runnable, "invoke"))      # 执行
print(hasattr(Runnable, "ainvoke"))     # 异步执行
print(hasattr(Runnable, "stream"))      # 流式执行
print(hasattr(Runnable, "astream"))     # 异步流式执行
print(hasattr(Runnable, "batch"))       # 批量执行
print(hasattr(Runnable, "abatch"))      # 异步批量执行
```

#### 图状态

图状态是整张图的共享数据空间，图在执行期间，每个节点都可以获取到完整的图状态，也可以更新图状态。

图执行完后，得到的结果就是最新的图状态。

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/图状态.png)


图状态本质上是一个字典，字典的每一个字段称之为 channel （通道）

## 环境搭建

### 供应商选择

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/供应商.png)


|                     | 推理成本               | 开发成本（指模型调用接口能力，需考虑模型本身能力） | 运维成本（指统计模型调用次数等等） | 服务器成本 | 适用                   |
| ------------------- | ---------------------- | -------- | -------- | ---------- | ---------------------- |
| 聚合商              | 自有模型低，三方模型高 | 低       | 低       | 无         | 中小型企业             |
| 源头厂商 + 自建网关 | 低                     | 低       | 低       | 高         | 大中型企业             |
| 源头厂商 无网关     | 低                     | 中       | 高       | 无         | 学习<br />快速原型迭代 |

任务：
1. 完成阿里百炼平台的`API-KEY`申请
2. 配置环境变量

```python
!uv add pydantic-settings==2.14.1
```

```python
# 读取环境变量
from langgraph_python.core.config import anthropic_settings, openai_settings
```

```python
openai_settings
```

```python
anthropic_settings
```

### 监控/评测平台

https://smith.langchain.com/

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/监控平台.png)

## 模型 Model（langchina框架的）

langchain官网：https://docs.langchain.com/oss/python/langchain/agents

### Model解决了什么问题
model 是 LangChain 的核心组件，它抽象了不同模型的调用差异，对外提供统一外观
![image](https://raw.githubusercontent.com/JJ-front/store-img/master/langChina理解.png)

处理流程：

- langchina代码 -> 找到对应的模型提供方（Provider） -> 服务器（聚合商网关/自建网关/服务商官方网关） -> 大模型

### 创建模型

```python
!uv add langchain==1.3.14 
!uv add langchain-openai==1.4.1
!uv add langchain-anthropic==1.5.3
```

```python
from langgraph_python.core.config import openai_settings, anthropic_settings
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model_provider="anthropic",
    model=anthropic_settings.default_model
)
```

```python
response = await model.ainvoke("你好")
```

```python
print(f"返回类型：{type(response)}")
print(f"回复文本：{response.text}")
print(f"工具调用：{response.tool_calls}")
print(f"响应块：{response.content_blocks}")
print(f"额外信息：{response.additional_kwargs}")
print(f"token消耗：{response.usage_metadata}")
```

### OpenAI接口的问题

-  OpenAI的Provider把模型相应的思维链丢了
    - 为啥？
        - OpenAI 官方接口标准中，不暴露思维链（模型思考过程）  

目前社区的解决办法：

- 自定义 Provider
- 使用 Anthropic 接口
- 换其他第三方的集成（例如 OpenRouter）
- 抛弃 `langchain` 的 `model`，通过 `OpenAI SDK` 自行封装

### 流式传输

```python
chunks = model.astream("你好")
async for chunk in chunks:
    for block in chunk.content_blocks:
        print(block)
```

### 消息

```python
from langchain.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage

# user、system、assistant、tool

messages = [
    SystemMessage("请使用猪八戒的语气回复"), # role:system
    HumanMessage("你好，呆子") # role:user
]

response = await model.ainvoke(messages) # 返回AIMessage
```

### 多轮对话

```python
messages.append(response)
messages.append(HumanMessage("想挨棍子了？"))
```

```python
messages
```

```python
response = await model.ainvoke(messages)
```

### 工具

```python
from langchain.tools import tool

# 定义工具
@tool
def get_weather(location: str) -> str:
    """
    获取天气

    参数：
    - location: 城市名称
    """
    return f"It's sunny in {location}."

# 绑定工具
model_with_tools = model.bind_tools([get_weather])

response = await model_with_tools.ainvoke("伦敦的天气如何？")
```

```python
from langchain_core.runnables import Runnable
```

```python
print(isinstance(get_weather, Runnable))
print(isinstance(model, Runnable))
```


## 消息（langchina框架的）
![image](https://raw.githubusercontent.com/JJ-front/store-img/master/消息.png)
### 补充一个小技巧

1. 快捷键 `Ctrl+,`（Windows/Linux）/ `Cmd+,`（Mac）打开设置

2. 搜索框输入：`files.exclude`

3. 点击**添加模式**，填入：

    ```
    **/__pycache__
    **/__init__.py
    **/py.typed
    ```

安装插件：Toggle Excluded Files


### 消息类型
```python
from langgraph_python.core.create_model import create_model

model = create_model()
```
```python
from langchain.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage

messages = [
    SystemMessage("你是一个智能天气助手。"),
    HumanMessage("你好！请问今天成都的天气怎么样？我下午想去公园散步。"),
    AIMessage(
        content="",
        content_blocks=[{
            "type": "reasoning",
            "reasoning": "我需要调用get_weather工具获取准确的天气数据。"
        }],
        tool_calls=[{
            "id": "call_123456",
            "name": "get_weather",
            "args": {
                "city": "成都"
            }
        }]
    ),
    ToolMessage(
        content="成都今天是晴天，气温 25°C",
        tool_call_id="call_123456"  # 必须与AI消息中的tool_calls id匹配
    )
]
await model.ainvoke(messages)
```

```python
# 所有的消息都继承自 BaseMessage
from langchain.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langchain_core.messages import BaseMessage

print(
    issubclass(SystemMessage, BaseMessage),
    issubclass(HumanMessage, BaseMessage),
    issubclass(AIMessage, BaseMessage),
    issubclass(ToolMessage, BaseMessage),
)
```

### 消息格式

#### 纯文本消息

略

#### 图片消息

```python
# 通过 URL 或 base64 编码的图片数据来发送图片消息
url1="https://fastly.picsum.photos/id/57/800/600.jpg?hmac=Geuc5OABDrI_1EI9yvAjSWKQpjo0S6g9Y5mB9JxI4r8"
url2="https://fastly.picsum.photos/id/58/800/600.jpg?hmac=yQHfIMWMXYg4f264WBOGMBWTYbv6NqTJMVz7r67kN3w"
messages = [
    # 一个HumanMessage可以有多个content_block
    HumanMessage([
        {"type": "text", "text": "比较这两张图片风格的差异"},
        {"type": "image", "url": url1},
        {"type": "image", "url": url2}
        # {"type": "image", "base64": "...", "mine_type": "image/png"}  
    ])
]
await model.ainvoke(messages)
```

#### 音频消息

注意：需要模型支持ASR能力，否则会报错。本节的示例使用支持ASR的模型。

> 百炼平台没有免费的ASR模型，注意运行期间会产生费用

```python

import base64
with open("./assets/audio/test.mp3", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode()
data_url = f"data:audio/mpeg;base64,{audio_base64}"

asr_model = create_model(
    model_name="qwen3.5-omni-plus",
    provider="openai_reasoning"
)

messages = [
    HumanMessage([
        {"type": "text", "text": "请告诉我这段音频的内容"},
        {"type": "audio", "base64": data_url, "mime_type": "audio/mpeg"}
    ])
]

await asr_model.ainvoke(messages)
```

#### 更多消息格式

其他消息格式需要模型、模型服务商和提供程序的支持

https://docs.langchain.com/oss/python/langchain/messages#content-block-reference

### 消息模板
- 支持的消息模板
    - f-string
    - jinja2(官方不推荐，容易产生注入攻击)
    - mustache（官方推荐）


mustache语法实例：
```python
from langchain_core.utils.mustache import render

result = render(
    template="Hello {{name}}, you have {{count}} messages", 
    data={"name": "世界", "count": 3}
)

print(result)   # Hello 世界, you have 3 messages
```

```python
# 使用封装
from langgraph_python.template import prompt_from_filename

prompt_from_filename(
    filename="system",
    data={"cwd":"/yuanjin", "os":"mac", "is_git": True}
)
```

## Reducer

### Reducer 的本质

Reducer 在 Python 中表达为一个函数，它规定了两个数据（前一个、后一个）如何合并为一个新数据。

```python
# 通过相加合并
def add(a, b):
    return a + b

# 始终使用新数据覆盖旧数据
def overwrite(a, b):
    return b
```

```python
print(add(1, 2))
print(add([1,2], [3,4]))
print(add("a", "b"))
```

```python
import operator # 使用 python 自带的 operator 模块

print(operator.add(1, 2))
print(operator.add([1,2], [3,4]))
print(operator.add("a", "b"))
```

### State 中的 Reducer

在 LangGraph 中，状态中的每一个通道都会对应到一个 Reducer，如果没有指定，它会默认使用覆盖 Reducer。

在 LangGraph 中，它要求 Reducer 的返回类型要保持一致。

```python
from typing import List, Annotated, TypedDict, NotRequired
import operator

class MyState(TypedDict):

    # 覆盖 reducer
    covered: NotRequired[str]
    
    # 追加 reducer
    append_list: NotRequired[Annotated[List[str], operator.add]]

    # 保留最大值的 reducer
    high_score: NotRequired[Annotated[int, lambda a,b:max(a,b)]]
```

```python
# 测试

def node1(state: MyState):
    print("进入node1的状态：", state)
    return {
        "covered": "node1 result", 
        "append_list": ["node1 result"],
        "high_score": 5
    }

def node2(state: MyState):
    print("进入node2的状态：", state)
    return {
        "covered": "node2 result", 
        "append_list": ["node2 result"],
        "high_score": 3
    }

from langgraph.graph import StateGraph, START, END

# 创建图
workflow = StateGraph(MyState)
(
    workflow.add_node(node1)
    .add_node(node2)
    .add_edge(START, "node1")
    .add_edge("node1", "node2")
    .add_edge("node2", END)
)

# 编译图
graph = workflow.compile()

# 执行
await graph.ainvoke({})
```

### 内置的Reducer: add_messages

```python
from langchain.messages import SystemMessage, HumanMessage, AIMessage
messages = [
    SystemMessage("系统消息", id=1),
    HumanMessage("用户消息1", id=2)
]
```

```python
from langgraph.graph.message import add_messages


messages = add_messages(messages, [
    AIMessage("AI回复1", id=3),
    HumanMessage("用户消息2", id=4)
])
messages
```

```python
messages = add_messages(messages, AIMessage("AI回复2", id=5))
messages
```

```python
messages = add_messages(messages, AIMessage("AI回复1-改", id=3))
messages
```

### 工程推进

#### 目录结构

```yaml
langgraph_python
├── 📁 core          # 核心功能：模型、核心配置
├── 📁 graphs        # 各种图
├── 📁 nodes         # 节点
├── 📁 states        # 图状态声明
├── 📁 templates     # 提示词模板
```

#### 图结构

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/图结构.png)


#### 测试

```python
from langgraph_python.graphs.core_agent_graph import build_graph

graph = build_graph().compile()

await graph.ainvoke({
    "messages":[
        HumanMessage("你好")
    ]
})
```

## Agent Server

Agent Server 可以帮你搞定 API 接口和数据持久化

### 安装 LangGraph CLI

```bash
uv add "langgraph-cli[inmem]==0.4.31"
```

验证是否安装成功：

```bash
langgraph --version
```

### 配置文件

见 `langgraph.json`

### 启动服务

在工程根目录执行：

```bash
langgraph dev
```

启动后，可以通过以下地址访问：http://127.0.0.1:2024/docs

### 使用 Studio

https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024

浏览器打开上面的 Studio 地址，即可在可视化界面中与 Agent 对话、查看图结构和运行轨迹。

### 使用 Agent Chat

打开 <https://agentchat.vercel.app/>，填入本地服务地址 `http://127.0.0.1:2024` 和图 ID（本工程的图 ID 为 `agent`），即可在网页上直接与 Agent 聊天。

## 超步

Pregel 中有一个算法叫做 BSP （Bulk Synchronous Parallel，整体同步并行计算模型）

超步是 BSP 并行计算中的一个基本计算迭代单元。

一个完整的 BSP 程序就是由一系列串行执行的超步组成的

注意：超步是一个运行时概念，而非编译时

## 线程和检查点

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/线程和检查点.png)


- **检查点 checkpointer**

  位置：图的start节点前后及超步之后。

  作用：记录图的当前状态。

  持久化：需要在图编译时指定持久化方式。支持 memory、postgres、sqllite、自定义

- **线程 thread**

  一个图在哪个线程上运行？可以在图运行时指定线程ID。

- **Turn/Run**

  在某个线程上，一个图从开始执行到结束，就称之为一个turn或一个run。



图在线程上执行，每个线程可以有多个run，每个run涉及到多个检查点，检查点出现在起始节点和超步之后，每个超步包含多个节点。

```python
from langgraph_python.graphs.core_agent_graph import build_graph
from langgraph.checkpoint.memory import InMemorySaver

# 编译时指定检查点的持久化器
graph = build_graph().compile(checkpointer=InMemorySaver())
```

```python
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

config:RunnableConfig = {
    "configurable":{
        "thread_id": "chat 1"
    }
}

await graph.ainvoke(
    input={
        "messages": [
            HumanMessage("你好，我叫袁霸天")
        ]
    },
    config=config
)
```

```python
await graph.ainvoke(
    input={
        "messages": [
            HumanMessage("你知道我是谁吗？")
        ]
    },
    config=config
)
```

```python
await graph.ainvoke(
    input={
        "messages": [
            HumanMessage("你能做什么？")
        ]
    },
    config=config
)
```

```python
latest = graph.get_state(config)
latest
```

```python
history = graph.get_state_history(config)
history = [h for h in history]
history
```

在 Agent Server 中：

- **不能为检查点指定存储器**

  Agent Server 会自动注入存储器，你仅需管理 Agent Server 即可

- **API中已包含对Thread、Checkpointer、Run的管理**

  将来会讲解API
  
## 工具节点

### 定义工具

```python
from langchain.tools import tool

# tool 装饰器会将函数转换为 Runnable

@tool
def get_weather(city: str):
    """
    获取某个城市的天气，返回的温度为摄氏度

    参数：
    - city: 城市名称
    """
    return {
        "city_name":"beijing",
        "temperature": 25,
        "weather": "cloudy"
    }
```

```python
get_weather.tool_call_schema.model_json_schema() # type: ignore
```

```python
get_weather.invoke({
    "city":"北京"
})
```

```python
!uv add pydantic==2.13.4
```

```python
from pydantic import BaseModel, Field

class WeatherInput(BaseModel):
    """查询天气的输入参数"""
    city: str = Field(description="城市名称")

@tool(args_schema=WeatherInput)
def get_weather(city: str):
    """获取某个城市的天气，返回的温度为摄氏度"""
    return {
        "city_name":"beijing",
        "temperature": 25,
        "weather": "cloudy"
    }
```

```python
!uv add tavily-python==0.7.26
```

```python
from langgraph_python.tools.web import web_search, fetch_url
```

```python
await web_search.ainvoke({
    "query": "黄金价格"
})
```

```python
await fetch_url.ainvoke({
    "urls":["https://cn.tradingview.com/symbols/XAUUSD"]
})
```

### 定义工具节点

见工程代码

## Mock Model

某些场景的测试需要使用模拟的模型，比如：报错、死循环、工具调用错误、...

### langchain_core 中的模拟模型

| 模拟模型 | 用途 |
| --- | --- |
| `FakeChatModel` | 最简单的模拟聊天模型，无论输入什么消息，都固定返回 `fake response` 字符串，用于最基本的单元测试 |
| `FakeListChatModel` | 模拟聊天模型，内部维护一个字符串列表 `responses`，每次调用依次（循环）返回列表中的一条作为回复，也支持流式输出 |
| `FakeMessagesListChatModel` | 模拟聊天模型，内部维护一个 `BaseMessage` 列表 `responses`，每次调用依次（循环）返回列表中的一条消息，可以返回带工具调用等结构的消息 |
| `GenericFakeChatModel` | 通用模拟聊天模型，接收一个消息迭代器 `messages`，每次调用取出一条（`AIMessage` 或字符串）作为回复，支持同步、异步与流式测试 |
| `ParrotFakeChatModel` | 鹦鹉学舌式模拟聊天模型，会把输入消息列表中的最后一条消息原样返回，用于测试消息回显逻辑 |
| `FakeListLLM` | 模拟普通 LLM（文本补全模型），内部维护一个字符串列表 `responses`，每次调用依次（循环）返回一条，用于非聊天类模型的测试 |
| `FakeStreamingListLLM` | 模拟支持流式输出的 LLM，继承自 `FakeListLLM`，除了依次返回列表中的回复外，还支持按流式块返回，并可模拟在指定块位置抛错 |

### 使用封装好的 mock model

- `mock_model`: `core/mock_model.py`
- `mock_model 配置`: `core/mock_model.config.jonc`

```python
from langgraph_python.core.mock_model import mock_model
from langchain.messages import HumanMessage, AIMessage, ToolMessage

model  = mock_model()
```

```python
await model.ainvoke([
    HumanMessage("你好！"),
    ToolMessage(content="当前时间:xxxx", tool_call_id="ab")
])
```

```python
chunks = model.astream([
    HumanMessage("你好!")
])
async for chunk in chunks:
    for block in chunk.content_blocks:
        print(block)
```

## 部署模式
![image](https://raw.githubusercontent.com/JJ-front/store-img/master/部署模式.png)


|             | Agent Server 模式                  | 手动模式                    |
| ----------- | ---------------------------------- | --------------------------- |
| compile配置 | 除 checkpointer 外，其他需要配置   | 全部需要                    |
| invoke配置  | 不需要                             | 全部需要                    |
| invoke之后  | 不需要                             | 全部需要                    |
| 学习        | 核心概念<br />Agent Server API接口 | 核心概念<br />langgraph API |

在 Agent Server 模式中，你只需要做两件事：

1. 建立编译好的图结构

2. 看懂`Agent Server API`

## 模型配置的动态切换

### 操作步骤

- 在创建模型时，配置可动态切换的字段名
- 在运行时，可以注入新的配置从而更改
    - 任意runnable的所有方法都有一个config参数，可以动态修改模型参数

```python
from langgraph_python.core.config import anthropic_settings
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

# 创建模型时，可以指定哪些字段可以在运行时重新配置
model = init_chat_model(
    model_provider="anthropic",
    model=anthropic_settings.default_model,
    configurable_fields=[
        "model", 
        "temperature",
        "top_p",
        "thinking"
    ]
)
```

```python
from langchain_core.callbacks import BaseCallbackHandler


class ConfigPrinter(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        params = kwargs["invocation_params"]
        print("本次调用使用的模型配置：")
        print(f"  Model:       {params.get('model')}")
        print(f"  Temperature: {params.get('temperature')}")
        print(f"  Top P:       {params.get('top_p')}")
        print(f"  Thinking:    {params.get('thinking')}")
        print(f"  Top K:       {params.get('top_k')}")


await model.ainvoke(
    input=[HumanMessage("你好")],
    config={
        "callbacks": [ConfigPrinter()]
    }
)
```

```python
await model.ainvoke(
    [HumanMessage("你好")],
    config={
        "configurable": {
            "model": "qwen3.7-max",
            "temperature": 0.5,
            "top_p": 0.9,
            "thinking": {"type": "disabled"},
            "top_k": 50,
        },
        "callbacks": [ConfigPrinter()],
    }
)
```

```python
from langgraph_python.graphs.core_agent_graph import build_graph

graph = build_graph().compile()

await graph.ainvoke(
    input={
        "messages": [HumanMessage("你好")]
    },
    config={
        "configurable": {
            "model": "qwen3.7-max",
            "temperature": 0.5,
            "top_p": 0.9,
            "thinking": {"type": "disabled"},
            "top_k": 50,
        },
        "callbacks": [ConfigPrinter()],
    }
)
```

## RunnableConfig

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/RunnableConfig.png)


### 注入和读取配置

```python
from typing_extensions import TypedDict
from langchain_core.runnables import RunnableConfig, ensure_config
from langgraph.graph import StateGraph


class State(TypedDict):
    pass


# 第一个节点：通过依赖注入读取 RunnableConfig
def node_di(state, config: RunnableConfig):
    return {}


# 第二个节点：通过 ensure_config 读取 RunnableConfig
def node_ensure(state):
    config = ensure_config()
    return {}


builder = StateGraph(State)
builder.add_node(node_di)
builder.add_node(node_ensure)
builder.set_entry_point("node_di")
builder.add_edge("node_di", "node_ensure")
builder.set_finish_point("node_ensure")

graph = builder.compile()

await graph.ainvoke(
    input={}, 
    config={
        "configurable": {
            "a": "1"
        }
    }
)
```

### 动态改变模型配置

- 其他功能上节课已完成
- 修改`call_model`节点，当模型名称为`fake`时，使用`mock_model`

```python
from langgraph_python.graphs.core_agent_graph import build_graph
from langchain.messages import HumanMessage

graph = build_graph().compile()
```

```python
await graph.ainvoke(
    input={
        "messages": [HumanMessage("你好，你是谁？")]
    },
    config={
        "configurable": {
            "model": "fake"
        }
    }
)
```

### 动态决定系统提示词

1. 去掉系统提示词模板
2. 去掉图状态中的系统提示词
3. `call_model`节点需要动态读取系统提示词配置

```python
await graph.ainvoke(
    input={
        "messages": [HumanMessage("你好，你是谁？")]
    },
    config={
        "configurable": {
            "system_prompt": "你是一个金融分析师"
        }
    }
)
```

### 动态决定工具列表

1. 修改`tools/__init__.py`，支持按照字符串列表返回工具列表
2. 修改`call_model`节点，根据配置的工具列表绑定工具

```python
await graph.ainvoke(
    input={
        "messages": [HumanMessage("你绑定了哪些工具？")]
    },
    config={
        "configurable": {
            "tools": ["get_current_time"]
        }
    }
)
```

### 其他预设配置

| 字段 | 作用 |
| --- | --- |
| `configurable` | 用户自定义任意键值 |
| `configurable.thread_id` | 线程id |
| `configurable.max_concurrency` | 一个超步中并行任务数上限（默认10） |
| `recursion_limit` | 单次run的超步上限（默认 1000） |
| `tags` | 给这次运行打标签，用于追踪/过滤 |
| `metadata` | 自定义元数据（LangSmith 追踪用） |
| `callbacks` | 回调处理器（监听事件、自定义追踪） |
| `run_name` | 给运行命名 |
| `run_id` | 手动指定运行 ID |

```python
await graph.ainvoke(
    input={
        "messages": [HumanMessage("现在什么时间")]
    },
    config={
        "configurable": {
            "model":"fake",
            "system_prompt":"你是一名金融分析师"
        },
        "recursion_limit": 3,
        "tags": ["金融分析", "fake model"],
        "metadata": {
            "app_version": "0.0.1",
            "env": "dev"
        },
        "run_name": "金融Agent"
    }
)
```

## Runtime

`LangGraph`提供了两种注入自定义配置的渠道：

1. 通过`config.configurable`注入，通过`config.configurable`读取
2. 通过`context`注入，通过`runtime.context`读取

目前的情况是：

- `LangGraph`官方建议使用`context`进行自定义配置
- `config.configurable`仅用于配置线程id
- `LangGraph`仍然支持两种自定义配置的方式
- 如果使用`Agent Server`，两者不能混用，建议使用`context`

最佳实践 —— 用一个就行，别两个一起用：
- 新项目一律使用`context`
- 旧项目用的是哪个，就继续用哪个，不要混

### 注入和使用 Context

```python
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langgraph.runtime import Runtime, get_runtime
from langgraph.config import get_config
from langgraph.graph import END, START, StateGraph


# 1. 定义 ContextSchema：本次运行允许传入哪些配置（必须有默认值或必传字段）
class ContextSchema(BaseModel):
    user_id: str = Field(description="用户id")
    locale: str = Field(description="语言偏好", default="zh-CN")



# 2. 定义图状态
class State(TypedDict):
    pass

# 3. 在节点中读取 Context
def greet(state: State, runtime: Runtime[ContextSchema]):
    user_id = runtime.context.user_id
    locale = runtime.context.locale
    runtime = get_runtime()
    config = get_config()
    return {}

# 4. 创建图时传入 context_schema
builder = StateGraph(State, context_schema=ContextSchema)
builder.add_node(greet)
builder.add_edge(START, "greet")
builder.add_edge("greet", END)

graph = builder.compile()

# 5. 调用时传入 context
await graph.ainvoke(
    input={},
    context=ContextSchema(user_id="张三"),
)
```

### 修改自定义配置为 context

- 在`states/core_agent_state.py`中添加`ContextSchema`
- 在`graphs/core_agent_graph.py`中注入`context_schema`
- 在`call_model`中消费`context`

```python
from langgraph_python.graphs.core_agent_graph import build_graph
from langchain.messages import HumanMessage

graph = build_graph().compile()
```

```python
from langgraph_python.states.core_agent_state import ContextSchema

await graph.ainvoke(
    input={
        "messages": [HumanMessage("你好，你是谁？")]
    },
    context=ContextSchema(model="fake"),
)
```

### 核心理解

Assistants = 图 + 配置

## Assistant API

可以通过`Agent Server`暴露的`Assistant API`管理AI助手

API文档地址：http://localhost:2024/docs#tag/assistants

API调用：推荐 `langgraph_sdk`

### 安装 LangGraph SDK

本课件使用 `langgraph-sdk` 访问 Assistant API，先通过 UV 安装：

```python
!uv add langgraph-sdk==0.4.2
```

### 创建客户端

连接本地 Agent Server（默认端口 2024），获得 `client.assistants` 子客户端：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

### 创建 Assistant

> POST /assistants

创建时会为该 Assistant 生成初始版本（version=1）。

```python
# 为 agent 图创建 Assistant
# - context：静态上下文，会注入到图的 Runtime 中
# - metadata：附加元数据，可用于后续搜索过滤
assistant = await client.assistants.create(
    graph_id="agent",
    name="假模型", # 取一个直观的名称，用户友好，无功能含义
    description="最多允许运行10个超步", # 描述，无功能含义
    context={"model": "fake"},
    config={
        "recursion_limit": 10
    }
)
assistant
```

保存 Assistant ID 供后续接口使用：

```python
assistant_id = assistant["assistant_id"]
assistant_id
```

### 获取 Assistant

> GET /assistants/{assistant_id}

通过 ID 获取 Assistant 的详细信息：

```python
assistant = await client.assistants.get(assistant_id)
assistant
```

### 更新 Assistant

> PATCH /assistants/{assistant_id}

更新 Assistant 的名称、描述、配置等。更新后会生成一个新版本，并将其设为最新版本。

```python
assistant_v2 = await client.assistants.update(
    assistant_id,
    description="最多允许20个超步",
    config={
        "recursion_limit":20
    }
)
assistant_v2
```

### 获取 Assistant 版本列表

> POST /assistants/{assistant_id}/versions

列出 Assistant 的全部历史版本：

```python
versions = await client.assistants.get_versions(assistant_id)
versions
```

### 设置最新版本

> POST /assistants/{assistant_id}/latest

将某个历史版本设为最新版本，用于版本回滚：

```python
# 回滚到版本 1
assistant = await client.assistants.set_latest(assistant_id, version=1)
print(f"当前最新版本: {assistant['version']}, 名称: {assistant['name']}")
```

### 搜索 Assistant

> POST /assistants/search

按名称、graph_id、metadata 过滤，支持分页与排序。该接口同样用于列出全部 Assistant。

```python
# 按名称模糊搜索（不区分大小写的子串匹配）
result = await client.assistants.search(
    graph_id="agent",
    limit=10,
)
result
```

使用 `select` 可指定返回字段：

```python
result = await client.assistants.search(
    limit=2,
    offset=0,
    sort_by="created_at",
    sort_order="desc",
    select=["assistant_id", "name", "created_at"]
)
result
```

### 统计 Assistant 数量

> POST /assistants/count

按条件统计 Assistant 数量：

```python
count = await client.assistants.count()
print(f"数量: {count}")
```

### 获取 Assistant 图结构

> GET /assistants/{assistant_id}/graph

获取 Assistant 对应的图结构（节点、边）。

```python
graph = await client.assistants.get_graph(assistant_id)
print("节点：", [n for n in graph["nodes"]])
print("边：", [e for e in graph["edges"]])
```

### 获取 Assistant Schema

> GET /assistants/{assistant_id}/schemas

获取图输入、输出、状态、配置和上下文的 JSON Schema：

```python
schema = await client.assistants.get_schemas(assistant_id)
schema
```

### 删除 Assistant

> DELETE /assistants/{assistant_id}

删除 Assistant，其所有版本也会一并删除。删除后再次查询会抛出 `NotFoundError`：

```python
from langgraph_sdk.errors import NotFoundError

await client.assistants.delete(assistant_id)

try:
    await client.assistants.get(assistant_id)
except NotFoundError as e:
    print("已删除：", e)
```

## 子图

### 子图的两种通信模式

![子图模式](https://resource.duyiedu.com/yuanjin/202608111244714.svg)

### 子图持久化模式

子图会自动继承父图的检查点的存储方式，因此**子图不需要配置检查点的存储方式**。

但是你可以控制子图检查点的持久化行为。

```python
# 持久化行为取值: None | True | False
sub_graph.compile(checkpointer=持久化行为取值)
```



| 模式                                                         | `checkpointer=` | 行为                                                         |
| :----------------------------------------------------------- | :-------------- | :----------------------------------------------------------- |
| [每次调用](https://docs.langchain.com/oss/python/langgraph/use-subgraphs#per-invocation-default) | `None` （默认） | 每次调用都会重新开始，并继承父级的检查点器，以支持在单次调用中的中断和持久执行。 |
| [每线程](https://docs.langchain.com/oss/python/langgraph/use-subgraphs#per-thread) | `True`          | 状态在同一线程上的调用之间累积。每次调用都会从上次停止的地方继续。 |
| [无状态](https://docs.langchain.com/oss/python/langgraph/use-subgraphs#stateless) | `False`         | 完全没有检查点机制——运行起来就像普通的函数调用一样。没有中断或持久化执行。 |

### 子Agent模式

1. 不同的子Agent使用同一张图的不同配置
2. 提供调用子Agent的工具即可
3. 通信模式：节点内调用
4. 持久化模式：None

## Thread API

可以通过 `Agent Server` 暴露的 `Thread API` 管理线程（图的持久化状态）

API文档地址：http://localhost:2024/docs#tag/threads

API调用：推荐 `langgraph_sdk`

本节先补充上节课遗漏的"子图"接口，再讲解 Thread 接口。

### 安装 LangGraph SDK

上一节课已经安装过 `langgraph-sdk`，这里重复执行也无副作用，仅保证课件可独立运行：

```python
!uv add langgraph-sdk==0.4.2
```

### 创建客户端

连接本地 Agent Server（默认端口 2024），获得 `client.threads` 子客户端：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

### 补充：获取子图

> GET /assistants/{assistant_id}/subgraphs
>
> GET /assistants/{assistant_id}/subgraphs/{namespace}

子图接口返回的是图中**结构化定义**的子图节点。当前注册的 `agent` 图没有结构化子图（其子 Agent 是通过工具动态调用编译的子图，不算结构化子图），因此返回空对象。

先获取一个已有 Assistant 的 ID：

```python
# 获取一个已有的 agent Assistant
assistants = await client.assistants.search(graph_id="agent", limit=1)
assistant_id = assistants[0]["assistant_id"]
assistant_id
```

```python
# 当前图没有结构化子图，返回空对象
subgraphs = await client.assistants.get_subgraphs(assistant_id)
subgraphs
```

```python
# 按命名空间查询子图，同样为空
subgraphs = await client.assistants.get_subgraphs(assistant_id, namespace="child:graph")
subgraphs
```

### 创建线程

> POST /threads

创建线程时可附带元数据，并通过 `graph_id` 关联图：

```python
# 创建线程
# metadata：附加元数据，可用于后续搜索过滤
thread = await client.threads.create(
    metadata={
        "title": "新会话",
        "user_id": "007",
        "graph_id": "agent",
    },
)
thread
```

极少用的字段说明（需要时查询）：

- ttl（Time-To-Live）: 可以控制线程存活周期，比如1个月后自动清理线程数据
- supersteps：在初始化线程时，可以直接传递每一个检查点的状态

保存 Thread ID 供后续接口使用：

```python
thread_id = thread["thread_id"]
thread_id
```

### 获取线程

> GET /threads/{thread_id}

通过 ID 获取线程的详细信息：

```python
thread = await client.threads.get(thread_id)
thread
```

返回字段说明：

- state_updated_at：线程状态最近更新时间（每次运行产生新检查点时变化）
- status：线程状态，如 idle（空闲）/ busy（执行中）/ interrupted（中断）/ error（出错）
- config：最新运行使用的配置，来自 assistant 的 config
- values：线程当前的图状态值（如消息列表），未运行过时为 None

### 更新线程

> PATCH /threads/{thread_id}

更新线程的元数据（`metadata`）等字段，新的元数据会与已有元数据合并：

```python
thread_v2 = await client.threads.update(
    thread_id,
    metadata={"title": "langgraph_sdk的使用方法"},
)
thread_v2
```

返回字段与「获取线程」一致，区别在于其 `metadata` 已与传入的新元数据合并（旧的 `title`、`graph_id` 等会保留）。

### 搜索线程

> POST /threads/search

按 `metadata`、`values`、`status` 等过滤，支持分页与排序。该接口同样用于列出全部线程：

```python
# 按 metadata 过滤
result = await client.threads.search(
    metadata={"user_id": "007"},
    limit=10,
)
result
```

```python
# 使用 select 指定返回字段，并按创建时间倒序
result = await client.threads.search(
    limit=5,
    offset=0,
    sort_by="created_at",
    sort_order="desc",
    select=["thread_id", "status", "created_at"],
)
result
```

返回的是线程对象列表，每个元素的字段与「获取线程」返回的结构一致；若指定了 `select`，则只返回选中的字段。

### 统计线程数量

> POST /threads/count

按条件统计线程数量：

```python
count = await client.threads.count()
print(f"线程数量: {count}")
```

### 复制线程

> POST /threads/{thread_id}/copy

复制线程会**连同状态和检查点一起复制**，得到一个新的线程。

下面从服务器上已有的、有运行记录的线程复制一份，得到的线程自带状态数据，正好用于接下来的"状态与历史"演示：

```python
source_id = "019fef6f-fc1f-72b2-a824-98a9c8fc4cda"
# 复制线程（连同状态与检查点一起复制）
copy_thread = await client.threads.copy(source_id)
copy_thread_id = copy_thread["thread_id"] # type: ignore
copy_thread_id
```

返回一个新的线程对象，字段与「获取线程」一致，`thread_id` 为新生成（旧线程不受影响）。

### 获取线程状态

> GET /threads/{thread_id}/state

获取线程的最新状态（即最新检查点的状态）。这里用上面复制出的线程演示（它自带状态数据）：

```python
state = await client.threads.get_state(copy_thread_id)
import json
print(json.dumps(state, indent=2, ensure_ascii=False))
```

返回字段说明：

- values：图的最新状态（如消息列表 messages）
- next：下一步要执行的节点列表；空列表表示图已执行完毕
- tasks：正在排队/执行中的任务
- metadata：本次运行的元数据（system_prompt、graph_id、assistant_id 等）
- checkpoint：最新检查点信息（checkpoint_id、thread_id、checkpoint_ns）
- checkpoint_id：最新检查点 ID，每个超步产生一个
- parent_checkpoint / parent_checkpoint_id：上一个检查点
- interrupts：当前的中断（human-in-the-loop 触发 interrupt 时才会有）
- created_at：检查点创建时间

### 获取线程历史

> GET /threads/{thread_id}/history

获取线程的全部历史状态（每个超步产生一个检查点，对应一个状态）：

```python
history = await client.threads.get_history(copy_thread_id, limit=10)
checkpoints = [state["checkpoint"] for state in history]
print(json.dumps(history, indent=2, ensure_ascii=False))
```

返回的是状态历史列表，每个元素对应一次超步执行后产生的一个检查点，字段与「获取线程状态」返回的结构一致，其中 `metadata.step` 为超步序号，`checkpoint` 里是 `checkpoint_id` 等检查点信息。

### 获取指定检查点状态

> GET /threads/{thread_id}/state/{checkpoint_id}

通过 `checkpoint_id` 获取某个历史检查点的状态。先取历史中的一个检查点 ID：

```python
# 获取指定检查点的状态
state = await client.threads.get_state(copy_thread_id, checkpoint_id="1f1954b1-a620-642e-8000-8ca661c7fcb5")
state
```

返回字段与「获取线程状态」一致，只是对应的是指定检查点那一刻的状态（可用于回溯/时间旅行）。

### 清理线程

> POST /threads/prune

按 ID 清理线程。`strategy="delete"` 会删除整个线程，`strategy="keep_latest"` 则只清理旧检查点但保留线程及最新状态。

先创建一个临时线程用于清理演示：

```python
# 清理临时线程（delete 策略会删除整个线程）
result = await client.threads.prune(
    thread_ids=[copy_thread_id],
    strategy="keep_latest",
)
result
```

返回字段说明：

- pruned_count：实际清理的线程数量

### 删除线程

> DELETE /threads/{thread_id}

删除线程，其所有检查点也会一并删除。删除后再次查询会抛出 `NotFoundError`：

```python
from langgraph_sdk.errors import NotFoundError

await client.threads.delete(copy_thread_id)

try:
    await client.threads.get(copy_thread_id)
except NotFoundError as e:
    print("已删除：", e)
```

## Run API

可以通过 `Agent Server` 暴露的 `Run API` 管理运行（图的一次调用）

API文档地址：http://localhost:2024/docs#tag/thread-runs

API调用：推荐 `langgraph_sdk`

运行分两类：
- **有状态运行（Thread Runs）**：在某个线程上执行，会更新线程的状态与检查点
- **无状态运行（Stateless Runs）**：不绑定线程，运行结束即清理，无记忆

> 流式接口（`/runs/stream`）依赖"流式处理"概念，本节不讲解。

### 安装 LangGraph SDK

上一节课已经安装过 `langgraph-sdk`，这里重复执行也无副作用，仅保证课件可独立运行：

```python
!uv add langgraph-sdk==0.4.2
```

### 创建客户端

连接本地 Agent Server（默认端口 2024），获得 `client.runs` 子客户端：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

### 准备工作

有状态运行需要绑定一个线程。先获取一个已有的 `agent` Assistant，再创建一个线程：

```python
assistant_id = "efbf07f8-c28f-4db8-a7ff-17b58c4af012"

# 创建一个线程，用于有状态运行
thread = await client.threads.create(
    metadata={
        "__name__": "第20节课：Run API测试"  # langsmith studio 会自动读取该值
    }
)
thread_id = thread["thread_id"]
```

### 创建运行

#### 创建后台运行

> POST /threads/{thread_id}/runs

创建运行后**立即返回**（后台运行），不等待执行完成。适合"先创建、稍后取结果"或无人值守的场景：

```python
# 创建后台运行，立即返回，不等待执行完成
run = await client.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "你好"}]},
    metadata={"lesson": "第20节课的运行测试"},
)
run_id = run["run_id"]
run
```

#### 等待运行完成

> GET /threads/{thread_id}/runs/{run_id}/join

阻塞等待某个**已创建**的后台运行执行完成，运行完后返回图的最新状态

```python
# 阻塞等待运行执行完成，返回最终状态（values）
final_state = await client.runs.join(thread_id, run_id)
final_state
```

#### 创建并等待运行完成

> POST /threads/{thread_id}/runs/wait

一步完成"创建运行 + 等待执行完成"，直接返回最终状态。适合需要同步拿到结果的场景：

```python
# 创建运行并等待执行完成，一步到位
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "第二个问题：地球为什么是圆的？"}]}
)
result
```

`wait` 与 `create + join` 的效果等价，只是封装成了一个接口。

#### 创建运行的可配置字段

- `thread_id`: 指定运行的线程
- `assistant_id`: 指定运行的AI助理
- `input`: 注入的状态
- `metadata`：本次运行的元数据，可用于后续搜索、过滤
- `config` / `context`：指定这次运行使用的配置，会覆盖 `assistant` 的对应配置
- `after_seconds`：指定多少秒后开始运行，用于定时运行
- `if_not_exists`：线程不存在时的处理，`reject`（默认，报错）/ `create`（自动创建线程）
- `durability`：控制检查点（checkpoint）写入的频率

  | 模式            | 行为                                                 | 代价                                             |
  | :-------------- | :--------------------------------------------------- | :----------------------------------------------- |
  | `exit`          | 只在图**退出时**（成功 / 出错 / 中断）持久化一次状态 | 性能最好，但中途崩溃则中间状态全丢，无法恢复     |
  | `async`（默认） | 下一步执行的同时**异步**后台写入检查点               | 兼顾性能与可靠，但崩溃时最后一个检查点可能没写入 |
  | `sync`          | 下一步开始前**同步**写入检查点                       | 最可靠（每步都落盘），性能开销最大               |

#### run 对象字段说明

- run_id：运行 ID
- thread_id：运行所属的线程
- assistant_id：本次运行使用的助手
- status：运行状态，刚创建时为 `pending`（排队中）
- metadata：本次运行的元数据
- kwargs：创建运行时的参数（input、config、context 等）

### 运行管理

#### 获取运行

> GET /threads/{thread_id}/runs/{run_id}

通过 run_id 获取运行的最新信息，最常用的是查看 `status`（运行是否完成）：

```python
# 通过 run_id 获取运行的最新信息
run = await client.runs.get(thread_id, run_id)
print(f"运行状态: {run['status']}")
run
```

#### 列出运行

> GET /threads/{thread_id}/runs

列出线程上的运行记录，支持分页、按状态过滤、指定返回字段。该接口同时用于列出线程上的全部运行：

```python
# 列出该线程上的运行记录
runs = await client.runs.list(thread_id, limit=10)
import json
print(json.dumps(runs, indent=2, ensure_ascii=False))
```

```python
# 按状态过滤 + 指定返回字段
runs = await client.runs.list(
    thread_id,
    limit=10,
    status="success",
    select=["run_id", "status", "created_at"],
)
runs
```

#### 删除运行

> DELETE /threads/{thread_id}/runs/{run_id}

删除运行记录，删除后再次查询会抛出 `NotFoundError`：

```python
from langgraph_sdk.errors import NotFoundError

# 删除运行
await client.runs.delete(thread_id, run_id)

try:
    await client.runs.get(thread_id, run_id)
except NotFoundError as e:
    print("已删除：", e)
```

```python
# 删除后，检查点也会被一并删除
await client.threads.get_state(thread_id=thread_id)
```

### 无状态运行（Stateless Runs）

无状态运行**不绑定已有线程**。服务器会为每次运行临时创建线程，运行结束后默认删除（`on_completion="delete"`）。

特点：
- 无记忆：每次运行相互独立，不共享状态
- 轻量：无需先创建线程，适合一次性调用

#### 创建无状态后台运行

> POST /runs

与有状态后台运行的区别：不传 `thread_id`：

```python
# 创建无状态后台运行（不传 thread_id）
run = await client.runs.create(
    thread_id=None,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "无状态运行：一次性的问答"}]},
)
print(f"状态: {run['status']}")
run
```

#### 无状态等待输出

> POST /runs/wait

创建无状态运行并直接等待输出，常用于在代码里同步调用一次图：

```python
# 创建无状态运行并等待输出
result = await client.runs.wait(
    thread_id=None,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "无状态等待输出"}]},
)
result
```

#### 批量创建运行

> POST /runs/batch

一次创建多个无状态后台运行，立即返回运行列表：

```python
# 一次创建多个无状态后台运行，立即返回
runs = await client.runs.create_batch([
    {"assistant_id": assistant_id, "input": {"messages": [{"role": "user", "content": "批次 1"}]}},
    {"assistant_id": assistant_id, "input": {"messages": [{"role": "user", "content": "批次 2"}]}},
    {"assistant_id": assistant_id, "input": {"messages": [{"role": "user", "content": "批次 3"}]}},
]) # type: ignore
print(f"创建数量: {len(runs)}")
print([(r["run_id"], r["status"]) for r in runs])
```

## Cron API

可以通过 `Agent Server` 暴露的 `Cron API` 按指定的时间计划**定时运行**图（类似操作系统的 `cron` 定时任务）

API文档地址：http://localhost:2024/docs#tag/crons

API调用：推荐 `langgraph_sdk`

Cron 分两类：
- **无状态 Cron（Stateless Crons）**：每次执行都新建一个线程，运行结束后删除
- **有状态 Cron（Thread Crons）**：绑定一个**固定的线程**，每次执行都复用该线程，可以积累上下文

### 安装 LangGraph SDK

上一节课已经安装过 `langgraph-sdk`，这里重复执行也无副作用，仅保证课件可独立运行：

```python
!uv add langgraph-sdk==0.4.2
```

### 创建客户端

连接本地 Agent Server（默认端口 2024），获得 `client.crons` 子客户端：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

### 准备工作

需要准备一个 `agent` Assistant（用来定时执行的图），以及一个线程（用于有状态 Cron 的演示）：

```python
assistant_id = "efbf07f8-c28f-4db8-a7ff-17b58c4af012"

# 创建一个线程，用于有状态 Cron 演示
thread = await client.threads.create(
    metadata={
        "__name__": "第21节课：Cron API测试"
    }
)
thread_id = thread["thread_id"]
```

### 创建 Cron

#### 创建无状态 Cron

> POST /runs/crons

无状态 Cron 每次执行时都会**自动创建一个新的线程**。用 `on_run_completed` 控制线程去留：
- `delete`（默认）：运行完成后删除线程，无任何残留
- `keep`：保留线程，会不断积累线程数据，需要自己清理

> 为了不在课堂上真的频繁触发任务，这里先创建 `enabled=False` 的禁用 Cron，稍后再演示启用：

```python
# 创建无状态 Cron（每次执行都会新建线程）
cron = await client.crons.create(
    assistant_id=assistant_id,
    schedule="*/2 * * * *",  # 每 2 分钟执行一次
    input={"messages": [{"role": "user", "content": "定时任务：汇报一下当前时间"}]},
    metadata={"lesson": "第21节课：无状态Cron测试"},
    enabled=False,  # 先禁用，避免课堂演示时频繁触发
)
cron
```

`*/2 * * * *` 是标准的 **cron 表达式**，由 5 个字段组成：

| 位置 | 字段 | 取值范围 | 示例说明 |
| :--- | :--- | :--- | :--- |
| 1 | 分钟 | 0-59 | `*/2` 表示每 2 分钟 |
| 2 | 小时 | 0-23 | `9` 表示早上 9 点 |
| 3 | 日 | 1-31 | `*` 表示每天 |
| 4 | 月 | 1-12 | `*` 表示每月 |
| 5 | 星期 | 0-6（0 为周日） | `0` 表示周日 |

常用示例：
- `0 9 * * *`：每天早上 9 点
- `*/5 * * * *`：每 5 分钟
- `0 0 * * 1`：每周一零点

不传 `timezone` 时按 **UTC** 时区解释。

#### 创建线程 Cron（有状态）

> POST /threads/{thread_id}/runs/crons

与无状态 Cron 的区别：通过 `create_for_thread` 绑定一个固定的线程。每次执行都往**同一个线程**里追加消息，可以积累多轮对话的上下文：

```python
# 创建绑定线程的 Cron（每次执行都复用同一个线程）
thread_cron = await client.crons.create_for_thread(
    thread_id=thread_id,
    assistant_id=assistant_id,
    schedule="0 9 * * *",  # 每天早上 9 点
    input={"messages": [{"role": "user", "content": "每日晨报"}]},
    metadata={"lesson": "第21节课：线程Cron测试"},
    enabled=False,  # 先禁用
)
thread_cron_id = thread_cron["cron_id"] # type: ignore
thread_cron
```

#### cron 对象字段说明

- `cron_id`：Cron 任务 ID
- `thread_id`：绑定的线程（无状态 Cron 会为每次执行新建，通常为空）
- `assistant_id`：执行时使用的助手
- `schedule`：cron 表达式
- `payload`：每次执行时要创建运行的参数（input、config 等）
- `next_run_date`：下一次执行时间
- `end_time`：Cron 的结束时间（为空则无限期运行）
- `enabled`：是否启用
- `metadata`：创建时传入的元数据，可用于搜索过滤

### Cron 管理

#### 搜索 Cron

> POST /runs/crons/search

列出 / 搜索全部 Cron 任务，支持按 `assistant_id`、`thread_id`、`enabled`、`metadata` 精确过滤，并支持分页与排序：

```python
# 按 metadata 精确过滤
crons = await client.crons.search(
    metadata={"lesson": "第21节课：无状态Cron测试"},
)
crons
```

```python
# 列出全部 Cron（限制 10 条）
all_crons = await client.crons.search(limit=10)
[(c["cron_id"], c["schedule"], c["enabled"], c["next_run_date"]) for c in all_crons]
```

#### 根据 ID 获取 Cron

> GET /runs/crons/{cron_id}

根据 `cron_id` 精确获取**单个** Cron 任务。

> 当前 `langgraph-sdk==0.4.2` 的 `client.crons` 尚未封装该接口（只有 `search` 按条件过滤、`count` 统计），需要借助底层 HTTP 客户端 `client.http.get` 直接调用：

```python
# 根据 ID 获取单个 Cron
cron_detail = await client.http.get(f"/runs/crons/{thread_cron_id}")
cron_detail
```

#### 统计 Cron 数量

> POST /runs/crons/count

按条件统计 Cron 的数量：

```python
# 统计全部 Cron 数量
count = await client.crons.count()
count
```

#### 启用 / 禁用 Cron

> PATCH /runs/crons/{cron_id}

通过 `update(enabled=...)` 开关 Cron。这里把刚才禁用的无状态 Cron 启用，观察 `next_run_date` 开始生效：

```python
# 启用无状态 Cron
cron = await client.crons.update(
    cron_id=cron["cron_id"], # type: ignore
    enabled=True,
)
cron["enabled"], cron["next_run_date"]
```

```python
# 再次禁用，防止课堂期间真的执行
cron = await client.crons.update(
    cron_id=cron["cron_id"],
    enabled=False,
)
cron["enabled"]
```

#### 修改 Cron

> PATCH /runs/crons/{cron_id}

`update` 同样可以修改调度计划、输入、元数据等：

```python
# 修改线程 Cron 的调度计划
updated = await client.crons.update(
    cron_id=thread_cron_id,
    schedule="30 8 * * *",
    input={"messages": [{"role": "user", "content": "每日晨报（提前半小时）"}]},
)
updated["schedule"], updated["payload"]["input"]
```

#### 删除 Cron

> DELETE /runs/crons/{cron_id}

删除 Cron 任务，删除后再次查询会抛出 `NotFoundError`：

```python
crons = await client.crons.search()
crons
```

```python
from langgraph_sdk.errors import NotFoundError

for cron in crons:
    # 删除线程 Cron
    await client.crons.delete(cron["cron_id"])
    print(f'已删除:{cron["cron_id"]}')
```

## System API

Agent Server 还提供了一组 **System API**，用于**健康检查**、**服务器信息** 与 **监控指标**，方便部署、监控与运维。

API文档地址：http://localhost:2024/docs#tag/System

API调用：推荐 `langgraph_sdk`，但当前版本（`0.4.2`）**尚未封装 System 接口**，需要借助底层 HTTP 客户端 `client.http` 直接调用

System 接口共 4 个：
- **`GET /ok`**：健康检查，可选是否检查数据库连通性
- **`GET /info`**：服务器版本、功能开关与元数据
- **`GET /metrics`**：Prometheus / JSON 格式的系统监控指标
- **`GET /docs`**：API 文档页面（HTML）

### 安装 LangGraph SDK

上一节课已经安装过 `langgraph-sdk`，这里重复执行也无副作用，仅保证课件可独立运行：

```python
!uv add langgraph-sdk==0.4.2
```

### 创建客户端

连接本地 Agent Server（默认端口 2024）。System 接口没有独立的子客户端，全部通过 `client.http` 调用：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

### 健康检查 `GET /ok`

检查服务器是否健康，返回 `{"ok": true}`。`check_db` 参数可选，传 `1` 时同时检查数据库连通性：

```python
# 基本健康检查
await client.http.get("/ok")
```

```python
# 同时检查数据库连通性
await client.http.get("/ok", params={"check_db": 1})
```

> 服务器异常时（或数据库连不上且 `check_db=1`）会返回 `500`，`client.http` 会自动抛出 `ServerError`，适合在部署脚本 / 负载均衡的健康检查探针中使用。

### 服务器信息 `GET /info`

返回服务器版本、`langgraph` 库版本、功能开关（`flags`）与部署元数据（`metadata`）：

```python
info = await client.http.get("/info")
info
```

`info` 字段说明：

- `version`：LangGraph API 服务器版本
- `langgraph_py_version`：`langgraph` Python 库版本
- `flags`：已启用的功能特性开关
- `metadata`：服务器部署元数据

```python
# 分别查看各字段
print("服务器版本:", info["version"])
print("langgraph Python 版本:", info["langgraph_py_version"])
print("功能开关:", info["flags"])
print("部署元数据:", info["metadata"])
```

### 系统指标 `GET /metrics`

获取系统监控指标，支持两种输出格式（`format` 参数）：
- `prometheus`（默认）：Prometheus 文本格式，适合接入 Prometheus 采集器
- `json`：JSON 格式，包含队列统计、Worker 统计、HTTP 统计等，适合程序化处理

#### JSON 格式

`client.http.get` 内部会把响应体按 **JSON** 解析，因此 JSON 格式可以直接使用：

```python
metrics = await client.http.get("/metrics", params={"format": "json"})
metrics
```

```python
# 查看队列与 Worker 统计
metrics
```

#### Prometheus 格式

默认返回 `text/plain` 文本，`client.http.get` 会按 JSON 解析而报错。需要借助底层的 `httpx.AsyncClient`（即 `client.http.client`）获取原始响应文本：

```python
# Prometheus 格式（text/plain），使用原始 httpx 客户端获取
r = await client.http.client.get(
    "/metrics",
    params={"format": "prometheus"},
)
print("Content-Type:", r.headers["content-type"])
print(r.text[:1000])
```

#### 为什么 Prometheus 格式不能用 `client.http.get`？

`client.http.get` 在拿到响应后，会把响应体交给 `orjson.loads` 解析成 Python 对象。Prometheus 文本格式不是 JSON，解析必然失败。所以凡是返回**非 JSON** 内容的接口（`/metrics` 的 Prometheus 格式、`/docs` 的 HTML），都要改用原始 `httpx` 客户端。

### API 文档 `GET /docs`

返回 Swagger / OpenAPI 交互式文档页面（HTML）。

## MCP API

Agent Server 可以将你的 Assistant 暴露为 MCP 服务。

你仅需要在MCP客户端中使用: http://127.0.0.1:2024/mcp/ 地址即可连接到该服务。

```python
!npx -y @modelcontextprotocol/inspector@1.0.0
```

```text
Starting MCP inspector...
⚙️ Proxy server listening on localhost:6277
🔑 Session token: e660e2576f71b49787db41685963ca7ee74fa55d903b90f63271dda32320abf7
   Use this token to authenticate requests or set DANGEROUSLY_OMIT_AUTH=true to disable auth

🚀 MCP Inspector is up and running at:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=e660e2576f71b49787db41685963ca7ee74fa55d903b90f63271dda32320abf7

🌐 Opening browser...
New StreamableHttp connection request
Query parameters: {"url":"http://127.0.0.1:2024/mcp/","transportType":"streamable-http"}
Created StreamableHttp client transport
Client <-> Proxy  sessionId: 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
Received POST message for sessionId 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
Received GET message for sessionId 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
Received POST message for sessionId 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
Received POST message for sessionId 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
Received POST message for sessionId 5b3e5cb7-f8f6-4074-93d8-14c3cc83690e
```

## 时间旅行

时间旅行：允许你从某一个检查点开始重新运行直到图结束。

支持两种模型的时间旅行：

- Replay: 从某个检查点的状态开始重新运行
- Fork：和 Replay 一样，只是运行时可以修改检查点状态

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/时间旅行.png)

### 如何实现时间旅行？

#### LangGraph API

```python
from langgraph_python.graphs.core_agent_graph import build_graph
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph_python.states.core_agent_state import ContextSchema
from langgraph.graph import START

context = ContextSchema(
    system_prompt="尽可能简短的回答问题，不要长篇大论",
    tools=[] # 不使用工具
)
checkpointer = InMemorySaver()
config:RunnableConfig = {
    "configurable":{
        "thread_id": "time_travel"
    }
}

graph = build_graph().compile(checkpointer=checkpointer)
```

```python
# 第一次运行
await graph.ainvoke(
    input={
        "messages": [
            HumanMessage("月亮离地球有多远")
    ]},
    config=config,
    context=context
)
```

##### 查看历史记录

```python
history = list(graph.get_state_history(config))
# 打印每个检查点的 checkpoint_id 及它的父检查点
for i, state in enumerate(history):
    cid = state.config["configurable"]["checkpoint_id"] # type: ignore
    parent = (
        state.parent_config["configurable"]["checkpoint_id"] # type: ignore
        if state.parent_config
        else None
    )
    print(f"{i:>2}  checkpoint_id={cid}  parent={parent}")
[[msg.text for msg in h.values["messages"]] for h in history]
```

```python
before_start = history[2].config
after_start = history[1].config
before_start, after_start
```

##### Replay

```python
await graph.ainvoke(
    input=None, # 不要有任何输入
    config=after_start,
    context=context
)
```

##### fork

Fork 与 Replay 的区别：可以先**修改检查点状态**再运行。

```python
# 修改状态
fork_config = graph.update_state(
    config=before_start,
    values={"messages": [HumanMessage("太阳距离地球有多远")]},
    as_node=START,
)
fork_config
```

```python
# replay
await graph.ainvoke(
    input=None, # 不要有任何输入
    config=fork_config,
    context=context
)
```

##### 最佳实践

- 刷新 AI 输出：找到AI结果之前的检查点，直接 replay 即可
- 修改内容：找到内容产出节点上一个检查点，指定`as_node`为内容产出节点，修改内容，然后从该检查点 replay

#### Agent Server

Agent Server 上运行的图同样基于检查点，因此时间旅行（Replay / Fork）可以直接通过 SDK 操作。

与 LangGraph API 的区别只在于：历史、状态与检查点都存在服务器上，通过 `client.threads` 查询与修改，再通过 `client.runs` 从指定检查点恢复运行。

API文档地址：http://localhost:2024/docs

##### 准备工作

获取一个 `agent` Assistant，创建线程并运行一次。`agent` 图会调用搜索工具，一次运行会产生多个检查点：

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")
client
```

```python
# 删除所有线程，免得看晕了
threads = await client.threads.search()
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])
```

```python
# 获取一个已注册的 agent Assistant
assistant_id = "71463029-b316-4f54-96a8-e7a65f00af62"
```

```python
# 创建线程，并运行一次产生多个检查点
thread = await client.threads.create(metadata={"__name__": "时间旅行"})
thread_id = thread["thread_id"]

await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "地球为什么是圆的？"}]},
)
thread_id
```

```text
'019ff9af-dce9-7e13-ba04-f669f16754d0'
```

```python
history = await client.threads.get_history(thread_id, limit=20)
before_start = {}
after_start = {}
for i, state in enumerate(history):
    step = state["metadata"].get("step") # type: ignore
    checkpoint_id = state["checkpoint"]["checkpoint_id"]
    print(f"{i:>2}  step={step:>3}  next={state['next']}  checkpoint_id={checkpoint_id}")
    if step == -1:
        before_start = state["checkpoint"]
    elif step == 0:
        after_start = state["checkpoint"]

before_start, after_start
```

```text
 0  step=  1  next=[]  checkpoint_id=1f196db7-a9bf-6ce6-8001-256a3d02170d
 1  step=  0  next=['model']  checkpoint_id=1f196db7-9a47-65a2-8000-1f0fd43da987
 2  step= -1  next=['__start__']  checkpoint_id=1f196db7-9a44-6a78-bfff-658db76986bd

({'checkpoint_id': '1f196db7-9a44-6a78-bfff-658db76986bd',
  'thread_id': '019ff9af-dce9-7e13-ba04-f669f16754d0',
  'checkpoint_ns': ''},
 {'checkpoint_id': '1f196db7-9a47-65a2-8000-1f0fd43da987',
  'thread_id': '019ff9af-dce9-7e13-ba04-f669f16754d0',
  'checkpoint_ns': ''})
```

##### Replay

> POST /threads/{thread_id}/runs/wait

```python
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input=None,
    checkpoint=after_start # type: ignore
)

result
```

##### fork

```python
from langgraph.graph import START
updated = await client.threads.update_state(
    thread_id,
    values={
        "messages": [
            {"role":"user", "content":"月球到地球距离是多少？"}
        ]
    },
    checkpoint=before_start, # type: ignore
    as_node=START,
)
updated_checkpoint = updated["checkpoint"]
updated_checkpoint
```

```python
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input=None,
    checkpoint=updated_checkpoint
)
result
```

#### 子图

子图无法做时间旅行

#### [选修]魔法版本实现

解决 `LangSmith Studio` 显示的 bug (也可能是`LangGraph`的设计缺陷)

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/时间旅行子图.png)


##### LangGraph API

###### replay

```python
# copy 模式: 魔法
# 1. 先 copy 一个检查点出来

fork_config = graph.update_state(
    after_start, # type: ignore
    values=None, # 这里必须要传None
    as_node="__copy__" # 固定值
)
fork_config
```

```python
# copy 模式：魔法
# 2. 使用copy的检查点运行
await graph.ainvoke(
    input=None, # 不要有任何输入
    config=fork_config,
    context=context
)
```

###### fork

```python
fork_config = graph.update_state(
    before_start, # type: ignore
    values=[
        [
            {"messages": [HumanMessage("太阳距离地球有多远？")]},
            START, # 在这里指定新状态来自于哪个节点
        ]
    ],
    as_node="__copy__", # 在这里用魔法
)
fork_config
```

```python
# 从修改后的检查点继续运行（next 为空，运行不会再有新输出，直接返回当前状态）
await graph.ainvoke(
    input=None, # 不要有任何输入
    config=fork_config,
    context=context
)
```

##### Agent Server

###### replay

```python
# 使用copy模式
# 1. copy 检查点

updated = await client.threads.update_state(
    thread_id=thread_id,
    values=None,
    checkpoint=after_start, # type: ignore
    as_node="__copy__",
)
updated_checkpoint = updated["checkpoint"]
updated_checkpoint
```

```python
# 使用copy模式
# 2. replay

result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input=None,
    checkpoint=updated_checkpoint
)

result
```

###### Fork

```python
updated = await client.threads.update_state(
    thread_id,
    values=[
        [
            {"messages": [{"role":"user", "content":"月球到地球距离是多少？"}]},
            START,
        ] # type: ignore
    ],
    checkpoint=before_start, # type: ignore
    as_node="__copy__",
)
updated_checkpoint = updated["checkpoint"]
updated_checkpoint
```

```text
{'thread_id': '019ff9af-dce9-7e13-ba04-f669f16754d0',
 'checkpoint_ns': '',
 'checkpoint_id': '1f196db8-33e9-600c-8001-80478af3def6'}
```

```python
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input=None,
    checkpoint=updated_checkpoint
)
result
```

```text
{'messages': [{'content': '月球到地球距离是多少？',
   'additional_kwargs': {},
   'response_metadata': {},
   'type': 'human',
   'name': None,
   'id': '908f65df-0938-40e8-b4bc-cd71917ed625'},
  {'content': '平均距离约为 38.44 万公里。',
   'additional_kwargs': {},
   'response_metadata': {'id': 'msg_cfe7a8f6-955f-9dd6-ab54-dea51c6a3986',
    'container': None,
    'model': 'qwen3.7-plus',
    'stop_details': None,
    'stop_reason': 'end_turn',
    'stop_sequence': None,
    'usage': {'cache_creation': None,
     'cache_creation_input_tokens': 0,
     'cache_read_input_tokens': 0,
     'inference_geo': None,
     'input_tokens': 30,
     'output_tokens': 12,
     'output_tokens_details': None,
     'server_tool_use': None,
     'service_tier': None,
     'prompt_tokens_details': {'cached_tokens': 0}},
    'model_name': 'qwen3.7-plus',
    'model_provider': 'anthropic'},
   'type': 'ai',
   'name': None,
   'id': 'lc_run--019ff9b0-2ef1-7793-90c4-8b7364c1f605-0',
   'tool_calls': [],
   'invalid_tool_calls': [],
   'usage_metadata': {'input_tokens': 30,
    'output_tokens': 12,
    'total_tokens': 42,
    'input_token_details': {'cache_read': 0, 'cache_creation': 0}}}]}
```

```python
from langgraph_sdk import get_client

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")

# 删除所有线程，免得看晕了
threads = await client.threads.search()
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

# 创建新线程
thread = await client.threads.create(
    metadata={
        "__name__": "手动重试错误"
    },
)
thread_id = thread["thread_id"]

# 获取一个已注册的 agent Assistant
assistant_id = "efbf07f8-c28f-4db8-a7ff-17b58c4af012"

# 查看结果
thread_id, assistant_id
```

## 手动错误重试

### 理解 invoke 机制

![image](https://raw.githubusercontent.com/JJ-front/store-img/master/手动重试错误.png)


### 手动错误重试

当图运行期间发生错误时，会：

- 立即停止图的运行
- 最新的检查点为错误发生之前的检查点

```python
try:
    result = await client.runs.wait(
        thread_id=thread_id,
        assistant_id=assistant_id,
        input={"messages": [{"role": "user", "content": "你好！"}]}
    )
    print(result)
except Exception as e:
    print(e)
```

```python
# 直接重新运行即可重试
try:
    result = await client.runs.wait(
        thread_id=thread_id,
        assistant_id=assistant_id,
        input=None # 不传 input
    )
    print(result)
except Exception as e:
    print(e)
```

## 容错机制

> 本节课的所有知识都仅涉及对图的改动，因此和哪种部署模式无关

### 重试策略

```python
from langgraph.types import RetryPolicy

# 可以所有节点添加重试策略
workflow.set_node_defaults(
    # 添加重试策略，最大重试次数3次
    retry_policy=RetryPolicy(max_attempts=3),
)

# 可以给某个节点添加重试策略，覆盖默认
workflow.add_node(
    "call_api",
    call_api,
    # 添加重试策略，最大重试次数3次
    retry_policy=RetryPolicy(max_attempts=3),
)
```

以下错误类型会被`LangGraph`认为是程序bug，不会引发重试：

- `ValueError`
- `TypeError`
- `ArithmeticError`
- `ImportError`
- `LookupError`
- `NameError`
- `SyntaxError`
- `RuntimeError`
- `ReferenceError`
- `StopIteration`
- `StopAsyncIteration`
- `OSError`

https://docs.langchain.com/oss/python/langgraph/fault-tolerance#parameters

### 超时策略

```python
from langgraph.types import TimeoutPolicy

# 可以所有节点添加超时策略
workflow.set_node_defaults(
    # 添加超时策略，run timeout：60秒，idel timeout：10秒
    timeout=TimeoutPolicy(run_timeout=60,idle_timeout=10),
)

# 可以给某个节点添加超时策略，覆盖默认
workflow.add_node(
    "call_api",
    call_api,
   	# 添加超时策略，run timeout：60秒，idel timeout：10秒
   	timeout=TimeoutPolicy(run_timeout=60,idle_timeout=10),
)
```

> 超时策略仅能作用于异步节点，想想为什么？

- run_timeout：从节点开始等，最多等多久能等到节点完成

- idle_timeout：从节点开始不断等，最多等多久能得到下一个信号发生

  信号：

  - LLM有新token到达

  - 其他信号

    https://docs.langchain.com/oss/python/langgraph/fault-tolerance#progress-signals

  - 子图有信号发生也算

### 错误兜底

```python
def my_error_handler(state: State, error: NodeError):
    # 该函数会代替节点的执行
    pass

# 可以所有节点添加错误兜底
workflow.set_node_defaults(
    # 添加错误处理函数
    error_handler=my_error_handler,
)

# 可以给某个节点添加错误兜底，覆盖默认
workflow.add_node(
    "call_api",
    call_api,
   	# 添加错误处理函数
   	error_handler=my_error_handler,
)
```

### 线上环境

超时 / 其他错误 --> 

重试 --> 

错误函数兜底 --> 

终止运行 --> 

用户手动刷新(replay) / 更改(fork) / 追加消息(invoke + input)

## Command

`Command` 是一种控制图执行的底层原语

```python
# 某个节点
def node(state: State):
    return { "foo": "bar" }
  
# 等效于
def node(state: State):
    return Command(
        update={"foo": "bar"}
    )
```

### 位置

`Command`可以用于三个地方：

- 节点返回
- 工具函数返回
- 图调用

#### 节点返回

```python
def node(state: State):
    return Command(...)
```

#### 工具函数返回

```python
@tool
def search(
  	query: str, 
  	runtime: ToolRuntime[ContextSchema, StateSchema] # 依赖注入
) -> Command:
    return Command(...)
```

- `runtime.tool_call_id` → 当前这次 tool call 的 id
- `runtime.state` → 当前图状态
- `runtime.context` → 传入的 context

#### 图调用

```python
graph.invoke(input=Command(...))
```

> 下节课学习

### 参数

`Command`对象中支持四个参数：

- `update`: 更新图状态的指令
- `goto`：指定下一个节点（动态边）
- `graph`：在子图中使用，跳到父图的某个节点
- `resume`：恢复中断，下节课学习



```python
def node(state:State):
   return Command(
   	  update={..}, # 更新的状态
      goto="node_b",
      graph=Command.PARENT
   )
```



### 使用方式

| 参数     | 节点返回/工具返回 | 图调用 |
| -------- | ----------------- | ------ |
| `update` | ✅                 | ❌      |
| `goto`   | ✅                 | ❌      |
| `graph`  | ✅（必须在子图中） | ❌      |
| `resume` | ❌                 | ✅      |

### 注意事项

节点的静态边和动态边都会得到执行。

## 中断

### 在任意位置中断

LangGraph允许你在图执行期间任意代码位置执行中断。

```python
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from langgraph_python.graphs.demo import (
    demo_interrupt_graph,
    demo_interrupt_parallel_graph,
    demo_subgraph_interrupt_graph,
)


checkpointer = InMemorySaver()
config:RunnableConfig = {
    "configurable":{
        "thread_id": "interrupt_demo"
    }
}
graph = demo_interrupt_parallel_graph.build_graph().compile(checkpointer)
```

### LangGraph API

#### 运行到中断

```python
result = await graph.ainvoke(
    input={}, # type: ignore
    config=config
)
result
```

```python
history = list(graph.get_state_history(config=config))
history
```

#### 多种方式查看中断

```python
interrupts = result.get("__interrupt__", [])
interrupts
```

```python
cur_cp = graph.get_state(config=config)
cp_interrupts = cur_cp.interrupts
cp_interrupts
```

#### 中断的恢复

```python
# 构建回答
interrupts = result.get("__interrupt__", [])
answers = {
    inter.id: True
    for inter in interrupts
}
answers
```

```python
from langgraph.types import Command

result = await graph.ainvoke(input=Command(resume=answers), config=config)

result
```

### Agent Server API

```python
from langgraph_sdk import get_client
from langgraph_sdk.schema import Command as SDKCommand

# 连接本地 Agent Server
client = get_client(url="http://localhost:2024")

# 直接使用 langgraph.json 中注册的图名称作为 assistant_id
assistant_id = "interrupt_parallel_graph"

# 删除所有线程，免得看晕了
threads = await client.threads.search()
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

# 创建新线程
thread = await client.threads.create(metadata={"__name__": "中断"})
thread_id = thread["thread_id"]
thread_id
```

#### 运行到中断

```python
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={},
)
result
```

#### 多种方式查看中断

```python
interrupts = result.get("__interrupt__", []) # type: ignore

interrupts
```

```python
cur_cp = await client.threads.get_state(thread_id=thread_id)
cp_interrupts = cur_cp['interrupts']

cp_interrupts
```

#### 中断恢复

```python
answers = {
    inter["id"]: True
    for inter in interrupts
}
answers
```

```python
# 同时恢复 A、B 的第一个中断，本次 run 会运行到 A、B 的第二个中断
result = await client.runs.wait(
    thread_id=thread_id,
    assistant_id=assistant_id,
    command=SDKCommand(resume=answers),
)
result
```

### 最佳实践

1. 永远不要捕获`interrupt`异常，至少不要捕获`GraphBubbleUp`异常，至至少少不要吞掉异常

2. 被中断的节点，在恢复时会重新运行，因此保证中断前副作用的幂等性

3. 节点运行过程中，如果要依次引发多个中断，必须确保中断的数量和顺序是稳定的

4. 子图的`checkpoint`必须设置为`None`或`True`才能正常的在父图中中断

5. 时间旅行会重新中断

## 人在回路 HITL(这个是中断的例子)

> 英文全称：**Human-in-the-Loop**，简称**HITL**


![人在回路流程：用户输入进入循环，节点中断后由用户参与决策，随后恢复执行并产生最终输出](https://raw.githubusercontent.com/JJ-front/store-img/master/人在回路.png)

### 设计 ask_question_tool 工具契约

**工具参数契约**

```json
{
  "question": "你希望使用哪种数据库？",
  "options": [
    {
      "title": "PostgreSQL",
      "description": "功能完善，适合生产环境",
      "recommended": true
    },
    {
      "title": "MySQL",
      "description": "使用广泛，生态成熟",
      "recommended": false
    },
    {
      "title": "SQLite",
      "description": "无需单独部署，适合本地开发",
      "recommended": false
    }
  ]
}
```


**中断契约**

```json
{
  "type": "ask_user_question",
  "question": "你希望使用哪种数据库？",
  "options": [
    {
      "title": "PostgreSQL",
      "description": "功能完善，适合生产环境",
      "recommended": true
    },
    {
      "title": "MySQL",
      "description": "使用广泛，生态成熟",
      "recommended": false
    },
    {
      "title": "SQLite",
      "description": "无需单独部署，适合本地开发",
      "recommended": false
    }
  ]
}
```

**回复契约**

纯字符串

```text
PostgreSQL
```

## 动态扇出

**map-reduce** 模式

![动态扇出的 MapReduce 模式](https://raw.githubusercontent.com/JJ-front/store-img/master/动态扇出.png)

## 运行取消

运行取消是 Agent Server 独有的功能。

当用户不再需要结果，或者任务执行时间过长时，可以通过 `cancel` 接口停止运行。

```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")
```

### 准备演示

本课使用 `cancel_demo_graph`。这个图中有几个慢节点，完整运行大约需要 6 秒，方便我们在它结束前取消。

```python
assistant_id = "efbf07f8-c28f-4db8-a7ff-17b58c4af012"

# 删除所有线程，免得看晕了
threads = await client.threads.search(limit=100)
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

thread = await client.threads.create(
    metadata={"__name__": "运行取消演示"}
)
thread_id = thread["thread_id"]
thread_id
```

### 创建后台运行

`client.runs.create()` 创建 Run 后会立即返回，图在 Agent Server 后台继续执行。

我们需要保留 `run_id`，因为取消接口需要同时知道 `thread_id` 和 `run_id`。

```python
run = await client.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={
        "messages": [
            {"role":"user", "content":"你好！"}
        ]
    },
)
run_id = run["run_id"]
run["status"]
```

```python
cur_run = await client.runs.get(thread_id, run_id)
cur_run["status"]
```

### 取消运行

调用 `client.runs.cancel()` 取消运行：

- `action="interrupt"`：停止运行，但保留 Run 记录和已经产生的检查点
- `wait=True`：等到取消真正完成后再返回

`interrupt` 是默认的 action，这里为了讲解清楚，将它显式写出来。

```python
await client.runs.cancel(
    thread_id=thread_id,
    run_id=run_id,
    action="interrupt", # interrupt是默认值，另一个值是 rollback
    wait=True,
)

print("取消请求已完成")
```

## 多任务策略

### 前置操作
```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")

assistant_id = "efbf07f8-c28f-4db8-a7ff-17b58c4af012"

# 删除所有线程，免得看晕了
threads = await client.threads.search(limit=100)
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

thread = await client.threads.create(
    metadata={"__name__": "多任务策略"}
)
thread_id = thread["thread_id"]
thread_id
```

多任务策略是 Agent Server 独有的功能。

它是指同一个线程内，前一个任务(run)还在运行，此时又发起一个新任务(run)，该如何处理？

比如`Run A`正在运行，此时发起`Run B`，如何处理`A`和`B`。

Agent Server 提供四种处理策略：

| 策略           | Run A        | Run B               | Run A 已产生的状态 |
| -------------- | ------------ | ------------------- | ------------------ |
| `enqueue` 默认 | 继续完成     | 排队等待            | 保留               |
| `reject`       | 继续完成     | 拒绝创建            | 保留               |
| `interrupt`    | 被中断       | 立即接替执行        | 保留已提交部分     |
| `rollback`     | 被中断并删除 | 从 A 之前的状态执行 | 回滚并删除         |

```python
import asyncio

run1 = await client.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={
        "messages": [
            {"role":"user", "content":"你好！"}
        ]
    },
)

# 等任务1运行一秒钟，模拟两次任务的时间差
await asyncio.sleep(1)

run2 = await client.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={
        "messages": [
            {"role":"user", "content":"hello！"}
        ]
    },
    multitask_strategy="rollback"
)
```

```python
current_run1 = await client.runs.get(thread_id, run1["run_id"])
current_run2 = await client.runs.get(thread_id, run2["run_id"])

current_run1['status'], current_run2['status']
```

## 事件流

### 什么是事件流

- 在大模型回复中，是指一个个token接收
- 在langgraph的图中，指在一些检查点、在一些节点会扔出一些东西。就是指一张图在运行期间，会发生一些事，这些事会不断的往外扔结果，这就是事件流

### 前置清理操作

```python

from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")

assistant_id = "2ac0901b-41bf-4d2b-a3b8-9cdee6a1af53"

# 删除所有线程，免得看晕了
threads = await client.threads.search(limit=100)
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

thread = await client.threads.create(
    metadata={"__name__": "事件流"}
)
thread_id = thread["thread_id"]
thread_id
```
### 在langgraph中如何获取流
- streaming API（老API）
  - 有v1版本、v2版本

- event-streaming API(新API)
  - 有v1、v2、v3版本


### 在Agent Server中如何获取流

- streaming API（老API，与langgraph的streaming 还有一些区别）
  - 有v1版本、v2版本
- protocal API(新API，与langgraph的event-streaming 还有一些区别)
  - 有v1版本、v2版本

### 多种方式获取流，应该用那套

使用streaming API的v1的版本，因为其他版本都有bug,不稳定，仅仅麻烦点

```python
from typing import AsyncIterator

from langgraph_sdk.schema import StreamPart

msg_types: dict[str, str] = {}
announced_subgraphs: set[str] = set()
msg_type_map = {
    'thinking': '思考：',
    'text': '回复：',
    'tool_use': '调用工具：'
}
def print_message(chunk: StreamPart):
    event_type, _, namespace = chunk.event.partition('|')
    if event_type != "messages": 
        return
    if chunk.data[1]['langgraph_node'] != 'model':
        return
    source = namespace or 'root'
    content_blocks = chunk.data[0]['content']
    for block in content_blocks:
        type = block['type']
        if type != msg_types.get(source):
            msg_types[source] = type
            if type not in msg_type_map:
                continue
            title = msg_type_map[type]
            if type == 'tool_use':
                title += block['name']
            if namespace and namespace not in announced_subgraphs:
                announced_subgraphs.add(namespace)
                print(f"\n子代理：\n{title}", flush=True)
            else:
                print(flush=True)
                print(title, flush=True)
        if type not in msg_type_map:
            continue
        if type == 'tool_use':
            continue 
        print(block[type], end='', flush=True)

chunks = []
async def print_stream(stream: AsyncIterator[StreamPart]):
    global chunks
    chunks = []
    msg_types.clear()
    announced_subgraphs.clear()
    result = {}
    async for chunk in stream:
        chunks.append(chunk)
        print_message(chunk)
        if chunk.event == 'values':
            result = chunk.data
    return result
```

```python
stream = client.runs.stream(
    thread_id=thread_id,
    assistant_id=assistant_id,
    input={
        "messages": [
            {"role": "user", "content": "写一首夏天的诗"}
        ]
    },
    stream_mode=[ # 流式输出SSE 的事件名称
        "values", # 获取图状态值
        "checkpoints", # 检查点信息
        "updates", # 每一个节点的返回结果
        "messages-tuple" # 消息内容
    ],
    stream_subgraphs=True, # 子图是否开启流式
    version="v1", # v1版本
)

output = await print_stream(stream)
```

```python
output
```

```python
from langgraph_sdk.schema import Command as SDKCommand

answers = {
    '806d9079dfa52181485476ba6c5ce802': '清新淡雅'
}
answers
```

```python
stream = client.runs.stream(
    thread_id=thread_id,
    assistant_id=assistant_id,
    command=SDKCommand(resume=answers),
    stream_mode=[
        "values",
        "checkpoints",
        "updates",
        "messages-tuple" 
    ],
    stream_subgraphs=True,
    version="v1",
)

output = await print_stream(stream)
```

## Store

`Checkpointer` 保存的是某个 `thread` 的图状态，不同线程之间的状态彼此隔离。但是在真实应用中，我们往往还需要保存一些**跨线程、跨会话的长期数据**。

`Store` 就是用来存储这类数据的。它不依附于某一次图的执行，可以让 Agent 在新的对话中仍然记得用户，也可以在多个线程或多个 Agent 之间共享数据。

通常可以用于实现长期记忆：

- **用户偏好**：用户曾经说过"回答时请使用中文"。即使下次开启了新对话，Agent 仍然可以从 `Store` 中读取这个偏好。
- **用户资料**：记住用户的姓名、职业、所在城市等稳定信息，在之后的不同会话中提供个性化服务。
- **状态跟踪**：把"用户正在学习 LangGraph"这类值得长期保留的信息从对话状态中提取出来，写入 `Store`。
- ...

### LangGraph API

#### 创建 Memory Store

Store 中的一条数据由三部分组成：

- `namespace`：命名空间，用元组表示，可以理解为数据所在的目录
- `key`：数据在当前命名空间中的唯一标识
- `value`：真正保存的数据，必须是字典

```
Store
└── namespace（命名空间）
    ├── key → value
    ├── key → value
    └── key → value
```

```python
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
namespace = ("users", "user_001", "memory")
```

#### 增加数据

使用异步方法 `aput` 写入数据。同一个命名空间中，`key` 唯一标识一条数据：

```python
await store.aput(
    namespace,
    key="profile",
    value={"name": "张三", "city": "上海", "job": "Python 工程师"},
)

await store.aput(
    namespace,
    key="preferences",
    value={"language": "中文", "response_style": "简洁"},
)
```

#### 查询单条数据

使用异步方法 `aget` 根据 `namespace + key` 精确查询一条数据：

```python
profile = await store.aget(namespace, key="profile")
profile
```

```text
Item(namespace=['users', 'user_001', 'memory'], key='profile', value={'name': '张三', 'city': '上海', 'job': 'Python 工程师'}, created_at='2026-08-18T02:02:10.402312+00:00', updated_at='2026-08-18T02:02:10.402314+00:00')
```

#### 查询多条数据

使用异步方法 `asearch` 查询某个命名空间下的多条数据：

```python
items = await store.asearch(namespace)
[(item.key, item.value) for item in items]
```

```text
[('profile', {'name': '张三', 'city': '上海', 'job': 'Python 工程师'}),
 ('preferences', {'language': '中文', 'response_style': '简洁'})]
```

#### 查询子命名空间

使用异步方法 `alist_namespaces` 查询父命名空间下的子命名空间。`prefix` 指定父命名空间，`max_depth` 限制返回的命名空间深度：

```python
namespaces = await store.alist_namespaces(
    prefix=("users",),
    max_depth=4,
)
namespaces
```

```text
[('users', 'user_001', 'memory')]
```

#### 修改数据

Store 没有单独的 `update` 方法。使用相同的 `namespace + key` 再次调用 `aput`，就会覆盖原数据：

```python
await store.aput(
    namespace,
    key="profile",
    value={"name": "张三", "city": "杭州", "job": "AI 工程师"},
)

updated_profile = await store.aget(namespace, key="profile")
updated_profile
```

```text
Item(namespace=['users', 'user_001', 'memory'], key='profile', value={'name': '张三', 'city': '杭州', 'job': 'AI 工程师'}, created_at='2026-08-18T02:05:09.322899+00:00', updated_at='2026-08-18T02:05:09.322901+00:00')
```

`aput` 会整体替换原来的 `value`，不会自动合并新旧字典。

#### 删除数据

使用异步方法 `adelete` 删除指定数据。删除不存在的数据不会报错：

```python
await store.adelete(namespace, key="profile")

# 删除后查询不到，返回 None
await store.aget(namespace, key="profile")
```

最后清理示例中剩余的数据：

```python
await store.adelete(namespace, key="preferences")
await store.asearch(namespace)
```

```text
[]
```

### Agent Server API

Agent Server 通过 Store API 对外提供长期存储能力。这些数据不依赖图、Assistant 或 Thread，可以直接通过 `client.store` 访问。

API 文档地址：http://localhost:2024/docs#tag/store

#### 创建客户端

连接本地 Agent Server（默认端口 2024）：

```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")
server_namespace = ("users", "user_002", "memory")
```

#### 增加数据

> PUT /store/items

使用 `put_item` 写入数据：

```python
await client.store.put_item(
    server_namespace,
    key="profile",
    value={"name": "李四", "city": "北京", "job": "Python 工程师"},
)

await client.store.put_item(
    server_namespace,
    key="preferences",
    value={"language": "中文", "response_style": "简洁"},
)
```

#### 查询单条数据

> GET /store/items

使用 `get_item` 根据 `namespace + key` 精确查询一条数据：

```python
profile = await client.store.get_item(
    server_namespace,
    key="profile",
)
profile
```

```text
{'namespace': ['users', 'user_002', 'memory'],
 'key': 'profile',
 'value': {'name': '李四', 'city': '北京', 'job': 'Python 工程师'},
 'created_at': '2026-08-18T02:05:56.665619+00:00',
 'updated_at': '2026-08-18T02:05:56.665624+00:00'}
```

#### 查询多条数据

> POST /store/items/search

使用 `search_items` 查询某个命名空间下的多条数据：

```python
result = await client.store.search_items(server_namespace)
[(item["key"], item["value"]) for item in result["items"]]
```

```text
[('profile', {'name': '李四', 'city': '北京', 'job': 'Python 工程师'}),
 ('preferences', {'language': '中文', 'response_style': '简洁'})]
```

#### 查询子命名空间

> POST /store/namespaces

使用 `list_namespaces` 查询父命名空间下的子命名空间：

```python
result = await client.store.list_namespaces(
    prefix=["users"],
    max_depth=4,
)
result["namespaces"]
```

```text
[['users', 'user_002', 'memory']]
```

#### 修改数据

> PUT /store/items

Store API 同样没有单独的更新接口。使用相同的 `namespace + key` 再次调用 `put_item`，就会覆盖原数据：

```python
await client.store.put_item(
    server_namespace,
    key="profile",
    value={"name": "李四", "city": "深圳", "job": "AI 工程师"},
)

updated_profile = await client.store.get_item(
    server_namespace,
    key="profile",
)
updated_profile
```

```text
{'namespace': ['users', 'user_002', 'memory'],
 'key': 'profile',
 'value': {'name': '李四', 'city': '深圳', 'job': 'AI 工程师'},
 'created_at': '2026-08-18T02:06:25.081953+00:00',
 'updated_at': '2026-08-18T02:06:25.081958+00:00'}
```

`put_item` 会整体替换原来的 `value`，不会自动合并新旧字典。

#### 删除数据

> DELETE /store/items

使用 `delete_item` 删除指定数据：

```python
await client.store.delete_item(server_namespace, key="profile")

# 通过搜索确认 profile 已被删除
result = await client.store.search_items(server_namespace)
[(item["key"], item["value"]) for item in result["items"]]
```

```text
[('preferences', {'language': '中文', 'response_style': '简洁'})]
```

最后清理示例中剩余的数据：

```python
await client.store.delete_item(server_namespace, key="preferences")
await client.store.search_items(server_namespace)
```

```text
{'items': []}
```

## 长期记忆

![长期记忆-简单设计](C:\Users\xiaolei520\Desktop\Agent开发笔记\Agent应用框架\课件\assets\长期记忆-简单处理.svg)

1. 新增检查节点`check`
   1. 检查 `runtime` 中是否存在 `store`
   2. 检查 `thread` 中是否包含 `user_id`
2. 新增提示词节点，向图状态注入系统提示词
   1. 图状态中新增系统提示词字段
   2. 提示词节点第一次加载时构建完整系统提示词，保存到图状态
3. 修改模型节点：模型节点直接读取图状态中的系统提示词
4. 新增长期记忆工具

### LangGraph API

直接编译并调用图，测试长期记忆的写入、Thread 快照、跨 Thread 读取和用户隔离。

```python
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

from langgraph_python.graphs.core_agent_graph import build_graph
from langgraph_python.states.core_agent_state import ContextSchema

# Store 保存跨 Thread 的长期记忆，Checkpointer 保存每个 Thread 的图状态
store = InMemoryStore()
checkpointer = InMemorySaver()
graph = build_graph().compile(
    store=store,
    checkpointer=checkpointer,
)

user_id = "001"
context = ContextSchema(system_prompt="尽量形成长期记忆！")
```

#### 1. 在第一个 Thread 中写入长期记忆

```python
thread_1_config: RunnableConfig = {
    "configurable": {"thread_id": "thread-001"},
    "metadata": {"user_id": user_id},
}

result = await graph.ainvoke(
    input={
        "messages": [
            HumanMessage("请记住：我最喜欢的电影是《宇宙探索编辑部》")
        ]
    },
    config=thread_1_config,
    context=context,
)
result["messages"][-1].content
```

```python
# 工具按照 user_id 将记忆写入 Store
memory_item = await store.aget(("users", user_id), key="memory")
memory_item
```

#### 2. 当前 Thread 仍然使用第一次运行时的系统提示词快照

长期记忆是在第一次运行期间才写入的，因此当前 Thread 已冻结的系统提示词中还没有这条记忆。

```python
thread_1_state = await graph.aget_state(thread_1_config)
print(thread_1_state.values["system_prompt"])
```

#### 3. 同一个用户新建 Thread，读取最新长期记忆

```python
thread_2_config: RunnableConfig = {
    "configurable": {"thread_id": "thread-002"},
    "metadata": {"user_id": user_id},
}

result = await graph.ainvoke(
    input={"messages": [HumanMessage("你知不知道我最喜欢的电影是什么？")]},
    config=thread_2_config,
    context=context,
)
result["messages"][-1].content
```

```python
thread_2_state = await graph.aget_state(thread_2_config)
print(thread_2_state.values["system_prompt"]) 
```

#### 4. 用户记忆是隔离的

```python
other_user_config: RunnableConfig = {
    "configurable": {"thread_id": "long-term-memory-thread-003"},
    "metadata": {"user_id": "002"},
}

result = await graph.ainvoke(
    input={"messages": [HumanMessage("我最喜欢的电影是什么")]},
    config=other_user_config,
    context=context,
)
other_user_state = await graph.aget_state(other_user_config)
print(other_user_state.values["system_prompt"])
result["messages"][-1].content
```

### Agent Server API

通过 LangGraph SDK 调用 Agent Server，重复验证相同的长期记忆流程。

运行以下代码前，先在终端执行 `uv run langgraph dev` 启动本地 Agent Server。

```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")
assistant_id = "46bf8031-082b-4d1d-a8df-9687787d9d40"
# 每次执行生成新用户，避免之前的测试数据影响结果
server_user_id = "003"
```

#### 1. 创建 Thread，并通过 Run 写入长期记忆

```python
# 删除所有线程，免得看晕了
threads = await client.threads.search(limit=100)
for t in threads:
    await client.threads.delete(thread_id=t['thread_id'])

server_thread_1 = await client.threads.create(
    metadata={
        "user_id": server_user_id,
        "__name__": "长期记忆测试：写入",
    }
)
server_thread_1_id = server_thread_1["thread_id"]
server_thread_1_id
```

```python
server_result = await client.runs.wait(
    thread_id=server_thread_1_id,
    assistant_id=assistant_id,
    input={
        "messages": [
            {"role": "user", "content": "请记住：我叫黑土，今年75，属虎"}
        ]
    }
)
server_result["messages"][-1]["content"] # type: ignore
```

```python
# 直接通过 Agent Server 的 Store API 检查工具写入的结果
server_memory_item = await client.store.get_item(
    ("users", server_user_id),
    key="memory",
)
server_memory_item["value"]
```

#### 2. 检查第一个 Thread 的系统提示词快照

```python
server_thread_1_state = await client.threads.get_state(server_thread_1_id)
print(server_thread_1_state["values"]["system_prompt"]) # type: ignore
```

#### 3. 同一个用户新建 Thread，读取最新长期记忆

```python
server_thread_2 = await client.threads.create(
    metadata={
        "user_id": server_user_id,
        "__name__": "长期记忆测试：跨 Thread 读取",
    }
)
server_thread_2_id = server_thread_2["thread_id"]

server_result = await client.runs.wait(
    thread_id=server_thread_2_id,
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "你知道我是谁吗？"}]}
)
server_result["messages"][-1]["content"] # type: ignore
```

```python
server_thread_2_state = await client.threads.get_state(server_thread_2_id)
print(server_thread_2_state["values"]["system_prompt"]) # type: ignore
```

#### 4. 用户记忆是隔离的

```python
other_server_thread = await client.threads.create(
    metadata={
        "user_id": f"004",
        "__name__": "长期记忆测试：用户隔离",
    }
)

server_result = await client.runs.wait(
    thread_id=other_server_thread["thread_id"],
    assistant_id=assistant_id,
    input={"messages": [{"role": "user", "content": "你知道我是谁吗？"}]}
)
other_server_state = await client.threads.get_state(other_server_thread["thread_id"])
print(other_server_state["values"]["system_prompt"]) # type: ignore
server_result["messages"][-1]["content"] # type: ignore
```

## A2A 协议

`MCP`：规定 `Agent` 如何与 `异构tool` 通信

`A2A`：规定 `Agent` 如何与 `异构Agent` 通信

![A2A 旅游多 Agent 协作](https://raw.githubusercontent.com/JJ-front/store-img/master/A2A.png)

- 通信协议：HTTP(S)
- 消息格式：JSON-RPC
- 协议官网：https://a2a-protocol.org/
- `Agent Server` 会自动帮你搭建好 `A2A` 服务器

### 创建 A2A 服务器

```python
from langgraph_sdk import get_client

client = get_client(url="http://localhost:2024")
```

```python
# 创建一个专门用于提供 A2A 服务的 assistant
assistant = await client.assistants.create(
    graph_id="agent",
    name="poet-agent", 
    description="专业诗人，可以编写古代、现代等不同风格的诗文", 
    context={
        "system_prompt": "1. 你必须使用子代理来完成诗文生成。"
                         "2. 在生成诗文的过程中你必须至少调用一次 ask_user_question 来确认需求"
    },
    metadata={
        "user_id": "a2a" # 模拟一个用户id
    }
)
assistant_id = assistant["assistant_id"]
assistant_id
```

### 访问 A2A 服务器

#### Agent Card

A2A 服务器会暴露一个URL地址，通常为：`/.well-known/agent-card.json`。

通过请求该地址，可以获取一个 `Agent Card`，它描述了如何与该 Agent 进行交流。

`Agent Server` 暴露的 URL 地址是：

`/.well-known/agent-card.json?assistant_id={assistant_id}`



## Agent部署

### 环境搭建

#### 创建容器网络

容器网络用于容器与容器之间进行通信。

```shell
docker network create local-net
```

#### 启动 PostgresSQL 容器

创建并启动PostgreSQL容器。

```shell
docker run -d \
  --name pg16 \
  --network local-net \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=123123 \
  -v pg_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16
```

#### 启动 pgAdmin

```bash
docker run -d \
  --name pgadmin4 \
  --network local-net \
  -e PGADMIN_DEFAULT_EMAIL=admin@qq.com \
  -e PGADMIN_DEFAULT_PASSWORD=123123 \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 5050:80 \
  dpage/pgadmin4
```

启动后，创建一个数据库`langgraph_db`

#### 启动 Redis 容器

```shell
docker run -d \
  --name redis7 \
  --network local-net \
  -v redis_data:/data \
  -p 6379:6379 \
  redis:7-alpine redis-server --appendonly yes
```

### 配置

#### 配置`langgraph.json`

```json
{
  "python_version": "3.13",
  "source": {
    "kind": "uv",
    "root": "."
  },
  "graphs": {
    "agent": "langgraph_python.dev:agent"
  },
  "env": ".env"
}
```

#### 配置工程使用的python版本

`.python-version`

```text
3.13
```

`pyproject.toml`

```toml
requires-python = ">=3.13"
```

```shell
uv sync
```

#### 配置环境变量

找到项目根目录下的`.env`，添加以下环境变量：

```env
DATABASE_URI=postgres://admin:123123@pg16:5432/langgraph_db
REDIS_URI=redis://redis7:6379/0
```

#### 配置`.dockerignore`

```text
.env
.git
.venv
.langgraph_api
.ruff_cache
.vscode
temp
课件
```

### 构建 Agent 镜像

```shell
make build TAG=0.1.0
```

### 启动 Agent Server 容器

```shell
docker run -d \
  --name langgraph-agent \
  --network local-net \
  --env-file .env \
  -p 8123:8000 \
  langgraph-python-agent:0.1.0
```

# langchain

## 认识 Agent

### 创建 Agent

```python
# 创建一个编译好的图
agent = create_agent(
    model="anthropic:qwen3.7-plus", # 必填，Provider:Model Name
)
```

### 选填参数

| 参数名           | 含义                                        | 默认                   |
| ---------------- | ------------------------------------------- | ---------------------- |
| `tools`          | 工具列表                                    | 无工具                 |
| `system_prompt`  | 系统提示词                                  | 无系统提示词           |
| `state_schema`   | 图状态的数据结构                            | 只有一个`messages`字段 |
| `context_schema` | context结构                                 | 无                     |
| `checkpointer`   | 检查点存储方案<br />使用AgentServer无须传递 | 无检查点               |
| `store`          | store存储方案<br />使用AgentServer无须传递  | 无store                |

## 结构化输出

### 含义

让某个`Agent`始终遵循某种`JSON`输出格式，比如：

```json
{
  "name": "张三",
  "phone": "13300001111",
  "address": "四川省成都市xxxx"
}
```

### 场景

- **信息抽取**

  ```json
  {
    "name": "张三",
    "phone": "13300001111",
    "address": "四川省成都市xxxx"
  }
  ```

- **分类或打标签**

  ```json
  {
    "category": "退款",
    "urgency": "高"
  }
  ```

- **情感分析**

  ```json
  {
    "sentiment": "负面",
    "score": 0.92,
    "reason": "用户对等待时间不满"
  }
  ```

- **生成数据库记录**

  ```json
  {
    "customer_name": "李明",
    "phone": "138...",
    "appointment_time": "2026-08-21 14:00"
  }
  ```

### 实现

```python
from pydantic import BaseModel, Field
from deepagents import create_deep_agent
from langchain.agents.structured_output import ToolStrategy

# 1. 定义输出 schema
class ArchitectureTable(BaseModel):
    """结构化架构分析输出。"""
    business_objective: str = Field(description="业务目标部分")
    success_metrics: str = Field(description="成功指标部分")
    system_impact: str = Field(description="系统影响部分")
    data_tasks: str = Field(description="数据任务部分")
    risks: str = Field(description="风险部分")
    phased_plan: str = Field(description="分阶段计划部分")

# 2. 创建 agent 时传入 response_format
agent = create_deep_agent(
    response_format=ToolStrategy(schema=ArchitectureTable), # 可选ToolStrategy、ProviderStrategy或者直接传递schema(ArchitectureTable)
)

# 3. 调用并获取结构化结果
result = agent.invoke({
    "messages": [{"role": "user", "content": "Analyze the architecture for project X"}]
})

# 4. 访问验证后的结构化输出
structured = result["structured_response"]
print(structured.business_objective)
print(structured.phased_plan)
```

- 工具调用模式（ToolStrategy）：强制让模型调用工具实现结构化输出
- 模型服务商模型（ProviderStrategy）：让模型服务商提供实现
  - 如何判断模型是否直接，查看模型接口文档生成内容接口，看以下：
  - **OpenAI**：检查模型接口是否支持 **`response_format: { type: "json_schema", ... }`**
  - **Anthropic (Claude)**：检查请求体中是否有 **`output_config`** 参数（内含 `format: { type: "json_schema", schema: ... }`

- 自动抉择模式：即直接传递schema,langchain 自动决策使用

## 中间件

使用 `Agent` 的中间件可以扩展图的能力

中间件的本质是一个继承自 `AgentMiddleware` 的类

```python
class TestMiddleware(AgentMiddleware):
  pass
```

在创建`Agent`的时候，可以将中间件的实例注入：

```python
create_agent(
	model="...",
  middleware=[TestMiddleware()] # 注入中间件
)
```

该类中的特定方法会参与到图的运行：

- `before_agent`
- `before_model`
- `after_model`
- `after_agent`
- `wrap_model_call`
- `wrap_tool_call`

每个方法称之为`钩子函数`，钩子函数分为两类：

- `节点钩子`：`before_xxx` & `after_xxx`

  所有的节点钩子会作为图节点运行

- `包裹钩子`：`wrap_xxx`

  所有的包裹钩子以洋葱模型在节点内运行

## 预置中间件



https://docs.langchain.com/oss/python/langchain/middleware/built-in



- **`ToolErrorMiddleware`（工具错误）**：捕获工具执行异常，并将其转换为模型可理解的错误消息。适合希望 Agent 自行修正参数或从工具错误中恢复的场景。
- **`ToolRetryMiddleware`（工具重试）**：在工具调用失败时自动重试，并支持指数退避。适合网络请求、外部 API 等可能暂时失败的工具。
- **`ModelRetryMiddleware`（模型重试）**：在模型调用失败时自动重试，并支持指数退避。适合处理模型服务的限流、超时或短暂不可用。
- **`ModelFallbackMiddleware`（模型降级）**：主模型调用失败时，按顺序切换到备用模型。适合需要提高可用性、实现跨厂商容灾的场景。
- **`SummarizationMiddleware`（对话摘要）**：当上下文接近限制时，将较早的对话压缩为摘要。适合长对话或历史消息较多的 Agent。

### **`HumanInTheLoopMiddleware`（人工审批）**

- 作用：在工具执行前暂停 Agent，等待人工批准、修改或拒绝。适合发送邮件、修改数据、资金交易等高风险操作。

- 中间件设计概念和使用：

  - 如何配置：

    - 中间件配置interrupt_on属性

      - 键为工具名称，值为运行的中断操作，包含：

        - approve：表示执行对应工具时需要审批
        - edit：表示执行对应工具时可以修改为其他工具调用
        - reject：只能拒绝，不允许执行该工具
        - respond：假装执行了该工具，实际没有执行，人工给回复

      - 示例：

        - ```python
          from langchain.agents.middleware import HumanInTheLoopMiddleware
          
          
          def format_description(tool_call, state, runtime):
              """根据本次工具调用动态生成审批说明。"""
              return f"即将写入文件：{tool_call['args']['file_path']}"
          
          
          def should_interrupt(request):
              """只有写入 /home/user 目录时才中断。"""
              return request.tool_call["args"]["file_path"].startswith("/home/user/")
          
          
          HumanInTheLoopMiddleware(
              interrupt_on={
                  # 调用时始终中断，允许 approve、edit、reject、respond
                  "write_file": True,
          
                  # 调用时不中断，直接执行
                  "read_file": False,
          
                  # 调用时始终中断，但只允许批准或拒绝
                  "delete_file": {
                      "allowed_decisions": ["approve", "reject"],
                      "description": "删除文件前需要人工确认。",
                  },
          
                  # 根据本次工具调用的参数，动态决定是否中断
                  "edit_file": {
                      "allowed_decisions": ["approve", "edit", "reject"],
                      "description": format_description,
                      "when": should_interrupt,
                  },
              },
              # 没有单独配置 description 时，使用这个前缀生成审批说明
              description_prefix="工具执行前需要人工审批",
          )
          ```

    - 中断消息格式

      - ```python
        {
          "action_requests": [ 	# 表示哪个工具被中断，以及工具对应的参数	
            {
              "name": "write_file",
              "args": {
                "file_path": "/home/user/notes.md",
                "content": "文件内容"
              },
              "description": "工具执行前需要人工审批……"
            }
          ],
          "review_configs": [ # 表示工具允许的操作
            {
              "action_name": "write_file",
              "allowed_decisions": ["approve", "edit", "reject", "respond"]
            }
          ]
        }
        
        ```

    - 恢复中断的消息格式

      - 批准:使用原工具名和原参数继续执行工具。

        - ```python
          {
            "decisions": [
              {
                "type": "approve"
              }
            ]
          }
          ```

      - 修改后批准

        - ```python
          {
            "decisions": [
              {
                "type": "edit",
                "edited_action": {
                  "name": "write_file",
                  "args": {
                    "file_path": "/home/user/notes.md",
                    "content": "修改后的文件内容"
                  }
                }
              }
            ]
          }
          ```

      - 拒绝:跳过本次工具执行。`message` 是可选的拒绝原因，中间件会将它作为失败的 `ToolMessage` 返回给模型

        - ```python
          {
            "decisions": [
              {
                "type": "reject",
                "message": "不允许覆盖该文件，请改用新文件名。"
              }
            ]
          }
          ```

      - 代替工具回答(response)

        - ```python
          {
            "decisions": [
              {
                "type": "respond",
                "message": "请将文件保存到 /home/user/drafts/notes.md。"
              }
            ]
          }
          ```

- **`ModelCallLimitMiddleware`（模型调用限制）**：限制单次运行或整个线程中的模型调用次数。适合防止 Agent 无限循环或调用成本失控。
- **`ToolCallLimitMiddleware`（工具调用限制）**：限制所有工具或指定工具的调用次数。适合控制高成本、高风险工具的使用频率。

### **`PIIMiddleware`（个人信息检测）**

- 作用：检测并按规则拦截、隐去、哈希或遮罩个人敏感信息。适合处理邮箱、信用卡号等隐私数据的场景。

- 能够检测哪些类型？

  - 内置检查类型

  - | 类型          | 检测内容                 |
    | ------------- | ------------------------ |
    | `email`       | 邮箱地址                 |
    | `credit_card` | 通过 Luhn 校验的信用卡号 |
    | `ip`          | IPv4 地址                |
    | `mac_address` | MAC 地址                 |
    | `url`         | URL                      |

  - 检测到了有哪些处理手段（策略）？

  - | 策略     | 作用                       | 示例                  |
    | -------- | -------------------------- | :-------------------- |
    | `redact` | 使用占位符替换             | `[REDACTED_EMAIL]`    |
    | `mask`   | 隐藏一部分，只保留末尾字符 | `**** **** **** 1111` |
    | `hash`   | 替换为稳定的哈希值         | `<ip_hash:805ebf20>`  |
    | `block`  | 抛出异常并终止 Run         | `PIIDetectionError`   |

- 处理时机是什么？

  - `PIIMiddleware` 使用的是**节点钩子**，不是 `wrap_model_call` 或 `wrap_tool_call`。

    ```text
      ...
       ↓
    before_model  ← 检查点
       ↓
    model
       ↓
    after_model   ← 检查点
       ↓
      ...
    ```

    `before_model` 和 `after_model` 都可能在一次 Run 中执行多次，因此模型输出检查针对的是**每次模型调用产生的 `AIMessage`**，而不只是 Run 的最终输出。

    | 参数                    | 默认值  | 检查对象                 | 执行位置                          |
    | ----------------------- | ------- | ------------------------ | --------------------------------- |
    | `apply_to_input`        | `True`  | 最近一条 `HumanMessage`  | `before_model`                    |
    | `apply_to_output`       | `False` | 最近一条 `AIMessage`     | `after_model`                     |
    | `apply_to_tool_results` | `False` | 工具产生的 `ToolMessage` | 下一次调用模型前的 `before_model` |

    检测到 PII 后，中间件会创建处理后的新消息，并返回 `{'messages': new_messages}` 更新图状态。因此它修改的不只是临时模型请求，最终图状态中的对应消息也会改变。

    > `block策略` 是例外：它会抛出异常并终止 Run，不会把脱敏消息写入状态。

- 代码示例：

  - 拦截模型输入（即`apply_to_input`=true）

    - 正常拦截

      - ```python
        middleware=[
            PIIMiddleware("email", strategy="redact"),
            PIIMiddleware("credit_card", strategy="mask"),
            PIIMiddleware("ip", strategy="hash"),
            PIIMiddleware("mac_address", strategy="redact"),
            PIIMiddleware("url", strategy="redact"),
        ]
        ```

      - ```python
        await run_agent(
            "pii_input",
            (
                "邮箱 zhangsan@example.com，"
                "卡号 4111 1111 1111 1111，"
                "IP 192.168.1.10，"
                "MAC 00:1A:2B:3C:4D:5E，"
                "网址 https://example.com/profile"
            ),
        )
        ```

    - 阻断报错

      - `pii_block` 使用以下配置：

      - ```python
        middleware=[
            PIIMiddleware("email", strategy="block"),
        ]
        ```

      - `block` 不会继续调用模型，而是让 Run 失败。

      - ```python
        try:
            await run_agent("pii_block", "我的邮箱是 zhangsan@example.com")
        except Exception as error:
            print(type(error).__name__)
            print(error)
        ```

    - 自定义拦截策略

      - ```python
        middleware=[
            PIIMiddleware(
                "student_id",
                detector=r"STU-\\d{6}", # 可以写函数
                strategy="redact",
            ),
        ]
        ```

      - 内置类型不能覆盖所有业务数据。例如，系统可能需要把学号当作 PII。可以通过 `detector` 提供正则表达式。`student_id` 是自定义类型名称，替换后的占位符为 `[REDACTED_STUDENT_ID]`。

  - 拦截模型输出

    - `pii_output` 使用以下配置：

    - ```python
      middleware=[
          PIIMiddleware(
              "email",
              strategy="redact",
              apply_to_input=False,
              apply_to_output=True,
          ),
      ]
      ```

    - Fake 模型会固定返回 `support@example.com`。中间件会在每次模型调用后的 `after_model` 中处理 `AIMessage`。

  - 拦截工具结果

    - ```pyth
      middleware=[
          PIIMiddleware(
              "email",
              strategy="redact",
              apply_to_input=False,
              apply_to_output=False,
              apply_to_tool_results=True,
          ),
      ]
      ```

### **`TodoListMiddleware`（待办列表）**

- 作用：为 Agent 提供任务拆分、计划和进度跟踪能力。适合需要协调多个步骤或工具的复杂任务。
  - 解决的是智能体在**长链条、多步骤任务**中容易出现的“迷失方向”或“进度不可见”的问题
- 处理机制
  - **注入专用工具（`write_todos`）**：启用该中间件后，智能体会自动获得一个名为 `write_todos` 的工具。智能体通过调用这个工具来创建、修改或标记整个待办清单。
  - **维护结构化状态（`todos`）**：清单以结构化数据的形式（包含 `content` 和 `status` 字段）存储在智能体的内部状态中。状态通常分为三种：`pending`（待处理）、`in_progress`（进行中）、`completed`（已完成）。
  - **注入系统提示词（System Prompt）**：中间件会自动在系统提示中注入指导语，告诉智能体**何时以及如何使用**这个工具。例如，提示智能体在复杂任务开始前先规划，并且每完成一步就立即标记，不要等到最后一次性标记。
  - **状态回注与进度同步**：在每次模型调用前，中间件会将当前的 `todos` 状态注入到上下文中，确保智能体“记得”自己的计划。



- **`LLMToolSelectorMiddleware`（工具筛选）**：先使用一个模型筛选与当前任务相关的工具，再调用主模型。适合工具数量较多，需要减少上下文消耗并提高选择准确性的 Agent。
- **`ProviderToolSearchMiddleware`（厂商工具搜索）**：将部分工具延迟加载，由模型厂商的服务端搜索按需返回。适合支持工具搜索的模型与大规模工具集。
- **`ShellToolMiddleware`（Shell 工具）**：为 Agent 提供持久的 Shell 会话以执行系统命令。适合开发、部署、测试和脚本自动化，使用时需配置合适的隔离策略。

### **`FilesystemMiddleware`（文件系统）**：

- 作用：为 Agent 提供列出、读取、写入和编辑文件的能力，也可配置持久存储。适合用文件保存上下文、产物或长期记忆的 Agent。

  - 实际是充当一个“可插拔的虚拟文件系统层”。它本身不直接存储文件，而是通过委托给不同的“后端”来工作，并在此过程中负责工具的动态过滤和上下文管理
  - ![](https://raw.githubusercontent.com/JJ-front/store-img/master/Filesystem中间件.png)
  
- 中间件设计概念：

  - **什么是“后端“？**

    - 实际就是一个py类，但是该类需要满足backend protocal协议，即需要提供以下方法的实现（同步版本和异步版本至少满足一套）：
      - **`ls`**: 列出目录内容。
      - **`read_file`**: 读取文件内容。
      - **`write_file`**: 创建或覆盖文件。
      - **`edit_file`**: 对文件进行精确的字符串替换。
      - **`glob`**: 按模式查找文件。
      - **`grep`**: 在文件中搜索文本。
      - **`delete`**: 删除文件或目录（视后端支持情况而定）。
      - **`upload_files`**：批量上传二进制文件到后端，支持部分成功
      - **`download_files`**：从后端批量下载文件，同样支持部分成功
    - 在deepAgent中，官方已经内置了很多后端：[后端 | LangChain 中文文档](https://langchain-doc.cn/v1/python/deepagents/backends.html#quickstart)
      - 其中sandbox后端还需要实现方法：
        - **`execute`**：在沙箱中执行 Shell 命令，返回输出和退出码
  
  - **后端路由**
  
    - ```python
      
      from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend
      
      agent = create_deep_agent(
          model=model,
          system_prompt=system_prompt,
          backend=CompositeBackend( # 混合后端
              default=StateBackend(), # 默认使用StateBackend
              routes={
                  "/static/": FilesystemBackend( # 匹配到这个路径的文件，则使用FilesystemBackend
                      root_dir="/Users/yuanjin/工作/课/录播课/AI/langchain-python/temp"
                  )
              },
          ),
      )
      
      ```
  
  - **文件操纵权限**：
  
    - ```python
      permissions = [
          # 禁止读取环境变量文件
          FilesystemPermission(
              operations=["read"],
              paths=["/home/user/workspace/.env", "/home/user/workspace/.env.*"],
              mode="deny",
          )
      ]
      
      FilesystemMiddleware(
          _permissions=permissions,
      )
      ```

    - 每条 `FilesystemPermission` 包含三个配置项：

      - `operations`：要限制的操作类型，可选 `read`、`write`

        | 操作类型 | 对应工具                            |
        | -------- | ----------------------------------- |
        | `read`   | `ls`、`read_file`、`glob`、`grep`   |
        | `write`  | `write_file`、`edit_file`、`delete` |
  
      - `paths`：要匹配的绝对路径，使用 POSIX 风格的 Glob 模式
  
      - `mode`：匹配后的处理方式，可选 `allow`、`deny`（拒绝）、`interrupt`（需要审批）

    - 匹配顺序

      - 权限规则按照声明顺序匹配，**第一条匹配的规则生效**。如果没有任何规则匹配，默认允许访问。
  
      - 因此，范围更具体的规则应该写在范围更大的规则前面：
  
        - ```PYTHON
          permissions = [
              # 先保护特殊文件
              FilesystemPermission(
                  operations=["read"],
                  paths=["/home/user/workspace/.env"],
                  mode="deny",
              ),
          
              # 再允许访问整个工作目录
              FilesystemPermission(
                  operations=["read", "write"],
                  paths=["/home/user/workspace/**"],
                  mode="allow",
              ),
          ]
          ```
  
      - 如果将 `allow /home/user/workspace/**` 放在前面，读取 `/home/user/workspace/.env` 时会先匹配 `allow`，后面的 `deny` 不会生效。
  
    - execute 逃逸
  
      - 如果`FilesystemMiddleware`提供了`execute`工具，则模型可能利用`execute`工具实现权限逃逸。比如Shell 命令可以通过 `cat`、`cp`、`rm` 等命令访问文件，绕过内置文件工具的权限检查。
      - 因此，当前版本不允许直接组合以下配置：
  
        - ```python
          create_deep_agent(
              backend=sandbox_backend,
              permissions=permissions,
          )
  

- **`SubAgentMiddleware`（子 Agent）**：允许主 Agent 将任务交给子 Agent，并隔离各自的上下文。适合需要分工、专业化处理或避免主上下文膨胀的复杂任务。

### **`RubricMiddleware`（评分标准，Beta）**

- 作用：让 Agent 按预设标准自我评估并反复改进，直到达标或达到最大迭代次数。适合具有明确质量标准的内容生成、代码生成等任务。
  - 当任务有明确的成功标准时（例如“代码必须通过测试”、“报告必须包含所有规定章节”），Agent 的首次输出往往“方向对了但没完全到位”。`RubricMiddleware` 的作用就是**把“差不多”变成“必须过”**，
- 作用机制：
  - 它的工作机制是一个 **“生成 → 评分 → 修正”** 的闭环，关键设计在于**职责分离**：
    1. **声明标准（Rubric）**：调用时传入一个字符串形式的 Rubric，例如“代码必须通过所有测试”或“输出必须包含三个指定部分”。中间件只有在收到 Rubric 时才会被激活。
    2. **生成输出**：主 Agent 正常执行任务并给出一个它认为“完成”的结果。
    3. **独立评分（Grader Sub-Agent）**：一旦主 Agent 准备结束（不再调用工具），中间件会启动一个**独立的评分器子 Agent**。这个评分器**不会盲目推理**，它可以被配置工具（如测试运行器、Linter）来**收集硬证据**，然后逐条对照 Rubric 进行判定。
    4. **结构化反馈与迭代**：
       - 如果评分器判定为 `needs_revision`（需要修改），它会给出**逐条、具体的 `gap` 反馈**（例如“测试 test_unhashable 失败，遇到不可哈希类型时崩溃”），而不是笼统的“再试试”。
       - 这条反馈会以合成消息的形式注入回主 Agent 的对话中，**主 Agent 看到具体问题后重新修改**，再次提交给评分器审查。
    5. **终止条件**：循环在以下任一情况发生时结束：
       - **`satisfied`**：所有标准均通过。
       - **`max_iterations_reached`**：达到设定的迭代上限（默认通常为 3，硬上限 20）。
       - **`failed`**：Rubric 本身格式错误或无法评估。
       - **`grader_error`**：评分器自身出错（如模型超时）。



- **`FilesystemFileSearchMiddleware`（文件搜索）**：为 Agent 提供 Glob 文件匹配和 Grep 内容搜索工具。适合在大型代码库或文件集中定位文件与内容。
- **`ContextEditingMiddleware`（上下文编辑）**：当上下文过长时，清理较早的工具调用结果并保留最近结果。适合工具调用频繁的长时间对话，可减少 token 消耗。
- **`LLMToolEmulator`（工具模拟）**：使用模型生成模拟的工具返回结果，代替真实工具执行。适合外部工具尚未实现、不可用或调用成本较高时进行测试与原型验证。

## 阶段总结

`LangChain` 基于 `LangGraph` 构建，它提供了以下核心功能：

1. 统一了模型和消息的外观，从而屏蔽了不同模型服务商的差异
2. 提供了便捷的工具封装能力
3. 基于`LangGraph`构建了`Agent`工作流
   1. 提供了`response_format`实现消息结构化
   2. 提供了强大灵活的中间件机制，并预设了大量中间件



# deepAgent

deepAgent就是在langChain的基础上，把许多的预设中间件内置进去了，同时也提供了自己的一些中间件进去

## 内置中间件一`PatchToolCallsMiddleware`

- 作用：这个中间件专门用来修复消息历史中的“悬空工具调用”（dangling tool calls）

- 场景：当 Agent 发出一个工具调用请求（AIMessage），但在工具真正执行或返回结果之前，因为某些原因（比如用户发了新消息、用户暂停回复）导致这个调用没有对应的工具返回结果（ToolMessage）时，就会出现“悬空”。

  - 导致的问题？

    - 许多主流模型提供商（尤其是 **Google Gemini**）强制要求请求中每个 `tool_calls` 都必须有对应的 `tool` 响应，数量不匹配会直接拒绝请求。 例如，OpenAI 会返回类似这样的错误：

      > ```
      > An assistant message with 'tool_calls' must be followed by tool messages responding to each 'tool_call_id'.
      > ```

    - 就算没有错误，因为这一条消息没有回复，也会导致模型不理解为什么没有回复，从而出现幻觉

- 中间件如何处理的？
  - **注入**一条合成的 ToolMessage 作为“占位结果”
  - 处理时机是啥？
    - 每一次run之前的**`before_agent`**钩子，扫描并修补整个消息历史

## 内置中间件二FilesystemMiddleware

看langChain的即可 一样

## E2B

### 什么是E2B

E2B 是一个开源的基础设施平台，主要用途是为 AI Agent（AI 智能体）提供安全、隔离的云端沙箱环境，让它们能安全地执行代码、运行命令和调用工具,从而不避免安全问题

![](https://raw.githubusercontent.com/JJ-front/store-img/master/沙箱.png)

函数计算：https://www.aliyun.com/product/fc

region对照表：https://help.aliyun.com/zh/ecs/user-guide/regions-and-zones

### 安装 E2B 依赖

```python
!uv add e2b
```

### 沙箱管理

#### 创建沙箱

```python
from langchain_python.core.config import sandbox_settings

sandbox_settings
```

```python
from e2b import AsyncSandbox

# 准备好沙箱配置
basic_config = {
    "timeout": 300, # 从创建开始计时，时间到了自动销毁
    "api_key": sandbox_settings.api_key,
    "api_url": sandbox_settings.api_url,
    "domain": sandbox_settings.domain,
}

sandbox = await AsyncSandbox.create(
    template=sandbox_settings.template,
    **basic_config,
) 
sandbox.sandbox_id
```

#### 连接已有沙箱

```python
sandbox = await AsyncSandbox.connect(
    sandbox_id=sandbox.sandbox_id, 
    **basic_config
)
sandbox.sandbox_id
```

#### 手动销毁沙箱

```python
await sandbox.kill()
```

#### 手动刷新时间

```python
await sandbox.set_timeout(300) # 从现在起再重新计时300秒后销毁
```

### 沙箱操作

#### 文件读写

```python
sandbox = await AsyncSandbox.create(
    template=sandbox_settings.template,
    **basic_config
) 
```

```python
file_path = "/home/user/workspace/test.txt"
await sandbox.set_timeout(300)
await sandbox.files.write(file_path, "Hello World!")
```

```python
await sandbox.set_timeout(300)
await sandbox.files.read(file_path)
```

#### 命令执行

```python
await sandbox.set_timeout(300)
await sandbox.commands.run("node --version")
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run("npm init -y", cwd="/home/user/workspace")
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run("ls", cwd="/home/user/workspace", timeout=60)
```

### 挂载 OSS

```python
import json
metadata_config = {
    "metadata":{
        "fc.sandbox.storage.oss": json.dumps({
            "mountPoints": [
                {
                    "bucketName": sandbox_settings.oss_bucket,
                    "mountDir": "/home/user/workspace",
                    "bucketPath": "/e2b-test/workspace",
                    "endpoint": sandbox_settings.oss_endpoint,
                    "readOnly": False,
                },
                {
                    "bucketName": sandbox_settings.oss_bucket,
                    "mountDir": "/home/user/output",
                    "bucketPath": "/e2b-test/output",
                    "endpoint": sandbox_settings.oss_endpoint,
                    "readOnly": False,
                }
            ]
        }),
        "fc.sandbox.auth.role": sandbox_settings.role_arn,
    }
}
```

```python
# 创建沙箱
sandbox = await AsyncSandbox.create(
    template=sandbox_settings.template,
    **basic_config, # type: ignore
    **metadata_config
)
```

```python
# 创建文件
await sandbox.set_timeout(300)
await sandbox.files.write("/home/user/workspace/source.txt", "source")
await sandbox.files.write("/home/user/output/output.txt", "output")
```

```python
await sandbox.kill()
```

```python
# 新建沙箱
sandbox = await AsyncSandbox.create(
    template=sandbox_settings.template,
    **basic_config, # type: ignore
    **metadata_config
)
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run("ls", cwd="/home/user/workspace")
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run("ls", cwd="/home/user/output")
```

### 沙箱实战

```python
# 创建沙箱
sandbox = await AsyncSandbox.create(
    template=sandbox_settings.template,
    **basic_config, # type: ignore
    **metadata_config
)
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run(
    "npm create vite@latest my-vue-app -- --template vue --no-interactive", cwd="/home/user/workspace"
)
await sandbox.set_timeout(300)
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run(
    "npm i", cwd="/home/user/workspace/my-vue-app"
)
await sandbox.set_timeout(300)
```

```python
await sandbox.files.write("/home/user/workspace/my-vue-app/vite.config.js", """
import vue from '@vitejs/plugin-vue';
import { defineConfig } from 'vite';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '',
});
""")
```

```python
await sandbox.set_timeout(300)
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run(
    "npm run build", cwd="/home/user/workspace/my-vue-app"
)
await sandbox.set_timeout(300)
```

```python
await sandbox.set_timeout(300)
await sandbox.commands.run(
    "cp -a /home/user/workspace/my-vue-app/dist /home/user/output/my-vue-app"
)
await sandbox.set_timeout(300)
```

```python
await sandbox.kill()
```

## 沙箱隔离方案

![](https://raw.githubusercontent.com/JJ-front/store-img/master/沙箱隔离.png)

这个key可以是线程，也可以是用户id,从而保证隔离性，看需求而定

## 实现服务端CodingAgent

```mermaid
flowchart TD
    User["用户提出编码需求"] --> Agent["Coding Agent<br/>模型分析、规划并决定调用工具"]

    subgraph Develop["开发阶段：Deep Agent 内置能力"]
        Tools["文件工具<br/>ls / read / write / edit / glob / grep<br/><br/>命令工具<br/>execute"]
        Backend["自定义 AliyunSandboxBackend"]
        Tools -->|"调用后端接口"| Backend
    end

    Agent -->|"反复调用"| Tools
    Backend -->|"get_sandbox(thread_id)"| Sandbox["阿里云 Sandbox<br/>读写文件、执行命令"]
    Sandbox -->|"工具执行结果"| Agent

    OSS[("OSS")]
    Sandbox <-->|"运行期间挂载并同步<br/>/home/user/workspace"| OSS

    Agent -->|"完成开发后调用"| Deploy["自定义 deploy 工具<br/>复制、校验产物并生成访问 URL"]
    Deploy -->|"取得同一个 Sandbox<br/>复制产物到 /home/user/output"| Sandbox
    Sandbox -->|"output 目录同步"| OSS
    OSS -->|"产物持久化完成"| Deploy
    Deploy -->|"部署成功后<br/>sandbox.kill()"| Destroy["销毁 Sandbox"]
    Deploy -->|"返回产物 URL"| Agent

    Agent -->|"基于部署结果生成"| Format["Response Format<br/>CodingAgentResponse"]
    Format --> Result["向用户返回<br/>status + summary + artifacts"]

    style Agent fill:#dbeafe,stroke:#2563eb
    style Tools fill:#f3e8ff,stroke:#9333ea
    style Backend fill:#f3e8ff,stroke:#9333ea
    style Sandbox fill:#dcfce7,stroke:#16a34a
    style OSS fill:#fef3c7,stroke:#d97706
    style Deploy fill:#fee2e2,stroke:#dc2626
    style Destroy fill:#f1f5f9,stroke:#64748b
    style Format fill:#dbeafe,stroke:#2563eb
    style Result fill:#dbeafe,stroke:#2563eb
```



### 实现阿里云沙箱后端

交给AI实现

### Deploy工具

```python
@tool(args_schema=DeployInput)
async def deploy(
    path: str,
    target_dirname: str,
    entry_files: list[str],
) -> list[str]:
    """
    把沙箱内的文件或目录部署到云存储，并返回入口文件的访问地址。

    调用示例：
    deploy(
    	path="/home/user/workspace/my-vue-app/dist", 
    	target_dirname="my-vue-app", 
    	entry_files=["index.html"]
    )

    返回示例：
    [
        "https://deploy.com/a2e9d7d8/output/my-vue-app/index.html"
    ]
    """

# 工具参数说明
class DeployInput(BaseModel):
    path: str = Field(
        description="沙箱内的产物路径，它可以是文件夹，也可以是文件。\n"
        "这些路径表示要最终交付给用户的产物。\n"
        "比如："
        '"/home/user/workspace/my-vue-app/dist"\n'
        '"/home/user/workspace/my-vue-app/assets/charts.png"\n'
        '"/home/user/workspace/my-vue-app/other.tar.gz"\n'
        "如果指定的是目录，该工具会自动递归读取该目录下的所有文件进行部署"
    )
    target_dirname: str = Field(
        description="部署的目标目录名称。\n"
        "该工具会把path指定的产物放到云存储的某个存储路径中。\n"
        "存储路径是： <前缀>/<target_dirname>/。"
        "前缀是什么你无需关心，你只需要指定target_dirname即可。\n"
        "建议该值直接取用workspace中的工程名字"
    )
    entry_files: list[str] = Field(
        min_length=1,
        description="指定部署完成过后，要访问的入口文件名称。\n"
        '比如：["index.html"、"chart.png"]',
    )
```

### 系统提示词

```text
# 角色

你是一个专门用于编写代码的 Agent。

# 产物交付边界

- 平台只提供**静态资源部署**功能。
- 最终能够部署和交付给用户的代码产物必须由静态文件组成，例如 HTML、CSS、JavaScript、图片、配置文件，或者可构建为静态文件的 Vue 等前端工程。
- 沙箱具备编写、构建和临时运行后端服务的能力，但平台**没有提供后端服务的部署功能**。

## 无法交付的需求

如果用户要求交付依赖以下能力的应用：

- 服务器端 API
- 数据库
- 后端身份认证
- 后台定时任务
- 需要持续运行的服务进程

你必须直接说明相关后端部分无法部署和交付，并拒绝实现无法交付的后端部分。不要将这一限制描述为沙箱没有后端开发能力。

# 沙箱环境

整个文件系统都运行在沙箱中。

## 工程目录

- `/home/user/workspace` 是用于创建工程的根目录。
- 每个工程都应在该目录下创建独立的子目录。
- 子目录名称应根据工程内容合理命名。
- 例如，Vue 工程可以创建在 `/home/user/workspace/my-vue-app` 中，其中 `my-vue-app` 是工程名称。

## 可用工具

沙箱中已经提供：

- Node.js 环境
- Python 环境
- Git
- Tar

你可以使用这些工具搭建、构建、检查和整理工程。

## 产物打包

如果产物文件较多，可以使用 Tar 将整个工程打包成 `.tar.gz` 压缩包，并将压缩包作为最终产物提供给用户。

## 静态资源访问路径

- 使用工程构建静态产物时，必须特别注意静态资源的访问路径。最终产物会部署在多层子目录下，因此静态资源应优先使用相对路径作为前缀，不要使用以 `/` 开头的绝对路径，否则资源可能无法访问。
- 例如，应使用 `<script src="./assets/index.js"></script>` 或 `<img src="./assets/logo.png">`，而不要使用 `<script src="/assets/index.js"></script>` 或 `<img src="/assets/logo.png">`。
- 使用 Vite 等构建工具时，应进行对应配置。例如 Vite 应将 `base` 设置为 `"./"`，确保构建后的 JavaScript、CSS 和图片通过相对路径加载。

## 产物部署与交付

- 每次完成用户交付的工作后，都必须调用 `deploy` 工具部署最终产物。
- 调用时，`path` 应指向已经检查或构建完成的文件或目录，`target_dirname` 应使用工程名称，`entry_files` 应列出需要交付给用户的入口文件。
- 只有 `deploy` 调用成功并返回访问地址后，才算完成交付。最终回复中必须把这些访问地址提供给用户。
```

### 格式化输出

```python
class DeployedArtifact(BaseModel):
    """已通过deploy工具部署的一个产物入口。"""

    name: str = Field(description="产物名称，例如首页或源码压缩包")
    mime_type: str = Field(
        description="产物的MIME类型，例如text/html、image/png或application/gzip"
    )
    url: str = Field(description="deploy工具返回的产物访问地址")


class CodingAgentResponse(BaseModel):
    """Coding Agent交付给用户的最终结构化响应。"""

    status: Literal["completed", "cannot_deliver"] = Field(
        description=(
            "已完成并部署产物时使用completed；"
            "需求超出平台交付能力时使用cannot_deliver"
        )
    )
    summary: str = Field(description="向用户说明完成内容或无法交付原因的简要总结")
    artifacts: list[DeployedArtifact] = Field(
        default_factory=list,
        description="deploy工具返回的全部产物入口；无法交付时为空列表",
    )
```

## 内置中间件三HumanInTheLoopMiddleware

看langChain的对应即可

## 多模态消息

### 多模态信息位置

- `ToolMessage`
- `HumanMessage`
- `AIMessage`：没有特殊处理，不做讨论
- `SystemMessage`：几乎不可能发生

### 多模态的核心问题

#### **消息格式问题**

发生在工具节点，当读取一张图片、pdf等文件后，应该构建一条多模块的消息格式



#### **模型能力问题**

不是所有模型都支持多模态，遇到不支持多模态的模型，应该重排消息，以避免请求报错。



这两件事情，Deep Agent已通过`FilesystemMiddleware`和`UnsupportedContentMiddleware`自动帮你处理好。

#### 如何处理的？

- 当工具读取图片或 PDF 时，`FilesystemMiddleware` 并非直接把原始数据丢进消息上下文。

  - **Blob 存储与指针替代**：如果开启了 `offload_binary_reads` 选项，中间件会把二进制数据存到后端文件系统的 `/blobs/` 目录下（按 SHA-256 哈希命名），并在消息中只保留一个轻量的指针，而不是体积庞大的 base64 数据。

- 处理模型不支持多模态的逻辑，已经被从 `FilesystemMiddleware` 中**剥离出来**，放入了专门的 `UnsupportedContentMiddleware`

  - **动态过滤**：这个中间件会在每次模型请求前，根据**当前实际使用的模型**（考虑到了模型动态切换的情况）来判断哪些多模态内容是不支持的。

    - 如何判断的呢？

      - `FilesystemMiddleware`会使用`wrap model hook`拦截消息块中的文件相关消息快，它会根据模型能力，决定是否给予模型相应文件消息。

        它的判断依据主要来自于模型对象的`profile`属性

        ```python
        profile = {
            # 是否支持对应输入类型
            "image_inputs": True,
            "pdf_inputs": True,
            "audio_inputs": False,
            "video_inputs": False,
        
            # 是否允许媒体出现在工具结果 ToolMessage 中
            "image_tool_message": False,
            "pdf_tool_message": True,
        }
        # 没有声明则表示支持
        ```

  - **替换而非报错**：对于不支持的图片、PDF 等 block，它不会直接丢弃导致逻辑断裂，而是将其**替换为一段文字提示**（text notice），然后才发送请求。原始的多模态内容仍保留在线程中，一旦你切换到支持该多模态的模型，内容会再次被发送

### 工具节点产出

`FilesystemMiddleware`会使用`wrap tool hook`提供诸多文件处理工具，同时为了支持多模态，也会针对性的返回相应的`ToolMessage`

![](https://resource.duyiedu.com/yuanjin/202608281302604.svg)

## 内置中间件四 skillsMiddleware

- 作用：解决的是**如何让 Agent 在不占用过多上下文窗口的前提下，高效管理和使用大量专门技能（Skills）** 的问题。

  - 核心处理逻辑是**渐进式披露（Progressive Disclosure）**：不一次性加载所有技能细节，而是先给 Agent 看“菜单”，需要时再“点菜”读取完整内容

- 一些概念：

  - Skills 文件结构

    - https://agentskills.io/specification

    - ```python
      skills
      └── skill-1/
            ├── SKILL.md          # 必须: metadata + instructions
            ├── scripts/          # 可选: 可执行的代码
            ├── references/       # 可选: 包含一些额外的文档，Agent可以在需要时阅读。
            ├── assets/           # 可选: 图片、schemas、...
            └── ...               # 任意其他文件
      └── skill-2/
            ├── SKILL.md          # 必须: metadata + instructions
            ├── scripts/          # 可选: 可执行的代码
            ├── references/       # 可选: 包含一些额外的文档，Agent可以在需要时阅读。
            ├── assets/           # 可选: 图片、schemas、...
            └── ...               # 任意其他文件
      ```

  - Skills 后端选型

    | 存储方案 | 功能                     |
    | -------- | ------------------------ |
    | 沙箱     | 拥有全部功能             |
    | 其他     | 除执行之外的其他所有功能 |

- 处理流程：渐进式披露



```mermaid
flowchart TD
    A["create_deep_agent(skills=...)"] --> B["创建 SkillsMiddleware"]
    B --> C["before_agent / abefore_agent"]
    C --> D["扫描每个 source 的直接子目录"]
    D --> E["批量下载 */SKILL.md"]
    E --> F["解析 YAML Frontmatter"]
    F --> G["同名 Skill：后面的 source 覆盖前面的"]
    G --> H["写入 state.skills_metadata"]
    H --> I["每次调用模型前 wrap_model_call"]
    I --> J["将 Skill 列表注入 System Message"]
    J --> K{"模型判断 Skill 是否适用"}
    K -- 否 --> L["正常回答或调用其他工具"]
    K -- 是 --> M["调用 read_file 读取完整 SKILL.md"]
    M --> N["模型遵循 Skill 指令"]
    N --> O["读取辅助文件 / 调用工具 / 执行脚本"]
    O --> P["产生最终回答"]
```

## MCP工具注入

```PYTHON
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    connections={
        "langchain_mcp": {
            "transport": "streamable_http",
            "url": "https://docs.langchain.com/mcp",
        }
    },
    tool_name_prefix=True # 是否使用MCM名字拼接到tools名字前，防止重名
)
tools = await client.get_tools()
```

## 内置中间件五MemoryMiddleware

- 作用：解决的是**上下文窗口有限、会话结束后信息丢失、以及记忆注入与压缩时机错位**这三类问题。
- 处理机制
  - 拦截请求，做“回忆”与“保存”
    - **前置回忆**：在模型执行前，中间件根据当前用户输入，从外部适配器（如内存、Redis、mem0）中检索相关记忆，并注入到系统提示词中
    - **后置保存**：在流式响应结束后，延迟保存这一轮完整的用户-助手对话，提取事实或偏好并持久化，且不阻塞响应流。
  - deepAgent从 `AGENTS.md` 等文件加载记忆注入系统提示，并增加了信任验证引导与缓存控制。

## 上下文压缩

上下文压缩是指通过技术手段精简上下文内容，同时保证语义连贯。

上下文压缩的介入点主要有两个：

- **新消息防爆**：需要立即处理的新消息
- **上下文摘要**：需要处理的旧消息

### 新消息防爆

> 新消息防爆的处理特点是：
>
> 1. 针对的是新产生的消息
> 2. 处理是立即发生的
>
> 新消息代表着目前模型正在工作的内容，处理起来要非常谨慎，绝不能打破消息之间的因果关系。

#### 工具返回防爆

主要手段是：**窗口控量，卸载兜底**

##### 窗口控量

那些容易造成大结果的工具，需要通过参数让模型不要一次性拿完整结果。

比如`read_file`工具提供`offset`和`limit`，并给予了参数默认值

##### 卸载兜底

若工具返回超过了阈值，直接卸载。

```
[卸载后的结果] + [完整结果引用] → 模型
```



> 卸载兜底功能已由`FilesystemMiddleware`中间件实现。
>
> 你可以配置工具的卸载阈值
>
> ```python
> FilesystemMiddleware(
> tool_token_limit_before_evict=20000
> )
> ```


> 你可以配置特殊
>
> ```python
> backend=CompositeBackend(
> default=...,
> routes={},
> # 可配置 Deep Agent 内部产物的保存根目录
> artifacts_root="/home/user/workspace/.deepagents",
> )
> ```



#### 用户消息防爆

用户消息超过阈值，直接卸载

> 卸载兜底功能已由`FilesystemMiddleware`中间件实现。
>
> 你可以配置用户消息的卸载阈值
>
> ```python
> FilesystemMiddleware(
> 	human_message_token_limit_before_evict=50000
> )
> ```


```python
from langgraph_sdk import get_client

client = get_client(url="http://127.0.0.1:2024")

assistant_id = 'bc46c028-583a-563c-8327-8ab22872af90'
# 创建新线程
thread = await client.threads.create(metadata={"__name__": "用户消息卸载"})
thread_id = thread["thread_id"]
thread_id, assistant_id
```

```text
('01a05bd2-25aa-70d2-acef-7e8a51bf8382',
 'bc46c028-583a-563c-8327-8ab22872af90')
```

```python
resp = await client.runs.wait(
    input={
        "messages":[
            {
                "role":"user",
                "content": "\n".join([f"第{i}条消息" for i in range(1, 100000)])
            }
        ]
    },
    thread_id=thread_id, 
    assistant_id=assistant_id
)
```

> 思考：
>
> 1. 系统提示词过大要不要立即处理？
> 2. 工具参数过大要不要立即处理？
> 3. AI回复的普通消息要不要立即处理？

### 上下文摘要

上下文摘要只处理旧消息，它会让旧的因果关系变得模糊。

但由于它是旧的因果关系，因此这种模糊对整个会话的影响较小。

#### 处理旧的特殊工具参数

在Agent运行期间，有两个特殊工具调用：

- `write_file`：传入的新内容可能过大
- `edit_file`：传入的旧内容和新内容都可能过大

这两个工具都有共同特点：

- 工具的执行后，有价值的结果已落入文件
- 模型往往关心的是文件当下的状态，而工具的调用历史只代表改动过程
- 工具调用和工具返回的结果本身的因果关系就是暗淡的

```python
summarization_middleware = SummarizationMiddleware(
    model=model,
    backend=backend,

    # 旧工具调用参数卸载配置
    truncate_args_settings={
        # 对话达到模型上下文窗口的 85% 时，开始检查旧工具调用参数
        "trigger": ("fraction", 0.85),

        # 最近 10% 的上下文中的工具参数保持完整
        "keep": ("fraction", 0.10),

        # 单个参数字符串超过 2000 个字符才卸载
        "max_length": 2_000,

        # 卸载后的提示文字
        "truncation_text": "...(argument truncated)",
    },
)
```

#### 处理整个上下文中的旧消息

```python
summarization_middleware = SummarizationMiddleware(
    model=model,
    backend=backend,

    # 整个对话达到模型上下文窗口的 85% 时触发摘要
    trigger=("fraction", 0.85),

    # 摘要时保留最近 10% 的上下文不参与摘要
    keep=("fraction", 0.10),
)
```

```python
assistant_id = '58534c12-9bc2-5cd2-b195-be42dfcd1f1f'
# 创建新线程
thread = await client.threads.create(metadata={"__name__": "历史上下文摘要"})
thread_id = thread["thread_id"]
thread_id, assistant_id
```

```text
('01a05bea-22bc-79f0-8ff6-c40e98bdbc46',
 '58534c12-9bc2-5cd2-b195-be42dfcd1f1f')
```

```python
messages = []

# 构造约 8.6 万 tokens 的历史对话：超过 85% 的摘要阈值，但摘要后只保留最近 10%
for round_id in range(1, 11):
    user_context = "\n".join(
        f"第{round_id}轮需求记录{i}：报表需保留订单编号、客户名称、销售额和退款状态。"
        for i in range(1, 426)
    )
    assistant_context = "\n".join(
        f"第{round_id}轮处理记录{i}：已核对字段映射、异常值规则和汇总口径。"
        for i in range(1, 426)
    )
    messages.extend([
        {"role": "user", "content": user_context},
        {"role": "assistant", "content": assistant_context},
    ])


messages
```

```python
resp = await client.runs.wait(
    input={
        "messages":messages
    },
    thread_id=thread_id, 
    assistant_id=assistant_id
)
```

## 内置中间件六TodoListMiddleware

看langChain

## 内置中间件七RubricMiddleware

看langChain
