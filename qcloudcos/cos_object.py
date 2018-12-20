import requests
from qcloudcos.cos_auth import Auth
from django.conf import settings
from .utils import get_logger


LOGGER = get_logger('Tencent Cos')


class CosObject(object):
    def __init__(self, option=None):
        if not option:
            self.option = settings.QCLOUD_STORAGE_OPTION
        else:
            self.option = option

    def get_object(self, name, is_private=False):
        method = 'get'
        appid = self.option['Appid']
        SecretID = self.option['SecretID']
        SecretKey = self.option['SecretKey']
        region = self.option['region']
        bucket = self.option['bucket']
        if name[0] != '/':
            name = '/' + name
        objectName = name
        url = "http://%s-%s.%s.myqcloud.com%s" % (bucket, appid, region, objectName)
        s = requests.Session()
        if is_private:
            auth = Auth(appid, SecretID, SecretKey, bucket, region, method, objectName)
            Authorization = {'Authorization': auth.get_authorization()}
            s.headers.update(Authorization)

        r = s.get(url)
        return r

    def put_object(self, name, content):
        method = 'put'
        appid = self.option['Appid']
        SecretID = self.option['SecretID']
        SecretKey = self.option['SecretKey']
        region = self.option['region']
        bucket = self.option['bucket']
        if name[0] != '/':
            name = '/' + name
        objectName = name
        url = "http://%s-%s.%s.myqcloud.com%s" % (bucket, appid, region, objectName)

        s = requests.Session()
        auth = Auth(appid, SecretID, SecretKey, bucket, region, method, objectName)
        Authorization = {'Authorization': auth.get_authorization()}
        s.headers.update(Authorization)

        r = s.put(url, data=content)
        if r.status_code == 200:
            return r
        else:
            LOGGER.info(r.content)

    def head_object(self, name, is_private=False):
        method = 'head'
        appid = self.option['Appid']
        SecretID = self.option['SecretID']
        SecretKey = self.option['SecretKey']
        region = self.option['region']
        bucket = self.option['bucket']
        if name[0] != '/':
            name = '/' + name
        objectName = name
        url = "http://%s-%s.%s.myqcloud.com%s" % (bucket, appid, region, objectName)
        s = requests.Session()
        if is_private:
            auth = Auth(appid, SecretID, SecretKey, bucket, region, method, objectName)
            Authorization = {'Authorization': auth.get_authorization()}
            s.headers.update(Authorization)

        r = s.head(url)
        return r

    def delete_object(self, name):
        method = 'delete'
        appid = self.option['Appid']
        SecretID = self.option['SecretID']
        SecretKey = self.option['SecretKey']
        region = self.option['region']
        bucket = self.option['bucket']
        if name[0] != '/':
            name = '/' + name
        objectName = name
        url = "http://%s-%s.%s.myqcloud.com%s" % (bucket, appid, region, objectName)

        s = requests.Session()
        auth = Auth(appid, SecretID, SecretKey, bucket, region, method, objectName)
        Authorization = {'Authorization': auth.get_authorization()}
        s.headers.update(Authorization)

        r = s.delete(url)
        if r.status_code == 204:
            return True
