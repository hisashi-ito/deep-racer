# -*- coding: utf-8 -*-
#
# 報酬関数例3
#
# ジグザグ走行を抑止
#
def reward_function(params):
    # 急ハンドルぐわい
    STEERING_THRESHOLD = 20.0
    
    # コースの中にいるか判定値(boolean)
    all_wheels_on_track = params['all_wsheels_on_track']

    # ハンドルのきり幅
    # -30度から30度までを取得(プラスマイナスは無視)
    steering = abs(params['steering_angle']) 

    # Default値
    reward = 1.0

    if not all_wheels_on_track:
        # 基本コースアウトしたらあかん
        reward = 1e-3
    else:
        if steering >= STEERING_THRESHOLD:
            # 思っきり急ハンドル時は0.7 掛け
            reward = reward * 0.7

    # 報酬を返却
    return reward
