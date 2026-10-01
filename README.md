# Hello GitHub

一个写给编程新手的小小开源项目。

它很简单：运行一下，它会向你打招呼；再给它两个数字，它还能顺手帮你做加法。

```
$ python hello_github.py
Hello, GitHub! 欢迎来到开源世界。
想试试加法？运行：python hello_github.py 3 5

$ python hello_github.py 3 5
3 + 5 = 8
```

---

## 这个项目能做什么

| 功能 | 怎么用 | 效果 |
| --- | --- | --- |
| 打招呼 | `python hello_github.py` | 输出一句问候语 |
| 加法计算 | `python hello_github.py 3 5` | 输出 `3 + 5 = 8` |

支持整数和小数，负数也没问题：

```
$ python hello_github.py 1.5 2.25
1.5 + 2.25 = 3.75

$ python hello_github.py -7 2
-7 + 2 = -5
```

---

## 怎么运行

### 第一步：确认电脑上有 Python

打开终端（Windows 用 PowerShell 或 CMD，macOS / Linux 用 Terminal），输入：

```bash
python --version
```

如果显示了版本号（例如 `Python 3.13.0`），说明已经有了，跳到下一步。

如果提示「不是内部或外部命令」「command not found」，说明还没装：

- 去 <https://www.python.org/downloads/> 下载安装包
- **Windows 用户注意**：安装时务必勾选 **Add Python to PATH**，否则装完还是找不到命令
- 装完关掉终端重新打开，再执行一次 `python --version` 确认

> 本项目的代码只需要 Python 3.6 以上版本，**不需要安装任何第三方库**。

### 第二步：把代码下载到本地

**方式一：直接下载压缩包（推荐新手）**

1. 打开本项目页面，点右上角绿色的 **Code** 按钮
2. 选择 **Download ZIP**
3. 解压到你喜欢的位置，比如桌面

**方式二：用 git 克隆（如果你已经装了 git）**

```bash
git clone https://github.com/old6-six6/hello-github.git
```

### 第三步：运行

先进入项目文件夹：

```bash
cd hello-github
```

然后运行：

```bash
python hello_github.py
```

看到 `Hello, GitHub! 欢迎来到开源世界。` 就成功了。

想试试加法，在后面加上两个数字：

```bash
python hello_github.py 3 5
```

---

## 项目文件说明

```
hello-github/
├── hello_github.py   主程序，所有代码都在这里
├── README.md         你现在正在看的这份说明
├── LICENSE           开源许可证（MIT）
└── .gitignore        git 的忽略清单，告诉 git 哪些文件不用上传
```

整个程序只有 50 行左右，而且每一段都有中文注释。如果你想学 Python，可以直接打开 `hello_github.py` 读一读，看不懂的地方不影响使用。

---

## 常见问题

**Q：提示 `python: command not found` 或 `'python' 不是内部或外部命令`**

A：Python 没装好，或者没加进系统 PATH。Windows 重装时记得勾选 **Add Python to PATH**。

**Q：Windows 上提示 `'python' 不是...`，但我知道自己装了 Python**

A：试试用 `py` 代替 `python`，例如 `py hello_github.py`。Windows 上有时是这个名字。

**Q：输出出现乱码**

A：这是终端编码的问题，不影响程序本身。Windows 用户可以先用 `chcp 65001` 把终端切成 UTF-8 再运行。

**Q：输入 `abc` 这种不是数字的东西会怎样**

A：程序会友好地提醒 `参数必须是数字哦`，不会崩溃。

**Q：能算乘法或者减法吗**

A：目前还不能。不过欢迎你自己动手改一改——这正是开源最好玩的地方。

---

## 我想参与改进

非常欢迎！哪怕你刚开始学编程也没关系。

在 GitHub 上你可以：

- 点右上角的 **Star** ⭐ 表示喜欢
- 点 **Issues** 提出建议或报告问题
- 点 **Fork** 把项目复制到你自己的账号下，改完后发起 **Pull Request** 把你的改动贡献回来

---

## 许可证

本项目使用 [MIT License](LICENSE)，你可以自由地使用、修改和分发。

---

Made with ❤️ by [old6-six6](https://github.com/old6-six6) —— 我的第一个开源项目
