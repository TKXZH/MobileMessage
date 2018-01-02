

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import json
appid = 1400058993;
appkey = "c0184f30f7f282d129457c544c0b7fce";
phone_numbers = ["18721919982", "18883870720", "17521097596"];
template_id = 7839;

ssender = SmsSingleSender(appid, appkey)
try:

    result = ssender.send(0, 86, phone_numbers[0],
        "zzzzz")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print json.dumps(result, ensure_ascii=False, encoding='UTF-8')