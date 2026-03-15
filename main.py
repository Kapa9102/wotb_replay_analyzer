from fileprep.replay_loader import replay_loader

def main():
    file_module = replay_loader("./replays")
    file_module.start()


    
    file_module.clean()

if __name__ == "__main__":
    main()












