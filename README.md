# webPageParser
网页内容抓取分为动态网页和静态网页
1 动态网页：即网页内容会动态加载，如ajax加载。这种情况代码使用Phantomjs模拟浏览器操作，获取页面内容。
2 静态网页：即通过url发request 能直接获得所需要的html内容，可使用lxml包获取网页内容，为什么静态页面不用Phantomjs？因为Phantomjs比较耗资源，如果大量的静态网内容抓取，可节约资源。

网页上的内容抓取，所有需要的内容可以归纳为三种类型： 简单的字符串str类型，object类型，列表list类型。

使用时只要编辑配置文件
配置文件简单介绍：
field： 一条数据的节点
events：事件集合
event：单独一个事件，如鼠标click
paging：翻页
field 中 name 属性为要抓取后的数据存储时的名字，xpath 属性为网页上内容的 xpath值。
详细的配置介绍可查看constant包下的常量类，也可参看demo.xml

