# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#这里调用py接口存数据(要写SQL),其实是不明智的做法，可加入抽象层，将直接对mysql的直接操作封装(参考Django中Model,元类)

class HexunPipeline(object):
    def __init__(self):
        #刚开始时连接对应数据库
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="hexun")

    def process_item(self, item, spider):
        #print("process_item被调用")
        #每一个博文列表页中包含多篇博文的信息，我们可以通过for循环一次处理各博文的信息
        for j in range(0, len(item["name"])):
            # 将获取到的name、url、hits、comment分别赋给各变量
            name=item["name"][j]
            url=item["url"][j]
            hits=item["hits"][j]
            comment=item["comment"][j]
            #构造对应的sql语句，实现将获取到的对应数据插入数据库中（！）
            sql="insert into myhexun(name,url,hits,comment) VALUES('"+name+"','"+url+"','"+hits+"','"+comment+"')"
            #通过query实现执行对应的sql语句
            self.conn.query(sql)
            #print(hits)
        return item

    def close_spider(self,spider):
        # 最后关闭数据库连接
        self.conn.close()
