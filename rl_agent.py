
import numpy as np

class ContentRecommenderAgent:
    def __init__(self, n_actions, n_states, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.n_actions = n_actions
        self.n_states = n_states
        self.q_table = np.zeros((n_states, n_actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
    
    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.n_actions)  # Exploration
        else:
            return np.argmax(self.q_table[state])  # Exploitation
    
    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state, best_next_action]
        self.q_table[state, action] += self.learning_rate * (td_target - self.q_table[state, action])

n_states = 10  
n_actions = 5  
agent = ContentRecommenderAgent(n_actions, n_states)

state = 0  
action = agent.choose_action(state)
reward = 1  
next_state = 1  
agent.update_q_value(state, action, reward, next_state)
