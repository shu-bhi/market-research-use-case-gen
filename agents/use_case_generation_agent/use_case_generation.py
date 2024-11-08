import yaml

class UseCaseGenerationAgent:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def generate_use_cases(self, industry, offerings):
        if industry == "Retail":
            return ["Supply Chain Optimization", "Predictive Maintenance", "Workforce Training"]
        return ["Customer Personalization", "Operational Analytics"]
