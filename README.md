# Introduction to this repository

本仓库主要用于复现《python编程快速上手——让繁琐工作自动化》一书中的多个项目（主要集中于后半部分）。

# 1. chapter6

## 1.1 bulletPointAdder.py - 将剪贴板中每一行前加上*号

bulletPointAdder.py 脚本将从剪贴板中取得文本，在每一行开始处加上星号和空格，然后将这段新的文本贴回到剪贴板。例如，如果我将下面的文本复制到剪贴板（取自于维基百科的文章“List of Lists of Lists”）：
```txt
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
```
然后运行程序，剪贴板中就会包含下面的内容：
```txt
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
```
这段前面加了星号的文本，就可以粘贴回维基百科的文章中，成为一个无序列表。

# 2. chapter7

## 2.1 phoneAndEmail.py - 在剪贴板的文本中查找电话号码和E-mail地址

在一篇长的网页或文章中，找出所有电话号码和邮件地址

# 3. chapter8

## 3.1 randomQuizGenerator.py - 生成问题次序随机的测验问卷文件

进行美国各州首府的一个小测验。

创建35份不同的测验试卷。为每份试卷创建50个多重选择题，次序随机。为每个问题提供一个正确答案和3个随机的错误答案，次序随机。将测验试卷写到35个文本文件中。将答案写到35个文本文件中。

## 3.2 multiclipboard.py - 多重剪切板

编写一个Python程序，追踪几段文本。

该程序将利用一个关键字保存每段剪贴板文本。例如，当运行py mcb.pyw save spam，剪贴板中当前的内容就用关键字spam保存。通过运行py mcb.pyw spam，这段文本稍后将重新加载到剪贴板中。如果用户忘记了都有哪些关键字，他们可以运行py mcb.pyw list，将所有关键字的列表复制到剪贴板中。

程序应当：
- 针对要检查的关键字，提供命令行参数。
- 如果参数是save，那么将剪贴板的内容保存到关键字。
- 如果参数是list，就将所有的关键字拷贝到剪贴板。
- 否则，就将关键词对应的文本拷贝到剪贴板。