from mastodon import Mastodon

app_name = "アプリの名前"
mail = "マストドンにログインするメールアドレス"
password = "マストドンにログインするパスワード"

url = "https://mastodon.comorichico.com"

Mastodon.create_app(app_name,
                    api_base_url=url,
                    to_file="cred.txt"
                    )

mastodon = Mastodon(
     client_id="cred.txt",
     api_base_url=url
)

mastodon.log_in(
     mail,
     password,
     to_file="auth.txt"
)