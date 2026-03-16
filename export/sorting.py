from replay_parser.filter import player, player_list
import matplotlib.pyplot as plt

import csv

class sorter: 
    def __init__(self, plist):
        self.plist = plist
        pass 

    def by_dmg(self, order = 1):
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.avg, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.avg, reverse=True)
            
    def by_kapas(self, order = 1):
        self.plist.refresh_players()
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.kapas_cv_score, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.kapas_cv_score, reverse=True)

    def by_accuracy(self, order = 1):
        self.plist.refresh_players()
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.accuracy_score, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.accuracy_score, reverse=True)

    def by_effaccuracy(self, order = 1):
        self.plist.refresh_players()
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.eff_accuracy_score, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.eff_accuracy_score, reverse=True)

    def by_xp(self, order = 1):
        self.plist.refresh_players()
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.xp, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.xp, reverse=True)

    def by_battles(self, order = 1):
        self.plist.refresh_players()
        if order == 0:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.battles, reverse=False)
        elif order == 1:
            self.plist.players = sorted(self.plist.players, key=lambda player: player.battles, reverse=True)

    def write_csv(self):
        field_num  = 10
        NAMES   = []
        BT      = []
        KAPAS   = []
        AVG     = []
        EFF_ACC = []
        ACC     = []
        BLCK    = []
        SHOTS   = []
        HITS    = []
        PENS    = []
        FRAGS   = []


        for player in self.plist.players:
            NAMES.append(player.name)
            BT.append(player.battles)
            KAPAS.append(int(player.kapas_cv_number()))
            AVG.append(int(player.avg))
            BLCK.append(int(player.blocking_ratio()))
            EFF_ACC.append(int(player.eff_accuracy()))
            ACC.append(int(player.accuracy()))
            SHOTS.append(int(player.shots))
            HITS.append(int(player.hits))
            PENS.append(int(player.pens))
            FRAGS.append(int(player.dmg_destroyed))

        CT = [ NAMES, BT, KAPAS, AVG, EFF_ACC, BLCK, SHOTS, HITS, PENS
                ]
        HEAD = [
                ["NAME", "BATTLES","AVG", "SHOTS", "HITS", "PENS","ACC EFF%", "ACC %", "BLOCK %", "FRAGS"],
                NAMES,
                BT, 
                AVG,
                SHOTS,
                HITS,
                PENS,
                EFF_ACC,
                ACC,
                BLCK,
                FRAGS,
                ]

        with open("data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEAD[0])
            for j in range(len(BT)):
                FD = []
                for i in range(1, field_num+1):
                    FD.append(HEAD[i][j])
                writer.writerow(FD)

        rows = list(zip(*HEAD[1:]))
        fig, ax = plt.subplots()
        ax.axis("off")

        ax.table(
            cellText=rows,
            colLabels=HEAD[0],
            loc='center'
        )
        plt.savefig("performance.png", bbox_inches="tight", dpi=300)



