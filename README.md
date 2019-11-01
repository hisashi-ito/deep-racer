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
```python
{
    "all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
    "x": float,                        # vehicle's x-coordinate in meters
    "y": float,                        # vehicle's y-coordinate in meters
    "distance_from_center": float,     # distance in meters from the track center 
    "is_left_of_center": Boolean,      # Flag to indicate if the vehicle is on the left side to the track center or not. 
    "heading": float,                  # vehicle's yaw in degrees
    "progress": float,                 # percentage of track completed
    "steps": int,                      # number steps completed
    "speed": float,                    # vehicle's speed in meters per second (m/s)
    "steering_angle": float,           # vehicle's steering angle in degrees
    "track_width": float,              # width of the track
    "waypoints": [[float, float], … ], # list of [x,y] as milestones along the track center
    "closest_waypoints": [int, int]    # indices of the two nearest waypoints.
}
```
以下に各パラメータについて説明する。
#### *all_wheels_on_track*
タイプ: Boolean  
範囲: True|False  

車両がトラック内にあるのかトラック外にあるのかを示す Boolean フラグ。ホイールのいずれかがトラックの境界線の外側にある場合は、トラック外 (False) です。すべてのホイールが 2 つのトラック境界の内側にある場合はトラック内 (True) です。次の図は、車両がトラック上にあることを示しています。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-all_wheels_on_track-true.png" width="250px"><br>車両がトラックに入っているばあい
</p>

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-all_wheels_on_track-false.png" width="250px"><br>車両がトラックから外れている場合
</p>

#### *closest_waypoints*  
タイプ: [int, int]  
[範囲]: [0:Max-2,1:Max-1] 

(x, y) の現在位置に最も近い 2 つの隣接する waypoint のゼロベースのインデックス。距離は車両の中心からのユークリッド距離によって測定されます。Max はウェイポイントリストの長さです。ウェイポイント で示している下図では、closest_waypoints は [16, 17] になります。[16, 15] になる可能性もあります。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-waypoints.png" width="300px"><br>車両がトラックから外れている場合
</p>

#### *distance_from_center*  
タイプ: float  
範囲: 0:~track_width/2  

車両の中心とトラックの中心との間のメートル単位の変位。観察可能な最大変位は、エージェントのいずれかの車輪がトラックの境界線の外側にあるときに発生し、トラックの境界線の幅に応じて、track_width の半分よりわずかに小さいまたは大きい場合があります。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-distance_from_center.png" width="300px"><br>車両のセンターからの位置
</p>

#### *heading*  
タイプ: float  
範囲: -180:+180  

座標系の x 軸に対する車両の進行方向 (度単位)。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-heading.png" width="300px"><br>座用系のｘ軸に対する車両の進行方向(度単位)
</p>

#### *is_left_of_center*  
タイプ: Boolean  
範囲: True | False  

車両がトラックの中心より左側 (True) にあるのか右側 (False) にあるのかを示す Boolean フラグ。

#### *progress* 
タイプ: float  
範囲: 0:100  
トラック完走の割合。

#### *speed*
タイプ: float  
範囲: 0.0:5.0   

車両の観測速度 (メートル/秒)。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-speed.png" width="300px"><br>速度
</p>

#### *steering_angle*
タイプ: float  
範囲: -30:30  

車両の中心線からの前輪のステアリング角 (度単位)。負の記号 (-) は右へのステアリングを意味し、正の (+) 記号は左へのステアリングを意味します。次の図に示すように、車両の中心線はトラックの中心線と必ずしも平行ではありません。  

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-steering.png" width="300px"><br>ステアリング角度
</p>

#### *step*
タイプ: int  
範囲: 0:Nstep  
完了したステップ数。ステップは、現在のポリシーに従って車両がとる行動に対応します。  

#### *track_width*
タイプ: float  
範囲: 0:Dtrack  

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-track_width.png" width="300px"><br>トラック幅
</p>

#### *x, y*
タイプ: float  
範囲: 0:N  

トラックを含むシミュレーション環境の x 軸と y 軸に沿った車両中心の位置 (メートル単位)。原点は、シミュレーション環境の左下隅にあります。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-x-y.png" width="300px"><br>x,y
</p>

#### *waypoint*
タイプ: [float, float] の list  
[範囲]: [[xw,0,yw,0] … [xw,Max-1, yw,Max-1]]  
トラックの中心に沿ったトラック依存 Max マイルストーンの順序付きリスト。各マイルストーンは、(xw、i、yw、i) の座標で表されます。ループされたトラックの場合、最初と最後のウェイポイントは同じです。直線のトラックなどループされないトラックの場合、最初と最後のウェイポイントは異なります。

<p align="center">
<img src="https://docs.aws.amazon.com/ja_jp/deepracer/latest/developerguide/images/deepracer-reward-function-input-waypoints.png" width="300px"><br>waypoints
</p>

### 報酬関数例
1. 
