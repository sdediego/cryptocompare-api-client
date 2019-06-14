#!/usr/bin/env python
# encoding: utf-8


class BaseError(Exception):
    """
    Handle generic exception.
    """

    def __init__(self, message, code=None):
        """
        Initialize base error class.

        :param str message: error description message.
        :param int code: error code number.
        """
        if code is not None:
            self.code = code
            message = 'Error {code}. {msg}'.format(code=code, msg=message)
        self.message = message
        super(BaseError, self).__init__(message)


class CryptoCompareAPIHttpRequestError(BaseError):
    """
    Handle exception for CryptoCompare API http requests.
    """
    pass
