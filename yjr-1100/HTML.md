

[TOC]

# 一、互联网原理  

​	HTML : 制作网页   

​	通过浏览器输入网址  http协议  发送请求到服务器，服务器响应，把文件传输到浏览器

​	数据：文字，图片，视频，音频等。

### 	1、服务器

​	本身也是电脑，server。功能比普通计算机强大，用于存放文件，数据上传和更改在本地计算机，通过一些管理软件远程控制服务器，服务器要二十四小时开机

### 	2、浏览器

​	网页请求和接受的客户端。browser。发起http请求，接受服务器传输的文件，由不同厂商提供和维护，全球五大浏览器，谷歌（chrome），火狐（Firefox）、IE、苹果（Safari）、欧朋（opera）。浏览器不同版本渲染能力不同，浏览效果不一样。

​	请求的数据不是存在浏览器软件上，而是存在本地的一个临时文件夹。

### 	3、http协议

​	http：hypertext transfer protocol,超文本传输协议  F12 看请求

# 二、HTML基础

### 	1、 纯文本

​	 纯文本：只包含文字，如 记事本文件（只保存文字内容，没有任何形式，其设置格式后只是在本地显示，在其它电脑看到的没有格式。）

​	HTML  css  JS 都是纯文本文件 只要是纯文本文件都可用任意的纯文本编辑器进行编辑

<!--专门制作网页的软件-->：<Dreamweaver   Sublime   Webstorm>

### 	2、HTML的基本概念

​	HTML：hypertext markup language  超文本编辑语言

​	作用：制作网页页面 负责描述文档的语义，计算机不会主动分析人说话的语义，HTML 用文本给普通文本添加语义，这些文本就是超文本，超文本在浏览器中不会显示，通过一些标签来控制语义

>><h1>:将两个标签的内部的文本添加了一级标题的语义</h1>:将两个标签的内部的文本添加了一级标题的语义

>><h2>:将两个标签的内部文本添加了二级标签的语义</h2>:将两个标签的内部文本添加了二级标签的语义

>><p>将两个标签内添加一个段落的语义</p>:将两个标签内添加一个段落的语义

h1标签的作用不是让字变大变粗，而是添加了一个标题语义，真正的样式是css控制

### 3、sublime的基本操作

##### 配置sublime：

​	shift+ctrl+p →→install Package→→chinese 配置中文环节

​	shift+ctrl+p →→install Package→→emmet  插件

##### 快捷键：	

​	ctrl+滚轮  放大缩小字体

​	shift+ctrl+D 复制光标所在行

​	shift+ctrl+k 删除光标所在行

​	shift+ctrl+⬆ 上移当前行

​	shift+ctrl+⬇  下移当前行

​	标签名→ tab 自动生成标签对

​	html：xt → tab  自动生成html的结构  XHTML1.0  transitional 版本

​	html：xt → tab  自动生成html的结构  XHTML1.0  strict 版本

​	html：5 → tab  自动生成html的结构  HTML5 版本

​	按住滑轮向下拉 :  多段同时输入

​	h$*数字 → tab  生成标签从h1到h数字

​	p*数字 → tab  生成数字个p标签

# 三、HTML结构

### 1、HTML骨架

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>我是标题</title>
</head>
<body>
	我是内容
