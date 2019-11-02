# -*- coding: utf-8 -*-
#
# 報酬関数例8
#
# 1) コース上に設定されたポイントに向かって進むように制御する
# 2) waypointとステアリング向きによって右左のステアリングに対して報酬の差を導入
#
def reward_function(params):
    # コースの中にいるか判定値(boolean)
    all_wheels_on_track = params['all_wheels_on_track']
    if not all_wheels_on_track:
        # 基本コースアウトしたらあかん
        reward = 1e-3
        return reward

    import math
    # コース上に敷き詰められたwaypoints を取得
    waypoints = params['waypoints']
    # 自車から一番近いwaypointを取得(2つ取得できる)
    closest_waypoints = params['closest_waypoints']
    # 座標系の x 軸に対する車両の進行方向 (度単位)。
    heading = params['heading']
    # ステアリングの角度
    steering_angle = params['steering_angle']
    # 報酬のDefault値
    reward = 1.0

    # 現在の位置から最も近い次のwaypointと前のwaypointを取得する
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # 前のwaypointから次のwaypointに向かう角度(radian)を計算する
    # math.atan2(y, x) で角度が求まる。角度はラジアン
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # コース上の基準軸に対する車体の向き(heading) と直近のwaypointを繋ぐ角度の差を見る
    delta  = track_direction - heading
    if delta > 5:
        # 進行すべき方向から右にいる場合
        if steering_angle < 0:
            # 右ステアリングだったら報酬を減らす
            reward *= 0.7
        else:
            # 左ステアリングだったらなにもしない
            pass
    elif delta < -5: 
        # 進行すべき方向から左にいる
        if steering_angle > 0:
            # 左ステアリングだったら報酬をへらす
            reward *= 0.7
        else:
            # 右ステアリングだったらなにもしない
            pass
    else:
        # 連れがわずかなので報酬をアップ
        reward *= 2.0

    # 直近のwaypointを繋ぐ向きの差分を取る
    direction_diff = abs(delta)

    # waypointに沿った傾きと大きく乖離している場合は
    # ペナルティを課す
    DIRECTION_THRESHOLD = 20.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # 報酬を返却
    return reward
