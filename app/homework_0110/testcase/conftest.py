# -*- coding:utf-8 -*-
__author__ = "leo"

import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="function", autouse=True)
def scrcpy_record():
    cmd = "scrcpy --record file.mp4"
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    print(p)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
