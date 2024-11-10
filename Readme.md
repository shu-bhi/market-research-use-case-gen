 Market Research & Use Case Generation System

This project is a multi-agent architecture designed to generate relevant AI and Generative AI (GenAI) use cases for a specific company or industry. It leverages various agents to conduct market research, identify relevant industry standards, and propose GenAI use cases to improve operational efficiency and customer experience. Additionally, it gathers relevant datasets to support the proposed use cases and suggests potential AI solutions.

---

## Project Structure

```
project_directory/
├── agents/
│   ├── industry_research_agent/
│   │   ├── __init__.py
│   │   └── industry_research.py
│   ├── use_case_generation_agent/
│   │   ├── __init__.py
│   │   └── use_case_generation.py
│   ├── resource_asset_collection_agent/
│   │   ├── __init__.py
│   │   └── resource_asset_collection.py
│   └── genai_solution_agent/
│       ├── __init__.py
│       └── genai_solution.py
├── configs/
│   ├── project_config.yaml
│   ├── logging_config.yaml
│   └── agent_settings.yaml
├── datasets/
│   ├── supply_chain_optimization/
│   │   └── supply_chain_data_sample.csv
│   ├── predictive_maintenance/
│   │   └── predictive_maintenance_sample.csv
│   └── workforce_training/
│       └── workforce_training_sample.csv
└── main.py
```

### Folder Breakdown

- `agents/`: Contains the various agents responsible for different tasks:
  - **industry_research_agent**: Performs industry research to identify key areas of focus.
  - **use_case_generation_agent**: Generates relevant AI/GenAI use cases.
  - **resource_asset_collection_agent**: Collects datasets for the proposed use cases.
  - **genai_solution_agent**: Proposes GenAI solutions based on identified needs.
  
- `configs/`: Contains configuration files for project settings and logging.

- `datasets/`: Sample datasets for testing use cases.

- `main.py`: Main script to run the project and initialize agents.

---

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/market-research-use-case-gen.git
   cd market-research-use-case-gen
   ```

2. **Install Dependencies**

   Install the required packages specified in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Project Settings**

   Update the `configs/project_config.yaml` file with relevant project settings and credentials.

---

## Usage

1. **Run the Program**

   To execute the main script:

   ```bash
   python main.py
   ```

2. **Functionality**

   The program performs the following steps:

   - **Industry Research**: Gathers industry-specific information and strategic areas.
   - **Use Case Generation**: Proposes use cases based on industry trends and standards.
   - **Resource Collection**: Searches for datasets on Kaggle, GitHub, etc., and saves links to support the use cases.
   - **GenAI Solutions**: Suggests AI solutions like document search, automated reporting, and chat systems.

---

## Agents Overview

### IndustryResearchAgent

Fetches industry-specific information and identifies key focus areas to understand the company's operational context.

### UseCaseGenerationAgent

Analyzes industry standards and trends to propose relevant AI and GenAI use cases aimed at improving processes, efficiency, and customer satisfaction.

### ResourceAssetCollectionAgent

Searches for and collects relevant datasets on platforms like Kaggle and GitHub. Saves the dataset links to text files for easy reference.

### GenAISolutionAgent

Proposes AI-driven solutions for common challenges in the industry, such as document automation and customer support enhancements.

---

## Example Use Cases

| Use Case                    | Description                                                                                             | Dataset Links                                                                                                                                              |
|-----------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Supply Chain Optimization   | Enhance demand forecasting and inventory management to reduce costs and improve product availability.   | [Link](https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company), [GitHub](https://github.com/samirsaci/supply-chain-optimization) |
| Predictive Maintenance      | Predict equipment failures to optimize maintenance scheduling and reduce unplanned downtime.            | [Link](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification), [GitHub](https://github.com/Yi-Chen-Lin2019/Predictive-maintenance-with-machine-learning) |
| Workforce Training and Support | Provides personalized training and guidance for employees to improve productivity and reduce errors. | No dataset required |

---

## Configuration Files

- **project_config.yaml**: Contains global project configurations.
- **logging_config.yaml**: Specifies logging configurations.
- **agent_settings.yaml**: Manages specific agent settings for customization.