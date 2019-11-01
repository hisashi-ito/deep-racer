# -*- coding: utf-8 -*-
#
# 報酬関数例2
#
# 速いスピードがよい
#
def reward_function(params):
    # コースの中にいるか判定値(boolean)
    all_wheels_on_track = params['all_wheels_on_track']
    # スピードを取得(m/sec)
    speed = float(params['speed'])
    
    # 高速と低速を判別する閾値を定義
    # 動作設定によって変動する
    SPEED_THRESHOLD = 3.0

    # コースアウト状態
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # 低速走行
        reward = 0.5
    else:
        # 高速走行時
        reward = 1.0

    # 報酬を返却
    return reward
