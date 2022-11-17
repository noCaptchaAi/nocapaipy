import json
import requests
import os
import sys

class Nocapaipy:
    def __init__(self, images, target, method, sitekey, site, ln, uid, apikey, softid=None):
        self.images = images
        self.target = target
        self.method = method
        self.sitekey = sitekey
        self.site = site
        self.ln = ln
        self.softid = softid
        self.uid = uid
        self.apikey = apikey

    def solve(self):
        base64_json = {
            "images": self.images,
            "target": self.target,
            "method": self.method,
            "sitekey": self.sitekey,
            "site": self.site,
            "ln": self.ln,
        }
        if self.softid:
            base64_json["softid"] = self.softid
        base64_json = json.dumps(base64_json)

        try:
            r = requests.post(
                "https://free.nocaptchaai.com/api/solve",
                headers={
                    "Content-type": "application/json",
                    "uid": self.uid,
                    "apikey": self.apikey,
                },
                data=base64_json,
            )
            return json.dumps(r.json())
        except Exception as err:
            return json.dumps({"error": str(err)})
