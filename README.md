# douban
豆瓣top250电影爬取
douban2.py是原作者写的，处理函数中每次返回一个list和一个url，同时写入这个list，并且在循环中执行下一次爬取。
douban.py是自己写的，判断只要有下一页就递归执行处理函数，最后返回一个总的list，然后循环写入。
原始教程位于https://zhuanlan.zhihu.com/p/20423182
