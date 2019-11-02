# -*- coding: utf-8 -*-
#
# 報酬関数例6
#
# 車の細かい動作は規定せずに
# 達成するここと、スピードが速いことを報酬とする。
#
# https://github.com/scottpletcher/deepracer/blob/master/iterations/v4-SelfMotivator.md
#
def reward_function(params):
    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
    
    return float(reward)
