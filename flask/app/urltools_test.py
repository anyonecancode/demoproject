from app import app
import pytest
from app.urltools import Paginated
from flask import request

class TestPagination(object):

    def testRequiresRequest(self):
        with pytest.raises(TypeError):
            Paginated.getCurrentPage()

    def testGetCurrentPageDefaultsToOne(self):
        with app.test_request_context('/'):
            assert Paginated.getCurrentPage(request) == 1

    def testGetCurrentPageReadsFromQueryParam(self):
        with app.test_request_context('/?page=42'):
            assert Paginated.getCurrentPage(request) == 42

    def testGetCurrentPageReadsOnlyFirstParam(self):
        with app.test_request_context('/?page=52&page=32&page=76'):
            assert Paginated.getCurrentPage(request) == 52
