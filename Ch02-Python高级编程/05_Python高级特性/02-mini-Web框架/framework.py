# -*- coding: utf-8 -*-
"""
 * @file     framework.py
 * @brief    
 * @author   YongDu
 * @date     2022-10-01
"""

import time

route_list = list()


def route(path):
    def decorator(func):
        route_list.append((path, func))

        def inner():
            return func()

        return inner

    return decorator


@route("/index.html")
def index():
    status = "200 OK"
    response_header = [("Server", "PWS2.0")]

    with open("template/index.html", "r") as file:
        file_data = file.read()
    data = file_data.replace("{%content%}", time.ctime())
    return status, response_header, data


@route("/center.html")
def center():
    status = "200 OK"
    response_header = [("Server", "PWS2.0")]
    with open("template/center.html", "r") as file:
        file_data = file.read()
    data = time.ctime()
    result = file_data.replace("{%content%}", data)
    return status, response_header, result


def not_found():
    status = "404 Not Found"
    response_header = [("Server", "PWS2.0")]
    data = "not found"
    return status, response_header, data


def handle_request(env):
    request_path = env["request_path"]

    for path, func in route_list:
        if request_path == path:
            return func()
    else:
        return not_found()
