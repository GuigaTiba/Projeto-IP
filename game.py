class Game():
    def __init__(self, width=25, height=25):
        self.player = {
            'x': 1,
            'y': 0,
            'vert_speed': 0,
            'vert_acc': -1
        }

        self.width = width
        self.height = height


    def update(self):
        self.player_update()

    def player_update(self):
        playa = self.player
        playa['y'] = max(playa['y'] + playa['vert_speed'], 0)

        playa['vert_speed'] = playa['vert_speed'] + playa['vert_acc']

        if playa['y'] == 0 and playa['vert_speed'] < 0:
            playa['vert_speed'] = 0

    
    def player_act(self, cmd, args=None):
        if cmd == 'jump':
            self.player_jump()
        return
    
    def player_jump(self):
        playa = self.player
        if playa['y'] == 0 and playa['vert_speed'] == 0:
            playa['vert_speed'] = 4

    def player_pos(self):
        playa = self.player
        return (playa['x'], (self.height - playa['y']) - 1)