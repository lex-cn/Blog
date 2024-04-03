---
name : pandas 知识点总结
toc       : true
---



### No module named 'pandas.core.indexes'

[python 3.x - ModuleNotFoundError: No module named 'pandas.core.indexes' - Stack Overflow](https://stackoverflow.com/questions/51285798/modulenotfounderror-no-module-named-pandas-core-indexes)

[python - ImportError: No module named 'pandas.indexes' - Stack Overflow](https://stackoverflow.com/questions/37371451/importerror-no-module-named-pandas-indexes)




## Pandas保存数据到文件

DataFrame 数据的保存和读取

```python
df.to_csv # 写入到 csv 文件
pd.read_csv # 读取 csv 文件
df.to_json # 写入到 json 文件
pd.read_json # 读取 json 文件
df.to_html  # 写入到 html 文件
pd.read_html # 读取 html 文件
df.to_excel # 写入到 excel 文件
pd.read_excel # 读取 excel 文件
```

### `pandas.DataFrame.to_csv`

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

### `pandas.DataFrame.to_json()`

将 Dataframe 写入到 json 文件

[官方文档](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html)

```python
DataFrame.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True,
    date_unit='ms', default_handler=None, lines=False, compression=None, index=True)
```

参数：

- `path_or_buf` : 文件路径，如果没有指定则将会直接返回字符串的 json。



### pandas.DataFrame.to_html

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


### pandas.DataFrame.to_excel

将 DataFrame 写入 excel 文件

[pandas.DataFrame.to\_excel](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html)

```python
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='',
    float_format=None, columns=None, header=True, index=True,
    index_label=None, startrow=0, startcol=0, engine=None,
    merge_cells=True, encoding=None, inf_rep='inf', verbose=True,
    freeze_panes=None)
```

### `pandas.read_excel()`


可能遇到的报错：

```
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
```

解决方法：安装 xlrd 包。

stackoverflow 讨论：[Python: Pandas pd.read\_excel giving ImportError: Install xlrd >= 0.9.0 for Excel support](https://stackoverflow.com/questions/48066517/python-pandas-pd-read-excel-giving-importerror-install-xlrd-0-9-0-for-excel)

其他文章：

- [http://www.dcharm.com/?p=584](http://www.dcharm.com/?p=584)
- [https://blog.csdn.net/sinat\_29957455/article/details/79059436](https://blog.csdn.net/sinat_29957455/article/details/79059436)
- [https://www.cnblogs.com/pengsixiong/p/5050833.html](https://www.cnblogs.com/pengsixiong/p/5050833.html)



## Pandas 查询


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


## Pandas 提速

- [Pandas进阶之提速遍历操作 - 简书](https://www.jianshu.com/p/56a50a6c961c)
- [pandas 判断某一列数据是否在另一列中 - 简书](https://www.jianshu.com/p/a3f60ceff8bf)
- [pandas筛选某列是否包含指定的字符串 - 知乎](https://zhuanlan.zhihu.com/p/81009691)
- [Python3 pandas(3)筛选数据isin(), str.contains() - 知乎](https://zhuanlan.zhihu.com/p/29720881)
- [numpy ndarray 按条件筛选数组，关联筛选_y小川的专栏-CSDN博客](https://blog.csdn.net/blackyuanc/article/details/77948703)
- [numpy中实现ndarray数组返回符合特定条件的索引方法_python_脚本之家](https://www.jb51.net/article/138290.htm)
- [从 Pandas 小白到 Pandas 能手 | 远行的舟](https://www.longzf.com/from_Pandas-wan_to_Pandas-master/)
- [pandas条件查询条件筛选优化_zypaslx的专栏-CSDN博客](https://blog.csdn.net/zypaslx/article/details/108647971)


`pd.reset_index()` 函数解析_python重置索引
