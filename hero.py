class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBlind()
        self.accept_events()
    def cameraBlind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True
    def cameraPu(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def accept_events(self):
        base.accept( 'c', self.changeView)
        base.accept("n", self.turn_left)
        base.accept("n"+"-repeat", self.turn_left)
        base.accept("B", self.turn_right)
        base.accept("B"+"-repeat", self.turn_right)
    def changeView(self):
        if self.cameraOn:
            self.cameraPu()
        else:
            self.cameraBlind()
    
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    
    def 

