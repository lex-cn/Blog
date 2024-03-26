---
name : pandas 知识点总结
toc       : true
---





## No module named 'pandas.core.indexes'

[python 3.x - ModuleNotFoundError: No module named 'pandas.core.indexes' - Stack Overflow](https://stackoverflow.com/questions/51285798/modulenotfounderror-no-module-named-pandas-core-indexes)

[python - ImportError: No module named 'pandas.indexes' - Stack Overflow](https://stackoverflow.com/questions/37371451/importerror-no-module-named-pandas-indexes)




## Pandas保存数据到文件

DataFrame 数据的保存和读取

```python
df.to_csv #写入到 csv 文件
pd.read_csv #读取 csv 文件
df.to_json 写入到 json 文件
pd.read_json 读取 json 文件
df.to_html 写入到 html 文件
pd.read_html 读取 html 文件
df.to_excel 写入到 excel 文件
pd.read_excel 读取 excel 文件
```

# `pandas.DataFrame.to_csv`

将 DataFrame 写入到 csv 文件

[官网文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html)

```python
DataFrame.to_csv(
    path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None,
    header=True, index=True,  index_label=None, mode='w',
    encoding=None, compression=None, quoting=None, quotechar='"',
    line_terminator='\n', chunksize=None, tupleize_cols=None,
    date_format=None, doublequote=True, escapechar=None, decimal='.')
```

参数：

- `path_or_buf` : 文件路径，如果没有指定则将会直接返回字符串的 json
- `sep` : 输出文件的字段分隔符，默认为 “,”
- `na_rep` : 用于替换空数据的字符串，默认为''
- `float_format` : 设置浮点数的格式（几位小数点）
- `columns`: 要写的列
- `header` : 是否保存列名，默认为 True ，保存
- `index` : 是否保存索引，默认为 True ，保存
- `index_label` : 索引的列标签名

# `pandas.DataFrame.to_json`

将 Dataframe 写入到 json 文件

[官方文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html)

```python
DataFrame.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True,
    date_unit='ms', default_handler=None, lines=False, compression=None, index=True)
```

参数：

- `path_or_buf` : 文件路径，如果没有指定则将会直接返回字符串的 json。



# pandas.DataFrame.to_html

将 Dataframe 写入到 html 文件

[pandas.DataFrame.to_html.html](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html)

```python
DataFrame.to_html(buf=None, columns=None, col_space=None, header=True,
    index=True, na_rep='NaN', formatters=None,                  float_format=None,
    sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None,
    escape=True, max_rows=None, max_cols=None, show_dimensions=False,
    notebook=False, decimal='.',                  border=None, table_id=None)
```

`df.to_html` 生成的是一个 html 格式的 table 表，我们可以在前后加入其他标签，丰富页面。ps：如果有中文字符，需要在 head 中设置编码格式。

参考：[Pandas Dataframes to\_html: Highlighting table rows](https://cntofu.com/book/46/python/pandas_dataframes_tohtml__highlighting_table_rows.md)


# pandas.DataFrame.to_excel

将 DataFrame 写入 excel 文件

[pandas.DataFrame.to\_excel](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html)

```python
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='',
    float_format=None, columns=None, header=True, index=True,
    index_label=None, startrow=0, startcol=0, engine=None,
    merge_cells=True, encoding=None, inf_rep='inf', verbose=True,
    freeze_panes=None)
```

### pandas.read_excel可能遇到的报错：


```
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
```

解决方法：安装 xlrd 包。

stackoverflow 讨论：[Python: Pandas pd.read\_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)

其他文章：

- [http://www.dcharm.com/?p=584](http://www.dcharm.com/?p=584)
- [https://blog.csdn.net/sinat\_29957455/article/details/79059436](https://blog.csdn.net/sinat_29957455/article/details/79059436)
- [https://www.cnblogs.com/pengsixiong/p/5050833.html](https://www.cnblogs.com/pengsixiong/p/5050833.html)

---
created: 2023-06-20T09:35:38 (UTC +08:00)
tags: [dataframe to_csv]
source: https://blog.csdn.net/dongbao520/article/details/119799975
author: 成就一亿技术人!
---

# pandas.DataFrame.to_csv实用方法_dataframe to_csv_海宝7号的博客-CSDN博客

> ## Excerpt
> pandas.DataFrame.to_csvDataFrame.to_csv( path_or_buf = None , sep = ‘,’ , na_rep = ‘’ , float_format = None , columns = None , header = True , index = True , index_label = None , mode = ‘w’ , encoding = None , compression = ‘infer ’ ,引用= None , quotechar

---
[pandas](https://so.csdn.net/so/search?q=pandas&spm=1001.2101.3001.7020).DataFrame.to\_csv
[DataFrame](https://so.csdn.net/so/search?q=DataFrame&spm=1001.2101.3001.7020).to\_csv( path\_or\_buf = None , sep = ‘,’ , na\_rep = ‘’ , float\_format = None , columns = None , header = True , index = True , index\_label = None , mode = ‘w’ , encoding = None , compression = ‘infer ’ ,引用= None , quotechar =’“’， line\_terminator =无， CHUNKSIZE =无， DATE\_FORMAT =无，双引号=真， escapechar =无，小数= ‘。’ ,错误= ‘strict’ , storage\_options = None )\[来源\]
将对象写入逗号分隔值 (csv) 文件。

参数
path\_or\_buf str 或文件句柄，默认无
文件路径或对象，如果提供 None 则结果作为字符串返回。如果传递了非二进制文件对象，则应使用newline=’‘打开它，禁用通用换行符。如果传递了二进制文件对象，则mode可能需要包含’b’。

在 1.2.0 版更改:引入了对二进制文件对象的支持。

sep str，默认’,’
长度为 1 的字符串。输出文件的字段分隔符。

na\_rep str，默认 ‘’
缺少数据表示。

float\_format str，默认无
浮点数的格式字符串。

列顺序，可选
要写入的列。

[header](https://so.csdn.net/so/search?q=header&spm=1001.2101.3001.7020) bool 或 str 列表，默认为 True
写出列名。如果给出了字符串列表，则假定它是列名称的别名。

索引布尔值，默认为 True
写行名称（索引）。

index\_label str 或序列，或 False，默认 None
如果需要，索引列的列标签。如果没有给出，并且 标头和索引为 True，则使用索引名称。如果对象使用 MultiIndex，则应给出序列。如果 False 不打印索引名称的字段。使用 index\_label=False 更容易在 R 中导入。

模式字符串
Python 写模式，默认’w’。

编码str，可选
表示在输出文件中使用的编码的字符串，默认为 ‘utf-8’。如果path\_or\_buf 是非二进制文件对象，则不支持编码。

压缩str 或 dict，默认为“推断”
如果是 str，则代表压缩模式。如果是 dict，则 ‘method’ 处的值是压缩模式。压缩模式可以是以下任何可能的值：{‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}。如果压缩模式是 ‘infer’ 并且path\_or\_buf是类似路径的，则从以下扩展名中检测压缩模式：’.gz’、’.bz2’、’.zip’ 或 ‘.xz’。（否则不压缩）。如果给出的 dict 和 mode 是 {‘zip’, ‘gzip’, ‘bz2’} 之一，或推断为上述之一，则其他条目作为附加压缩选项传递。

在 1.0.0 版更改：如果压缩模式为“zip”，则现在可能是一个以“method”键作为压缩模式和其他条目作为附加压缩选项的字典。

在 1.1.0 版更改:压缩模式“gzip”和“bz2”以及“zip”支持将压缩选项作为 dict 中的键传递。

在 1.2.0 版更改:二进制文件对象支持压缩。

在 1.2.0 版更改：以前的版本将 ‘gzip’ 的 dict 条目转发到 gzip.open而不是gzip.GzipFile，这会阻止设置mtime。

从 csv 模块引用可选常量
默认为 csv.QUOTE\_MINIMAL。如果您设置了float\_format， 则浮点数将转换为字符串，因此 csv.QUOTE\_NONNUMERIC 会将它们视为非数字。

quotechar str，默认 ‘"’
长度为 1 的字符串。用于引用字段的字符。

line\_terminator str，可选
要在输出文件中使用的换行符或字符序列。默认为os.linesep，这取决于调用此方法的操作系统（’\\n’ 用于 linux，’\\r\\n’ 用于 Windows，即）。

chunksize int 或 None
一次写入的行。

date\_format str，默认无
日期时间对象的格式字符串。

双引号布尔值，默认为 True
控制字段内的quotechar 的引用。

escapechar str，默认无
长度为 1 的字符串。 适当时用于转义sep和quotechar 的字符。

十进制字符串，默认’.’
识别为小数分隔符的字符。例如，对欧洲数据使用“,”。

错误str，默认“严格”
指定如何处理编码和解码错误。有关open()完整的选项列表，请参阅错误参数。

1.1.0 版中的新功能。

storage\_options dict，可选
对特定存储连接有意义的额外选项，例如主机、端口、用户名、密码等。对于 HTTP(S) URL，键值对urllib作为标头选项转发到。对于其他 URL（例如以“s3://”和“gcs://”开头），键值对被转发到 fsspec。请参阅fsspec和urllib了解更多详情。
![在这里插入图片描述](pandas.DataFrame.to_csv%E5%AE%9E%E7%94%A8%E6%96%B9%E6%B3%95_dataframe%20to_csv_%E6%B5%B7%E5%AE%9D7%E5%8F%B7%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/x-oss-process=image.png)

1.2.0 版中的新功能。
[参考来源：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to\_csv.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)




## pandas 查询


```python
import pandas as pd
import numpy as np

df=pd.DataFrame({'Name':['JOHN','ALLEN','BOB','NIKI','CHARLIE','CHANG'], 'Age':[35,42,63,29,47,51], 'Salary_in_1000':[100,93,78,120,64,115], 'FT_Team':['STEELERS','SEAHAWKS','FALCONS','FALCONS','PATRIOTS','STEELERS']})

df.loc[(df['Salary_in_1000']>=100) & (df['Age']< 60) & (df['FT_Team'].str.startswith('S')),['Name','FT_Team']]

idx = np.where((df['Salary_in_1000']>=100) & (df['Age']< 60) & (df['FT_Team'].str.startswith('S')))

df.query('Salary_in_1000 >= 100 & Age < 60 & FT_Team.str.startswith("S").values')

df[(df['Salary_in_1000']>=100) & (df['Age']<60) & df['FT_Team'].str.startswith('S')][['Name','Age','Salary_in_1000']]

df[df.eval("Salary_in_1000>=100 & (Age <60) & FT_Team.str.startswith('S').values")]
```


- [Pandas dataframe filter with Multiple conditions - kanoki](https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/)


## pandas提速

- [Pandas进阶之提速遍历操作 - 简书](https://www.jianshu.com/p/56a50a6c961c)
- [pandas 判断某一列数据是否在另一列中 - 简书](https://www.jianshu.com/p/a3f60ceff8bf)
- [pandas筛选某列是否包含指定的字符串 - 知乎](https://zhuanlan.zhihu.com/p/81009691)
- [Python3 pandas(3)筛选数据isin(), str.contains() - 知乎](https://zhuanlan.zhihu.com/p/29720881)
- [numpy ndarray 按条件筛选数组，关联筛选_y小川的专栏-CSDN博客](https://blog.csdn.net/blackyuanc/article/details/77948703)
- [numpy中实现ndarray数组返回符合特定条件的索引方法_python_脚本之家](https://www.jb51.net/article/138290.htm)
- [从 Pandas 小白到 Pandas 能手 | 远行的舟](https://www.longzf.com/from_Pandas-wan_to_Pandas-master/)
- [pandas条件查询条件筛选优化_zypaslx的专栏-CSDN博客](https://blog.csdn.net/zypaslx/article/details/108647971)


---
created: 2023-09-03T23:55:48 (UTC +08:00)
tags: [python重置索引]
source: https://blog.csdn.net/qq_51392112/article/details/130669791
author: 成就一亿技术人!
---

# 【Python_Pandas】reset_index() 函数解析_python重置索引_笃℃的博客-CSDN博客

> ## Excerpt
> 【Python_Pandas】reset_index() 函数解析_python重置索引

---
## 【Python\_Pandas】[reset\_index](https://so.csdn.net/so/search?q=reset_index&spm=1001.2101.3001.7020)函数解析

### 文章目录

-   [【Python\_Pandas】reset\_index函数解析](https://blog.csdn.net/qq_51392112/article/details/130669791#Python_Pandasreset_index_0)
-   -   [1\. 介绍](https://blog.csdn.net/qq_51392112/article/details/130669791#1__2)
    -   [2\. 示例](https://blog.csdn.net/qq_51392112/article/details/130669791#2__21)
    -   -   [2.1 参数drop](https://blog.csdn.net/qq_51392112/article/details/130669791#21_drop_22)
        -   [2.2 参数inplace](https://blog.csdn.net/qq_51392112/article/details/130669791#22_inplace_45)
        -   [2.3 参数level](https://blog.csdn.net/qq_51392112/article/details/130669791#23_level_71)
        -   [2.4 参数col\_level](https://blog.csdn.net/qq_51392112/article/details/130669791#24_col_level_101)
        -   [2.5 参数col\_fill](https://blog.csdn.net/qq_51392112/article/details/130669791#25_col_fill_126)
    -   [参考](https://blog.csdn.net/qq_51392112/article/details/130669791#_163)

## 1\. 介绍

pandas.DataFrame.reset\_index

```
reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
```

1）函数作用：

-   重置索引或其level。
    -   重置数据帧的索引，并使用默认索引。如果数据帧具有多重索引，则此方法可以删除一个或多个level。

2）参数：

-   drop: 重新设置索引后是否将原索引作为新的一列并入DataFrame，默认为**False**
-   inplace: 是否在原DataFrame上改动，默认为False
-   level: 如果索引(index)有多个列，仅从索引中删除level指定的列，默认删除所有列
-   col\_level: 如果列名(columns)有多个级别，决定被删除的索引将插入哪个级别，默认插入第一级
-   col\_fill: 如果列名(columns)有多个级别，决定其他级别如何命名

3）返回

-   DataFrame or None。具有新索引的数据帧，如果inplace=True，则无索引。

## 2\. 示例

### 2.1 参数drop

-   False：表示重新设置索引后，将原索引作为新的一列并入DataFrame，
-   True：表示删除原索引

```
import pandas as pd
import numpy as np

df = pd.DataFrame([('bird', 389.0), ('bird', 24.0), ('mammal', 80.5), ('mammal', np.nan)],
                  index=['falcon', 'parrot', 'lion', 'monkey'], columns=('class', 'max_speed'))
print(df)
print('\n')

df1 = df.reset_index()
print(df1)
print('\n')

df2 = df.reset_index(drop=True)
print(df2)
```

-   输出：
    ![在这里插入图片描述](%E3%80%90Python_Pandas%E3%80%91reset_index()%20%E5%87%BD%E6%95%B0%E8%A7%A3%E6%9E%90_python%E9%87%8D%E7%BD%AE%E7%B4%A2%E5%BC%95_%E7%AC%83%E2%84%83%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/c83a584bd04f43ca97de6b4dc0b9efba.png)

### 2.2 参数inplace

-   True表示：在原DataFrame上修改，返回为None
-   False：将修改后的DataFrame作为新的对象返回

```
import pandas as pd
import numpy as np

df = pd.DataFrame([('bird', 389.0), ('bird', 24.0), ('mammal', 80.5), ('mammal', np.nan)],
                  index=['falcon', 'parrot', 'lion', 'monkey'], columns=('class', 'max_speed'))
print(df)
print('\n')

df1 = df.reset_index()
print(df1)
print('\n')

df2 = df.reset_index(inplace=True)
print(df2)
print('\n')
print(df)
```

-   输出：
    ![在这里插入图片描述](%E3%80%90Python_Pandas%E3%80%91reset_index()%20%E5%87%BD%E6%95%B0%E8%A7%A3%E6%9E%90_python%E9%87%8D%E7%BD%AE%E7%B4%A2%E5%BC%95_%E7%AC%83%E2%84%83%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/473a055c27d14d05bc7406e1abb07203.png)

### 2.3 参数level

如果索引有多个列，仅从索引中删除由level指定的列，默认删除所有列。

-   输入整数时表示将index的names中下标为level的索引删除；
-   输入为字符串时表示将名字为level的索引删除

```
import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([('bird', 'falcon'), ('bird', 'parrot'), ('mammal', 'lion'), ('mammal', 'monkey')], names=['class', 'name'])
columns = pd.MultiIndex.from_tuples([('speed', 'max'), ('species', 'type')])
df = pd.DataFrame([(389.0, 'fly'), ( 24.0, 'fly'), ( 80.5, 'run'), (np.nan, 'jump')], index=index, columns=columns)

print(df)
print('\n')

df0 = df.reset_index()
print(df0)
print('\n')

df1 = df.reset_index(level=1)
print(df1)
print('\n')

df2 = df.reset_index(level='name')
print(df2)
```

-   输出：
    ![在这里插入图片描述](%E3%80%90Python_Pandas%E3%80%91reset_index()%20%E5%87%BD%E6%95%B0%E8%A7%A3%E6%9E%90_python%E9%87%8D%E7%BD%AE%E7%B4%A2%E5%BC%95_%E7%AC%83%E2%84%83%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/99cd510a09cd452493c258d9e03ac9e6.png)

### 2.4 参数col\_level

如果列名(columns)有多个级别，决定被删除的索引将插入哪个级别，默认插入第一级(col\_level=0)

```
import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([('bird', 'falcon'), ('bird', 'parrot'), ('mammal', 'lion'), ('mammal', 'monkey')], names=['class', 'name'])
columns = pd.MultiIndex.from_tuples([('speed', 'max'), ('species', 'type')])
df = pd.DataFrame([(389.0, 'fly'), ( 24.0, 'fly'), ( 80.5, 'run'), (np.nan, 'jump')], index=index, columns=columns)

print(df)
print('\n')

df1 = df.reset_index(level=0, col_level=0)
print(df1)
print('\n')

df2 = df.reset_index(level=0, col_level=1)
print(df2)
print('\n')
```

-   输出：
    ![在这里插入图片描述](%E3%80%90Python_Pandas%E3%80%91reset_index()%20%E5%87%BD%E6%95%B0%E8%A7%A3%E6%9E%90_python%E9%87%8D%E7%BD%AE%E7%B4%A2%E5%BC%95_%E7%AC%83%E2%84%83%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2/fb670719ca4b491aa05fa1aff4320a44.png)

### 2.5 参数col\_fill

重置索引时被删除的索引只能插入一个级别，

-   如果列名(columns)有多个级别，那么这个列的列名的其他级别如何命名就由col\_fill决定，默认不做填充，
-   如果传入None则用被删除的索引的名字填充

```python
import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([('bird', 'falcon'), ('bird', 'parrot'), ('mammal', 'lion'), ('mammal', 'monkey')], names=['class', 'name'])
columns = pd.MultiIndex.from_tuples([('speed', 'max'), ('species', 'type')])
df = pd.DataFrame([(389.0, 'fly'), ( 24.0, 'fly'), ( 80.5, 'run'), (np.nan, 'jump')], index=index, columns=columns)

print(df)
print('\n')

df0 = df.reset_index(level=0, col_level=0)
print(df0)
print('\n')

df1 = df.reset_index(level=0, col_level=0, col_fill=None)
print(df1)
print('\n')

df2 = df.reset_index(level=0, col_level=1, col_fill='species')
print(df2)
print('\n')

df3 = df.reset_index(level=0, col_level=0, col_fill='genus')
print(df3)
print('\n')
```

## 参考

【1】https://blog.csdn.net/weixin\_43298886/article/details/108090189
