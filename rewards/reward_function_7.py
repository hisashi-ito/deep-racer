# -*- coding: utf-8 -*-
#
# 報酬関数例7
#
# 有効な施策を組みわせる
# ・急ハンドル禁止
# ・waypoinsへ沿う
#
def reward_function(params):
    import math
    # 急ハンドルぐわい
    STEERING_THRESHOLD = 20.0
    
    # コースの中にいるか判定値(boolean)
    all_wheels_on_track = params['all_wheels_on_track']

    # ハンドルのきり幅
    # -30度から30度までを取得(プラスマイナスは無視)
    steering = abs(params['steering_angle']) 

    # Default値
    reward = 1.0

    if not all_wheels_on_track:
        # 基本コースアウトしたらあかん
        reward = 1e-3
        return reward

    else:
        if steering >= STEERING_THRESHOLD:
            # 思っきり急ハンドル時は0.7 掛け
            reward = reward * 0.7

    # コース上に敷き詰められたwaypoints を取得
    waypoints = params['waypoints']
    # 自車から一番近いwaypointを取得(2つ取得できる)
    closest_waypoints = params['closest_waypoints']
    # 座標系の x 軸に対する車両の進行方向 (度単位)。
    heading = params['heading']

    # 現在の位置から最も近い次のwaypointと前のwaypointを取得する
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # 前のwaypointから次のwaypointに向かう角度(radian)を計算する
    # math.atan2(y, x) で角度が求まる。角度はラジアン
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # コース上の基準軸に対する車体の向き(heading)
    # 直近のwaypointを繋ぐ向きの差分を取る
    direction_diff = abs(track_direction - heading)

    # waypointに沿った傾きと大きく乖離している場合は
    # ペナルティを課す
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # 報酬を返却
    return reward