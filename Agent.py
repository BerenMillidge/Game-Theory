
class BaseAgent(object):
    def __init__(self, strategy, params):
        self.strategy = strategy
        self.params = params
        self.reward = 0

    def calculate_action(self, behaviour_list):
        self.strategy(behaviour_list, self.params)

    def update_reward(self, reward):
        self.reward += reward

    def get_reward(self):
        return self.reward

class RandomAgent(object):
    def __init__(self, cooperate_p, defect_p):
        self.cooperate_p = cooperate_p
        self.defect_p = defect_p
        self.reward = 0

    def calculate_action(self, p):
        #presymably insetead it's just cooperate if not defect, so it doesn't make much diff lol. that's what we'll go for atm
        #actions are 0 = cooperate, 1 = defect
        if self.cooperate_p <=p:
            return 0
        if self.cooperate_p > p:
            return 1

    def update_reward(self, reward):
        self.reward += reward

    def get_reward(self):
        return self.reward