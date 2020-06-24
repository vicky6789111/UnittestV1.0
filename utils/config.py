import os, sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 获取根目录绝对路径

def abPath():
    ab_PATH = os.path.abspath(__file__)
    # ABSPATH=os.path.abspath(os.path.join(ab_PATH, "../../../"))
    ABSPATH = os.path.dirname(os.path.dirname(ab_PATH))
    return ABSPATH


driver = webdriver.Chrome(ChromeDriverManager().install())

config = {
    "projectPath": {
        "webDriver": driver,
        "excelDir": abPath() + r"\data",
        "reportPath": abPath() + r'\reports',
        ###################functional test case########################
        "loginFunctionTestCaseDir": abPath() + r'\testCases\loginFunction',

        ###################scenario test case########################
        "loginScenarioTestCaseDir": abPath() + r'\testCases\scenario'
    },
    "productPath": {
        "loginPage": r"https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    }
}
