[TOC]



# **css**

## 一、CSS的基础知识

### 1、css  概念

​		css：层叠式样式表。规定了html 标签在网页上的显示样式。

​		前端三层：

​				html				结构层，搭建网页的整体结构

​				css					样式层，装饰页面

​				Javascript		行为层，页面交互效果

### 2、css  作用

​		css 两个重要的概念：层叠式，样式。

​		样式 ：html 标签在页面的显示效果。 某个标签有什么样式就写什么

```html
div{
	width: 300;
	height:300;
	background:yellow;
}
```

  	  css样式设置时有两个关键：`选择器` ，`样式表 ` 

​	 	 css作用细化

* 给文本添加文字样式
* 给盒子添加属性进行结构布局

### 3、css几个小属性

  	① 文字样式

  		字体、颜色、大小。

  	    大小：font-size。以像素为单位

  		 颜色：color。属性值有几种选择方案：十六进制，RGB,颜色名。

> 白色的几种表示方法：#ffffff，rgb（255，255，255），white。		

​			字体：font-family，有中文字体和英文字体。英文常用：Arial，consolas。中文：默认字体为宋体，常用：微软雅黑。  

​			所有字体用双引号包裹，字体与字体之间用逗号隔开。一般把英文字体写在前，中文写在后。

> ​	微软雅黑：Microsoft Yahei
>
> ​            宋体：SimSun

 	② 盒子实体化基本属性

  		实体化：将盒子给宽和高，背景色，边框。

  		 宽度：width        高度：height

  		  背景色：background-color

   		 边框：border，复合属性，有多个属性值，属性值之间用空格隔开。边框的颜色，宽度，线的类型。

> 实线边框：solid 。
>
> > borser: 5px solid red;				

### 4、css的书写位置

​		根据书写css属性的位置不同，将样式表分为三种：行内式、内嵌式、外链式

​		`行内式：<div style="color:red;font-size:30px;width:200;height:200"></div>`

​		`内嵌式：写在html文件里head标签里的一对style标签里，写时要先选中要写的东西，style标签有一个type属性“text/css”，表示style内部写的时纯文本类型的css` 

```html
<head>
    <style type="text/css">
    	div{
    		border:3px solid blue;
        }
    </style>
</head>

```

​			`外链式：将css单独写在另一个扩展名为.css的文件里。`

### 5、css的注意事项

  		html的属性和属性值，键值对：k="v"

  		css的属性和属性值，键值对：k:v 并且多个属性之间必须用分号隔开。

当需要把代码传到网上时，为了提高加载速度，需要删除所有的空格，换行，缩进。

## 二、基础选择器

选择器：指的是我们需要添加样式的标签的元素的模式。

### 1、标签选择器

​	通过标签名直接选择相应的标签，标签是什么就用什么选择，标签选择器选择的是所有页面中的对应标签

​	 

因为标签选择器会选中所有的标签，实际工作中不会用来更改某一个元素属性，因为会影响其他标签

用途：进行初始样式的设置，或者清除默认样式

### 2、id选择器

通过标签的id属性来选择相应的标签

书写方式：<font color="red">#</font>开头，后面紧跟<font color="red">id名</font>中间没有空格，id选择器一次只能选出一个标签。

id名必须以字母开头，后面可以是下划线，数字，严格区分大小写。一个页面不许出现两个同样的id名

### 3、类选择器

通过标签的class属性来选择这个标签。

选择器写法，<font color="red" size="6">.</font>开头,后面紧跟<font color="red">class属性值</font>，中间不能有空格，class属性可以不唯一。

优点：可以选择一部分标签，添加相同属性。

善用原子类（只有一个css属性的选择器），一个class可以同时有多个属性值，即添加有多个类名，多个类名之间用空格隔开。

### 4、通配符*

​	可以选中包括body在内的所有<font color="green">标签</font>元素

实际工作中很少使用。

## 三、高级选择器

基础选择器不能满足我们所有的需求，在基础选择器上进行了延申。

### 1、后代选择器

又叫包含选择器，        通过标签之间的嵌套，层级关系，限定我们大体范围，在该范围中查找相关元素

```html
.box2<!--一个标签的class属性--> li{
color:red;
}
```

后代选择器，用空格来分隔两个标签，空格左侧是空格右侧的祖先元素，开始的祖先元素一般不用标签选择器，写他的class值，但也可以用标签选择器，同样的，子代可以用标签选择器，也可以用类选择器。