</body>
</html>
```
* html：  最根本的标签，表示网页

* head： 网页的头部，里面是网页的配置，除了title其他的内容在网页中不显示

* title：   网页的标题，

* body： 用户能看到的内容

![](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%202019-10-02%20072722.png)

### 2、文档DTD

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

​	DTD ：doctype definition。文档类型定义，定义此HTML文件用的是什么版本的html规范。HTML规范是我们书写HTML要遵循的规范，规定了我们使用的标签和语法。

### 3、html标签

```html
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
```

​	html标签 是双标签，开始和结束标签成对出现。

​	html有两个属性：

​		1、xmlns : xml的namespace 规定了使用标签的命名规范。

​		2、xml:lang : 规定html文件标签都必须使用英文。

### 4、head标签

​	head标签是双标签，里面是我们对网页的配置。

​	head标签内部

​	***mata标签：***规范我们网页使用的字符集。

```html 
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
```

> > 国际标准字库：utf-8，包括世界上人类的说有语言，中文占3个字节

> > 国家标准字库：gb2312/gbk，包括所有的简体字，大部分繁体，一些特殊符号。中文占2个字节。

>  **注意**：规定的字符集必须与编辑软件的保存字符集类型一致，否则会出现乱码
>
> <img src="https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%202.png" alt="批注 3" style="zoom:80%;" />

​		***title 标签：***双标签，内部书写网页的标题。

```html
<title>我是标题</title>
```

> > 搜索引擎优化，SEO 提升我们搜索排名，title里的文字会作为关键字首先被搜索引擎抓取。

# <font color="red" size="70">四、HTML的语法</font>

### **1、标签之间对换行空格不敏感**

​		标签之间对换行空格不敏感，对标签之间的嵌套敏感 （为了保证代码可读性强，可对标签合理缩进。）

```html
<html>
    <head>
        <title>巴拉巴拉</title>
        <div>
            <p>
           		<h1>
                    
            
            	</h1>
            </p>
        </div>
    </head>
