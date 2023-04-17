import bokeh.plotting as bkp
from bokeh.plotting import ColumnDataSource
from bokeh.models import HoverTool, Slider, CustomJS, Div, WheelZoomTool, LabelSet, CrosshairTool
from bokeh.models.callbacks import CustomJS
from common.draw_base import PointsLayer, CurveLayer, CircleLayer, \
    TextLabelLayer, MultiPolygonLayer, MultiLinesLayer

def GenTopViewFigsGroup(dict_set):
    title_name = list(dict_set.keys())[0]
    x_label = list(dict_set.values())[0]['x_label']
    y_label = list(dict_set.values())[0]['y_label']
    WIDTH = list(dict_set.values())[0]['size'][0]
    HEIGHT = list(dict_set.values())[0]['size'][1]
    fig = bkp.figure(title=title_name, x_axis_label=x_label, y_axis_label=y_label, match_aspect=True, \
                width=WIDTH, height=HEIGHT)
    fig.toolbar.active_scroll = fig.select_one(WheelZoomTool)
    fig.toolbar_location = "above"
    MeasureTools(fig)
    return fig

# dict_set = {'title1': {'source_data_keys':['',''], 'color': ['red','green'], 'size':[700,200], 'x_label': 't(s)', 'y_label':'v(m/s)', 'x_range':[-0.5, 7.5], 'y_range':[-0.5,0.5]}, 'title2': {}}
def GenPlanningFigsGroupAtRelativeTime(dict_set, dict_planning_data):
    dict_planning_fig = {}
    for key_title, value in dict_set.items():
        first_source_key = value['source_data_keys'][0]
        fig = bkp.figure(title=key_title, x_axis_label=value['x_label'], y_axis_label=value['y_label'], \
            width=value['size'][0], height=value['size'][1], x_range=value['x_range'], y_range=value['y_range'])
        fig.toolbar.active_scroll = fig.select_one(WheelZoomTool)
        dict_planning_fig[key_title] = fig
    return dict_planning_fig

def GenPlanningStFigsGroup(dict_set, dict_planning_data):
    dict_planning_st_fig = {}
    for key_title, value in dict_set.items():
        fig = bkp.figure(title=key_title,
                    x_axis_label=value['x_label'],
                    y_axis_label=value['y_label'],
                    match_aspect=False,
                    width=value['size'][0],
                    height=value['size'][1],
                    x_range=[-0.5, 5.5],y_range=[0,150])
        fig.toolbar.active_scroll = fig.select_one(WheelZoomTool)
        fig.toolbar_location = "above"
      # fig.legend.click_policy = 'hide'
    #   MeasureTools(fig)
        dict_planning_st_fig[key_title] = fig
    return dict_planning_st_fig

def GenFctOutSignalFigsGroup(dict_set, dict_fct_data):
    dict_control_fig = {}
    for key_title, value in dict_set.items():
        first_source_key = value['source_data_keys'][0]
        if len(dict_fct_data[first_source_key]) > 0:
          min_y, max_y = min(dict_fct_data[first_source_key]) - 0.5, max(dict_fct_data[first_source_key]) + 0.5
        else:
          print(first_source_key + 'is empty!')
          min_y, max_y = -1, 1
        fig = bkp.figure(title=key_title, x_axis_label=value['x_label'], y_axis_label=value['y_label'], \
            plot_width=value['size'][0], plot_height=value['size'][1], y_range=[min_y, max_y])
        for data_key, data_color in zip(value['source_data_keys'], value['color']):
            data_source = ColumnDataSource(data={'r_t':dict_fct_data['r_t'], str(data_key):dict_fct_data[str(data_key)]})
            line = fig.line('r_t', str(data_key), source=data_source, color=data_color, line_width=1, alpha=0.6)
            hover = HoverTool(renderers=[line], tooltips=[(data_key, '@'+str(data_key))], mode='vline')
            fig.add_tools(hover)
            fig.toolbar.active_scroll = fig.select_one(WheelZoomTool)
            fig.toolbar_location = "above"
            # fig.legend.click_policy = 'hide'
        dict_control_fig[key_title] = fig
    return dict_control_fig

class MeasureTools:
    def __init__(self, fig):
        self.fig = fig
        line_params = {
            'legend_label': 'measure tool',
            'alpha': 0.5,
            'line_width':2,
            'line_color': 'purple'
        }
        text_params = {}
        point_params = {
            'size': 3,
            'color': 'firebrick'
        }
        self.ends = PointsLayer(fig, point_params)
        self.line = MultiLinesLayer(fig, line_params)
        self.text = TextLabelLayer(fig, text_params)
        
        self.old_xs, self.old_ys = 'xs', 'ys'
        
        
        self.old_datasource = ColumnDataSource(data={
            self.old_xs: [],
            self.old_ys: []
        })
        self.setEvent()
    
    def setEvent(self):
        
        callback = CustomJS(
            args=dict(
                line_source =self.line.data_source, 
                text_source = self.text.data_source,
                end_source = self.ends.data_source,
                old_source = self.old_datasource
            ) ,
            code="""
const x=cb_obj.x;
const y=cb_obj.y;
console.log('Tap event occurred at x-position: ' + cb_obj.x)
console.log('Tap event occurred at y-position: ' + cb_obj.y)

if(old_source.data['xs'].length == 0){
    old_source.data['xs']=[x];
    old_source.data['ys']=[y];
    
    end_source.data['pts_xs']=[x];
    end_source.data['pts_ys']=[y];
    
    line_source.data['pts_xs']=[];
    line_source.data['pts_ys']=[];
    text_source.data['pts_xs']=[];
    text_source.data['pts_ys']=[];
    text_source.data['texts']=[];
}else{
    
    // get last point
    const ox = old_source.data['xs'][0];
    const oy = old_source.data['ys'][0];
    console.log(x,y,ox,oy);

    // clear last point
    old_source.data['xs']=[];
    old_source.data['ys']=[];
    
    // put last and current point
    end_source.data['pts_xs']=[x, ox];
    end_source.data['pts_ys']=[y, oy];
    line_source.data['pts_xs']=[[x, ox]];
    line_source.data['pts_ys']=[[y, oy]];
    text_source.data['pts_xs']=[(x+ox)/2.0];
    text_source.data['pts_ys']=[(y + oy)/2.0];
    
    const dis = Math.sqrt(Math.pow(ox-x,2) + Math.pow(oy-y,2));
    text_source.data['texts']=[dis.toFixed(4)];
    
}

line_source.change.emit();
text_source.change.emit();
old_source.change.emit();
end_source.change.emit();

""")
        self.fig.js_on_event('tap', callback)