```html
<style>
		.box2 li{
			color: red;
		}
	</style>
</head>
<form action="">
	<div class="box1">
		<div>
			<div class="box2">
				<ul>
					<li>1</li>
					<li>1</li>
					<li>1</li>
					<li>1</li>
					<li>1</li>
				</ul>
			</div>
		</div>
		<div class="box3">
			<ul>
				<li>2</li>
				<li>2</li>
				<li>2</li>
				<li>2</li>
				<li>2</li>
			</ul>
		</div>
	</div>
</form>
</body>
```

```html
<head>
<style>
		div div div li{
			color: red;
		}
	</style>
</head>
<form action="">
	<div class="box1">
		<div>
			<div class="box2">
				<ul>
					<li>1</li>
					<li>1</li>
					<li>1</li>
					<li>1</li>
					<li>1</li>
				</ul>
			</div>
		</div>
		<div class="box3">
			<ul>
				<li>2</li>
				<li>2</li>
				<li>2</li>
				<li>2</li>
				<li>2</li>
			</ul>
		</div>
	</div>
</form>
```

以上两种的效果都是![批注 2019-10-04 083753](D:\杨嘉睿\HTML学习\批注 2019-10-04 083753.png)

但是第二种太麻烦

### 2、交集选择器

既满足条件一也满足条件二。如果有两个不同类型的标签是同一个class值，我们只想让其中一个标签的样式改变而不让另一个改变就用交集选择器。

写法：选择器之间直接链接，没有任何符号。交集还可以连续书写，`li.one.bo{ color:red;}`这表示既是li标签，有one和bo class属性

```html
<style>
		li.one{
			color: red;
		}
	</style>
</head>
<form action="">
	<div class="box1">
		<div>
			<ul>
				<li class="one">1</li>
				<li>1</li>
				<li>1</li>
				<p class="one">1</p>				
            </ul>
		</div>
	</div>
</form>
```

### 3、并集选择器

多个选择器选中的元素有同样的样式

写法，不同选择器之间用逗号连接

## 四、继承性和层叠性

### 1、继承性

​	有一些属性给祖先元素设置后，后代元素会继承。继承文字样式，层叠式的第一个特性

### 2、层叠性

同一个标签可以被多个选择器选中，但是到底显示哪个选择器的样式

涉及选择器权重问题：如果有一个样式所有选择器都有，那么``通配符<标签选择器<类选择器<id选择器``如果有的样式只有某个选择器有，那只显示该有的样式。

有高级选择器时，数选择器的个数，先数id选择器的个数，然后数类选择器，再数标签选择器的数，谁的数多就是谁，有并集选择器时，把并集里的选择器分开数，不能和前面的混到一起。如果权重相同，谁写在后面就是谁。

如果没有选中，看继承，离哪个祖先元素近就继承哪个，如果距离一样，就看祖先的权重，如果距离权重相同，后写的覆盖先写的

关键字!important给单一属性添加，在属性值后添加，该属性的权重提升到最大，即使选择器权重低也没影响。不适用于就近原则，

## 五、css属性

主要分类：文本、盒模型、背景、浮动、定位

### <font color="blueyellow" size="6">文本</font>

### 1、字体

> color:字体颜色

​			色值：十六进制、RGB、颜色名、rgba 实际工作中，设计提取色值，吸取色值

​			颜色使用，背景色，边框色

> font-family：字体

​			中文:微软雅黑 、宋体

​			英文：Arial 、 Consola

> font-size ：字号

​			字体大小；自己设置一个通用字体大小，如果不设置，浏览器会有一个自己的默认字号。

​			常用字号：12/14/16/18/20       firework软件可以让我们量字号大小

>  line-height ：行高

​				一行文字实际占的高度，单位是像素或百分比。

​				文字在自己的行高内垂直居中

​    		***注意：***行高属性必须写在文字字号的后面 `font:14px/27px "宋体"`  复合写法： 字号/行高  “字体”

>  font-weight :字体加粗

​				属性值：数字、单词

​				数字越大越粗4：00 正常粗细，700 加粗

​				单词：bold 加粗，  normal 正常。

> font-style :字体样式

​				设置字体倾斜或正常

​				取值：normal 正常，italic 斜体，oblique 斜体。

<font color="green" size="5">font 复合属性书写：</font>

`font：bold italic 14px/28px "微软雅黑"  `

### 2、文本

>  text-align 文字对齐方式 

