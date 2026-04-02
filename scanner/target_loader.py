def load_targets():

    targets = []

    try:
        with open("targets.txt", "r") as f:
            for line in f:
                target = line.strip()

                if target:
                    targets.append(target)

    except FileNotFoundError:
        print("targets.txt not found!")

    return targets
