import logging
import allure
import pytest
from airtest.core.api import *

logger = logging.getLogger(__name__)
epic = os.getenv('client_platform')
feature = 'app'
story = 'all'


@allure.epic(epic)
@allure.feature(feature)
@allure.story(story)
class TestDemo(object):
    @pytest.fixture(scope="function")
    def app(self, request, app_fixture):
        app_ins = app_fixture

        @allure.step
        def setup_func():
            """
            用例前置
            """
            app_ins.start_phone_app()
            sleep(2)

        @allure.step
        def teardown_func():
            """
            用例后置
            """
            app_ins.stop_phone_app()
            sleep(2)

        request.addfinalizer(teardown_func)  # 注册teardown, 这样即使setup出现异常，也可以最终调用到
        setup_func()
        return app_ins

    @allure.severity(allure.severity_level.BLOCKER)
    def test_home_to_second(self, app):
        """
        测试home to second
        """
        app.home_page.click_next()
        sleep(2)
        assert app.second_page.is_second_page(), "确认进入second页失败"

        app.second_page.click_back()
        sleep(2)
        assert app.home_page.is_home_page(), "确认退出到home页失败"
