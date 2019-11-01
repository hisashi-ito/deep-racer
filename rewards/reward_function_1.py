# -*- coding: utf-8 -*-
#
# 報酬関数例1
#
# まっすぐ走るとお得な場合
#
def reward_function(params):
    # トラックの幅
    track_width = params['track_width']
    # センターラインからの距離
    distance_from_center = params['distance_from_center']

    # センターラインからの距離に応じて報酬を設定する
    marker_1 = 0.1 * track_width
    marker_2 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    else:
        # 0.5より大きい場合はコースアウトしているので報酬は少ない
        reward = 1e-3

    # 報酬を返却
    return reward
