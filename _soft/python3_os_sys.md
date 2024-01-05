```
name :
```

python3 中获取文件后缀名的方法


```python
os.path.splittext(path)[-1]
```

判断文件的后缀名

```python
path = 'test.py'
bool = path.endswith('.py')
print(bool)
```

扩展home目录

```python
my_dir = os.path.expanduser('~/some_dir')
```

