# [AWS DeepRacer](https://aws.amazon.com/jp/deepracer/)

<p align="center">
<img src="https://user-images.githubusercontent.com/8604827/68000757-a257a600-fca4-11e9-80e9-6a7bc36192c9.png" width="250px">
</p>

AWS DeepRacer の各種実験と報酬関数の実装例を記載します。基本的には[公式ページ](https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/deepracer-reward-function-input.html)を参考にします。

## 報酬関数
報酬関数として以下の関数を定義して利用します。関数名は固定です。
```python
def reward_function(params) :
    reward = ...
    # reward として車の状態に対して１つのスカラ値(float)を返却する
    return float(reward)
```
### 入力パラメータ一辞書
報酬関数の入力値として車の状態を入力値として取れるパラメータを入力できます。
params 辞書オブジェクトには、次のキーと値のペアが含まれています。



