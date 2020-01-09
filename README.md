# IOT project：Automatic_Pedfeeder

## 專案由來
由於家裡養了一隻貓咪，但是每次要手動倒飼料真的很麻煩，倒太多吃不完會招來昆蟲，倒太少又會被貓咪煩。於是想出一個影像辨識的方法，透過此方法讓飼料機器決定要不要倒飼料。

## 專案構想
如題想做一個貓咪飼料自動餵食IOT。想用影像辨識去辨識出寵物碗的飼料多寡及空碗時間，去決定要不要放食物在寵物碗上，然後會去記錄每一次的餵食時間，讓主人知道貓咪今天的健康狀況。由於會怕此餵食器會貓咪飢餓太久(因貓咪每天的食量有時會不一定)，會每兩小時傳一次照片狀況，讓主人決定要不要使用手機功能使寵物餵食器餵食。
下圖為成品雛形。


## 材料準備
* Raspberry pi
  * 影像辨識處理，自動餵食功能處理。
* SG90 servo motor 馬達 x1
  * 可以透過馬達操控讓飼料瓶倒出飼料
* 攝影鏡頭 x1(野餐盒有)
  * 影像辨識功能用
* DIY飼料瓶
  * 考參考這個網址去做https://www.youtube.com/watch?v=Gx2KbgzPnPU
  * pp塑膠瓦楞板
  * 紙板
  * 橡皮筋
  * 飼料罐
  * 竹筷
* 寵物碗

## 零件說明
### SG90 servo motor
![image](https://github.com/monkey-huang/Automatic_Pedfeeder/tree/master/image/SG90_serve.png)

## 專案電路設計
![image](https://github.com/monkey-huang/Automatic_Pedfeeder/tree/master/image/my_circuit.png)
## 專案各檔案說明

## raspberry pi裡套件安裝教學

### keras套件安裝順序
