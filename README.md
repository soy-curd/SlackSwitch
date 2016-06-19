# SlackSwitch
Arduinoの入力をSlackに通知するbotです。

## ハードウェア

+ Arduino
+ 100均のボタン押すと光るやつ
+ 抵抗とか適当に

## 使い方
+ SlackのIncoming WebHookを設定し、URLを取得。
+ 環境変数`SLACK_URL`に上記で取得したURLを設定。
+ pythonを以下のように起動。

```
pip install -r python/requirements.txt
python python/oha.py
```
