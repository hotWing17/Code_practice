[TOC]
# JavaSE学习笔记
---

## 1.日常注意点
### 1.1 命名规范
- 包名：小写
- 类名，接口名：首字符大写
- 变量，方法名：驼峰命名法
- 常量名：全部大写
### 1.2 字节大小
> char:2字节 　float:4字节 　double:8字节
### 1.3 JUnit单元测试方法的使用
1. 测试方法上面必须使用@Test注解进行修饰。
2. 测试方法必须使用public void 进行修饰，不能带有任何参数。
3. 新建一个源代码目录用来存放测试代码。
4. 测试类的包应该与被测试类的包保持一致。
5. **具体配置环境和使用方法可以看“Ubuntu重装操作”里面的“IDEA”**

## 2.基本语法
### 2.1 运算符
- s+=2; 和 s=s+2;区别(+完之后是否会改变s的类型)
- 左移、右移符号(">>"_带符号右移；">>>"_不带符号右移)
- '^'异或符号（实现交换两个变量的值）
- break和continue 带标签的使用方法

### 2.2数组
#### 2.2.1 数组的默认初始化值
- **注意** 类里面的基本数据类型默认值同理(不是类内部的话基本数据类型要初始化，不然会报错)
- byte short int long 初始化默认值为0
- float double 初始化默认值为0.0
- char 初始化默认值为空格‘’
- booelean 初始化默认值为false
- 对于引用类型构成的数组而言， 初始化默认值为null
#### 2.2.2 null类型调用‘toString’方法引发空指针错误
#### 2.2.3 Arrays.sort()数组排序算法  

## 3.面向对象编程
> **三大特征**：封装 继承 多态
> **类的成员**: 属性 方法 构造器 初始化块 内部类
### 3.1匿名类对象的使用
> 只能在创建的时候调用一次

### 3.2 可变个数的形参的方法
- 格式：对于方法的形参，(数据类型 ... 形参名)
- 注意1：使用可变个数的形参方法 与 方法的形参使用数组 是一致的,如下
```java
public void sayHello(String ... args);
public void sayHello(String[]  args); 
```
- 注意2：若方法中存在可变个数的形参，那么一定要声明在形参的最后
```java
public void sayHello(int i, String ... args);
```
- 注意3：在一个方法中，最多声明一个可变参数的形参

### 3.3 方法的参数传递
> **规则**：java中的参数传递机制:值传递机制
> 1)形参是基本数据类型: 实参的值 -> 形参的基本数据类型的变量
> 2)形参是引用数据类型：实参的引用类型变量的值 -> 形参的引用类型变量

### 3.4 权限修饰符
- public
- protected
- 缺省
- private
> 以上用来修饰属性、方法，其中以上四个只有“public”和“缺省”可以修饰类

### 3.5 “this”关键字
- this(name);可以用来显示的调用当前类的重载的指定的构造器
- this(形参列表)必须在首行

### 3.6 "package"和"import"关键字
- "import static"导入包里面的属性或者方法
- “import java.lang.*”只能导入"lang"下的所有类或接口，其后的子类不能导入

## 4 类的高级特性1
### 4.1 继承
- extends关键字
- 当父类中有私有属性或方法时，子类获取的得到，但是由于封装性的原因，不能直接调用
- 仅支持单继承
#### 4.1.1 方法的重写(覆盖)
> 子类继承父类之后，父类的方法不适用，子类可以对父类的方法进行重写、覆盖
> 明白和"方法的重载"的区别
> **重写规则：**
> 1) 要求子类方法的“返回值类型 方法名(参数列表)”与父类方法一样
> 2) 子类方法的修饰符不能小于父类方法的修饰符
> 3) 若父类抛出异常，则子类方法抛出的异常类型不能大于父类的
> 4) 子父类的方法必须同为static或同为非static的
#### 4.1.2 super关键字
- 构造器默认：super()->调用父类的构造器,必须在首行
- super.属性名 ->调用父类属性
- super.方法名 ->调用父类方法
- 子类、父类的方法和属性重名时，要调用父类的就用super关键字
- 和“this(形参列表)”不能同时存在，两个都没有写的时候，默认调用super()

### 4.2 多态
- 子类对象的多态性：父类的引用指向子类对象(实际调用的是子类重写父类的方法)
- 向上转型，向下转型，小到大强制转型：Person p = new Woman; Woman w = (Woman)p;
- 传参数时：向下转型public void fun(Animal a){} //可以传"new Dog()"进去
- 属性不存在多态性

