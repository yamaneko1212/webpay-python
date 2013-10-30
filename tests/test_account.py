# coding: utf-8
from webpay.webpay import WebPay
from httmock import HTTMock
import pytest

import tests.helper as helper
import webpay.errors as errors

class TestAccount:
    def test_retrieve(self):
        with HTTMock(helper.mock_api('/account', 'account/retrieve.txt')):
            account = WebPay('test_key').account.retrieve()

        assert account.id == 'acct_2Cmdexb7J2r78rz'
        assert account.email == 'test-me@example.com'
        assert account.currencies_supported == ['jpy']

    def test_delete_data(self):
        with HTTMock(helper.mock_api('/account/data', 'account/delete.txt')):
            assert WebPay('test_key').account.delete_data()