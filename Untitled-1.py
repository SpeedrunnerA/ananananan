from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmaager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = self.loader.loadModel('Boeing707.egg')
        self.texture = self.loader.loadTexture('BoeingTexture.tif')
        self.model.reparentTo(self.render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
game = Game()
game.run()