
# Xnode AI Agent Operating System Prototype

This project is a prototype for an Agent Operating System (Agent-OS) designed to enable collaboration between vertical AI agents in an enterprise setting.

## Project Structure

```
Xnode-Agent-OS/
├── src/
│   ├── agents/                 # AI agents (Data Analysis, Workflow Automation, Reinforcement Agent)
│   ├── core/                   # Message bus and base classes
│   ├── dashboard/              # Agent performance monitoring
│   ├── ml/                     # Machine learning training and model
│   ├── utils/                  # Shared utilities
│   └── main.py                 # Entry point for the Agent OS
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Features Implemented

### 1. System Architecture
- Modular codebase supporting multiple AI agents with isolated responsibilities.
- MessageBus enables message-based inter-agent communication.

### 2. Agent Development
- DataAnalysisAgent: Performs linear regression using a trained ML model.
- WorkflowAutomationAgent: Logs and responds to workflow events.
- ReinforcementLearningAgent: Optional bonus agent using Q-learning to simulate learning behavior.

### 3. Machine Learning Integration
- A trained regression model (model.pkl) is integrated into DataAnalysisAgent.
- Model is dynamically loaded and updated using new input.

### 4. Performance Monitoring
- Dashboard prints key metrics including agent activity, task duration, and success.

### 5. Bonus: Reinforcement Learning
- A simple Q-learning agent that updates policy over time with simulated actions and rewards.

## Installation and Setup

```bash
# Clone the repo
git clone https://github.com/Flash-dev-sudo/Xnode-Agent-OS.git
cd Xnode-Agent-OS

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # On Windows
# or
source venv/bin/activate         # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/ml/train.py

# Run the system
python src/main.py
```

## Example Output

```
Starting Xnode Agent Operating System...
[DataAgent] -> Regression complete. Prediction: 8.00, RMSE: 0.00
[WorkflowAgent] -> Event of type 'info' logged.
Training RLAgent using Q-Learning...
Episode 1: Total Reward = 2
Episode 2: Total Reward = -1
Episode 3: Total Reward = 1
Episode 4: Total Reward = 3
Episode 5: Total Reward = 0

==== Agent Performance Report ====
Agent: DataAgent
 - task_duration: 0.0
 - success: True

Agent: WorkflowAgent
 - task_duration: 0.0
 - success: True

Agent: RLAgent
 - trained_episodes: 5
==================================
```

## Contact

Developed by Tushar 
