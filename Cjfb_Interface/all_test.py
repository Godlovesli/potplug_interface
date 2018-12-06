 # !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time,sys
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
proPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(proPath)
# now = time.strftime("%Y-%m-%d %H_%M_%S")
reportPath = os.path.join(proPath, "report" , 'result.html')
# test_dir='./cjinterface_new'  #v7interface

def testrunner():
    test_dir = os.path.join(proPath, 'v7interface')  # 用例文件夹
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    fp = open(reportPath, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'饭煲接口测试报告',
                            description=u'用例执行情况：',
                            verbosity=2

                            )
    runner.run(discover)
    fp.close()


if __name__=="__main__":
    testrunner()
