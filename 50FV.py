
import os
import requests
import time

# أخذ البيانات من متغيرات البيئة
owner_number = os.environ.get('OWNER_NUMBER', '')
owner_password = os.environ.get('OWNER_PASSWORD', '')
member1_number = os.environ.get('MEMBER1_NUMBER', '')
member1_password = os.environ.get('MEMBER1_PASSWORD', '')
member2_number = os.environ.get('MEMBER2_NUMBER', '')


def get_token(number, password):
    url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
    payload = {
        'grant_type': "password",
        'username': number,
        'password': password,
        'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
        'client_id': "ana-vodafone-app"
    }
    headers = {
        'User-Agent': "okhttp/4.11.0",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'silentLogin': "false",
        'x-agent-operatingsystem': "13",
        'clientId': "AnaVodafoneAndroid",
        'Accept-Language': "ar",
        'x-agent-device': "Xiaomi 21061119AG",
        'x-agent-version': "2024.12.1",
        'x-agent-build': "946",
        'digitalId': "28RI9U7IINOOB"
    }
    resp = requests.post(url, data=payload, headers=headers).json()
    return resp.get('access_token', '')

def get_headers(number, token):
    return {
        'api-version': 'v2',
        'x-agent-operatingsystem': 'rel.se.infra.20200819.140601',
        'Authorization': f'Bearer {token}',
        'clientId': 'AnaVodafoneAndroid',
        'x-agent-build': '623',
        'Accept': 'application/json',
        'msisdn': number,
        'Accept-Language': 'ar',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'mobile.vodafone.com.eg',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rTime left: {remaining} seconds")
        sys.stdout.flush()
        time.sleep(1)
    print("\n✅ Countdown finished.")

def redistribute_quota10():
    print("🔄 Redistributing 10% quota")
    token = get_token(owner_number, owner_password)
    url32 = 'https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
    hd22 = {
        "Host": "web.vodafone.com.eg",
        "Connection": "keep-alive",
        "Content-Length": "72",
        "DNT": "1",
        "msisdn": owner_number,
        "Accept-Language": "EN",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "clientId": "WebsiteConsumer",
        "channel": "WEB",
        "Origin": "https://web.vodafone.com.eg",
        "Referer": "https://web.vodafone.com.eg/"
        }
    data22 = '{"name":"FlexFamily","type":"QuotaRedistribution","category":[{"value":"47","listHierarchyId":"TemplateID"},{"value":"percentage","listHierarchyId":"familybehavior"}],"parts":{"member":[{"id":[{"value":"'+owner_number+'","schemeName":"MSISDN"}],"type":"Owner"},{"id":[{"value":"'+member2_number+'","schemeName":"MSISDN"}],"type":"Member"}],"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","value":"10","type":"percentage"}]}}}'
    r3 = requests.patch(url32,headers=hd22,data=data22).text
    print(r3)

def send_invitation_40():
    print("📤 Sending 40% invitation to Member 1")
    token = get_token(owner_number, owner_password)
    url32 = 'https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
    hd22 = {
        "Host": "web.vodafone.com.eg",
        "Connection": "keep-alive",
        "Content-Length": "72",
        "DNT": "1",
        "msisdn": owner_number,
        "Accept-Language": "EN",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "clientId": "WebsiteConsumer",
        "channel": "WEB",
        "Origin": "https://web.vodafone.com.eg",
        "Referer": "https://web.vodafone.com.eg/"
    }
    data22 = '{"name":"FlexFamily","type":"SendInvitation","category":[{"value":"523","listHierarchyId":"PackageID"},{"value":"47","listHierarchyId":"TemplateID"},{"value":"523","listHierarchyId":"TierID"},{"value":"percentage","listHierarchyId":"familybehavior"}],"parts":{"member":[{"id":[{"value":"'+owner_number+'","schemeName":"MSISDN"}],"type":"Owner"},{"id":[{"value":"'+member1_number+'","schemeName":"MSISDN"}],"type":"Member"}],"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","value":"40","type":"percentage"}]}}}'
    r3 = requests.post(url32,headers=hd22,data=data22).text
    print(r3)



def accept_invitation():
    print("✅ Accepting invitation")
    token = get_token(member1_number, member1_password)
    url3 = 'https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
    headers = get_headers(member1_number, token)
    data = f'''{{"category":[{{"listHierarchyId":"TemplateID","value":"47"}}],
    "name":"FlexFamily",
    "parts":{{"member":[{{"id":[{{"schemeName":"MSISDN","value":"2{owner_number}"}}],"type":"Owner"}},
    {{"id":[{{"schemeName":"MSISDN","value":"{member1_number}"}}],"type":"Member"}}]}},
    "type":"AcceptInvitation"}}'''
    print(requests.patch(url3, headers=headers, data=data).text)
  
    print("🔄 Redistributing 40% quota")
    token = get_token(owner_number, owner_password)
    url32 = 'https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
    hd22 = {
        "Host": "web.vodafone.com.eg",
        "Connection": "keep-alive",
        "Content-Length": "72",
        "DNT": "1",
        "msisdn": owner_number,
        "Accept-Language": "EN",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "clientId": "WebsiteConsumer",
        "channel": "WEB",
        "Origin": "https://web.vodafone.com.eg",
        "Referer": "https://web.vodafone.com.eg/"
    }
    data22 = '{"name":"FlexFamily","type":"QuotaRedistribution","category":[{"value":"47","listHierarchyId":"TemplateID"},{"value":"percentage","listHierarchyId":"familybehavior"}],"parts":{"member":[{"id":[{"value":"'+owner_number+'","schemeName":"MSISDN"}],"type":"Owner"},{"id":[{"value":"'+member2_number+'","schemeName":"MSISDN"}],"type":"Member"}],"characteristicsValue":{"characteristicsValue":[{"characteristicName":"quotaDist1","value":"40","type":"percentage"}]}}}'
    r3 = requests.patch(url32,headers=hd22,data=data22).text
    print(r3)    
def cancel_invitation():
    print("🚫 Cancelling invitation")
    token = get_token(owner_number, owner_password)
    url3 = 'https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup'
    headers = get_headers(owner_number, token)
    data = {
        "category": [{"listHierarchyId": "TemplateID", "value": "47"}],
        "createdBy": {"value": "MobileApp"},
        "parts": {
            "characteristicsValue": {
                "characteristicsValue": [
                    {"characteristicName": "Disconnect", "value": "0"},
                    {"characteristicName": "LastMemberDeletion", "value": "1"}
                ]
            },
            "member": [
                {"id": [{"schemeName": "MSISDN", "value": owner_number}], "type": "Owner"},
                {"id": [{"schemeName": "MSISDN", "value": member1_number}], "type": "Member"}
            ]
        },
        "type": "FamilyRemoveMember"
    }
    print(requests.post(url3, headers=headers, json=data).text)
    
    
import requests
import json

def Total():
    print("✅ Total Flex")
    token = get_token(owner_number, owner_password)
    url = (
        "https://web.vodafone.com.eg/services/dxl/usage/usageConsumptionReport"
        f"?bucket.product.publicIdentifier={owner_number}&@type=aggregated"
    )

    headers = {
        "Host": "web.vodafone.com.eg",
        "Connection": "keep-alive",
        "DNT": "1",
        "msisdn": owner_number,
        "Accept-Language": "EN",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "clientId": "WebsiteConsumer",
        "channel": "WEB",
        "Origin": "https://web.vodafone.com.eg",
        "Referer": "https://web.vodafone.com.eg/"
    }

    response = requests.get(url, headers=headers)
    #print(response.text)
    data = response.json()

    for section in data:
        if "bucket" in section:
            for bucket in section["bucket"]:
                if bucket.get("usageType") == "limit":   
                    target_amount= bucket["bucketBalance"][0]["remainingValue"]["amount"]
                    print(f"📊 Total Flex: {target_amount}")
    return None
    
    
cycle_number = 1
while True:
    print(f"\n🚀 Starting cycle /{cycle_number}...\n")
    
    
    redistribute_quota10()
    print("\n⏳ Waiting 300 seconds before continuing...\n")
    countdown(300)
    
    time.sleep(2)
    send_invitation_40()
    
    
    
    time.sleep(2)
    accept_invitation()
    #redistribute_quota()
    
    
    
    
    print("\n⏳ Waiting 2 seconds before cancelling invitation...\n")
    time.sleep(2)
    cancel_invitation()
    
    Total()
    
    
    # Step 5: Wait before restarting
    print("\n⏳ Waiting 300 seconds before next cycle...\n")
    countdown(300)
    
    cycle_number += 1