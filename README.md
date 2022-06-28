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