# Python 常用内置函数速查笔记

> 整理范围：日常开发、数据处理、脚本编写中最高频的 Python 内置函数。
> 每个函数都附有 **语法签名** + **作用说明** + **可运行示例**。

---

## 目录

1. [类型转换](#一类型转换)
2. [数学与数值运算](#二数学与数值运算)
3. [序列与容器操作](#三序列与容器操作)
4. [迭代与生成器](#四迭代与生成器)
5. [输入输出](#五输入输出)
6. [对象与属性](#六对象与属性)
7. [字符串与编码](#七字符串与编码)
8. [动态执行与反射](#八动态执行与反射)
9. [list 常用方法（增删改查）](#九list-常用方法增删改查)
10. [tuple 常用操作](#十tuple-常用操作不可变序列)
11. [set 常用方法](#十一set-常用方法去重与集合运算)
12. [dict 常用方法](#十二dict-常用方法增删改查与遍历)
13. [速查表](#十三速查表)

---

## 一、类型转换

### `int(x, base=10)`
将字符串或数字转换为整数，可指定进制。
```python
int("42")        # 42
int("1010", 2)   # 10（二进制字符串）
int("ff", 16)    # 255（十六进制字符串）
int(3.9)         # 3（向下取整，不四舍五入）
```

### `float(x)`
将字符串或数字转换为浮点数。
```python
float("3.14")    # 3.14
float(7)         # 7.0
```

### `str(object)`
将任意对象转换为字符串。
```python
str(123)         # '123'
str([1, 2])      # '[1, 2]'
```

### `bool(x)`
将值转换为布尔值。**为假的值**：`0`、`0.0`、`""`、`None`、空容器 `[] () {}`、`False`。
```python
bool(1)          # True
bool(0)          # False
bool("hello")    # True
bool([])         # False
```

### `list()` / `tuple()` / `set()` / `dict()`
在容器类型之间相互转换。
```python
list("abc")                # ['a', 'b', 'c']
tuple([1, 2, 3])           # (1, 2, 3)
set([1, 2, 2, 3])          # {1, 2, 3}（自动去重）
dict([("a", 1), ("b", 2)]) # {'a': 1, 'b': 2}
list(range(3))             # [0, 1, 2]
```

### `chr(i)` / `ord(c)`
整数与字符的互转（基于 Unicode 码点）。
```python
ord("A")   # 65
chr(65)    # 'A'
chr(20013) # '中'
```

### `hex(x)` / `oct(x)` / `bin(x)`
将整数转为十六进制 / 八进制 / 二进制字符串。
```python
hex(255)   # '0xff'
oct(8)     # '0o10'
bin(5)     # '0b101'
```

---

## 二、数学与数值运算

### `abs(x)`
返回绝对值。
```python
abs(-5)     # 5
abs(3.14)   # 3.14
abs(-3 + 4j)  # 5.0（复数的模）
```

### `round(x, ndigits=0)`
四舍五入。注意 Python 的银行家舍入规则：`.5` 会舍到最近的偶数。
```python
round(3.14159, 2)  # 3.14
round(2.5)         # 2（银行家舍入，2 是偶数）
round(3.5)         # 4（4 是偶数）
```

### `pow(x, y, mod=None)`
求 `x` 的 `y` 次方，可带模运算（比 `pow(x,y) % mod` 更快）。
```python
pow(2, 3)         # 8
pow(2, 10, 1000)  # 24（即 2**10 % 1000）
```

### `sum(iterable, start=0)`
对可迭代对象求和，`start` 是初始值。
```python
sum([1, 2, 3, 4])       # 10
sum([1, 2, 3], 100)     # 106
```

### `min(iterable, key=...)` / `max(iterable, key=...)`
返回最小 / 最大值，`key` 指定比较依据。
```python
min([3, 1, 4, 1, 5])              # 1
max(["apple", "pear", "banana"], key=len)  # 'banana'
```

### `divmod(a, b)`
返回 `(商, 余数)` 的元组。
```python
divmod(10, 3)   # (3, 1)
divmod(7, 2)    # (3, 1)
```

### `len(s)`
返回对象的长度（字符串、列表、元组、集合、字典、range 等）。
```python
len("hello")          # 5
len([1, 2, 3])        # 3
len({"a": 1, "b": 2}) # 2
```

---

## 三、序列与容器操作

### `range(start, stop, step=1)`
生成不可变的整数序列（惰性求值，内存友好）。**左闭右开**。
```python
list(range(5))         # [0, 1, 2, 3, 4]
list(range(2, 8))      # [2, 3, 4, 5, 6, 7]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
list(range(5, 0, -1))  # [5, 4, 3, 2, 1]
```

### `enumerate(iterable, start=0)`
同时返回索引和元素，遍历时最常用。
```python
for i, fruit in enumerate(["apple", "banana"], start=1):
    print(i, fruit)
# 1 apple
# 2 banana
```

### `zip(*iterables)`
将多个可迭代对象按位置打包成元组。长度不同时取最短的。
```python
list(zip([1, 2, 3], ["a", "b", "c"]))  # [(1, 'a'), (2, 'b'), (3, 'c')]
names = ["Tom", "Jerry"]
ages = [5, 6]
dict(zip(names, ages))                  # {'Tom': 5, 'Jerry': 6}
```

### `sorted(iterable, key=..., reverse=False)`
返回**新**的排序列表（不改变原列表）。`key` 指定排序依据，`reverse=True` 降序。
```python
sorted([3, 1, 2])                         # [1, 2, 3]
sorted([3, 1, 2], reverse=True)           # [3, 2, 1]
sorted(["aa", "b", "ccc"], key=len)       # ['b', 'aa', 'ccc']
# 按字典的某个字段排序
students = [{"name": "Tom", "score": 85}, {"name": "Jerry", "score": 92}]
sorted(students, key=lambda s: s["score"], reverse=True)
```

### `reversed(seq)`
返回反向迭代器，不改变原序列。
```python
list(reversed([1, 2, 3]))  # [3, 2, 1]
"".join(reversed("abc"))   # 'cba'
```

### `filter(function, iterable)`
筛选出使 `function` 返回真值的元素，返回迭代器。
```python
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))  # [2, 4]
# function 传 None 时，保留所有真值元素
list(filter(None, [0, 1, "", "a", None]))            # [1, 'a']
```

### `map(function, iterable, ...)`
对每个元素应用 `function`，返回迭代器。
```python
list(map(str, [1, 2, 3]))            # ['1', '2', '3']
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]
list(map(pow, [2, 3], [4, 5]))       # [16, 243]（2**4, 3**5）
```

### `slice(start, stop, step)`
创建一个切片对象，可用于自定义 `__getitem__` 或 `operator.itemgetter`。
```python
s = slice(1, 5, 2)
[0, 1, 2, 3, 4, 5][s]  # [1, 3]
```

---

## 四、迭代与生成器

### `iter(obj)` / `next(iterator, default)`
`iter` 获取迭代器，`next` 逐个取值；耗尽后可返回默认值。
```python
it = iter([1, 2, 3])
next(it)        # 1
next(it)        # 2
next(it)        # 3
next(it, "end") # 'end'（已耗尽，返回默认值）
```

### `all(iterable)` / `any(iterable)`
`all` 所有元素为真返回 `True`；`any` 任意元素为真返回 `True`。
```python
all([True, 1, "a"])   # True
all([True, 0])        # False
any([0, "", False])   # False
any([0, "", 3])       # True
```

---

## 五、输入输出

### `print(*objects, sep=" ", end="\n", file=..., flush=False)`
打印输出。`sep` 分隔符，`end` 结尾符。
```python
print("a", "b", "c")          # a b c
print("a", "b", sep="-")      # a-b
print("hello", end=" ")       # 不换行
print("world")                # hello world
```

### `input(prompt)`
读取用户输入，**返回字符串**。
```python
name = input("请输入名字: ")
age = int(input("请输入年龄: "))   # 记得转 int
```

### `open(file, mode="r", encoding="utf-8")`
打开文件，配合 `with` 使用会自动关闭。常用模式：`r` 读、`w` 写（覆盖）、`a` 追加、`rb`/`wb` 二进制。
```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好\n")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 读全部
    # for line in f:         # 或逐行读
    #     print(line, end="")
```

### `format(value, format_spec)`
格式化单个值。等价于 f-string 中的格式说明。
```python
format(3.14159, ".2f")   # '3.14'
format(255, "x")         # 'ff'
format(0.1, ".2%")       # '10.00%'
# 也可以用 f-string 达到同样效果
f"{3.14159:.2f}"         # '3.14'
```

---

## 六、对象与属性

### `type(obj)`
返回对象的类型。
```python
type(1)          # <class 'int'>
type("a")        # <class 'str'>
type(1) is int   # True
```

### `isinstance(obj, class_or_tuple)` / `issubclass(cls, cls_or_tuple)`
判断对象是否为某类型（**推荐代替 `type` 做类型判断**，支持继承）。`issubclass` 判断类的继承关系。
```python
isinstance(1, int)            # True
isinstance(True, int)         # True（bool 是 int 子类）
isinstance(1, (int, float))   # True
issubclass(bool, int)         # True
```

### `hasattr(obj, name)` / `getattr(obj, name, default)` / `setattr(obj, name, value)` / `delattr(obj, name)`
属性检查与动态读写。
```python
class Person:
    name = "Tom"

hasattr(Person, "name")       # True
getattr(Person, "name")       # 'Tom'
getattr(Person, "age", 0)     # 0（不存在返回默认值）
setattr(Person, "age", 18)    # 动态添加属性
delattr(Person, "age")
```

### `callable(obj)`
判断对象是否可调用（函数、方法、类、实现了 `__call__` 的对象）。
```python
callable(print)      # True
callable(len)        # True
callable("abc")      # False
```

### `id(obj)` / `dir(obj)` / `vars(obj)`
`id` 返回对象内存地址；`dir` 列出属性名；`vars` 返回 `__dict__`。
```python
id(123)          # 一串内存地址整数
dir("abc")       # 字符串的所有方法
vars(Person)     # 类的命名空间字典
```

### `super()`
调用父类方法，多用于子类 `__init__` 中。
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # 调用父类构造
        self.breed = breed

d = Dog("旺财", "金毛")
d.name, d.breed   # ('旺财', '金毛')
```

---

## 七、字符串与编码

### `repr(obj)`
返回对象的「可读表示」，通常是能还原对象的字符串（与 `str` 不同，`repr` 面向调试）。
```python
repr("hello")   # "'hello'"（带引号）
str("hello")    # 'hello'
repr([1, 2])    # '[1, 2]'
```

### `hash(obj)`
返回对象的哈希值（不可变对象才有）。
```python
hash("abc")     # 一串整数
hash((1, 2))    # 元组可哈希
# hash([1, 2])  # TypeError: 列表不可哈希
```

### `bytes()` / `bytearray()`
二进制数据。`bytes` 不可变，`bytearray` 可变。
```python
bytes("中文", encoding="utf-8")      # b'\xe4\xb8\xad\xe6\x96\x87'
b"abc".decode("utf-8")               # 'abc'
```

---

## 八、动态执行与反射

### `eval(expression)` / `exec(code)`
`eval` 计算单个表达式并返回值；`exec` 执行语句块（无返回值）。
> ⚠️ 谨慎使用：执行用户输入有安全隐患。

```python
eval("1 + 2 * 3")      # 7
exec("x = 10\nprint(x * 2)")   # 输出 20
```

### `compile(source, filename, mode)`
把源代码编译为可执行对象，供 `eval`/`exec` 使用。
```python
code = compile("1 + 1", "<string>", "eval")
eval(code)   # 2
```

### `globals()` / `locals()`
返回全局 / 局部命名空间字典。
```python
x = 1
globals()["x"]   # 1
```

### `staticmethod()` / `classmethod()` / `property()`
装饰器底层实现，通常用 `@staticmethod`、`@classmethod`、`@property` 语法糖。
```python
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return 3.14 * self._r ** 2

    @classmethod
    def unit(cls):
        return cls(1)

    @staticmethod
    def info():
        return "Circle 类"

Circle.unit().area   # 3.14
Circle.info()        # 'Circle 类'
```

---

## 九、list 常用方法（增删改查）

> ⚠️ 先分清两类东西，这是最容易搞混的地方：
> - **内置函数**：`len()` / `sorted()` / `reversed()` —— 写在列表**外面**，一般不改变原列表。
> - **列表方法**：`l.append(x)` —— 用点号调用，**多数在原地修改**，返回值是 `None`。

### 一张表看懂：谁改原地，谁生成新的

| 需求 | 原地修改（返回 None） | 返回新对象（原列表不动） |
|------|----------------------|------------------------|
| 加元素 | `l.append(x)`、`l.extend(it)`、`l.insert(i, x)` | `l + [x]`、`l1 + l2`、`l * 3` |
| 删元素 | `l.remove(x)`、`l.pop(i)`、`l.clear()`、`del l[i]` | 列表推导式 `[x for x in l if 条件]` |
| 排序 | `l.sort()` | `sorted(l)` |
| 反转 | `l.reverse()` | `list(reversed(l))`、`l[::-1]` |
| 复制 | —— | `l.copy()`、`l[:]`、`list(l)` |

---

### 增（添加元素）

#### `l.append(x)`
在**末尾追加一个元素**（把 x 当成一整个对象）。原地修改，返回 `None`。
```python
l = [1, 2]
l.append(3)        # [1, 2, 3]
l.append([4, 5])   # [1, 2, 3, [4, 5]]  ← 整个列表变成 1 个元素
```

#### `l.extend(iterable)`
把可迭代对象里的元素**逐个**加到末尾（会拆开）。
```python
l = [1, 2]
l.extend([3, 4])   # [1, 2, 3, 4]
l.extend("ab")     # [1, 2, 3, 4, 'a', 'b']（字符串会被拆成字符）
l += [5]           # 等价于 l.extend([5])，同样是原地修改
```

#### `l.insert(i, x)`
在下标 `i` 处插入 x，后面的元素整体后移。`i` 超出范围不报错：太大相当于追加到末尾，负数会插到前面。
```python
l = [1, 2, 3]
l.insert(1, "a")   # [1, 'a', 2, 3]
l.insert(0, "头")  # ['头', 1, 'a', 2, 3]
l.insert(99, "尾") # 插到末尾
```

#### 用 `+` / `*` 拼出新列表（原列表不动）
```python
[1, 2] + [3, 4]    # [1, 2, 3, 4]
[0] * 3            # [0, 0, 0]
```

---

### 删（删除元素）

#### `l.remove(x)`
删除**第一个值等于 x** 的元素 —— 按**值**删，不是按**下标**。值不存在会 `ValueError`。
```python
l = [1, 2, 3, 2]
l.remove(2)        # [1, 3, 2]（只删掉第一个 2）
```

#### `l.pop(i=-1)`
删除**指定下标**的元素并**返回**它；不传参数默认删最后一个。空列表或下标越界会报错。
```python
l = [1, 2, 3]
last = l.pop()     # last = 3，l 变成 [1, 2]
first = l.pop(0)   # first = 1，l 变成 [2]
# 栈：l.append(x) 入栈，l.pop() 出栈（后进先出）
```

#### `l.clear()`
清空所有元素（列表对象本身还在，其他指向它的变量会看到它变空）。
```python
l = [1, 2, 3]
l.clear()          # []
```

#### `del l[i]` / `del l[i:j]` / `del l`
```python
l = [1, 2, 3, 4, 5]
del l[0]           # [2, 3, 4, 5]
del l[1:3]         # [2, 5]
l[0:1] = []        # 用切片赋空列表删除，等价于 del l[0:1]
del l              # 连变量一起删掉（再引用会 NameError）
```

#### 按条件过滤掉元素（不想原地改时）
```python
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]    # [2, 4, 6]，nums 不变
nums[:] = [x for x in nums if x % 2 == 0]  # 加 [:]，把结果塞回原列表
```

---

### 查（查找与统计）

#### `l.index(x, start=0, end=len(l))`
返回**第一个值等于 x 的下标**；找不到报 `ValueError`（不确定时先用 `in` 判断）。
```python
l = ["a", "b", "c", "b"]
l.index("b")       # 1
l.index("b", 2)    # 3（从下标 2 开始找）
"z" in l           # False ← 安全的存在性判断
```

#### `l.count(x)`
统计值等于 x 的元素个数。
```python
[1, 2, 2, 3].count(2)   # 2
```

#### `x in l` / `x not in l`
判断是否存在，返回布尔值，常直接写进 `if`。
```python
3 in [1, 2, 3]      # True
"a" not in ["b"]    # True
if "a" in ["a", "b"]:
    print("有")
```

#### 访问与切片（不是方法，但天天用）
```python
l = [10, 20, 30, 40, 50]
l[0], l[-1]        # 10, 50（-1 是最后一个）
l[1:3]             # [20, 30]（左闭右开）
l[::-1]            # [50, 40, 30, 20, 10]（反转的新列表）
```

---

### 改（修改、排序、复制）

#### `l[i] = x` / 切片赋值
```python
l = [1, 2, 3]
l[0] = 100                  # [100, 2, 3]
l[1:3] = ["a", "b", "c"]    # [100, 'a', 'b', 'c']（切片赋值长度可以不一样）
```

#### `l.reverse()`
**原地**反转，返回 `None`。
```python
l = [1, 2, 3]
l.reverse()               # l 变成 [3, 2, 1]
list(reversed([1, 2, 3])) # [3, 2, 1]，原列表不动
```

#### `l.sort(key=None, reverse=False)`
**原地**排序，返回 `None`。`key` 指定排序依据（参数和内置 `sorted` 一样）。
```python
l = [3, 1, 2]
l.sort()                    # [1, 2, 3]
l.sort(reverse=True)        # [3, 2, 1]
words = ["ccc", "a", "bb"]
words.sort(key=len)         # ['a', 'bb', 'ccc']
students = [{"name": "Tom", "score": 85}, {"name": "Jerry", "score": 92}]
students.sort(key=lambda s: s["score"], reverse=True)   # 按分数降序
```

#### `l.copy()` / 切片复制 / 深拷贝
```python
a = [1, 2, [3, 4]]
b = a              # 别名：a 和 b 是同一个列表，改一个另一个也变
b.append(9)        # a 也变成 [1, 2, [3, 4], 9] ← 别名的坑

c = a.copy()       # 浅拷贝：外层独立，嵌套的 [3, 4] 仍共享
d = a[:]           # 同样效果
e = list(a)        # 同样效果

import copy
f = copy.deepcopy(a)   # 深拷贝：连嵌套内容一起复制，彻底独立
```

---

### ⚠️ 新手最容易踩的 5 个坑

1. **方法返回 `None`，千万别接返回值**
   ```python
   l = [1, 2]
   l = l.append(3)     # ❌ l 变成 None，[1, 2] 也找不回来了
   l.append(3)         # ✅ 原地修改，不用赋值
   ```
2. **`append` 加整体，`extend` 拆开加**
   ```python
   l = [1]; l.append([2, 3])    # [1, [2, 3]]
   l = [1]; l.extend([2, 3])    # [1, 2, 3]
   l = [1]; l += [2, 3]         # [1, 2, 3]（+= 等价于 extend）
   ```
3. **`remove` 按值删，`pop` 按下标删**
   ```python
   [1, 2, 3].remove(2)   # ✅ 按值删
   [1, 2, 3].pop(2)      # ✅ 按下标删，返回 3
   # [1, 2, 3].pop("a")  # ❌ TypeError：pop 要的是下标
   ```
4. **边遍历边删会漏掉元素**（删掉一个后后面的元素前移，迭代器正好跳过它）
   ```python
   nums = [1, 2, 2, 3, 4]
   for x in nums[:]:        # 遍历副本，对原列表动手
       if x % 2 == 0:
           nums.remove(x)   # [1, 3]
   # 更推荐的写法：不改原列表，直接生成新列表
   nums = [x for x in nums if x % 2 != 0]
   ```
5. **`sorted()` 与 `sort()` 别搞混，`reversed()` 与 `reverse()` 同理**
   ```python
   l = [3, 1, 2]
   sorted(l)     # 返回 [1, 2, 3]，l 还是 [3, 1, 2]
   l.sort()      # l 变成 [1, 2, 3]，返回值是 None
   ```

---

## 十、tuple 常用操作（不可变序列）

> tuple 是**不可变**序列：没有 `append`/`remove`/`sort` 这些方法，只有 `count` 和 `index`。
> 它的价值在于「不会被误改」+ 可以当 dict 的 key + 一次返回多个值。

### 创建

#### 普通创建与单元素陷阱
```python
t = (1, 2, 3)
t = 1, 2, 3          # 括号可以省略，只要用逗号隔开
one = (5)            # ❌ 这是 int 5，不是元组
one = (5,)           # ✅ 单元素元组必须带逗号
empty = ()           # 空元组
tuple([1, 2])        # (1, 2)    由其他可迭代对象转换
tuple("ab")          # ('a', 'b')
```

#### 与 list 互转
```python
tuple([1, 2, 3])     # (1, 2, 3)
list((1, 2, 3))      # [1, 2, 3]
```

---

### 查（读取与统计）

```python
t = (10, 20, 30, 20)
t[0], t[-1]        # 10, 20
t[1:3]             # (20, 30)   ← 切片出来还是元组
t[::-1]            # (20, 30, 20, 10)
len(t)             # 4
t.count(20)        # 2      ← 元组只有 count / index 两个方法
t.index(20)        # 1
20 in t            # True
min(t), max(t), sum(t)   # 10, 30, 80   ← 这些是内置函数，不是方法
```

---

### 解包（tuple 最常用的玩法）

```python
a, b = (1, 2)             # a=1, b=2
a, b = b, a               # 交换两个变量，不用临时变量
x, y = (3, 5)             # 坐标拆成两个变量

first, *rest = (1, 2, 3, 4)   # first=1, rest=[2, 3, 4]（* 收集剩余，结果是 list）
*init, last = (1, 2, 3, 4)    # init=[1, 2, 3], last=4

# 函数一次返回多个值（本质就是返回元组）
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo=1, hi=4

# 遍历 [(key, value), ...] 结构的列表
for name, age in [("Tom", 5), ("Jerry", 6)]:
    print(name, age)
```

---

### 改？

元组本身不能改，但「重建一个」可以；`+=` 会生成**新**元组（这点和 list 原地修改不一样）。
```python
t = (1, 2)
# t[0] = 9        # ❌ TypeError: 'tuple' object does not support item assignment
t = (9,) + t[1:]  # ✅ 拼出一个新元组：(9, 2)

t2 = t
t += (3,)         # t 变成新对象，t2 仍指向原来的元组
print(t, t2)      # (9, 2, 3) (9, 2)

# ⚠️ 元组的「不可变」只到第一层：里面装 list 时照样能改
t3 = (1, [2, 3])
t3[1].append(4)   # 合法！t3 变成 (1, [2, 3, 4])
```

---

### 什么时候用 tuple 而不是 list

- 数据**固定不变**（坐标、RGB、一年的 12 个月）：用元组防误改。
- 需要当 **dict 的 key** 或放进 set（list 不可哈希，tuple 可以）：
```python
location = {(1, 2): "起点", (3, 4): "终点"}
{(1, 2), (3, 4)}          # ✅ 可以放进 set
# {[1, 2]}                # ❌ TypeError: unhashable type: 'list'
```
- 想要省一点内存，或者函数要返回多个值。
- 需要排序 / 筛选时，结果都是 **list**：`sorted(t)`、`[x for x in t if x > 1]`。

### ⚠️ 3 个坑

1. **单元素必须带逗号**：`(5)` 是 int，`(5,)` 才是元组。
2. **`t += (...)` 不是原地修改**：和 `l += [...]` 不同，元组会生成新对象，别的变量看到的还是旧值。
3. **元组只保护第一层**：里面装 list / dict 时，内层内容照样能改。

---

## 十一、set 常用方法（去重与集合运算）

> set 是**无序、不重复**的集合，元素必须可哈希（不能放 list / dict）。
> 两大优势：`in` 判断是 O(1)（列表是 O(n)），以及一行搞定去重和交并差。

### 创建

```python
s = {1, 2, 3}
s = set([1, 2, 2, 3])    # {1, 2, 3}   自动去重
s = set("hello")         # {'h', 'e', 'l', 'o'}（重复的 l 只留一个）
empty = set()            # ✅ 空集合
empty = {}               # ❌ 这是空字典，不是空集合！
s = {x for x in range(5) if x % 2 == 0}   # 集合推导式 {0, 2, 4}
```

---

### 增

#### `s.add(x)`
加一个元素；已存在则什么都不做（**不报错**）。
```python
s = {1, 2}
s.add(3)          # {1, 2, 3}
s.add(1)          # 还是 {1, 2, 3}
```

#### `s.update(iterable)`
一次加多个（相当于并集后就地更新）。
```python
s = {1, 2}
s.update([3, 4])      # {1, 2, 3, 4}
s.update("ab")        # {1, 2, 3, 4, 'a', 'b'}
```

---

### 删

#### `s.remove(x)` 与 `s.discard(x)` ← 最常问的区别
```python
s = {1, 2, 3}
s.remove(1)      # {2, 3}
# s.remove(9)    # ❌ KeyError：元素不存在就报错
s.discard(9)     # ✅ 不存在也不报错（不确定时优先用它）
```

#### `s.pop()` / `s.clear()`
```python
s = {1, 2, 3}
x = s.pop()      # 随机删掉一个并返回它（set 没有「第几个」的概念）
s.clear()        # set()
# set().pop()    # ❌ KeyError：空集合 pop 会报错
```

#### `del s`
```python
s = {1, 2}
del s            # 连变量一起删掉，再引用会 NameError
```

---

### 查

```python
s = {1, 2, 3}
3 in s           # True    ← 比列表的 in 快得多，「是否见过」首选 set
len(s)           # 3
# s[0]           # ❌ TypeError：set 无序无下标，不能索引/切片
sorted(s)        # [1, 2, 3]   要按顺序看，先转成 list
```

---

### 集合运算（交并差）—— set 的杀手锏

```python
a = {1, 2, 3}
b = {3, 4}

a | b    # 并集 {1, 2, 3, 4}        等价 a.union(b)
a & b    # 交集 {3}                 等价 a.intersection(b)
a - b    # 差集 {1, 2}（在 a 不在 b）  等价 a.difference(b)
a ^ b    # 对称差 {1, 2, 4}（只在其中一个里）  等价 a.symmetric_difference(b)

a.issubset(b)      # False：a 是 b 的子集吗？  也可写 a <= b
a.issuperset(b)    # False：a 包含 b 吗？      也可写 a >= b
a.isdisjoint(b)    # False：两个集合完全不相交吗？（没有共同元素）

# 就地运算（会修改 a）
a |= b     # a 变成并集 {1, 2, 3, 4}
a &= b     # a 变成交集
a -= b     # a 变成差集
```

---

### 典型用法

```python
# 1) 去重（会丢顺序）
nums = [1, 2, 2, 3, 1]
list(set(nums))              # [1, 2, 3]

# 2) 去重且保持原顺序（用 dict.fromkeys）
list(dict.fromkeys(nums))    # [1, 2, 3]

# 3) 两个列表找共同元素 / 独有元素
A = ["a", "b", "c"]; B = ["b", "c", "d"]
set(A) & set(B)              # {'b', 'c'}
set(A) - set(B)              # {'a'}

# 4) 大数据量判断「在不在」：set 比 list 快几个数量级
seen = set()
for x in [1, 2, 3, 2]:
    if x in seen:
        print("重复:", x)     # 重复: 2
    seen.add(x)
```

---

### ⚠️ 3 个坑

1. **`{}` 是空字典**，空集合只能写 `set()`。
2. **元素必须可哈希**：`{1, [2]}` ❌；要放组合值就用元组 `{(1, 2), (3, 4)}`。
3. **无序无下标**：不能 `s[0]`、不能切片，打印顺序也不保证；要顺序先 `sorted(s)`。另外 `remove` 不存在会报错、`discard` 不报错，记牢这条能省很多调试时间。

---

## 十二、dict 常用方法（增删改查与遍历）

> dict 是**键值对**映射：键必须可哈希且唯一，值随意。
> Python 3.7+ 起**保留插入顺序**（遍历顺序 = 你插入的顺序）。

### 创建

```python
d = {"name": "Tom", "age": 18}
d = dict(name="Tom", age=18)              # 键都是字符串时可用这种写法
d = dict([("a", 1), ("b", 2)])            # 由键值对序列创建
d = dict(zip(["a", "b"], [1, 2]))         # {'a': 1, 'b': 2}  与 zip 搭配很常用
d = {k: 0 for k in ["a", "b"]}            # 字典推导式 {'a': 0, 'b': 0}
empty = {}                                # 空字典
```

---

### 增 / 改

#### `d[key] = value`
键存在就**覆盖**，不存在就**新增** —— 只有这一种写法，不用记两个方法。
```python
d = {"a": 1}
d["b"] = 2       # 新增 {'a': 1, 'b': 2}
d["a"] = 99      # 覆盖 {'a': 99, 'b': 2}
d["age"] += 1    # ❌ 键不存在时 KeyError → 先写 d["age"] = d.get("age", 0) + 1
```

#### `d.update(other)`
批量新增 / 覆盖（另一个字典或键值对序列），原地修改。
```python
d = {"a": 1}
d.update({"b": 2, "a": 9})      # {'a': 9, 'b': 2}   同名的会被覆盖
d.update([("c", 3)])            # {'a': 9, 'b': 2, 'c': 3}
```

#### `d.setdefault(key, default=None)`
键存在 → 返回它的值（不动）；不存在 → 插入 `key: default` 并返回 default。适合「只初始化一次」。
```python
d = {"a": 1}
d.setdefault("a", 100)     # 返回 1，d 不变
d.setdefault("b", 0)       # 返回 0，d 变成 {'a': 1, 'b': 0}

# 典型场景：按城市分组
groups = {}
for name, city in [("Tom", "北京"), ("Jerry", "上海"), ("Bob", "北京")]:
    groups.setdefault(city, []).append(name)
groups     # {'北京': ['Tom', 'Bob'], '上海': ['Jerry']}
```

#### 合并字典：`|`（Python 3.9+）
```python
{"a": 1} | {"b": 2}     # {'a': 1, 'b': 2}
{"a": 1} | {"a": 9}     # {'a': 9}    右边覆盖左边
d |= {"c": 3}           # 就地合并
# 老版本写法：d3 = {**d1, **d2}
```

---

### 查（读取）

#### `d[key]` 与 `d.get(key, default)` ← 最容易踩的差别
```python
d = {"a": 1}
d["a"]               # 1
# d["b"]             # ❌ KeyError：键不存在就报错
d.get("b")           # None：不存在返回 None（不报错）
d.get("b", 0)        # 0：不存在返回指定默认值  ✅ 推荐

"a" in d             # True   判断的是「键」是否存在
"x" not in d         # True
len(d)               # 1
```

#### 取全部键 / 值 / 键值对
```python
d = {"a": 1, "b": 2}
d.keys()             # dict_keys(['a', 'b'])
d.values()           # dict_values([1, 2])
d.items()            # dict_items([('a', 1), ('b', 2)])
list(d.keys())       # ['a', 'b']
list(d.values())     # [1, 2]
list(d.items())      # [('a', 1), ('b', 2)]
```

---

### 删

#### `d.pop(key, default)`
删掉键并**返回**它的值；键不存在时：给了 default 就返回 default，没给就 KeyError。
```python
d = {"a": 1, "b": 2}
d.pop("a")           # 返回 1，d 变成 {'b': 2}
d.pop("z", None)     # 返回 None（安全）
```

#### `d.popitem()` / `del d[key]` / `d.clear()`
```python
d = {"a": 1, "b": 2}
d.popitem()          # 返回并删除最后一个键值对 ('b', 2)（3.7+ 后进先出）
del d["a"]           # 删掉指定键；不存在报 KeyError
d.clear()            # 清空 -> {}
```

---

### 遍历

```python
d = {"a": 1, "b": 2}

for k in d:                       # 只遍历键（等价 for k in d.keys()）
    print(k)

for k, v in d.items():            # 最常用：同时拿键和值
    print(k, v)

for v in d.values():              # 只遍历值
    print(v)

# 遍历中直接增删键会 RuntimeError: dictionary changed size during iteration
for k in list(d.keys()):          # 先转成 list 快照，再改
    d[k] = d[k] * 10
```

---

### 常用套路

```python
# 1) 计数（统计出现次数 / 词频）
counts = {}
for w in "a b a c a".split():
    counts[w] = counts.get(w, 0) + 1        # {'a': 3, 'b': 1, 'c': 1}
# 也可以用 collections.Counter("a b a c a".split())，一行搞定

# 2) 按值排序取前几名（得到的是 list of tuple）
scores = {"Tom": 85, "Jerry": 92, "Bob": 78}
sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:2]
# [('Jerry', 92), ('Tom', 85)]

# 3) 反转键值（前提：值唯一）
{v: k for k, v in {"a": 1, "b": 2}.items()}    # {1: 'a', 2: 'b'}

# 4) 比较两个字典的键差异
d1 = {"a": 1}; d2 = {"a": 1, "b": 2}
d2.keys() - d1.keys()        # {'b'}
```

---

### 复制

```python
d = {"a": [1, 2]}
e = d                # 别名：改 e 就是改 d
f = d.copy()         # 浅拷贝：外层独立，嵌套的 [1, 2] 仍共享
import copy
g = copy.deepcopy(d) # 深拷贝：彻底独立
```

---

### ⚠️ 4 个坑

1. **`d[k]` 取不存在的键会 KeyError**：不确定就用 `d.get(k, 默认值)`。
2. **`{}` 是空字典、`set()` 是空集合**：想要空集合别写成 `{}`。
3. **`in` 判断的是键不是值**：判断值要用 `value in d.values()`（O(n)，慢）。
4. **遍历中增删键会报错**：先 `list(d.items())` 拿快照，或先收集要删的键、循环结束后统一删。

---

## 十三、速查表

| 分类 | 函数 | 一句话作用 |
|------|------|-----------|
| 类型转换 | `int` `float` `str` `bool` | 转整数 / 浮点 / 字符串 / 布尔 |
| 容器转换 | `list` `tuple` `set` `dict` | 转列表 / 元组 / 集合 / 字典 |
| 数学 | `abs` `round` `pow` `sum` | 绝对值 / 四舍五入 / 幂 / 求和 |
| 数学 | `min` `max` `divmod` | 最小 / 最大 / 商和余数 |
| 序列 | `range` `enumerate` `zip` | 整数序列 / 索引+元素 / 打包 |
| 序列 | `sorted` `reversed` `slice` | 排序 / 反转 / 切片对象 |
| 高阶 | `filter` `map` | 筛选 / 映射 |
| 迭代 | `iter` `next` `all` `any` | 迭代器 / 取值 / 全真 / 任一真 |
| 输入输出 | `print` `input` `open` | 打印 / 输入 / 打开文件 |
| 对象 | `type` `isinstance` `issubclass` | 类型 / 类型判断 / 继承判断 |
| 属性 | `hasattr` `getattr` `setattr` | 属性检查与动态读写 |
| 对象 | `callable` `id` `dir` `vars` | 可调用? / 地址 / 属性名 / 命名空间 |
| 字符串 | `repr` `hash` `bytes` | 可读表示 / 哈希 / 字节串 |
| 动态 | `eval` `exec` `compile` | 求值 / 执行 / 编译 |
| 其他 | `len` `chr` `ord` `hex` `bin` `oct` | 长度 / 字符转码 / 进制转换 |
| list 增 | `append` `extend` `insert` `+` `*` | 末尾加一个 / 末尾加多个 / 指定位置插入 / 拼出新列表 |
| list 删 | `remove` `pop` `clear` `del` | 按值删 / 按下标弹出并返回 / 清空 / 按下标或切片删 |
| list 查 | `index` `count` `in` | 值→下标 / 统计个数 / 是否存在 |
| list 改 | `l[i]=` `reverse` `sort` `copy` | 改元素 / 原地反转 / 原地排序 / 拷贝（别名会联动） |
| tuple | `count` `index` `解包` | 计数 / 值→下标 / `a, b = t`、`a, *rest = t`（不可变，可当 dict 的 key） |
| set 增删 | `add` `update` `remove` `discard` `pop` | 加一个 / 加多个 / 不存在报错地删 / 不存在不报错地删 / 随机删一个 |
| set 运算 | `\|` `&` `-` `^` `union` `intersection` | 并集 / 交集 / 差集 / 对称差（去重、判重首选） |
| dict 增改 | `d[k]=` `update` `setdefault` `\|` | 新增或覆盖 / 批量合并 / 不存在才初始化 / 合并两个字典（3.9+） |
| dict 查 | `d[k]` `get` `keys` `values` `items` | 直接取（不存在报错）/ 安全取带默认值 / 键 / 值 / 键值对 |
| dict 删 | `pop` `popitem` `del` `clear` | 弹出指定键 / 弹出最后一个 / 删键 / 清空 |

---

## 学习建议

1. **先记高频**：`len` `range` `enumerate` `zip` `sorted` `map` `filter` `min/max` `sum` `any/all` —— 这 11 个覆盖了 80% 的日常场景。
2. **多写列表推导式**：`map`/`filter` 很多时候可以用更直观的列表推导式替代。
   ```python
   [x * 2 for x in range(5)]                    # 等价于 list(map(...))
   [x for x in range(10) if x % 2 == 0]         # 等价于 filter(...)
   ```
3. **类型判断用 `isinstance` 而非 `type`**：前者支持继承，是官方推荐写法。
4. **list 方法先记两条规律**：多数**原地修改**、返回值是 `None`；`sorted()` 生成新列表，`l.sort()` 改原列表。
5. **选容器先问自己 3 句话**：要按顺序、要频繁增删 → `list`；固定不变或要当 key → `tuple`；要去重、要做交并差、要快速判重 → `set`；要按键取值 → `dict`。
6. **别背签名**：用到时 `help(len)` 或 `len.__doc__` 随时查。
