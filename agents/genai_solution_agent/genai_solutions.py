import yaml

class GenAISolutionAgent:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def propose_genai_solutions(self, use_case):
        if use_case == "Supply Chain Optimization":
            return ["AI-powered demand forecasting", "Real-time inventory optimization"]
        elif use_case == "Predictive Maintenance":
            return ["Predictive analytics for equipment failure", "Automated maintenance scheduling"]
        elif use_case == "Workforce Training":
            return ["Virtual training assistants", "Automated knowledge base suggestions"]
        return []
