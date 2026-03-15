class player:

    def __init__(self, name_, id_):
        # updated 
        self.id   = id_
        self.name = name_

        self.battles         = 0
        self.avg             = 0
        self.xp              = 0
        self.shots           = 0
        self.hits            = 0
        self.pens            = 0
        self.assist          = 0
        self.hits_recv       = 0
        self.pens_recv       = 0
        self.nonpens_recv    = 0
        self.dmg_enemies     = 0
        self.dmg_destroyed   = 0

    def update(self, battles, avg, xp, 
               shots, hits, pens, assist, 
               hits_recv, pens_recv, nonpens_recv,
               dmg_enemies, dmg_destroyed):

        self.battles += 1

        self.avg += (avg - self.avg) / self.battles
        self.xp  += (xp  - self.xp ) / self.battles
        self.assist += (assist - self.assist) / self.battles

        self.shots += shots
        self.hits  += hits
        self.pens  += pens
        self.hits_recv += hits_recv
        self.pens_recv += pens_recv
        self.nonpens_recv += nonpens_recv
        self.dmg_enemies += dmg_enemies
        self.dmg_destroyed += dmg_destroyed

    def accuracy(self):
        if self.shots == 0: 
            return 100
        else: 
            return self.hits * 100 / self.shots 

    def eff_accuracy(self):
        if self.shots == 0: 
            return 100
        else: 
            return self.pens * 100 / self.shots 

    def blocking_ratio(self):
        if self.hits_recv == 0:
            return 100
        else: 
            return self.nonpens_recv * 100 / self.hits_recv

    def position_eff(self):
        if self.hits_recv == 0:
            return 0
        else: 
            return self.nonpens_recv * 100 * (min(1, self.hits_recv * self.hits_recv  / 25)) / self.hits_recv 

    def kapas_cv_number(self):
        return self.avg * 0.4 +  self.xp * 0.01 +  self.position_eff() * 0.2 +  self.assist * 0.01 + self.eff_accuracy(); 

    def pretty(self):
        pass

