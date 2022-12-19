## 前置作業

您需要在 Discord 開發人員網站上創建一個機器人帳戶，並邀請機器人到您的私人群組。
此外，您也必須註冊 Twitter 開發人員帳號，並取得 API_KEY 和 TOKEN

您可以透過下列步驟來完成 Discord 機器人操作：

1. 前往 https://discord.com/developers/applications/me
2. 點選 "New Application" 按鈕
3. 輸入您想要給應用程式設定的名稱，然後點選 "Create" 按鈕
4. 在左側菜單，點擊「Bot」選項。
5. 點擊「Add Bot」按鈕。
6. 輸入機器人的名稱，然後點擊「Save Changes」按鈕。
7. 接著左側菜單，點擊「OAuth2 > URL Generator」選項。
8. "SCOPES"勾選「bot」選項。
9. 接著你可以選取要開放給機器人的權限
10. 複製"GENERATED URL"的內容，貼到瀏覽器的網址列就可以邀請機器人到你的 Discord 群組了

## 正式開始

1. 安裝套件

```
pip install -r requirements.txt
```

2. 新增.env 檔案

```
API_KEY="這裡放推特開發人員API_KEY"
API_KEY_SECRET="這裡放推特開發人員API_KEY_SECRET"
ACCESS_TOKEN="這裡放推特開發人員ACCESS_TOKEN"
ACCESS_TOKEN_SECRET="這裡放推特開發人員ACCESS_TOKEN_SECRET"
BOT_TOKEN="這裡放Discord機器人的TOKEN"
```

3. 到要放置推文的頻道內輸入以下指令:

```
$推特搜尋 "要搜尋的關鍵字" "要排除的關鍵字" 特定讚數大於N的推文
```

例如 : `$推特搜尋 "iphone OR ios" "android,google" 100`

若機器人回應:"頻道 ID: channelID 開始獲取推文"，代表成功，機器人會每隔 1 小時檢查一次是否有新推文
*默認搜尋只含影片或圖片的推文，排除回應及引用的推文
*由於在 discord 輸入#可能會觸發 discord 連結頻道的命令，避免跟搜尋關鍵字衝突，所以要搜尋帶#Tag 的關鍵字請把#改成!

4. 若要停止某個頻道的自動發文，可以使用以下指令:

```
$停止推文
```

6. 指令:$清理對話，默認刪除 100 筆頻道消息，可選擇輸入 0~100 來刪除指定筆數的消息

```
$清理對話 10
```
