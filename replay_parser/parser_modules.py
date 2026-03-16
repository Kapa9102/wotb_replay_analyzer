import os
from .filter import player, player_list
from . import battle_rep_pb2
from termcolor import colored

DEBUG_PREFIX = "parser/parser: "
DEF_DIR_NAME = "replays_loaded"
DEFAULT_UNZIP_NAME = "battle_results.dat"

class parser_manager:
    # directory is the deflation one
    def __init__(self, dirname):
        if os.path.isdir(dirname):
            print(colored("[1]", 'green'), "Found protobuf raw directory!")
            self.dirname = dirname
        else: 
            print(colored("[0]", 'red'), DEBUG_PREFIX + "cannot initialize parser manager, no such file or dir")
            self.dirname = ""
        

    # read all the files and store them into the player list structure
    def parse(self):
        total_result = player_list()
        
        for file in os.listdir(self.dirname):
            current_result = self.fetch(file);
            total_result.update(current_result)
            # for player in current_result.players:
                
            # total_result.update(current_result);
        total_result.collision()


    # extracts all the replay data from the file
    def fetch(self, filename):

        proto_main = battle_rep_pb2.main()

        # read binary data from the file
        try:
            print(colored("[1]", 'green'), f"Reading {filename}!")
            with open(DEF_DIR_NAME + '/' + filename, "rb") as bin_ref:
                raw = bin_ref.read()

        except Exception as E:
            print(colored("[0]", 'red'), DEBUG_PREFIX + f"Can't read {filename}!")
            pass
        
        # convert the binary data into proto message

        try:
            proto_main.ParseFromString(raw)
        except Exception as E:
            print(colored("[0]", 'red'), DEBUG_PREFIX + f"Can't convert binary {filename} to protobuf msg!")

        return proto_main
            


    


    # read all the files
    # - detect the directory
    # - iterate over the files
    # - parse each file indivdually receive msg from it
    # - store each msg in the player_list