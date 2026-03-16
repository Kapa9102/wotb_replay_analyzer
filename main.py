from fileprep.replay_loader import replay_loader
from replay_parser.filter import player, player_list
from replay_parser.parser_modules import parser_manager
DEF_DIR_NAME = "replays_loaded"
DEFAULT_UNZIP_NAME = "battle_results.dat"

def main():
    file_module = replay_loader("./replays")
    file_module.start()

    file_fetcher = parser_manager(DEF_DIR_NAME);
    file_fetcher.parse()
    
    file_module.clean()

if __name__ == "__main__":
    main()


  










