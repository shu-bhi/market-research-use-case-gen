import yaml

class ResourceAssetCollectionAgent:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def search_datasets(self, use_case):
        if use_case == "Supply Chain Optimization":
            return [
                "https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company",
                "https://github.com/samirsaci/supply-chain-optimization"
            ]
        elif use_case == "Predictive Maintenance":
            return [
                "https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification",
                "https://github.com/Yi-Chen-Lin2019/Predictive-maintenance-with-machine-learning"
            ]
        return []

    def save_resource_links(self, use_case, links):
        with open(f"{use_case}_resources.txt", "w") as file:
            for link in links:
                file.write(f"{link}\n")
        print(f"Saved resources for {use_case}")
