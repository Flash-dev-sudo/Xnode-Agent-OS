import os
import sys
import time

# Ensure correct path for local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.message_bus import MessageBus
from agents.data_analysis_agent import DataAnalysisAgent
from agents.workflow_automation_agent import WorkflowAutomationAgent
from dashboard.monitor import DashboardMonitor
from ml.reinforcement_learning import ReinforcementLearningAgent

def main():
    print("Starting Xnode Agent Operating System...\n")

    # Initialize communication and monitoring
    message_bus = MessageBus()
    monitor = DashboardMonitor()

    # Initialize agents
    data_agent = DataAnalysisAgent("DataAgent", message_bus, monitor)
    workflow_agent = WorkflowAutomationAgent("WorkflowAgent", message_bus)
    rl_agent = ReinforcementLearningAgent("RLAgent")

    # Register agents
    for agent in [data_agent, workflow_agent]:
        message_bus.register(agent.name)

    # Simulated task to DataAgent
    task = {
        "type": "regression_request",
        "data": {"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]},
        "sender": "UserInterface",
        "receiver": "DataAgent"
    }
    message_bus.send(task["receiver"], task)

    # Simulated task to WorkflowAgent
    event = {
        "action": "log_event",
        "payload": {"type": "info"},
        "sender": "UserInterface",
        "receiver": "WorkflowAgent"
    }
    message_bus.send(event["receiver"], event)

    # Simulate agent message processing
    for _ in range(3):
        for agent in [data_agent, workflow_agent]:
            msg = message_bus.receive(agent.name)
            if msg:
                start_time = time.time()
                result = agent.handle_task(msg) if hasattr(agent, "handle_task") else agent.handle_event(msg)
                end_time = time.time()
                print(f"[{agent.name}] -> {result}")
                monitor.record_task(agent.name, start_time, end_time)

    # Bonus: Run reinforcement learning training
    rl_agent.train(episodes=5)
    monitor.record_custom_metric("RLAgent", "trained_episodes", 5)

    # Final performance report
    monitor.get_status([data_agent, workflow_agent, rl_agent])
    

if __name__ == "__main__":
    main()
