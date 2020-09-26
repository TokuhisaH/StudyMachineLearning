# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#売上と気温
input_data=np.array([[20,30],[23,32],[28,40],[30,44]])
#データの数を行方向へカウントすることで持ってこれる
data_number = input_data.shape[0]

#正規化
'''
xの最大値=30
yの最大値=44

xの最小値=20
yの最小値=30

xの最大-最小＝10
yの最大-最小＝14

'''
#input_dataの最小値
#axisはどの方向のデータの最小値を取るかの指定 0は列方向の中から小さい行をもってくる
#keepdimsで次元を変えないようにする
input_data_min=np.min(input_data,axis=0,keepdims=True)
x_min=input_data_min[0,0]
y_min=input_data_min[0,1]

input_data_max=np.max(input_data,axis=0,keepdims=True)
x_max=input_data_max[0,0]
y_max=input_data_max[0,1]

#縮小の作業input_dataからx,yの最小値を引き、最大-最小で割る
input_data_normalized=(input_data-input_data_min)/(input_data_max-input_data_min)
    
#エポック数（任意）
epochs=100
#学習率（任意）正規化したら0.1くらいで試してみるといい
alpha = 0.1
#重み（ランダム 今はわかりやすくするために0.1）
w0 = 0.1
w1 = 0.1

'''
誤差関数の２乗したもとの値
(w0 + w1x1 -y1)^2
=w0^2 + w1^2x1^2+y1^2+2w0w1x1-2w1x1y1-2y1w0
'''

for t in range(epochs):
    dw0 = 0
    dw1 = 0
    for i in range(data_number):
        '''
        w0、w1で微分すると
        dw0 = dw0 + 2w0 +2w1x1 -2y1
        dw1 = dw1 + x1(2w1x1 + 2w0 -2y1)
        '''
        #接戦の傾きを合計する(微分する前に足してもいいけどこっちのが楽)
        #(x,y)に合わせてinput_dataの中身を動かす
        dw0 = dw0 + 2*w0 +2*w1*input_data_normalized[i,0] -2*input_data_normalized[i,1]
        dw1 = dw1 + input_data_normalized[i,0]*(2*w1*input_data_normalized[i,0] + 2*w0 -2*input_data_normalized[i,1])
    
    #傾きの方向に進んでいく
    #傾きの下り方向に進めていくことで最小の値を求めていく
    w0 = w0 -alpha*(dw0)
    w1 = w1 -alpha*(dw1)
    print(dw1)

#誤差関数をグラフにプロットするための式
#x軸の（最小、最大、その間に何個の点を取るか）
'''
x=np.linspace(0,1,100)
#式
y= w0 + w1*x

plt.plot(x,y)

for u in range(data_number):
    #scatter:散布図
    plt.scatter(input_data_normalized[u,0],input_data_normalized[u,1])
'''

#正規化したやつをもとに戻す作業
#データを弄るのではなくグラフを操作する
#今回はx方向に10、y方向に14で割って、（20,30）で平行移動していた
x1=np.linspace(15,30,100)

y1=(w0+w1*(x1-20)/10)*14+30

plt.plot(x1,y1)

for u in range(data_number):
    #scatter:散布図
    plt.scatter(input_data[u,0],input_data[u,1])
