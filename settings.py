# -*- coding: utf-8 -*

class Settings():
    """描述游戏的各项设置参数。"""
    
    def __init__(self):
        self.screen_width = 100
        self.screen_height = 100
        self.bg_color = (100, 255, 100)
        self.blob_num_init = 5
        self.blob_generate_rate = 1
        self.blob_explode_time = 5
        self.blob_explode_range_rate = 2
        self.blob_size_bottom = 4
        self.blob_size_top = 10
    
