import json

dict_topic = {
    'relative_loc': 'common/localization/relative_localization', \
    'fct_out': 'np/apps/fct_out', \
    'fct_debug_out': 'np/debug/dgb_fct', \
    'ehy_rme': 'np/apps/ehy_rme_road_outputs', \
    'ehy_tse' : 'np/apps/ehy_tse_outputs', \
    'veh_10ms': 'common/vehicle_in/vehicle_10ms', \
    'veh_50ms': 'common/vehicle_in/vehicle_50ms', \
    'dgb_aeb': 'np/debug/dgb_aeb_strtg'
}

## web html fig set
dict_fct_out_fig_set = {
    'control data: variable key data': \
        {'source_data_keys':['acc_cmd'], 'color':['red'], 'size':[1000,200], 'x_label':'t(s)', 'y_label':'None'},
    'control data: lon acc cmd': \
        {'source_data_keys':['acc_cmd'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    'control data: lon acc p': \
        {'source_data_keys':['acc_p'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    'control data: lon acc i': \
        {'source_data_keys':['acc_i'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    'control data: lon acc d': \
        {'source_data_keys':['acc_d'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    'control data: lon acc ff': \
        {'source_data_keys':['acc_ff'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    'control data: lon acc pitch': \
        {'source_data_keys':['acc_pitch'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'m/s^2'},
    # 'fct_out: lateral active': \
    #     {'source_data_keys':['LatCtrlActv'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'None'},
    # 'fct_out: target acceleration': \
    #     {'source_data_keys':['TargetAccel'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'acc(m/s^2)'},
    # 'fct_out: longitudinal active': \
    #     {'source_data_keys':['VlcReqFct'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'None'}
    # 'fct_out: heading error': \
    #     {'source_data_keys':['h'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'h(rad)'},
    # 'fct_out: heading error rate': \
    #     {'source_data_keys':['dh'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'dh(rad/s)'},
    # 'fct_out: steer of lat error': \
    #     {'source_data_keys':['steer_l'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: steer of lat error rate': \
    #     {'source_data_keys':['steer_dl'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: steer of heading error': \
    #     {'source_data_keys':['steer_h'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: steer of heading error rate': \
    #     {'source_data_keys':['steer_dh'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: steer cmd VS steer fb position': \
    #     {'source_data_keys':['steer_cmd', 'steer_fb'], 'color':['red', 'green'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: steer feedforward': \
    #     {'source_data_keys':['steer_ff'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'steer(percent)'},
    # 'fct_out: speed tracking': \
    #     {'source_data_keys':['v_ref', 'v_car'], 'color':['red', 'green'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'speed(m/s)'},
    # 'fct_out: acc openloop': \
    #     {'source_data_keys':['a_cmd', 'a_car', 'a_ref'], 'color':['red', 'green', 'blue'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'acc(m/s^2)'},
    # 'fct_out: station error': \
    #     {'source_data_keys':['s_error'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'acc(m/s^2)'},
    # 'fct_out: speed error': \
    #     {'source_data_keys':['v_error'], 'color':['red'], 'size':[500,200], 'x_label':'t(s)', 'y_label':'speed(m/s)'}
}

dict_planning_fig_set = {
    'Planning: speed': \
        {'source_data_keys':['v'], 'color': ['red'], 'size':[250,200], 'x_label': 'relative_t(s)', 'y_label':'speed(m/s)', 'x_range':[-0.5, 7.5], 'y_range':[-0.5,35]},
    'Planning: acceleration': \
        {'source_data_keys':['a'], 'color': ['red'], 'size':[250,200], 'x_label': 'relative_t(s)', 'y_label':'acc(m/s^2)', 'x_range':[-0.5, 7.5], 'y_range':[-2,2]},
    'Planning: kappa': \
        {'source_data_keys':['k'], 'color': ['red'], 'size':[250,200], 'x_label': 'relative_t(s)', 'y_label':'curvature(1/m)', 'x_range':[-0.5, 7.5], 'y_range':[-0.025,0.025]},
    'Planning: kappa rate': \
        {'source_data_keys':['dk'], 'color': ['red'], 'size':[250,200], 'x_label': 'relative_t(s)', 'y_label':'curvature rate(1/m*s)', 'x_range':[-0.5, 7.5], 'y_range':[-0.0025,0.0025]},
}

dict_main_fig_set = {
    'Top View In VCS': {'size':[1000,300], 'x_label':'x(m)', 'y_label':'y(m)'}
}
dict_sub_fig_set = {
    'Over View': {'size':[800,800], 'x_label':'x(m)', 'y_label':'y(m)'}
}
dict_planning_sl_fig_set = {
    'Planning SL': {'size':[500,400], 'x_label':'s(m)', 'y_label':'l(m)'}
}
## animation element set
layer_localization_car_set = {
    'legend_label': 'et7', 'line_color': 'red', 'fill_color': 'red', 'line_width': 0, 'alpha':0.5
    # 'line_dash': '4 4', 'line_width': 2, 'line_color': 'red', 'alpha': 0.5
}

layer_prediction_obs_set = {
    'legend_label': 'prediction_obs', 'line_color': 'blue', 'fill_color': 'blue', 'line_width': 0, 'alpha':0.5
}

layer_prediction_traj_set = {
    'line_width': 1.0, 'line_color': 'red', 'alpha': 0.5
}

layer_fusion_obs_set = {
    'legend_label': 'fusion_obs', 'line_color': 'yellow', 'fill_color': 'yellow', 'line_width': 3, 'alpha':0.5
}

layer_fusion_traj_set = {
    'line_width': 1.0, 'line_color': 'black', 'alpha': 0.5
}

layer_planing_label_set = {
    'text_alpha':0.8, 'text_color': 'red', "text_font_size": "7pt"
}

layer_planing_decision_label_set = {
    'text_alpha':0.8, 'text_color': 'red'
}

layer_planning_path_set = {
    'legend_label': 'planning_path', 'line_width': 1, 'line_color': 'red', 'alpha': 1.0
}

layer_planning_kappa_set = {
    'line_width': 1, 'line_color': 'red', 'alpha': 0.5
}

layer_planning_speed_set = {
    'line_width': 1, 'line_color': 'red', 'alpha': 0.5
}

layer_planning_acc_set = {
    'line_width': 1, 'line_color': 'red', 'alpha': 0.5
}

layer_planning_stitch_path_set = {
    'legend_label': 'planning_path', 'line_width': 1, 'line_color': '#1e271f', 'alpha': 1.0
}

layer_planning_stitch_kappa_set = {
    'line_width': 1, 'line_color': '#1e271f', 'alpha': 1.0
}

layer_planning_stitch_speed_set = {
    'line_width': 1, 'line_color': '#1e271f', 'alpha': 1.0
}

layer_planning_stitch_acc_set = {
    'line_width': 1, 'line_color': '#1e271f', 'alpha': 1.0
}

layer_planning_sl_obs_set = {
    'line_color': 'red', 'fill_color': 'blue', 'line_width': 0, 'alpha':0.3
}

layer_fct_out_cursor_set = {
    'line_dash': '4 4', 'line_color': 'red', 'alpha': 0.5
}

layer_lane_curv_set = {
    'legend_label': 'lane', 'line_width': 1, 'line_color': 'gray', 'alpha': 0.25
}

layer_road_model_poly_line_set = {
    'legend_label': 'road_model_poly', 'line_width': 1, 'line_color': 'red', 'alpha': 1.0
}

layer_road_model_point_line_set = {
    'legend_label': 'road_model_points', 'line_width': 1, 'line_color': 'yellow', 'line_dash': '4 4', 'alpha': 1.0
}

# planning trajectory frame figs
dict_planning_dynamic_fig_set = {
    'Planning: speed': \
        {'source_data_keys':['v'], 'color': ['red'], 'size':[300,200], \
            'x_label': 'relative_t(s)', 'y_label':'speed(m/s)', \
                'x_range':[-0.5, 7.5], 'y_range':[-0.5,35]},
    'Planning: acceleration': \
        {'source_data_keys':['a'], 'color': ['red'], 'size':[300,200], \
            'x_label': 'relative_t(s)', 'y_label':'acc(m/s^2)', \
                'x_range':[-0.5, 7.5], 'y_range':[-2,2]},
    'Planning: kappa': \
        {'source_data_keys':['k'], 'color': ['red'], 'size':[300,200], \
            'x_label': 'relative_t(s)', 'y_label':'curvature(1/m)', \
                'x_range':[-0.5, 7.5], 'y_range':[-0.025,0.025]},
    'Planning: kappa rate': \
        {'source_data_keys':['dk'], 'color': ['red'], 'size':[300,200], \
            'x_label': 'relative_t(s)', 'y_label':'curvature rate(1/m*s)', \
                'x_range':[-0.5, 7.5], 'y_range':[-0.0025,0.0025]},
}

dict_planning_st_fig_set = {
    'Planning ST': {'size':[600,400], 'x_label':'t(s)', 'y_label':'s(m)'}, \
    'DP_ST': {'size':[800,400], 'x_label':'t(s)', 'y_label':'s(m)'}, \
    'Spline_ST': {'size':[800,400], 'x_label':'t(s)', 'y_label':'s(m)'}
}
###