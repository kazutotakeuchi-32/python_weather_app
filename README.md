# 天気情報の取得システム
- 天気情報を取得し通知するシステム
- 1日毎の天気情報をDynamoDBに書き込む
- 1週間毎の天気情報をcsvファイルに出力しS3に吐き出す。

## インフラ構成図
### 1日毎の天気情報をDynamoDBに保存
- EventBridgeでjobを設定
- Lambda関数でOpenWeatherから今日の天気情報を取得する
- データをLINE Notiyに通知
→ 異常系な場合は、「システムエラーです」と通知
- 問題がなければDynamoDBに1日毎の天気情報を書き込む
<img src="https://i.gyazo.com/fe3a19d9a0e3cda44bee2623c9384601.png" alt="インフラ構成図１">

### 1週間毎の天気情報をcsvファイルに出力しS3に吐き出す。
- EventBridgeでjobを設定
- Lambda関数で１週間の天気情報をDynamoDBから取得
- CSVファイルに出力
- S3にputする。
<img src="https://i.gyazo.com/623d058c485a3a2a2fa2cb09906d769c.png" alt="インフラ構成図2">

