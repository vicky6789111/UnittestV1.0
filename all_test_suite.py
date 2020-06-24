import unittest
import self
from testCases.scenario.LoginTest import CasesALL
from utils.config import config
from utils.generate_summary_report import report


def loginFunctionTestSuite(self):
    loginFunctionTestCaseDir = config["projectPath"]["loginFunctionTestCaseDir"]
    # suite = unittest.TestSuite()
    loginTestSuite = unittest.defaultTestLoader.discover(loginFunctionTestCaseDir, pattern="*Test_*.py")
    generateReport = report(loginTestSuite)
    return generateReport


def loginScenarioTestSuite(self):
    testSuite = unittest.TestSuite()
    loginTestCases = unittest.TestLoader().loadTestsFromTestCase(CasesALL)  # 必须是testcase的儿子或者孙子
    testSuite.addTests(loginTestCases)
    generateReport = report(testSuite)
    return generateReport


if __name__ == "__main__":
    loginScenarioTestSuite(self)
    loginFunctionTestSuite(self)