### 4.3 Object类及equals()、toString()方法
#### 4.3.1 equals()方法
- ”==“ 符号对于引用数据类型：比较的是引用类型变量的地址值是否相等
- 只能处理引用类型变量
- 有些类(如“String”)重写了equals()方法
- **String类**：创建的常量放在“字符串常量池”里面
```java
String str1 = "AA"  //1和2都指向字符串常量池
String str2 = "AA"
String str3 = new String("AA")  // 3指向对象的地址，对象里面的String属性还是指向常量池
```

#### 4.3.2 toString()方法
- 打印一个对象的引用时，实际就是调用该对象的toString()方法
    > 没有重写的toString()方法返回 该对象所在的类及对应的堆空间对象实体的首地址值

### 4.4 包装类(Wrapper)
     针对八种基本定义相应的引用类型--包装类(有了类的特点，就可以调用类中的方法)

基本数据类型 | 包装类
:---: | :---:
boolean | Boolean
byte | Byte
short | Short
int | **Integer**
long | Long
char | **Character**
float | Float
double | Double

     基本数据类型 包装类 String 三者之间的转换

转换 | 方法
:---: | :---
基本数据类型 ---> 包装类 | 调用包装类的构造器 Integer **Ex:** Integer i1 = new Integer(i);
包装类 ---> 基本数据类型 | 调用包装类的xxxValue()方法 **Ex:** int i2 = i1.intValue();
基本数据类型、包装类---> String | 调用String类的valueOf(xxx)方法 **Ex:** String str2 = String.valueOf(12)
String--->基本数据类型、包装类 | 调用包装类的parseXxx()方法 **Ex:** int i = Integer.parseInt(str2)

- **注意**：
1. Boolean构造器输入字符串是除了“true”,其余全是返回“false”
2. JDK5.0之后，有自动装箱和拆箱(**装箱：** Integer i3 = 23  **拆箱：** int i5 = i3)

## 4 类的高级特性2
### 4.1 static关键字
    静态结构的生命周期早于非静态的结构，同时被回收也晚于非静态结构
**修饰属性(类属性)**
- 存放位置：静态域
- 实例变量 or 类变量(static)
- 直接通过类调用
**修饰方法(类方法)**
- 非静态的方法可以调用静态方法
- 静态方法里面不能有this或super关键字的
- 静态方法只能调用静态的方法或者静态属性

### 4.2 单例设计模式
**使得一个类只能创建一个对象实例**
- 饿汉式和懒汉式(区别：创建类的时间是在类加载时，还是在第一次调用单体类时)
- Runtime类也是一个单体类
```java
//饿汉式
class Singleton {
    //1.私有化构造器，使得在类的外部不能够调用此构造器
    private Singleton() {
    }
    //2.在类的内部创建一个类的实例
    private static Singleton instance = new Singleton();

    //3.私有化此对象，通过公共的方法来调用
    //4.此公共的方法，只能通过类来调用，因为设置为static的,同时类的实例也必须为static声明的
    public static Singleton getInstance() {
        return instance;
    }
}

//懒汉式：可能存在线程安全问题
public static Singleton1 getInstance() {
        if(instance == null){
            instance = new Singleton1();
        }
        return instance;
    }
```

### 4.3 类的初始化块(或代码块)
1. 代码块如果有修饰符的话，那么只能使用static
2. 静态代码块
    ```java
    static{
    }
    ```
    >(1)随着类的加载而加载
    >(2)内部只能执行静态的结构(类属性、类方法)

3. 非静态代码块
    >(1)可以为类的属性进行初始化
    >(2)可以有多个代码块，顺序执行
    >(3)每创建一个对象，代码块就加载一次
    >(4)非静态代码块的执行顺序早于构造器

### 4.4 final关键字
- 修饰类:不能被继承
- 修饰方法：不能被重写
- 修饰属性：此属性就是一个常量，初始化后不可再被赋值，习惯上，常量用大写字符表示
    ①此常量不能使用默认初始化
    ②显示的赋值、代码块、构造器
**变量用static、final修饰**：全局常量

### 4.5 抽象应用(abstract)
```java
abstract class Person{ // 抽象类
    public abstract void eat(); // 抽象方法
    public abstract void walk();
}
```
#### 4.5.1. 修饰类：抽象类
    ①不可以被实例化
    ②抽象类有构造器
    ③抽象方法所在类一定是抽象类
#### 4.5.2. 修饰方法：抽象方法
    ①若子类继承抽象类，**没有重写**所有的抽象方法，意味着此类中仍有抽象类，则此类必须声明为抽象的！