</html>
```

### **2、空白折叠现象**

​		在普通文本内部：如果有空格，缩进，换行，将这些空白区折叠为一个空格显示。

<img src="https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%203.png" alt="批注 3" style="zoom:80%;" />

### **3、html标签**

​		标签：也叫标记。

   * 标签必须写在尖括号中<p> 

   * 双标签必须成对出现

   * 双标签中结束标签必须有关闭符号 **“/”**  

   * 标签分类：

     容器级：内部还可以嵌套任意类型标签

     文本级：只能放文字，图片，表单元素，不能放容器级标签。        	

### **4、标签属性**

​		每个标签都有自己特定的属性。（属性都用属性值，属性名（k），属性值（v），且书写时用键值对写法）

  * 属性写在标签的其实标签内，与标签名之间用 *空格隔开* ，属性与属性之间也用空格隔开

  * 键值对书写格式：
    $$
    k="v"
    $$
    中间不能有空格

  * 属性值必须用 *双引号* 包裹，XHTML 严格要求用 *双引号* 。

		* 标签的属性值可以有一个或多个，多个属性值之间用 *空格* 隔开，但必须都在引号内部。

# 五、HTMl 的标签

### 1、h系列

​		从h1~h6 级别依次降低，h1权重最高，最便于搜索引擎搜索。一个页面一般只有一个h1标签，且给logo，

​		所有的h系列标签都是容器级，但不存在嵌套关系。

​		h标签的属性：

* id 设置标签id名，用于页面内锚点跳转

### 2、p标签

​		paragraph，文本级标签

​		**注意**:一个 p标签 只能作用一个段落		

### 3、img标签

​		image 图片的意思，表示引入一张图片，本身相当于一个特殊的文本。

​		img 标签是一个 单标签 ，可插入图片类型：jpg、png、gif。			

​		img 标签  ``<img />``  属性：

  * src：source 表示图片路径  <!--必须写的属性-->

    **路径就是查找相关文件位置的方法。查找方式有两种：**

    ​		相对路径：查找文件时，从html文件本身出发，查找文件位置。

    > > > 同级查找：直接书写文件名字（包括文件名和扩展名）

    > > > 子集查找：进入文件查找过程。书写对应文件夹的名字/书写对应文件名字
    > > >
    > > > ``<img src="wenjianjia/tupian.jpg" />``

    > > > 上级查找：文件放在上一级的文件夹里，先退出当前文件夹，用符号``../`` 退出几级写几次。
    > > >
    > > > ``<img src="../tupian.jpg" />``
    >
    > **注意** ：
    >
    > * 以上说的级别是对于 当前正在编辑的html文件所说的。
    > * 不能跨磁盘进行查找

    ​			绝对路径：从磁盘出发查找文件，以http://开头的也是绝对路径。

    **注意** ：常用相对路径和网址的形式来查找图片。



- ​			width：  表示图片的宽度，单位是px，单独设置宽度，高度会等比例缩放
- ​			height： 表示图片的高度，单位是px，单独设置高度，宽度会等比例缩放
- ​			border ：边框属性；它的值可以表示边框的厚度
- ​			title： 设置提示文本
- ​			alt： 设置图像没有找到时候的替换文本

### 4、a 标签

​		anchor：超级链接，可以跳转到相应的网页，是双标签。

​		a 标签  ``<a>文字，图片提示跳转的地方</a>``  的属性：

* href ：设置跳转到的路径 <!--必须有--> 

* target ：表示是否在新标签页打开链接，属性值”_blank“表示在 新窗口打开，默认是在原来窗口打开。

* name： 用于标记锚点位置

* title ：鼠标悬停文本  ``<a title="悬停提示内容"></a>``

* 页面内锚点跳转：

  > 添加锚点的方法

  > > ​	给对应位置的标签添加一个id属性，属性值就是 id 名  ``<a href="#id"></a>`` 
  > >
  > > ​	跳转锚点：把href 属性写为#id 名

  > > ​	在需要添加锚点的位置，加入一个a 标签，不用href 属性，添加一个 name属性
  > >
  > > ​	跳转锚点：把href 属性写为#name 名  ``<a href="#name"></a>``

  > **注意**：id名 和name 名在网页内必须唯一
>
  > `href="#"`时，默认回到网页顶部位置，`href`属性值设置为`mailto:邮箱地址`，这样做可以调起邮箱应用，发送邮件到对应地址。

  ``跨页面锚点跳转  <a href="页面路径#id名"></a>``

  # 六、列表

  ​		将一些内容或者样式相近的相关内容一起书写。

  ### 1、无序列表：

  ​			是一组标签。ul: unordered list       ;

  ​								     li: list item,列表项。

  ​			ul和li 是嵌套关系

  ​           li 标签是容器标签，里面还可以再嵌套无序列表。

  ```html
  <ul>
  <li>  </li>
  <li>  </li>
  <li>  </li>
  </ul>
  ```

    		无序列表只会搭建列表，没有小圆点等样式，小圆点是css弄的。

  ### 2、有序列表：

  ​		 是一组标签。ol:  ordered list   ;

  ​			 	 	 	 	    li: list item, 列表项。

  ​		   ol和li 是嵌套关系

  ​           li 标签是容器标签，里面还可以再嵌套有序列表，嵌套会缩进。

  ```html
  <ol>
  <li>  </li>
  <li>  </li>
  <li>  </li>
  </ol>
  ```

    		有序列表只会搭建列表，没有123等顺序样式，序号是css弄的，内置的预设样式。		

  ### 3、定义列表

  ​		有三个标签参与，dl dt dd

  ​		有自己定义的主题，定义的解释。

  ```html
  <dl>
      <dt></dt>
      <dd></dd>
      
      <dt></dt>
      <dd></dd>
  </dl>
  ```

   	dl 嵌套 dt 和 dd ,一个dl 可以嵌套几个dt 和dd 

   	dl：definition  list定义列表

   	dt ：definition title 定义的主题

   	dd : definition description 定义主题的解释，解释前面最近的dt 

   	一个dt 可以有一个或者多个dd去解释，也可以不加dd

   	dt 和 dd 都是容器级标签

#  七、div 和 span 		

### 1、div 和 span 的认识

 		统称为盒子，双标签

 		div 是大的范围，span 是小的跨度

 		div ：division 没有特殊语义，用来布局。里面经常放置有特殊功能，类似类型的标签，典型的容器级标签，可以放置任何标签

 		span ：小区域，小跨度，常用小范围布局。文本级标签，不能盛放容器级标签。

# 八、表格

 	1、表格基础

 			``table``，``tr``，``td``，三者之间是嵌套关系，```table > tr > td```

 			``table``: 表格。

​          	<font size="5" color="red">表格属性</font>

- ​	`cellpadding`，它规定了单元边沿与其内容之间的空白。

- ​    `width`，宽，值可以是像素，也可以是百分数

- ​    `height`，高，值可以是像素，也可以是百分数

-    `cellspacing`，它规定了单元格之间的间隔。

  

  			``tr ``：table rows，行。

 			`` td ``: table dock ， 单元格。

```html
<table border="1">
    <tr>
        <td>第一行第一列</td>
        <td>第一行第二列</td>
        <td>第一行第三列</td>
    </tr>
    <tr>
        <td>第二行第一列</td>
        <td>第二行第二列</td>
        <td>第二行第三列</td>
    </tr>
