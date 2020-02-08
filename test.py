import requests
import time
import jsonpath
from jiami import *


class Post:
    a = {"channelName": "dmkj_Android", "countryCode": "CN", "createTime": int(100 * time.time()),
         "device": "Xiaomi Mi MIX 2S", "hardware": "qcom", "modifyTime": int(100 * time.time()),
         "operator": "%E6%9C%AA%E7%9F%A5", "screenResolution": "1080-2116",
         "startTime": int(100 * time.time()) + 19602323,
         "sysVersion": "Android 29 10", "system": "android", "uuid": "A4:50:46:0F:74:AF", "version": "4.2.6"}
    headers = {
        'standardUA': str(a),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'appdmkj.5idream.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0'
    }

    def get_ids(self, token, uid):
        signtoken = get_signtoken(
            '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"","joinStartTime":"","keyword":"","level":"","page":"1","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}')
        # print(token, signtoken)
        str1 = '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"","joinStartTime":"","keyword":"","level":"","page":"1","signToken":"' + signtoken + '","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}'
        data = "dataKey=t%2BZ88oeo2xscPIEBzd1JWLr%2Faae06xI9WOwwXOVRupB%2BsAsl1nj2HDpZPc3ygHRlgm0glZajSvF7FsxbGiBe%2FcykCvyhloLZfYPGGLrCZV6ZBVDBHgwg6%2Fkq87A6A%2Bp%2BmTeUyp3eZz4voIGytVkwmlofr0Jn5bgBOitzBJtnq0I%3D&data={}".format(
            jiami(str1))

        url = "https://appdmkj.5idream.net/v2/activity/activities"

        res = requests.post(url, headers=self.headers, data=data).json()
        # print(res['data']['list'][1])
        names = jsonpath.jsonpath(res, '$..name')
        ids = jsonpath.jsonpath(res, '$..aid')
        statusTexts = jsonpath.jsonpath(res, '$..statusText')
        self.names = names
        self.ids = ids
        self.statusTexts = statusTexts
        # for name, id, statusText in zip(names, ids, statusTexts):
        #     print(name, id, statusText)
        # b = {}
        # for name, id, statusText in zip(names, ids, statusTexts):
        #     if '补发' in name:
        #         None
        #     elif '已结束' in statusText:
        #         print(name + '已经结束')
        #     elif '团日' in name:
        #         None
        #     elif '青年大学习' in name:
        #         None
        #     else:
        #         b[name] = id
        # print(b)
        # return b

    def get_info(self, id, token, uid):
        signtoken = get_signtoken(
            '{"activityId":"' + id + '","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}')

        str1 = '{"activityId":"' + id + '","signToken":"' + signtoken + '","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}'
        data = "dataKey=t%2BZ88oeo2xscPIEBzd1JWLr%2Faae06xI9WOwwXOVRupB%2BsAsl1nj2HDpZPc3ygHRlgm0glZajSvF7FsxbGiBe%2FcykCvyhloLZfYPGGLrCZV6ZBVDBHgwg6%2Fkq87A6A%2Bp%2BmTeUyp3eZz4voIGytVkwmlofr0Jn5bgBOitzBJtnq0I%3D&data={}".format(
            jiami(str1))
        url = "https://appdmkj.5idream.net/v2/activity/detail"
        res = requests.post(url, headers=self.headers, data=data)

        if res.json()['code'] == '100':
            return res
        else:
            return None

    def get_join(self, token, uid):
        signtoken = get_signtoken(
            '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"1","joinStartTime":"","keyword":"","level":"","page":"1","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}')
        str1 = '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"1","joinStartTime":"","keyword":"","level":"","page":"1","signToken":"' + signtoken + '","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}'
        data = "dataKey=t%2BZ88oeo2xscPIEBzd1JWLr%2Faae06xI9WOwwXOVRupB%2BsAsl1nj2HDpZPc3ygHRlgm0glZajSvF7FsxbGiBe%2FcykCvyhloLZfYPGGLrCZV6ZBVDBHgwg6%2Fkq87A6A%2Bp%2BmTeUyp3eZz4voIGytVkwmlofr0Jn5bgBOitzBJtnq0I%3D&data={}".format(
            jiami(str1))
        url = 'https://appdmkj.5idream.net/v2/activity/activities'
        res = requests.post(url, headers=self.headers, data=data)

        if res.json()['code'] == '100':
            return res.json()
        else:
            return None

    def get_can_join(self, token, uid):
        signtoken = get_signtoken(
            '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"1","joinStartTime":"","keyword":"","level":"","page":"1","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}')
        # print(token, signtoken)
        str1 = '{"catalogId":"","catalogId2":"","endTime":"","joinEndTime":"","joinFlag":"1","joinStartTime":"","keyword":"","level":"","page":"1","signToken":"' + signtoken + '","sort":"","specialFlag":"","startTime":"","status":"","token":"' + token + '","uid":' + uid + ',"version":"4.2.6"}'
        data = "dataKey=t%2BZ88oeo2xscPIEBzd1JWLr%2Faae06xI9WOwwXOVRupB%2BsAsl1nj2HDpZPc3ygHRlgm0glZajSvF7FsxbGiBe%2FcykCvyhloLZfYPGGLrCZV6ZBVDBHgwg6%2Fkq87A6A%2Bp%2BmTeUyp3eZz4voIGytVkwmlofr0Jn5bgBOitzBJtnq0I%3D&data={}".format(
            jiami(str1))

        url = "https://appdmkj.5idream.net/v2/activity/activities"

        res = requests.post(url, headers=self.headers, data=data).json()
        if res['data']['list']:
            names = jsonpath.jsonpath(res, '$..name')
            ids = jsonpath.jsonpath(res, '$..aid')
            statusTexts = jsonpath.jsonpath(res, '$..statusText')
            self.names = names
            self.ids = ids
            self.statusTexts = statusTexts
        else:
            return '没有活动可以参加'


if __name__ == '__main__':
    a = Post()
    try:
        with open('a.ini', 'r', encoding='utf-8') as f:
            token = f.readline().rstrip()
            name = f.readline().rstrip()
            uid = f.readline().rstrip()
            # a.get_ids(token, uid)
            # a.get_can_join(token, uid)
            # print(a.get_info('1774799', token, uid).text)
    except:
        None
        # print("token失效,重新获取")

        # a.get_ids(token)
        # a.get_ids(a.ids[1], token)
