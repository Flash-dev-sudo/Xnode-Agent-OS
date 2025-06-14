from .metrics import MetricsCollector
import time

class DashboardMonitor:
    def __init__(self):
        self.collector = MetricsCollector()

    def record_task(self, agent_name, start_time, end_time, success=True):
        duration = round(end_time - start_time, 2)
        self.collector.record(agent_name, "task_duration", duration)
        self.collector.record(agent_name, "success", success)

    def record_custom_metric(self, agent_name, metric_name, value):
        self.collector.record(agent_name, metric_name, value)

    def get_status(self, agents):
        metrics = self.collector.get_metrics()
        print("\n==== Agent Performance Report ====")
        for agent in agents:
            name = agent.name
            print(f"\nAgent: {name}")
            if name in metrics:
                for metric, value in metrics[name].items():
                    print(f" - {metric}: {value}")
            else:
                print(" - No metrics recorded.")
        print("==================================\n")
        return metrics