​	属性值：

- `left`：左对齐；
- `center`：居中对齐；
- `right`：右对齐；
- `justify`：两端对齐

> text-indent：文本缩进 

​		设置的是文本的首行缩进

​		值：em字符，px 像素，百分比（盒子的宽度的百分比，）。

![批注 2019-10-04 171341](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(9).png) 

> text-decoration 文本修饰

​		对于文本在整体上样式的一个修饰效果。有四种常见形式：

* 正常 ：none
* 上划线：overline
* 下划线：underline
* 中划线：line-through

所有的文本除了a标签内，都默认没有样式，a标签（超链接）默认下划线

### <font color="blueyellow" size="6">盒模型</font>

盒模型又叫框模型，

![批注 2019-10-04 173758](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(10).png)

一个盒子包含五个部分：宽度，高度，内边距，边框，外边距。

### 1、宽高

​			宽度：width 

​			高度：height

这个宽高规定我们实际书写内容的区域，盒子占有的位置还有内边距和边框

### 2、内边距   padding

​		位置在宽高和边框之间，上下左右四个方向都可以设置内边距。单位px

​			单一属性是各个方向的内边距：

* padding-top : 上内边距
* padding-right ：右内边距
* padding-bottom ：下内边距
* padding-left ：左内边距

复合写法 ：`padding ：上 右 下 左 ；`四值法

padding区域可以渲染背景颜色，图片

### 3、边框 border

​		盒子占有的最外层区域，复合属性。

> 按样式类型划分：
>
> > 线的宽度，border-width：
> >
> > > 单值法：四值相同
> > >
> > > 双值法：上下  右左  
> > >
> > > 三值法：border-width：上  右左 下  
> > >
> > > 四值法：border-width：上  右 下  左
> >
> > 线的颜色, border-color
> >
> > > 写法同上
> >
> > 线的样式 ：border-style
> >
> > > solid  实线
> > >
> > > dotted  点线
> > >
> > > dashed   虚线
> > >
> > > double  双线条
> > >
> > > groove   边框凹陷效果
> > >
> > > ridge    边框凸出效果
> > >
> > > inset   内容凹陷效果
> > >
> > > outset   内容突出效果
> > >
> > > none  无边框
>
> 根据方向分类
>
> ![批注 2019-10-04 193235](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(11).png)
>
> 必须把线宽，线性，颜色写完整

给单一方向的单一线型：

border-top-style

做一个三角![三角](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(12).png)

表格边框合并：

border-collapse 边框合并属性

默认值   separate

合并：collapse

### 4、外边距 margin

盒子与盒子之间的距离  设置方法同上

特殊的 让盒子居中

![批注 2019-10-04 195034](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(13).png)

给盒子设置好宽高，然后左右 auto。

## 六、盒模型拓展

### 1、清空默认样式

​	很多标签都有一些默认样式。

​	比如：body 、p、 div、 ul、li、ol、dl、dd、dt、h1。

​	ul、ol有一个list-style  需要清除。

​	a标签：有默认的字体样式，有下划线，字体颜色。

```html
*{
	margain:0;
	padding:0;
}
ul,ol
{
	list-style:none;
}
a{
	text-decoration:none;
	color:#dc2c2c
}
```

### 2、height

​	一般不设置盒子的高度，或者把高度属性值设为 auto，留给文字自动撑开。

​	目的：为了保证我们元素在添加或者删除的时候盒子高度可以自适应内容高度。实际工作中样式和结构是前端人员搭建的，实际文字和内容由后台人员导入，内容不一定和设置的一样

​	不一定不设置高度，设置内容溢出隐藏属性

> overflow:hidden;

### 3、宽度，高度剩余

一般右边根据内容不同，边距大小不同，没法设置padding-right，所以只设置左边的内边距，右边留给width 。

同理，高度剩余

### 4、margin

​	垂直方向上如果两个元素都有外边距，相交的部分会出行外边距重合。

```
div{
	width:200;
	height:200;
}
.box1{
	margin:50 0;
}
.box2{
	margin:40 0;
}
```

![批注 2019-10-05 071215](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(15).png)

嵌套的盒子margin也会重合，

​	如果父盒子和子盒子有同一方向的margin 那么只会显示出其中较大的一个，如果父盒子没有margin 但子盒子有，父盒子会随子盒子以同改变。

![批注 2019-10-05 071834](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(16).png)

