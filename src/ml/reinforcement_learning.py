import random
import numpy as np

class ReinforcementLearningAgent:
    def __init__(self, name="RLAgent", states=5, actions=3):
        self.name = name
        self.states = states
        self.actions = actions
        self.q_table = np.zeros((states, actions))
        self.alpha = 0.1       # learning rate
        self.gamma = 0.95      # discount factor
        self.epsilon = 0.2     # exploration rate
        self.training_log = []

    def train(self, episodes=5):
        print(f"\nTraining {self.name} using Q-Learning...\n")
        for episode in range(episodes):
            state = random.randint(0, self.states - 1)
            total_reward = 0

            for _ in range(5):  # steps per episode
                if random.random() < self.epsilon:
                    action = random.randint(0, self.actions - 1)
                else:
                    action = np.argmax(self.q_table[state])

                next_state = random.randint(0, self.states - 1)
                reward = random.choice([-1, 0, 1])
                total_reward += reward

                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])

                # Q-learning formula
                new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
                self.q_table[state, action] = new_value

                state = next_state

            print(f"Episode {episode+1}: Total Reward = {total_reward}")
            self.training_log.append(total_reward)
