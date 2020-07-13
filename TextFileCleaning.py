import pandas as pd

from collections import defaultdict

state_town_dict = defaultdict(list)
state_town_tuple_list = []

state_town_tuple_list = []
with open("university_towns.txt") as fref:
    for line in fref:
        lineWithoutSquare = line.split("[")[0].strip()
        if ":" in lineWithoutSquare and not ("(") in lineWithoutSquare:
            continue
        else:
            if not ("(") in lineWithoutSquare:
                state = lineWithoutSquare
            else:
                univTown = (
                    lineWithoutSquare.split(" (")[0].strip().split(",")[0].strip()
                )
                state_town_dict[state].append(univTown)
                state_town_tuple_list.append((state, univTown))

state_univtown_df = pd.DataFrame(state_town_tuple_list, columns=["State", "RegionName"])
state_univtown_df

