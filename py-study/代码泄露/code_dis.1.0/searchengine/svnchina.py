#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 0015 下午 1:11
# @Author  : xiaodong
# @Site    :
# @File    : github.py
# @Software: PyCharm
# 从githu上利用github高级搜索语法，进行搜索
__author__ = 'xiaodong'
__github__ = 'https://github.com/dongfangyuxiao/'
import requests
from lib import config
from lib import myrequests
req = myrequests
import re
from bs4 import BeautifulSoup
print "Search now is in svnchina"
class svnchina():
    def __init__(self,word,proxy=None):
        self.engine_name = 'svnchina'
        self.result = "" #本页搜索结果
        self.totalresult = "" #全部搜索结果
        self.server = 'www.svnchina.com'
        self.counter = 1 #页面数
        self.proxies = proxy
        self.type = ""
        self.word = word.replace(' ','%20')
        return



    def do_search(self):
        try:
            url = "http://{0}/project_open.php?search%5Bproject_name%5D={1}".format(self.server,self.word)
            print url
            r = req.get(url)
            self.result = r.content
            self.totalresult +=self.result
            return True
        except Exception, e:
            return False
    def check_next(self):
        renext = re.compile('">(.*?)gt;</a></li>')
        nextres = renext.findall(self.result)
        if nextres !=[]:
            nexty = "1"
        else:
            nexty = "0"
        return nexty
    def process(self):
        self.do_search()#svnchina实在太少了，就不翻页了

    def get_url(self):
        pattern_all = re.compile('SVN地址：(.*?)<br>')
        urls = pattern_all.findall(self.totalresult)
        #for url in urls:
            #print url
        if urls:
            return urls
        else:
            return False


    def run(self):
        self.process()
        self.d = self.get_url()
        return self.d


if __name__ == "__main__":
    seach = svnchina("alibaba")
    seach.run()