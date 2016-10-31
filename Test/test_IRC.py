import unittest
import threading
import pykka
import json
import os
import time
from Legobot.LegoError import LegoError
from Legobot.Message import Message, Metadata
from Legobot.Lego import Lego
from Legobot.Connectors.IRC import IRC

# Mock objects for testing

class TestIRC(unittest.TestCase):
    @staticmethod
    def test_initialization():
        baseplate = Lego.start(None, threading.Lock())
        baseplate_proxy = baseplate.proxy()
        baseplate_proxy.add_child(IRC,
                                  channels=['#foo'],
                                  nickname='test_nick',
                                  server='foo.testing',
                                  port=6667,
                                  use_ssl=False,
                                  username='test_username',
                                  password='test_password')
        # Cleanup
        children = baseplate_proxy.children.get()
        for child in children:
            child.stop()
        baseplate.stop()
