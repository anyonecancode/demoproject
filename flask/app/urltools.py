from functools import wraps
from flask import g, request, redirect, url_for
"""
Utilities for reading, setting, and in general working with urls
"""

class Paginated:
    """
    Decorator to support pagination
    """

    @staticmethod
    def getCurrentPage(request):
        return request.args.get('page', 1, type=int)
