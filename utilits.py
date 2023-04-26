import os

class Tile:
    def __init__(self, text) -> None:
        self.text = text
        self.flag = False
        
        self.create_tile()
        
        
    def create_tile(self):
        length = len(self.text)
        if self.flag:
            self.tile = [f"   ██{'█'*length}██", f"   ██{self.text}██", f"   ██{'█'*length}██"]
        else:
            self.tile = [f"     {' '*length}  ", f"     {self.text}  ", f"     {' '*length}  "]
            
    def is_flag(self, flag):
        self.flag = flag
        self.create_tile()
        
        
def draw_tile(list_tiles, num):
    result = ''
    for i in range(3):
        mask = ''
        for tile in list_tiles:
            tile.is_flag(False)
            list_tiles[num].is_flag(True)
            mask += tile.tile[i]
        result += mask + '\n'
    return result

###########################################################


list_tiles = [Tile('dsfsdfsdfsdsf'), Tile('sdgsdgsgdssgsgsdg'), Tile('fsdf')]
count = 0

while True:
    key = input()
    for i in range(len(list_tiles)):
        if (count % len(list_tiles)) == i:
            os.system('CLS')
            num = count % len(list_tiles)
            print(draw_tile(list_tiles, num))
            key = ''
    count += 1

