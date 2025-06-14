class WorkflowAutomationAgent:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus
        self.rules = {
            "send_email": self.send_email,
            "log_event": self.log_event,
            "escalate_issue": self.escalate_issue,
        }

    def handle_event(self, event):
        action = event.get("action")
        if action in self.rules:
            return self.rules[action](event.get("payload"))
        return f"Unknown action: {action}"

    def send_email(self, payload):
        recipient = payload.get("recipient")
        subject = payload.get("subject")
        return f"Email sent to {recipient} with subject: '{subject}'"

    def log_event(self, payload):
        event_type = payload.get("type")
        return f"Event of type '{event_type}' logged."

    def escalate_issue(self, payload):
        issue_id = payload.get("id")
        return f"Issue {issue_id} escalated to supervisor."
