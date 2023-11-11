class SupportAgent:
    def __init__(self, specialty, next_agent=None):
        self.specialty = specialty
        self.next_agent = next_agent

    def handle_issue(self, issue_type, issue_details):
        if issue_type == self.specialty:
            # handle the issue
            print(f"Handled {issue_type} issue by {self.specialty} specialist")
        elif self.next_agent:
            self.next_agent.handle_issue(issue_type, issue_details)
        else:
            print("Issue couldn't be handled")


if __name__ == "__main__":
    # Create a chain of agents
    payment_agent = SupportAgent("payment")
    shipping_agent = SupportAgent("shipping", payment_agent)

    # Raise an issue
    shipping_agent.handle_issue("payment", "Payment declined")
