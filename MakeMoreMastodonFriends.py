from mastodon import Mastodon
import requests
import time

#自分のマストドンのURL
mastodon_url = "https://mastodon.comorichico.com"
#友達を作りたいマストドンのURL
target_mastodon_url = "vtdon.com"
#target_mastodon_url = "mastodon-japan.net"

mastodon = Mastodon(
    client_id = "cred.txt",
    access_token = "auth.txt",
    api_base_url = mastodon_url
)

def get_directory(target_mastodon_url, local):
    offset = 80
    count = 0
    datasList = []
    headers = {"content-type": "application/json"}
    while(True):
        directory_url = "https://" + target_mastodon_url \
            + "/api/v1/directory?offset=" + str(offset*count) \
            + "&limit=80&order=new&local=" + local

        res = requests.get(directory_url, headers=headers)
        datas = res.json()
        print("合計で" + str((count*offset) + len(datas)) + "件取得しました")
        datasList.append(datas)
        if len(datas) != 80:
            break
        count += 1
        time.sleep(1)
    return datasList

datasList = []
local = "true"
datasList = get_directory(target_mastodon_url,local)
for datas in datasList:
    for data in datas:
        account_dicts = mastodon.account_search(data["acct"] + "@" + target_mastodon_url)
        if account_dicts:
            mastodon.account_follow(int(account_dicts[0]["id"]))
            print(data["acct"] + "@" \
                + target_mastodon_url + "さんをフォローしました")
        time.sleep(1)