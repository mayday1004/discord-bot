##前置作業

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

##正式開始

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
   `$初始化 channelID "要搜尋的關鍵字(可以搭配使用進階搜尋的搜尋運算符)"` \*默認搜尋讚數 > 50 且含連結的推文，排除回應的推文

4. 若機器人回應:頻道 ID: channelID 無誤，開始獲取推文 代表成功，機器人會每隔 1 小時檢查一次是否有新推文
