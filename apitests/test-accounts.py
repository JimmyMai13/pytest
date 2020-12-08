import logging
import pytest
log = logging.getLogger('TestUsers')


class TestUsers:


    @pytest.fixture()
    def setup(self, request, fix_base):
        log.info('Setup Users')
        self.base = fix_base

    get_accounts_test_plan = {'default_per_page_param_value': {'params': {}, 'expect': {"key": "per_page", "value": 100}},
                              'max_per_page_param_value': {'params': {'per_page': 250}, 'expect': {"key": 'per_page', 'value': 250}},
                              'invalid_per_page_param_value': {'params': {'per_page': "abc"}, 'expect': {"key": 'per_page', 'value': 1}}}

    @pytest.mark.parametrize('params', get_accounts_test_plan)
    def test_get_accounts(self, setup, params):
        log.info('test_get_users')
        resp = self.base.accounts.get_accounts(params=self.get_accounts_test_plan[params]['params'])
        assert resp[self.get_accounts_test_plan[params]['expect']['key']] == self.get_accounts_test_plan[params]['expect']['value']
