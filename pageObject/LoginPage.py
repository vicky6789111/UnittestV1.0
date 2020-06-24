class LoginPage():
    # Locators of all the elements
    textbox_name_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = r"//input[@class='button-1 login-button']"
    checkbox_remember_id = "RememberMe"
    textalert_wrongemail_id = "Email-error"
    textalert_wrongpw_classname ="message-error validation-summary-errors"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_name_id).clear()
        self.driver.find_element_by_id(self.textbox_name_id).send_keys(username)

    def setPW(self, pw):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(pw)

    def clickRememberCheckbox(self):
        self.driver.find_element_by_id(self.checkbox_remember_id).click()

    def clickLoginButton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def checkEmailErrorMessage(self):
        textEmailErrorMessage = self.driver.find_element_by_id(self.textalert_wrongemail_id).text
        return textEmailErrorMessage

    def checkPwErrorMessage(self):
        textPWErrorMessage =self.driver.find_elements_by_class_name(self.textalert_wrongpw_classname).text
        return textPWErrorMessage
