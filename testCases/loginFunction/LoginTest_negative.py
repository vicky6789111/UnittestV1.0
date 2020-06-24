import time
import unittest

from selenium import webdriver
import logging
from pageObject.LoginPage import LoginPage

from csv import excel
import ddt as ddt

from utils import config
from utils.config import config
from utils.excel_testdata_reader import ReadExcel

logging.basicConfig(level=logging.INFO)

excel = ReadExcel('loginTestData.xlsx', 2)


# 传数据的文件名字，索引，正向case 索引为0，反向为1
# excel 中如果想识别数字类型的字符串，数字前加 ‘
@ddt.ddt  # 实现数据驱动
class LoginTest_negative(unittest.TestCase):
    baseURl = config["productPath"]["loginPage"]
    driver = webdriver.Chrome(executable_path=config["projectPath"]["webDriver"])

    @classmethod
    def setUpClass(cls):
        logging.info("************Open chorme ***********")
        cls.driver.get(cls.baseURl)
        cls.driver.maximize_window()

    @ddt.data(*excel.next())
    def test_login(self, data):
        logging.info("************Start test_login ***********")
        lp = LoginPage(self.driver)
        print('每条用例具体内容 :' + data["TestGoal"])#打在测试报告上
        logging.info("Test point：" + data["TestGoal"])#打在控制台里

        lp.setUserName(data["UserName"])
        lp.setPW(data["Pw"])
        lp.clickRememberCheckbox()
        lp.clickLoginButton()
        time.sleep(1)
        errorMessage_in_excel = data["ErrorMessage"]
        errorMessage_in_page = self.driver.find_element_by_xpath("//*[text()='" +
                                                                 errorMessage_in_excel +
                                                                 "']").is_displayed()
        logging.info("************Start Assert ***********")
        self.assertEqual(errorMessage_in_page, True, "测试失败")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
