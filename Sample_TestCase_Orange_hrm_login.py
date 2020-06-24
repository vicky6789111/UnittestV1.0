from venv import logger
from selenium import webdriver
import unittest
import HtmlTestRunner
# Python, selenium, POM, unittest, Html report

# 继承 unittest.TestCase 就创建了一个测试样例。上述三个独立的测试是三个类的方法，这些方法的命名都以 test 开头。
# 这个命名约定告诉测试运行者类的哪些方法表示测试。

class OrangeHRMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\software\chromedriver.exe")
        cls.driver.maximize_window()
        logger.info("Test Start....")

    def test_homePageTitle(self):
        logger.info("Open Chorme....")
        self.driver.get(r"https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    # 调用 assertEqual() 来检查预期的输出； 调用 assertTrue() 或 assertFalse() 来验证一个条件；
    # 调用 assertRaises() 来验证抛出了一个特定的异常。使用这些方法而不是 assert 语句是为了
    # 让测试运行者能聚合所有的测试结果并产生结果报告。
    #  @unittest.skipIf(mylib.__version__ < (1, 3),
    def test_login(self):
        logger.info("Start login....")
        self.driver.get(r"https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        logger.info("Test complete....")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Unittest\\reports"))
    # unittest.main() 提供了一个测试脚本的命令行接口
# 如果想生成report必须用cmd运行： python Sample_TestCase_Orange_hrm_login.py
