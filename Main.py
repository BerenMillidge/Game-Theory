#okay, so this just let's us simulate these things. idk. let's get the logic working

import numpy as np
from Agent import *
from Game import *

def run_game(game, agents, epochs, verbose = False):

    #we're going to assume 2 agents for now
    agent1 = RandomAgent(0.5,0.5)
    agent2 = RandomAgent(0.7,0.3)
    reward_table = game.reward_table
    action_table = {}
    agent1_list = []
    agent2_list = []
    for i in range(epochs):
        rand1 = np.random.uniform()
        rand2 = np.random.uniform()
        a1_action = agent1.calculate_action(rand1)
        a2_action = agent2.calculate_action(rand2)
        agent1_list.append(a1_action)
        agent2_list.append(a2_action)
        agent1.update_reward(reward_table[a1_action][a2_action][0])
        agent2.update_reward(reward_table[a1_action][a2_action][1])
        if verbose:
            print("Round: " + str(i))
            if a1_action == 0:
                print("Agent 1 Cooperates")
                print(agent1.get_reward())
            if a1_action == 1:
                print("Agent 1 Defects!")
                print(agent1.get_reward())
            if a2_action == 0:
                print("Agent 2 Cooperates")
                print(agent2.get_reward())
            if a2_action == 1:
                print("Agent 2 Defects!")
                print(agent2.get_reward())

            print("  ")
            print("  ")

    action_table['agent1'] = agent1_list
    action_table['agent2'] = agent2_list
    print("Final Rewards:")
    print("Agent 1: ") + str(agent1.get_reward())
    print("Agent 2: ") + str(agent2.get_reward())
    return agent1.get_reward(), agent2.get_reward()


rewardTable = [[(5,5),(1,5)],[(5,1),(-1,-1)]]
PrisonersDilemna = Game(reward_table=rewardTable)
r1, r2 = run_game(PrisonersDilemna, [], 100,verbose=True)


#THIS is completely irrelevant but should be fun to look at. we can test out different strategies and also figure out how you want your agent
#to perform. we should also, if interested, implement genetic algorithms for his, as that would be awesome! if only we were not doing so
#when there's a dissertation due in 20 days, and we're fuckingdoomed for it!!! SHIT! this is really going to hurt us. argh!
#fuck fuck fuck fuck fuck fuck fuck fuck fuck and then there's a deathly startup too. argh.
#okay, let's do some work on that perhaps, and then... idk


        # no, this isn't working, my thing for the reward table is just failing really badly. ugh. thisgets the agents the same
        #really, each thing entry in the reward table should be a tuple, and then we just do it by agent number. so idk
        #we shuold easily be ale to fix this, we just choose not to lol!