</table>
```

   添加表头语义，th 标签表示表头单元格。在``tr ``中把``td`` 换为`` th`` 

scope 属性

`<th>`元素的`scope`属性用于定义表头数据与单元数据关联的方法。本例中值为`col`，表示规定的是列的表头。

| 值       | 含义                 |
| -------- | -------------------- |
| col      | 单元格是列的表头     |
| row      | 规定单元格是行的表头 |
| colgroup | 单元格是列组的表头   |
| rowgroup | 单元格是行组的表头   |

### 2、合并单元格

 		``td`` ,``th`` 有两个属性用来合并单元格  

 		  rowspan：合并行方向单元格

  		  colspan ：合并列方向单元格

  		 属性值是一些数字，是几就合并几个单元格，单元格上边线对齐的算一行。

```html
<table border="1">
		<tr>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
		</tr>
		<tr>
			<td rowspan="2">6</td>
			<td colspan="2">7</td>
			<td colspan="2">8</td>
		</tr>
		<tr>
			<td>9</td>
			<td>10</td>
			<td rowspan="2">11</td>
			<td>12</td>
		</tr>
		<tr>
			<td colspan="2">13</td>
			<td>14</td>
			<td>15</td>
		</tr>
```

![](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%202019-10-03%20064159.png) 

### 3、表格分区

 			标题：caption  ``<caption></caption>``  写在table 下一行

 			表头：thead  ``<thead></thead>``  写在caption下面

 			主题：tbody 

```html
<table border="1">
		<caption>各地区固定资产投资情况</caption>
		<thead>
			<tr>
				<th rowspan="2">地区</th> >
				<th colspan="2">按总量分</th>
				<th colspan="2">按比重分</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>本年初累计</td>
				<td>比去年增长</td>
				<td>本年初累计</td>
				<td>去年同期</td>
			</tr>
			<tr>
				<td>全国</td>
				<td>1876702</td>
				<td>6.5</td>
				<td>100</td>
				<td>100</td>	
			</tr>
			<tr>
				<td>宁夏</td>
				<td>568423</td>
				<td>10.9</td>
				<td>45</td>
				<td>44</td>
			</tr>
		</tbody>
```

 			![批注 2019-10-03 070346](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%202019-10-03%20070346.png)

# 九、表单

 		表单就是网页上可以供用户输入和选择的控件

### 1、form 标签

  		所有的表单元素需要写在form 标签内部，不是一个结构标签，而是功能性标签

  		功能：规定我们提交的数据发送到哪，发送到方法是什么。

   		method：提交数据的方法，属性值 get，post

  		 action： 提交的位置

### 2、文本框

  		  允许用户输入文本

   		  input标签：输入，单标签  ，

  				有一个属性：type。根据属性值不同，input标签代表的是不同表单元素，表单元素类似于特殊文本，type值是text时代表单行文本框。

​      			 属性：value。表示“值”,没输入之前的默认文本。

​								placeholder,也是没输入前显示的，但颜色浅，输入时消失。

​								size ，拓宽单行文本框

​								maxlength ，最大输入字符数

​								readonly，只读，不能删改



```html
<p>
   文本框:<input type="text" value="默认文本"/>