#### 4.5.3. abstract的限制
**注意**：abstract 不能用来修饰属性、构造器、private、final、static(原因)
- 属性：本身就不能修饰
- 构造器：构造器不能被重写
- private:子类不能覆盖（或重写）声明为private的方法的
- final
- static:直接通过类调用但是却没有功能，所以不能
#### 4.5.4 模板方法的设计模式
- 就是抽象类的设计
```java
// 计算一个方法的运算时间
abstract class Template {
    public abstract void code();

    public void spendTime(){
        long start = System.currentTimeMillis();
        code();
        long end = System.currentTimeMillis();
        System.out.println("花费的时间为：" + (end - start));
    }
}
```

### 4.6 接口(implements 和 interface)
- 只含有常量和抽象方法(接口与类 是并行的一个概念)
- 接口定义的是一种功能，可以被类所实现(**implements**)
- 实现接口的类，必须重写其中的所有抽象方法，否则仍为抽象类
- 类可以实现多个接口
- 接口之间的关系：继承(entends) **多继承**
    ```java
    interface AA{
        // 常量:所有常量都用(public static finnal)修饰，可省略
        public static final int I = 12;
        // 抽象方法:所有抽象方法都用(public abstract)修饰，可省略
        public static void method();
    }
    ```
#### 4.6.1 接口与具体的实现类之间也存在多态性
- 虚拟方法的调用
#### 4.6.2 接口“工厂方法”设计模式(FactoryMethod)

#### 4.6.3 接口“代理模式”
概述：为其他对象提供一种代理以控制对这个对象的访问

### 4.7 内部类
1. 类的内部再定义类
2. 成员内部类×(声明在类内部且方法外的) vs 局部内部类(声明在类的方法里)
#### 4.7.1 关于内部类要求掌握
1. 如何创建成员(静态、非静态)内部类的对象
2. 如何区分调用外部类、内部类的变量(尤其是变量重名时)
```java
Preson.this.name;
```
3. 局部内部类的使用(较少使用)

## 5 异常处理
```java
/*java.lang.Throwable
    |-----Error:错误，程序中不进行处理
    |-----Exception:异常，要求在编写程序时，就要考虑到对这些异常的处理
*/
```
### 5.1 常见的异常(Exception)
#### 5.1.1 编译时异常
#### 5.1.2 常见运行时异常
1. ArrayIndexOutOfBoundsException(数组越界异常)
2. ArithmeticException(算术异常)
3. ClassCastException(类型转换异常)
4. NullPointerException(空指针异常)

 ### 5.2 处理异常Exception的方法
**抓抛模型**
1. 抓：异常的处理：(1)try-catch-finally (2)throws + 异常的类型
2. 抛：(自动的抛出 vs 手动的抛出(throw + 异常类的对象))
    >(1)现成的异常类
    >(2)自己创键的异常类
#### 5.2.1 方法一
1. finally可选(无论如何都会被执行)
2. catch语句内部是对异常对象的处理
    >1. getMessage();
    >2. printStackTrace();
3. 多个catch语句，从上往下匹配，执行完就退出，不继续执行
4. 若多个异常类型是"并列"关系，顺序无关
    若多个异常类型是"包含"关系，需将子类放在父类上面

5. 对于运行异常来说可以不显示的进行处理
    对于编译时异常，必须要显示的进行处理
```java
try{
    //可能出现异常的代码
}catch(Exception e){
    //1. getMessage(); 获取错误信息
    //2. printStackTrace(); 打印错误的堆栈信息
}finally{
    //一定要执行的代码
}
```

#### 5.2.2 方法二(声明抛出异常)
1. 在方法的声明处，显示的抛出该异常对象的类型(**throws**)
```java
    public void method2() throws IOException{}
```
2. 手动的抛出一个异常(当代码不是按照本意执行时，手动抛出异常)(**throw**)
```java
    throw new RuntimeException("传入类型有误");
```
3. 抛出的异常类型，若是RuntimeException，可以不显式的处理
    若是一个Exception，必须显式的处理
4. 子类重写的父类方法，子类方法抛出的异常类型不能比父类方法抛出的异常类型大

#### 5.2.3 自定义一个异常类
1. 自定义的异常类继承现有的异常类
2. 提供一个序列号，提供几个重载的构造器(可以参考继承的类的结构)


## 6 Java集合
```java
/*Collection接口
    |-----Set接口:元素无序、不可重复的集合
            |-----HashSet(主要实现类)
            |-----LinkedHashSet
            |-----TreeSet
    |-----List接口:元素有序、可重复的集合
            |-----ArrayList(主要的实现类)
            |-----LinkedList
            |-----Vector(古老的实现类，线程安全的)
**Map接口：具有映射关系"key-value对"的集合
    |-----HashMap
    |-----LinkedHashMap
    |-----TreeMap
    |-----HashTable(子类：Properties)
*/
```

### 6.1 集合的方法

