# -*- coding: utf-8 -*-
import urllib
import json
import base64
from Crypto.Cipher import AES


class AESService(object):
    BLOCK_SIZE = 32
    PADDING = '{'
    SECRET = '72gvWKCtWxDoEwoCpkbdCChQ3a4knA7U'
    CIPHER = AES.new(SECRET)
    pad = staticmethod(lambda s: s + (
        (AESService.BLOCK_SIZE - len(s) % AESService.BLOCK_SIZE)
        * AESService.PADDING))

    @staticmethod
    def getCipheredString(info_str):
        return base64.b64encode(
            AESService.CIPHER.encrypt(AESService.pad(info_str)))


class PocketService(object):
    SERVICE_URL = "http://fireinice.3322.org:9080/sendpks/?"

    @staticmethod
    def getPocketInfo(url, title):
        info = {'url': url,
                'title': title}
        return PocketService.SERVICE_URL + urllib.urlencode({
            "info": AESService.getCipheredString(json.dumps(info))})
