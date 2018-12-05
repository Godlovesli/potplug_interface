#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 13:40
# @Author  : fengguifang
# @File    : cjbase.py
# @Software: PyCharm
from CJcryp import generateNonce, generateSignature,getSessionSecurity,encryptAES,decryptAES,md5
from urllib import urlencode, quote, unquote
from base.api_testdata import *
import unittest
import urllib, urllib2,requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#cjbase3是修改了cjmyhttpjs，加了一个循环，为了测试根据关键字进行搜索的接口，url_path = '/v7/recipe/people/query'
class CJMyTest(unittest.TestCase):

    def setUp(self):
        # self.base_url = 'https://capi.joyami.com'
        # self.base_url = 'http://10.0.10.100:17001'
        # self.base_url = 'https://sgmipotplug.joyami.com'
        # self.base_url = 'https://framipotplugapi.joyami.com'
        self.base_url='http://pre-plugapi.joyami.com'
        # self.base_url = 'https://rumipotplugapi.joyami.com'
        # self.base_url='https://pot.joyami.com/'

        self.nonce = generateNonce()
        self.key = getSessionSecurity(self.nonce)
        self.model_name=model_name
        self.deviceId=deviceid
        self.barcode=barcodeId
        self.language=language_name




    def cjmyhttp(self,method, url_path=None,post_data=None,token=None):
        url = self.base_url + url_path
        print url
        self.signature = generateSignature(self.nonce, method, url)
        print post_data
        params = urllib.urlencode(post_data)
        encoded = encryptAES(params, self.key)
        data = {'data': encoded}
        payload = urllib.urlencode(data)
        print "打印payload：%s" % payload
        print type(payload)
        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   # "Accept": "application/json;charset=UTF-8",
                   #  "contentType": "application/json",
                   'token': token
                   }
        if method == 'GET':
            url2 = url + '?' + payload


            request = urllib2.Request(url2, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        if method == 'POST':

            request = urllib2.Request(url, data=payload, headers=headers)
            # response = urllib2.urlopen(request)
            # result = response.read()
            # s = decryptAES(result, self.key)
            # return s
        response = urllib2.urlopen(request)
        result = response.read()
        # print "打印result:%s" % result
        print "打印result类型:%s" % type(result)
        s = decryptAES(result, self.key)
        # print s
        return s


    def  cjmyhttpjs(self, method, url_path=None, post_data=None, token=None):# 传json格式
        for i in range(50):
            print"打印i：%s" %i
            self.url = self.base_url + url_path
            print self.url
            self.signature = generateSignature(self.nonce, method, self.url)
            params1 = urllib.urlencode(post_data)
            print  "打印params1：%s"%params1
            params=unquote(params1)  #把%E6%B5%B7%E9%B2%9C的参数解码成中文
            encoded = encryptAES(params, self.key)
            data = {'data': encoded}
            payload = urllib.urlencode(data) #字典编码成字符串
            print "打印payload：%s"%payload
            jdata = json.dumps(post_data)
            # print "打印jdata数据：%s"%jdata
            headers = {
                'User-Agent': 'chunmiapp',
                'signature': self.signature,
                'token': token,
                'Content-Type': 'application/json',
                'nonce': self.nonce}
            if method == 'POST':
                request = urllib2.Request(self.url, data=jdata, headers=headers)

            if method == 'GET':
                url2 = self.url + '?' + payload
                request = urllib2.Request(url2, headers=headers)

                print 'url2 :', url2
            response = urllib2.urlopen(request)
            result = response.read()
            s = decryptAES(result, self.key)
        return s






    def cjbujiami(self,method, url_path=None,post_data=None,token=None):
        url = self.base_url + url_path
        print(url)
        self.signature = generateSignature(self.nonce,method, url)
        params = urllib.urlencode(post_data)
        print "打印params：%s" % params

        headers = {'nonce': self.nonce,
                   'User-Agent': 'chunmiapp',
                   'signature': self.signature,
                   "Accept": "application/json;charset=UTF-8",
                    "contentType": "application/json",
                   'token': token
                   }
        if method == 'GET':
            url2 = url + '?' + params
            print "打印url2：%s"%url2
            request = urllib2.Request(url2, headers=headers)
        if method == 'POST':
            request = urllib2.Request(url, data=params, headers=headers)
        response = urllib2.urlopen(request)
        result = response.read()
        print type(result)
        return result

    def tearDown(self):
        pass