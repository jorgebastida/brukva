#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RedisError(Exception):
    pass


class ConnectionError(RedisError):

    def __init__(self, *args, **kwargs):
        self.cmd_line = kwargs.pop('cmd_line', None)
        super(ResponseError, self).__init__(*args, **kwargs)

    def __repr__(self):
        message = self.args[0] if self.args else None
        if self.cmd_line:
            return '%s (on %s [%s, %s]): %s' % (self.__class__.__name__, self.cmd_line.cmd, self.cmd_line.args, self.cmd_line.kwargs, message)
        return '%s: %s' % (self.__class__.__name__, message)

    __str__ = __repr__


class RequestError(RedisError):
    pass


class ResponseError(RedisError):
    pass


class InvalidResponse(RedisError):
    pass
