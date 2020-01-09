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
![image](https://github.com/monkey-huang/Automatic_Pedfeeder/blob/master/image/SG90_serve.png)

* 如圖片所顯示的，分為control，GND，5V
  * GND部份去接地極
  * 5V去接5V電源
  * control的部分為控制馬達
## 專案電路設計
![image](https://github.com/monkey-huang/Automatic_Pedfeeder/blob/master/image/my_circuit.png)
* 記得control pin接的是11pin，BCM是17，程式控制的時候會用BCM 17方式去控制
## 專案各檔案說明
* camera.py：如檔案名稱，為拍照模組，拍完照之後會存在static的資料夾
* my_model_detection.h5：這個為我自己用keras訓練好的CNN模型，也可用你們自己另外訓練好的
* pretrainmodel.py：LOAD pretrainmodel與predict模組。
* app_sg90.py：flask網站整合模組，整合以上兩個模組在這個檔案裡，並且用網站的方式呈現。
## raspberry pi裡套件安裝教學，注意這是針對raspberry pi的
### flask套件安裝順序
```
installing flask
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-pip python-flask
sudo pip install flask

安裝 socketio
pip install flask-socketio
```
### keras套件安裝順序
```
sudo apt-get install python3-numpy
sudo apt-get install libblas-dev
sudo apt-get install liblapack-dev
sudo apt-get install python3-dev 
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-setuptools
sudo apt-get install python3-scipy
sudo apt-get update
sudo apt-get install python3-h5py

pip install scipy
pip install cython --user
pip install tensorflow
pip install keras --user
sudo apt-get install keras 
```
## 小問題解決方法指令
* 刪除不要的套件
  * $ sudo apt-get remove --purge --auto-remove [套件名稱]
  * 舉例:我要刪除libreoffice*的話：$ sudo apt-get remove --purge --auto-remove libreoffice*
## 影片demo
https://www.youtube.com/watch?v=jJnUdHY9Uhk

## 參考網址

* [寵物飼料器影片教學](https://www.youtube.com/watch?v=Gx2KbgzPnPU)
* [伺服馬達PWM程式教學](https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-mobel-3-%E5%88%A9%E7%94%A8-pwm-%E6%8E%A7%E5%88%B6%E4%BC%BA%E6%9C%8D%E9%A6%AC%E9%81%94)
* [flask 按鈕範例網址與安裝教學](https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/)
* [LOAD keras pretrain model教學](https://morvanzhou.github.io/tutorials/machine-learning/keras/3-1-save/)
* [在raspberrypi上安裝keras套件教學](https://ai-pool.com/d/how-to-install-keras-on-raspberry-pi-)
* [刪除不要的套件教學](http://yehnan.blogspot.com/2017/02/raspberry-pi.html)
