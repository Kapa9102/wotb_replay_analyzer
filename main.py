from fileprep.replay_loader import replay_loader
from replay_parser.filter import player, player_list
from replay_parser.parser_modules import parser_manager
from export.sorting import sorter
import csv

DEF_DIR_NAME = "replays_loaded"
DEFAULT_UNZIP_NAME = "battle_results.dat"
BEST_TO_WORST = 1
WORST_TO_BEST = 0

def main():
    file_module = replay_loader("./replays")
    file_module.start()

    file_fetcher = parser_manager(DEF_DIR_NAME);
    max_verstrappen = file_fetcher.parse()
    max_verstrappen.collision()

    # sorting module 

    sorting_module = sorter(max_verstrappen)

    # sorting_module.by_battles(order = BEST_TO_WORST)
    sorting_module.by_dmg(BEST_TO_WORST)
    sorting_module.write_csv()

    max_verstrappen.collision()

    # sorting_module.plist.collision()
    
    file_module.clean()

if __name__ == "__main__":
    main()
  










