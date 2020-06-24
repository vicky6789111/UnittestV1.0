import time
import unittest
from selenium import webdriver
import logging
from pageObject.LoginPage import LoginPage

from csv import excel
import ddt as ddt

from utils.config import config
from utils.excel_testdata_reader import ReadExcel

excel = ReadExcel('loginTestData.xlsx', 1)
# 0,1,2 代表的是 excel的索引
logging.basicConfig(level=logging.INFO)


@ddt.ddt  # 实现数据驱动
class LoginTest_positive(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # 类方法，整个测试类只执行一次前置
        pass #print('只执行一次的前置条件')

    def setUp(self):  # 执行每条用例前都会执行
        #print('每条用例执行前的前置条件')
        logging.info("************Open chorme ***********")
        self.baseURl = config["productPath"]["loginPage"]
        self.driver = webdriver.Chrome(executable_path=config["projectPath"]["webDriver"])
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

    @ddt.data(*excel.next())
    def test_login(self, data):
        print('每条用例具体内容'+data["TestGoal"])
        logging.info("************Start test_login ***********")
        lp = LoginPage(self.driver)
        logging.info("Test point：" + data["TestGoal"])

        lp.setUserName(data["UserName"])
        lp.setPW(data["Pw"])
        lp.clickRememberCheckbox()
        lp.clickLoginButton()
        time.sleep(1)

        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Login failed!!!")

    def tearDown(self):
        #print('每条用例执行后的后置条件')  # 执行每条用例以后都会执行
        self.driver.close()
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass # # print('只执行一次的后置条件')  # 类方法，整个测试类执行一次的后置


if __name__ == "__main__":
    unittest.main()
