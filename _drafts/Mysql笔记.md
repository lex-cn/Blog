
## mysql如何修改用户名

## 如何显示表中的最新数据

```sql
select * from 表名 order by 列名 [desc] limit 行数
```

## 查看服务器的状态

```sql 
show status;
```

## 查看服务器的当前链接数

```sql
show [full] processlist;
```

## 如何设置远程链接

```sql
update user set host=
```

## 远程连接mysql

```bash
$: Mysql -h 192.168.1.1 -P 3306 -u 用户名 -p[密码]
```
## 控制台内执行脚本

2.执行sql脚本,可以有2种方法:
第一种方法:

在命令行下(未连接数据库),输入 

```sql
   mysql -h localhost -u root -p123456 < F:\hello world\niuzi.sql 
```

(注意路径不用加引号的!!) 回车即可.

第二种方法:

在命令行下(已连接数据库,此时的提示符为 mysql> ),输入 source F:\hello
world\niuzi.sql (注意路径不用加引号的) 或者 \. F:\hello world\niuzi.sql (注意路
径不用加引号的) 回车即可

```sql
source 脚本完整路径
```

## 删除某个表格

```sql
delete from 表格名;
```

这条语句没有where语句，所以它将删除所有的记录，因此如果没有使用where的时候，要
千万小心。

```sql
delete from 表格名 where 条件A and 条件B;
```

例子：
```sql
DELETE FROM current_info WHERE DeviceID='A000' OR DeviceID='A002';
```

这样就好多了。

## 一次插入多个信息

```sql
INSERT INTO 表名 (DeviceID,Type) VALUES('A000', 0),('A000', 1),('A002', 0),('A002', 1);
```

## 删除一个表格

```sql
drop table 表名;
```

