import pytest

from generic.base_setup import Base_SetUp
from page.login_page import LoginPage
from page.enter_time_track_page import EnterTimeTrackPage
from generic.excel import Excel


class Test_ValidLogin(Base_SetUp):

    @pytest.mark.run(order=3)
    def test_valid_login(self):
        un = Excel.get_cell_data(self.XL_PATH, "validlogin", 2, 1)
        pw = Excel.get_cell_data(self.XL_PATH, "validlogin", 2, 2)
        # 1. Enter Valid UN
        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        # 2. Enter Valid PW
        loginpage.set_password(pw)
        # 3. Click on login Button
        loginpage.click_login_button()
        # 4. click on logout link
        homepage = EnterTimeTrackPage(self.driver)
        homepage.click_logout()
        # 5. Verify that  login is Displayed
        status=loginpage.verify_login_page_displayed(self.wait)
        assert status