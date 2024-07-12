
def time_conversion_before_reaching_top(vel, kick_height_from_bh):
    t = kick_height_from_bh / vel
    return t

def time_conversion_after_reaching_top(t, vel, cal_f_depth_between):
    t_2 = t + cal_f_depth_between/vel
    return t_2
