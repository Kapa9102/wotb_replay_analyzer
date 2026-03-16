from termcolor import colored
import os, os.path
import shutil
import pickle
import zipfile
# import defs.py
DEF_DIR_NAME = "replays_loaded"
DEFAULT_UNZIP_NAME = "battle_results.dat"
PREFIX_DEBUG = "filprep/replay_loader: "
class replay_loader:
    def __init__(self, dirname):
        self.dirname = dirname
        self.replays = [name for name in os.listdir(dirname) if 
                            os.path.isfile(os.path.join(dirname, name))]
        self.replays_len = len(self.replays)
    # unzip the file onto the dest
    def unzip_file_onto(self, repname, destdir):
        try: 
            with zipfile.ZipFile(repname, 'r') as zip_ref:
                zip_ref.extractall(destdir)
            print(colored('[1]', 'green'),"Extracted replay: ", repname, " successfuly!")
        except Exception as E:
            print(colored('[0]', 'red'), PREFIX_DEBUG + "Unzip_file_onto: ", E)



    # clean replay extractions after finishing extraction
    def clean_remains(self):
        GRBG = ["battle_results.dat", "meta.json", "data.wotreplay"]
        for file in GRBG:
            if os.path.exists(os.path.join(self.dirname, file)):
                os.remove(os.path.join(self.dirname, file))

    # deflate the replay of repname into destdir with index
    def deflate_replay(self, repname, destdir, index):
        self.unzip_file_onto(os.path.join(self.dirname, repname), self.dirname)

        try: 
            with open(os.path.join(self.dirname, DEFAULT_UNZIP_NAME), "rb") as pick_ref:
                protocol, raw = pickle.load(pick_ref, encoding="latin1");
            print(colored('[1]', 'green'),"Unpickled       : ", repname, " successfuly!")
        except Exception as E: 
            print(colored('[0]', 'red'), PREFIX_DEBUG + "Unpicklation error: ", E)

        NAME_INDEX = str(index + 1)  + "bh.dat";

        try:
            with open(os.path.join(destdir, NAME_INDEX), "wb") as wfd:
                wfd.write(raw.encode("latin1"))
                print(colored('[1]', 'green'),"Written replay  : ", os.path.join(destdir, NAME_INDEX) , " successfuly!")
        except Exception as E:
                print(colored('[0]', 'red'),PREFIX_DEBUG + "Cannot write replay: ", os.path.join(destdir, NAME_INDEX), E)
        print(" ")
        self.clean_remains()

    # run through all the replays and deflate them into one dir
    def deflate_replays(self):
        i = 0
        for file in self.replays: 
            if not os.path.isdir(DEF_DIR_NAME):
                os.mkdir(DEF_DIR_NAME)
            self.deflate_replay(file, DEF_DIR_NAME, i)
            i += 1

    def start(self):
        self.deflate_replays()

    def clean(self):
        if os.path.isdir(DEF_DIR_NAME):
            shutil.rmtree(DEF_DIR_NAME)
            print(colored('[1]', 'green'), PREFIX_DEBUG + "Temporary directory deleted successfuly!")
            return 
        print(colored('[0]', 'red'), PREFIX_DEBUG + "Temporary directory doesn't exist!")
