from generic.base_setup import Base_SetUp
from page.login_page import LoginPage
from page.enter_time_track_page import EnterTimeTrackPage
from generic.excel import Excel
class Test_ValidLogin(Base_SetUp):

    def test_valid_login(self):
        # 1. Enter Valid UN
        loginpage=LoginPage(self.driver)
        loginpage.set_username("admin")
        # 2. Enter Valid PW
        loginpage.set_password("manager")
        # 3. Click on login Button
        loginpage.click_login_button()
        # 4. Verify that Home page is Displayed
        homepage=EnterTimeTrackPage(self.driver)
        status=homepage.verify_home_page_displayed(self.wait)
        assert status