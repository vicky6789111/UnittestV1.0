import os
import time
import HTMLTestRunnerEN

from utils.config import config


def report(testSuite):
    timeStamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    path = config["projectPath"]["reportPath"]
    reportName = r' UITestReport' + timeStamp + '.html'
    file_path = os.path.join(path, reportName)
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerEN.HTMLTestReportEN(
        stream=fp,
        title='UIAutomationTestReport' + timeStamp,
        description='TestReport',
        tester='Qi Yue'
    )
    runner.run(testSuite)
    fp.close()
