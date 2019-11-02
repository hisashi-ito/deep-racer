# -*- coding: utf-8 -*-
#
# 報酬関数例5
#
# ステップとプロセスに関する報酬関数
#
def reward_function(params):
    # 学習で完了したステップ数
    steps = float(params['steps'])
    # 完走した割合[%]で表示されるので比率にする
    progress = float(params['progress']) / 100.0
    # ステップ最大数
    TOTAL_NUM_STEPS = 300.0
    # 報酬のDefault値
    reward = 1.0

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS):
        # 平均よりも完走率が上回っている場合
        # 報酬をブーストただし特定のタイミングでしたブーストしない
        reward += 10.0

    # 報酬を返却
    return reward