因此，一般给上面的盒子设置下边距或者给下面的盒子设上边界，不用都设置。

***注意***：强行给父盒子加一个边框，强制限定父盒子的位置，如此会让子盒子和父盒子留有间距///或者给父盒子设置padding属性，子盒子与父盒子的间距用padding撑开。

![](https://raw.githubusercontent.com/yjr-1100/my_sher_coder-1/master/yjr-1100/img/pz%20(1).png)

### 5、居中

文字居中：

​		单行文字水平方向文字居中：text-align：center；

​		单行文字垂直方向居中：行高等于盒子高

​		多行文本水平上下居中：text-align：center；盒子不设高度，内边距padding四边相等。

盒子居中：子盒子在父盒子内部居中显示。

​		水平居中：给自身添加宽度，用margin给两边挤出相同空白，maigin的属性值为1auto，自动撑开一个最大的边距

​		垂直居中：父盒子不设高度，内边距padding四边相等。

### 6、父子盒模型

​		子盒子的占位不能超过父盒子的内容区域，如果子盒子不设置宽度，会自动撑满父盒子，此时如果给子盒子设置padding和border子盒子会自动内减

## 七、标准文档流

常用的word文档就是一个经典的标准文档流，内容必须从上往下，从左往右，有一个光标控制。前面的内容大小或内容发生变化，后面的内容也会跟着变化。

​		制作的html网页：也是一个标准文档流。

### 1、从微观上有特殊性质

* 空白折叠现象
* 文字图片、表单元素等：高矮不齐，底边对齐
* 文字在盒子内如果一行写完自动换行

### 2、块级元素和行内元素（标签）

​		块级标签：所有的容器级标签，文本级标签中的p标签。

​		行内标签：除了p标签以外的所有文本级标签。

* 块级标签

* > 不论宽高是多少，会独占一行，可以设置宽高，嵌套关系里，子盒子不设置宽度会继承父盒子内容宽度的100%

* 行内标签

* > 不独占一行，可以与其它行内元素并排在一行。不能设置宽高，其他的外内边距等都可以正常设置，宽度靠内容撑开。

* 行内块标签

* > 可以并排在一行，还可以设置宽高

有一个属性可以在块级元素和行内元素之间进行转换

显示模式：display。标签在html中的渲染形式

属性值：块级 block，行内 inline ，行内块：inline-block

转换方法：`display :block;`or`display:inline`

标准文档流制作网页有局限：很多布局效果不能完成。

解决办法：让元素脱离标准流，既可以设置宽高，又可以一行排列。

脱离标准流的方法：<font size="4" color="blue">浮动、绝对定位、固定定位。</font>

## 八、浮动

​	浮动：float  。让我们的元素以某一个方向在一行并排排列。

​	浮动的效果：使元素脱离标准流，既可以设置宽高又可以排成一行

​	属性：left（左浮动），right（右浮动），从第一个元素开始一次去贴父元素 的左（右）边。

### 1、浮动的特性

> 浮动的元素脱离标准流

> 浮动的元素在一个父盒子内会根据书写标签的顺序会一次贴向前边
>
> 如果父盒子大小不够装下所有子元素，后，面的盒子会自动换行去贴上上个元素，如果还是不够，继续向上找元素贴，知道找到父盒子的边去贴，如果两个方向都有浮动，找自己方向上的上一个元素，如果高矮不同的元素，两个高的夹一个小的，那么第四个元素不会钻空去贴。

> 浮动不会有margin塌陷的效果

> 浮动会让出标准文档流的位置
>
> 元素在标准文档流中有自己的书写位置，一个元素写完之后才能加载另一个元素，元素浮动之后，不在标准文档流的位置，位置会让给后面的标准流元素。但是这样不好，

> 浮动有文字围绕效果
>
> 如果同一个父盒子里一个浮动一个没有浮动，浮动的元素压盖住没有浮动的元素，那么没浮动里的文字会围绕浮动 元素。

### 2、清除浮动

> 浮动的元素不能撑开父级，会影响后面的浮动

法一：给父级加高度，限制其中元素的浮动范围，但是效果不好，高度不能自适应。

法二：清楚浮动属性 clear 

​       属性值：left 、right、both

​        作用：清除自身受到的其他元素带来的浮动影响，但父盒子还是没有被撑开，而且如果margin 小于中间浮动的子元素，显示效果失效。

法三：隔墙法

​           在互相影响的元素中间加一个墙，隔开两边元素，墙上添加一个clear属性。

> 外墙法：在右浮动元素的父盒子之间隔墙。
>
> 在两个div之间再加一个div，给其设置clear属性，并设置hight属性，模仿margin的样式。真正的margin失效。

> 内墙法：在有浮动元素的盒子里加一个div，不进行浮动，设置clear属性。
>
> 但如果每个浮动都加墙，很麻烦啊！！！

法四：overflow:hidden

​           盒子内部的元素可以设置溢出模式，隐藏：hidden    溢出滚动： auto 

对于清除浮动来说，用overflow可以清楚一个盒子内的浮动的影响。

## 九、转换

### 1、2D转换

- 转动

  `transform:rotate(30deg);`

  元素顺时针旋转给定角度，可以是负值，逆时针。

- 移动

  `transform：translate(50px,100px);`

  把元素从左侧移动50像素，从顶端移动100像素。

- 伸缩

  `transform: scale(2,4);`

  宽度转换为原始尺寸的 2 倍，把高度转换为原始高度的 4 倍。

- 翻转

  `transform: skew(30deg,20deg);`

  围绕 X 轴把元素翻转 30 度，围绕 Y 轴翻转 20 度。

## 十、超链接a标签的修饰

### 1、a的四个显示状态

​		

```html
a:link{
	color:blue;/*什么操作都没有时*/
}
a:visited{
	color:purple;/*访问过后*/
}
a:hover{
	color:red;/*鼠标放在上面时*/
}
a:active{
	color:green;/*按下鼠标不放时*/
}
```

四个状态根据用户动作产生变化，动作没有发生，不会显示。

### 2、a的四个伪类的书写顺序

四个伪类都有自己的权重，权重相同，根据书写顺序不同，会层叠之前的状态，一般按照上面的顺序比较正常。

### 3、a的实际应用

a标签不能继承父级的 text-decoration ，color等样式，其他可以继承。实际使用中一般不会四个颜色，花里胡哨的，link和visited一边一样。

#### 背景色

我们可以使用`background-color`为元素设置背景色，通常属性值为颜色名称或颜色编码。

 

因为HTML文档中`body`元素包含了HTML文档的所有内容，所以如果要改变整个页面的背景颜色，只需要设置`body`元素的`background-color`属性。



我们可以使用`background-image`属性设置元素的背景属性，常见的网页背景图就是这样设置的。其中，属性值通过`url`指定图片链接。

 

书写格式：

 

```html
background-image: url("图片链接")
```

#### 平铺背景图像

指定了背景图像之后，默认背景图是平铺重复显示。如果想要设置图像在水平方向、垂直方向平铺或其他方式，可以设置`background-repeat`属性。

 

具体属性值设置如下：

 

| 样式         | 属性值    |
| ------------ | --------- |
| 水平平铺重复 | repeat-x  |
| 垂直平铺重复 | repeat-y  |
| 不重复平铺   | no-repeat |

 

例如：

 

1. 默认平铺

   ```
    body {     /*设置背景图片*/     background-image:url("./Assert/sun.jpg"); }
   ```

    ![img](https://www.educoder.net/api/attachments/174510)

2. repeat-x 

   ```
    body {     /*设置背景图片*/     background-image:url("./Assert/sun.jpg");     background-repeat: repeat-x; }
   ```

    ![img](https://www.educoder.net/api/attachments/174511)

3. repeat-y

   ```
    body {     /*设置背景图片*/     background-image:url("./Assert/sun.jpg");     background-repeat: repeat-y; }
   ```

    ![img](https://www.educoder.net/api/attachments/174513)

4. no-repeat

   ```
    body {     /*设置背景图片*/     background-image:url("./Assert/sun.jpg");      background-repeat: no-repeat; }
   ```

    ![img](https://www.educoder.net/api/attachments/174514)

#### 背景定位

当图像作为背景和文本显示在同一个位置时，为了页面排版更优美、更易于文本的阅读，我们可以使用`background-position`属性改变图像在背景中的位置:

 

举例如下：

 

```
body {    /*设置背景图片*/    background-image: url("https://www.educoder.net/attachments/download/211104");    background-repeat: no-repeat;    background-position: right top;}
```



| 属性值          |
| --------------- |
| `top left`      |
| `top center`    |
| `top right`     |
| `center left`   |
| `center center` |
| `center right`  |
| `bottom left`   |
| `bottom center` |
| `bottom right`  |