</p>
```

![批注 2019-10-03 071945](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%202019-10-03%20071945.png)

### 3、密码框

​		 input标签

  		 type属性是password

### 4、按钮

​		 input标签

 		 	1、普通按钮  type属性 ：button    

  			 2、提交按钮 type属性 ：submit

  			  3、重置按钮  type属性：reset

> 注意：通过value 来设置按钮上的文字

### 5、单选框

 		input标签

  			  type属性：radio  一组单选框只能选一个，但需要设置 name属性来设置哪几个单选框是同一组

![批注 2019-10-03 085129](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(2).png)

在选项后面加`<br>` 来使选项分段

### 6、多选框

 		input标签

   	 	 	  type属性 ： checkbox ，也可以加name名给其分组

​		 		  在选项后面加`<br>` 来使选项分段

<font size="5" color="green">**单选与多选通用属性**：</font>

`1、disabled`属性，

​	它会禁用该`input`元素，其默认值为`disabled`。

***注意：***

* 只要有`disabled`属性就会被禁用，不管它的值是什么；

* 不想被禁用，不添加`disabled`属性就可以了。

* 为了规范书写，一般添加`disabled="disabled"`就可以了。

`2、checked`属性，

​		它会默认选中该`input`元素

***注意：*** 

- 只要有`checked`属性就会被默认选中，不管它的值是什么；
- 不想被默认选中，不添加`checked`属性就可以了。
- 为了规范书写，一般添加`checked="checked"`。

### 7、文本域

  		  	 双标签： textarea。 可以输入多行文本。

 **两个属性值**：

*  cols : 属性值是数字，表示每一行有多少字节
* rows :属性值是数字，表示有多少行
* maxlength :属性是数字，表示最大能输入的字符数

<style></style>标签里设置宽度为200px，高度为120px 
```html
<style>
textarea{
	width : 200px ;
	height : 120px ;  
}
</style>
```

***注意***：width 和数字之间是冒号，数字后有封号

### 8、下拉菜单

​		一组标签，必须同时出现，有嵌套关系。

   		select：选择

​            option：选项  添加`selected="selected"`属性 默认选择该`option`

​          **select > option **  

```html
<select>
	<option>问答</option>
	<option>分享</option>
	<option>招聘</option>
	<option selected="selected">客户端测试</option>
</select>
```

![批注 2019-10-03 145329](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(7).png)

### 9、range表单

一个滑条样的东西，

属性：min 最小值

​			max 最大值

​			step：规定滑动的节点，如step="100",只能一次划100个值，不能放在中间。

​			value：初始滑块位置。

# 十、HTML 杂项

### 1、注释

​	 方便程序员自己看，不会再浏览器上渲染

 	 ``<!--注释-->`` sublime 快捷键 ctrl+/

### 2、字符实体

一些特殊符号不能直接在文本内容里显示，html 提供 了一套特殊符号的代替符号，叫做字符实体。

*  <    ``&lt;``
*   &gt;   ``&gt;``
* 无换行空格：&nbsp；
* 版权：&copy；

### 3、废弃标签

![批注 2019-10-03 094002](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(4).png)

![批注 2019-10-03 094419](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(5).png)

### 4、提高用户体验

`<label>`标签：***``<label></label>``***

 <font color="blue">双标签</font>，当点击`<label>`元素内的文本时，焦点会自动定位到与`<label>`标签绑定的表单元素上。通俗地说，就是点击文本也能选择表单元素。

```html
<label for="user">用户：</label>
<input type="text" id="user" name="user" /><br>
<label for="pwd">密码：</label>
<input type="password" id="pwd" name="password" />
```

![批注 2019-10-03 144518](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(6).png)

***注意：***`<label>`标签的`for`属性的值要和相应<font size="4" color="red">表单元素</font>的`id`的值相同。这样才能把`<label>`标签和表单元素绑定到一起