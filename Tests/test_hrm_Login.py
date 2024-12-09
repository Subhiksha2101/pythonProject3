import pytest

from Page.Kpi import Kpi
from Page.login import TestOrangeHRM


@pytest.mark.usefixtures("setup")
class TestPerformance:
    def test_login(self, setup):
        """Test for logging into OrangeHRM."""
        login_obj = TestOrangeHRM(setup)
        login_obj.login()

    def test_performance(self, login):
        """Test for accessing and configuring the Performance module."""
        kpi_obj = Kpi(login)
        kpi_obj.configure()