1. size()
2. add(Object obj)
3. addAll(Collection coll)
4. isEmpty()
5. clear()
6. contains(Object obj)：是否包含(自定义类对象则是判断equals()方法)
7. containsAll(Collection coll)
8. retainAll(Collection coll):求当前集合与coll的共有元素，返回给当前集合
9. remove（Object obj）:boolean
10. removeAll(Collection coll )
11. equals(Object obj):判断集合中的所有元素是否完全相同
12. hashCode():计算hash值
13. toArray():将集合转换成数组
    Object[] obj = coll.toArray();
14. **使用迭代器实现集合的遍历**
iterator():返回一个Iterator接口实现类的对象,进而实现集合的遍历
```java
    Iterator iterator = coll3.iterator();
    while(iterator.hasNext()){
        System.out.println(iterator.next());//next()导致向下引用移动
    }
```
15. **使用增强For循环实现集合的遍历**
```java
    for(Object i :coll3){   //注意：从"coll3"取一个元素赋值给”i“
        System.out.println(i);
    }
```

### 6.2 ArrayList 额外方法
**ArrayList:List的主要实现类**
1. void add(int index, Object ele):在指定的索引位置index添加元素ele
2. boolean addAll(int index, Collection eles)
3. Object get(int index):获取指定索引的元素
4. Object remove(int index):删除指定索引位置的元素
5. Object set(int index, Object ele):设置指定索引位置的元素为ele
6. int indexOf(Object obj):返回obj在集合中首次出现的位置。没有的话，返回-1
7. int lastIndexOf(Object obj)：返回obj在集合中最后一次出现的位置.没有的话，返回-1
8. List subList(int fromIndex, int toIndex):返回从fromIndex到toIndex结束的左闭右开一个子list

List常用的方法：增(add(Object obj)) 删(remove) 改(set(int index,Object obj))
            查(get(int index)) 插(add(int index, Object ele)) 长度(size())


### 6.3 Set接口
- 存储的元素是无序的(底层存储无序)，不可重复的
- **说明**： 要求添加进Set中的元素所在的类，一定要重写equals()和hashCode()方法。进而保证Set中元素的不可重复性
- Set中的元素是如何存储的呢？使用哈希算法
    >添加Set对象时：①hashCode() -> ②equals()
#### 6.3.1 HashSet(主要实现类)
#### 6.3.2 LinkedHashSet
- 使用链表维护了一个添加进集合中的顺序，导致当我们遍历LinkedHashSet集合元素时，按照添加进去的顺序遍历
- 插入性能略低于HashSet,迭代访问时有较好的性能
#### 6.3.3 TreeSet
1. 向TreeSet中添加的元素必须是同一个类的
2. 可以按照添加进集合中的元素的指定的顺序遍历(默认:从小到大) -> (需要实现Comparable接口的compareTo()方法)
3. 当向TreeSet中添加自定义类的对象时，有两种排序方法(用哪种排序方法取决于能否修改要比较的类)：
    >(1)自然排序:需要实现Comparable接口的compareTO()方法,在此方法中，指明按照自定义类的哪个属性进行排序
    >(2)定制排序:
    ①创键一个实现了Comparator接口的类对象
    ②将此对象作为形参传递给TreeSet的构造器中
    ③向TreeSet中添加Comparator接口中的compare方法中涉及的类的对象。
    ```java
    /*
	 * TreeSet的定制排序： 见下面的步骤 compare()与hashCode()以及equals()三者保持一致！
	 */
	@Test
	public void testTreeSet2() {
		// 1.创建一个实现了Comparator接口的类对象
		Comparator com = new Comparator() {
			// 向TreeSet中添加Customer类的对象，在此compare()方法中，指明是按照Customer
			// 的哪个属性排序的。
			@Override
			public int compare(Object o1, Object o2) {
				if (o1 instanceof Customer && o2 instanceof Customer) {
					Customer c1 = (Customer) o1;
					Customer c2 = (Customer) o2;
					int i = c1.getId().compareTo(c2.getId());
					if (i == 0) {
						return c1.getName().compareTo(c2.getName());
					}
					return i;
				}
				return 0;
			}
		};
		// 2.将此对象作为形参传递给TreeSet的构造器中
		TreeSet set = new TreeSet(com);
		// 3.向TreeSet中添加Comparator接口中的compare方法中涉及的类的对象。
		set.add(new Customer("AA", 1003));
		set.add(new Customer("BB", 1002));
		set.add(new Customer("GG", 1004));
		set.add(new Customer("CC", 1001));
		set.add(new Customer("DD", 1001));

		for (Object str : set) {
			System.out.println(str);
		}
	}
    ```

4. compareTo()方法 -> hashCode() -> equals()
