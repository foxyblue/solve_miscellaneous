


class Grid:
    def __init__(self, grid_h, grid_v, add_areas=0, area_type=None):
        self.grid_h = grid_h
        self.grid_v = grid_v
        self.add_areas = add_areas
        self.area_type = area_type
        
        self.create_grid()
        
    def create_grid(self):
        self.grid = [[
            (x, y)
            for x in range(self.grid_h)]
                for y in range(self.grid_v)        
        ]

        
print Grid(10,10).grid