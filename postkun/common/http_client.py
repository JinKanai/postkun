import json
import ssl
import sys
import traceback
import urllib.error
import urllib.request


class HttpClient:

    @staticmethod
    def get(url, headers):
        req = urllib.request.Request(url, headers=headers)
        return HttpClient.fetch_url(req)

    @staticmethod
    def post(url, contents, headers):
        try:
            req = urllib.request.Request(url, json.dumps(
                contents).encode(), headers=headers)
            return HttpClient.fetch_url(req)
        except ValueError as e:
            print(e)
            return False

    """
    @staticmethod
    def put(url, contents, headers):
        req = urllib.request.Request(url, json.dumps(contents), headers=headers)
        req.get_method = lambda: "PUT"
        return HttpHandler.fetch_api(req)
    @staticmethod
    def delete(url, headers):
        req = urllib.request.Request(url, headers=headers)
        req.get_method = lambda: "DELETE"
        return HttpHandler.fetch_api(req)
    """

    @staticmethod
    def fetch_url(req):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        body = None
        res = None
        try:
            res = urllib.request.urlopen(req, context=context)
            body = res.read().decode()
            #if res.length:
            #    body = json.load(res)

        except urllib.error.HTTPError as e:
            print(
                "HTTP Error has detected. Abort. status code is {0}.".format(e.code))
            print(traceback.format_exc())
            print(req.get_full_url())
            sys.exit(1)
        except urllib.error.URLError as e:
            print(
                "URL Error has detected. Abort. the reason is '{0}'.".format(e.reason))
            print(traceback.format_exc())
            print(req.get_full_url())
            sys.exit(1)
        except ValueError as e:
            print(traceback.format_exc())
            print(e)
            sys.exit(1)
        finally:
            if res:
                res.close()
        return body
