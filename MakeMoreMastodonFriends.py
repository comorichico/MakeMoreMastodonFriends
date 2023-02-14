from mastodon import Mastodon

mastodon = Mastodon(
    client_id = "cred.txt",
    access_token = "auth.txt",
    api_base_url = "https://mastodon.comorichico.com") #インスタンス

domain = "vtdon.com"
directory_uri = "https://" + domain + "/api/v1/directory"