#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 13:31
# @Author  : fengguifang
# @File    : test_v7recipedetail.py
# @Software: PyCharm

from base.cjbase import CJMyTest
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class v7recipedetailTest(CJMyTest):
    '''食谱详情'''


    @classmethod
    def setUpClass(cls):
        pass

    def test_recipedetail_success(self):
        '''传必填参数'''
        #测试环境3322
        r = self.cjmyhttpjs('GET',
                        '/v7/recipe/1/detail',
                        {'language':self.language,
                         'model':self.model_name,
                         'flag':'true'
                         }
                         )
        print r
        js = json.loads(r)  #3322是测试环境数据
        print js
        # print "食谱名称：%s"%js['result']['name']
        # print "食谱介绍：%s"%js['result']['content']
        # print "小贴士：%s" % js['result']['function']
        # alist = []
        # print js['result']['steps']
        # for i in js['result']['steps']:
        #     # print i['content']
        #     alist.append(i['content'])
        # print "食谱步骤：%s"%alist
        self.assertEqual(js['state'], 1)
        self.assertIn("操作成功", js['message'])
