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

# 4. chapter9

## 4.1 renameDates.py - 批量更改文件名称

假定有上千个文件，文件名包含美国风格的日期(MM-DD-YYYY)，需要将它们改名为欧洲风格的日期(DD-MM-YYYY)。

下面是程序要做的事：
- 检查当前工作目录的所有文件名，寻找美国风格的日期。
- 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。

## 4.2 backupToZip.py - 将一个文件夹备份到一个ZIP文件

项目文件保存在程序当前文件夹chapter9/AlsPythonBook中。希望为整个文件夹创建一个ZIP文件，作为“快照”。

希望保存不同的版本，ZIP文件的文件名每次创建时都有所变化。例如AlsPythonBook_1.zip、AlsPythonBook_2.zip、AlsPythonBook_3.zip等等。

# 5. chapter11

## 5.1 search.py - 在Bing上查询前几项结果

只要在命令行中输入查找主题，就能让计算机自动打开浏览器，并在新的选项卡中显示前面几项查询结果。

下面是程序要做的事：
- 从命令行参数中获取查询关键字。
- 取得查询结果页面。
- 为每个结果打开一个浏览器选项卡。

## 5.2 downloadXkcd.py - 下载所有的XKCD漫画

XKCD是一个流行的极客漫画网站，它符合结构：

首页 http://xkcd.com/ 中有最新的帖子，以及一个“前一篇”(“Prev”)按钮，将你带到以前的帖子。然后那个帖子也有一个“前一篇”按钮，以此类推。这创建了一条线索，从最近的页面，直到该网站的第一个帖子。

该程序用来下载该网站的所有漫画。

下面是程序要做的事：
- 加载主页；
- 保存该页的漫画图片；
- 转入前一张漫画的链接；
- 重复直到第一张漫画。

# 6. chapter13

## 6.1 combinePdfs.py - 从多个PDF中合并选择的页面

- 找到当前工作目录中所有PDF文件。
- 按文件名排序，这样就能有序地添加这些PDF。
- 除了第一页之外，将每个PDF的所有页面写入输出的文件。

# 7. chapter14 

## 7.1 removeCsvHeader.py - 从CSV文件中删除表头

打开当前工作目录中所有扩展名为.csv的文件，读取CSV文件的内容，并除掉第一行的内容重新写入同名的文件。这将用新的、无表头的内容替换CSV文件的旧内容。

该程序必须做到以下几点：
- 找出当前工作目录中的所有CSV文件。
- 读取每个文件的全部内容。
- 跳过第一行，将内容写入一个新的CSV文件。

## 7.2 quickWeather.py - 取得当前的天气数据

OpenWeatherMap.org提供了JSON格式的实时天气信息。

可从页面 http://api.openweathermap.org/data/2.5/forecast/daily?q=```<Location>```&cnt=3 下载今后几天的天气预报，并以纯文本打印出来。其中 ```<Location>``` 是想知道天气的城市。

该程序将执行以下操作：
- 从命令行读取请求的位置。
- 从OpenWeatherMap.org 下载JSON天气数据。
- 将JSON数据字符串转换成Python的数据结构。