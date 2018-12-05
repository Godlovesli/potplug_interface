#coding=utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 13:15
# @Author  : fengguifang
# @File    : test_v7recipequery.py
# @Software: PyCharm


# from base.cjbase import CJMyTest

from base.cjbase2 import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7recipequeryTest(CJMyTest):
    '''更多食谱，根据食谱类别和关键字进行查询'''
    url_path = '/v7/recipe/people/query'

    @classmethod
    def setUpClass(cls):
        pass
    def test_recipelist(self):
        '''获取食谱列表'''
        r = self.cjmyhttpjs('GET',
                            self.url_path,
                            {'language':self.language,
                             'model': self.model_name,
                             # 'perpage': 500

                             },
                            )

        print r
        js = json.loads(r)
        print  js
        js = json.loads(r)
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print "食谱个数：%s"%len(js['result'])
        for i in range(len(js['result'])):
            print"打印食谱列表名称：%s" %js['result'][i]['name']

    def test_recipequery_success(self):
        '''传必填参数'''

        r = self.cjmyhttpjs('GET',
                        self.url_path,

                        {
                         'language':self.language,
                          'model':self.model_name,
                          'pageno':1,
                          'perpage':10,
                           # 'categoryId':'3',
                            'params':'金针',   #Mushroom
                           'deviceId':self.deviceId


                         },


                         )

        print r
        js = json.loads(r)

        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
        print len(js['result'])
        for i in range(len(js['result'])):
            print js['result'][i]['name'],js['result'][i]['collectFlag']