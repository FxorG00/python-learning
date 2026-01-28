以下是根据您提供的文档内容，对其中涉及的SQL操作代码进行的总结。文档涵盖了SQL基础语法、MySQL使用以及Python与MySQL的交互。我会按照操作类型分类总结，并在相关部分嵌入文档中的图片以增强理解。图片将紧邻其原始描述位置嵌入。

### 一、SQL语言概述
SQL（Structured Query Language）是用于操作数据库的标准语言，文档中将其分为四类：
- **DDL（数据定义语言）**：用于管理数据库和表的结构，如创建、删除库和表。
- **DML（数据操纵语言）**：用于增删改数据记录。
- **DQL（数据查询语言）**：用于查询和计算数据。
- **DCL（数据控制语言）**：用于管理权限和用户（文档中未详细展开）。

SQL语法特征包括：大小写不敏感、以分号结尾、支持单行（`--` 或 `#`）和多行注释（`/* */`）。



### 二、DDL（数据定义语言）操作代码总结
DDL用于管理数据库和表的结构，常见操作包括：
- **数据库管理**：
  - 查看所有数据库：`SHOW DATABASES;`
  - 使用数据库：`USE 数据库名称;`
  - 创建数据库（指定字符集）：`CREATE DATABASE 数据库名称 CHARSET UTF8;`
  - 删除数据库：`DROP DATABASE 数据库名称;`
  - 查看当前数据库：`SELECT DATABASE();`
- **表管理**：
  - 查看所有表：`SHOW TABLES;`（需先选择数据库）
  - 创建表：定义列名和类型，例如：
    ```sql
    CREATE TABLE 表名称 (
        id INT,
        name VARCHAR(20),
        age INT
    );
    ```
    常见列类型包括：`INT`（整数）、`FLOAT`（浮点数）、`VARCHAR(长度)`（文本）、`DATE`（日期）、`TIMESTAMP`（时间戳）。
  - 删除表：`DROP TABLE 表名称;` 或 `DROP TABLE IF EXISTS 表名称;`（避免报错）。



### 三、DML（数据操纵语言）操作代码总结
DML用于操作数据记录，包括插入、删除和更新：
- **插入数据（INSERT）**：
  - 基础语法：`INSERT INTO 表 (列1, 列2, ...) VALUES (值1, 值2, ...);`
  - 示例：插入单条或多条记录，字符串需用单引号包围。
    ```sql
    -- 插入部分列
    INSERT INTO student (id, name) VALUES (10001, '周杰轮');
    -- 插入全部列（快捷写法）
    INSERT INTO student VALUES (10001, '周杰轮', 31);
    ```
- **删除数据（DELETE）**：
  - 语法：`DELETE FROM 表名称 WHERE 条件;`
  - 条件操作符：`=`, `>`, `<`, `>=`, `<=`, `!=` 等。
    ```sql
    -- 删除特定记录
    DELETE FROM student WHERE name = '林俊节';
    -- 删除全部记录
    DELETE FROM student;
    ```
- **更新数据（UPDATE）**：
  - 语法：`UPDATE 表名 SET 列 = 值 WHERE 条件;`
    ```sql
    -- 更新特定记录
    UPDATE student SET name = '陈一讯' WHERE id = 10001;
    -- 更新全部记录
    UPDATE student SET age = 11;
    ```



### 四、DQL（数据查询语言）操作代码总结
DQL用于查询数据，包括基础查询、过滤、分组聚合、排序和分页：
- **基础查询**：
  - 语法：`SELECT 字段列表 | * FROM 表;`
    ```sql
    -- 查询指定列
    SELECT id, name FROM student;
    -- 查询全部列
    SELECT * FROM student;
    ```
- **过滤查询（WHERE）**：
  - 语法：`SELECT ... FROM 表 WHERE 条件;`
    ```sql
    SELECT * FROM student WHERE age < 33;
    ```
- **分组聚合（GROUP BY）**：
  - 语法：`SELECT 字段 | 聚合函数 FROM 表 [WHERE 条件] GROUP BY 列;`
  - 聚合函数：`COUNT(*)`（计数）、`SUM(列)`（求和）、`AVG(列)`（平均值）、`MIN(列)`（最小值）、`MAX(列)`（最大值）。
    ```sql
    -- 按性别分组统计人数
    SELECT gender, COUNT(*) FROM student GROUP BY gender;
    ```
- **排序和分页**：
  - 排序（ORDER BY）：`SELECT ... ORDER BY 列 [ASC | DESC];`
    ```sql
    SELECT * FROM student ORDER BY age DESC;
    ```
  - 分页（LIMIT）：`SELECT ... LIMIT n [, m];`（n为起始索引，m为数量）
    ```sql
    -- 限制结果数量
    SELECT * FROM student LIMIT 5;
    -- 分页查询
    SELECT * FROM student LIMIT 10, 5;  -- 从第10条开始取5条
    ```
  - 执行顺序：`FROM` → `WHERE` → `GROUP BY` → `SELECT` → `ORDER BY` → `LIMIT`。



### 五、Python与MySQL交互操作代码总结
使用pymysql库在Python中操作MySQL：
- **安装pymysql**：`pip install pymysql`
- **连接数据库**：
  ```python
  from pymysql import Connection
  conn = Connection(
      host='localhost',  # 主机名
      port=3306,         # 端口
      user='root',      # 用户名
      password='123456' # 密码
  )
  print(conn.get_server_info())  # 打印数据库信息
  conn.close()  # 关闭连接
  ```
- **执行SQL语句**：
  - 非查询操作（如建表、插入）：需提交更改（commit）。
    ```python
    cursor = conn.cursor()
    conn.select_db("test")  # 选择数据库
    cursor.execute("CREATE TABLE test_pymysql (id INT, info VARCHAR(255))")
    conn.commit()  # 提交更改
    ```
  - 查询操作：使用`fetchall()`获取结果。
    ```python
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()  # 结果为元组嵌套元组
    for r in results:
        print(r)
    ```
- **自动提交**：在连接时设置`autocommit=True`避免手动commit。
  ```python
  conn = Connection(host='localhost', port=3306, user='root', password='123456', autocommit=True)
  ```



### 六、综合案例提示
文档最后提供了一个综合案例：使用Python读取文件数据（如CSV或JSON），并通过SQL写入MySQL数据库。关键步骤包括：
- DDL定义表结构（如`CREATE TABLE orders (...)`）。
- 使用pymysql执行INSERT语句。
- 注意数据格式转换和提交机制。

这个总结覆盖了文档中的主要代码操作，希望对您有帮助！如果您需要更详细的某个部分，我可以进一步展开。