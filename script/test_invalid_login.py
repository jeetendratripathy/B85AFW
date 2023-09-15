from generic.base_setup import Base_SetUp
from page.login_page import LoginPage
from page.enter_time_track_page import EnterTimeTrackPage
from generic.excel import Excel
class Test_InvalidLogin(Base_SetUp):

    def test_invalid_login(self):
        # 1. Enter invalid UN
        loginpage=LoginPage(self.driver)
        loginpage.set_username("abcd")
        # 2. Enter invalid PW
        loginpage.set_password("xyz")
        # 3. Click on login Button
        loginpage.click_login_button()
        # 4. Verify that Err Msg is Displayed
        status=loginpage.verify_err_msg_displayed(self.wait)
        assert status