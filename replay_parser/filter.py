import math
class player:
    def __init__(self, name_, id_):
        # updated 
        self.id   = id_
        self.name = name_
        self.clan = ""

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

        
        self.kapas_cv_score = 0
        self.accuracy_score = 0
        self.eff_accuracy_score = 0

    def update(self, avg, xp, 
               shots, hits, pens, assist, 
               hits_recv, pens_recv, nonpens_recv,
               dmg_enemies, dmg_destroyed, clan):
        self.clan = clan
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

    def refresh(self):
        self.kapas_cv_score = self.kapas_cv_number()
        self.accuracy_score = self.accuracy()
        self.eff_accuracy_score = self.eff_accuracy()

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
        return self.avg * 0.5 + self.xp * 0.1 +  self.assist * 0.1 + 2 * self.eff_accuracy() + self.accuracy(); 
  
    def pretty(self):
        pass


class player_list:
    def __init__(self):
        self.names = []
        self.players = []

    def players_count(self):
        return len(self.names)
    
    def is_in(self, name):
        return (name in self.names)

    def refresh_players(self):
        for player in self.players:
            player.refresh()
    
    def collision(self):
        with open("players.txt", "w") as fp:    
            for player in self.players:
                fp.write(f"{player.name: <25}{player.battles: <25}{math.trunc(player.avg): <25}"
                         f"{math.trunc(player.position_eff()): <25}{math.trunc(player.blocking_ratio()): <25}"
                         f"{player.shots: <25}{player.hits: <25}{player.pens: <25}"
                         f"{math.trunc(player.accuracy()): <25}{math.trunc(player.eff_accuracy()): <25}{math.trunc(player.kapas_cv_number()): <25}\n") 
                # "{player.position_eff(): >5}{player.blocking_ratio(): >4}{player.kapas_cv_number(): >6}{player.accuracy(): >5}{player.eff_accuracy(): >5}{player.assist: > 5}\n")
            #if player.battles > 1:
            #    print(f"{player.name} : {player.battles} ")

                

    def push_player(self, player):
        if not self.is_in(player.name):
            self.names.append(player.name)
            self.players.append(player)

    def update(self, protomsg):
        for player_iter in protomsg.players:
            if not self.is_in(player_iter.name_and_clan.name):
                # convert structure into player class
                temp_player_class = player(player_iter.name_and_clan.name, player_iter.player_id)

                for results_x in protomsg.players_result:
                    if results_x.results.player_id == player_iter.player_id:
                        results_x = results_x.results
                        temp_player_class.update(
                            results_x.damage, 
                            results_x.xp,
                            results_x.shots,
                            results_x.hits,
                            results_x.penetrations,
                            results_x.assist,
                            results_x.hit_received,
                            results_x.pens_received,
                            results_x.non_pen_received,
                            results_x.damaged_enemies,
                            results_x.damaged_destroyed,
                            player_iter.name_and_clan.clan
                            )

                self.push_player(temp_player_class)
            else: 
                for x in self.players:
                    if x.name == player_iter.name_and_clan.name:
                        for results_x in protomsg.players_result:
                           if results_x.results.player_id == player_iter.player_id:
                             results_x = results_x.results
                             x.update(
                             results_x.damage, 
                             results_x.xp,
                             results_x.shots,
                             results_x.hits,
                             results_x.penetrations,
                             results_x.assist,
                             results_x.hit_received,
                             results_x.pens_received,
                             results_x.non_pen_received,
                             results_x.damaged_enemies,
                             results_x.damaged_destroyed,
                             player_iter.name_and_clan.clan,
                             )

                # push it 
        pass

    def list(self):
        print("* Players list: ")
        i = 1
        for name in self.names:
            print(f"{i}-{name}")
            i += 1




