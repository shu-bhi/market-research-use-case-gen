from agents.industry_research_agent.industry_research import IndustryResearchAgent
from agents.use_case_generation_agent.use_case_generation import UseCaseGenerationAgent
from agents.resource_asset_collection_agent.resource_collection import ResourceAssetCollectionAgent
from agents.genai_solution_agent.genai_solutions import GenAISolutionAgent

import logging
import yaml

def main():
    logging.basicConfig(filename='project.log', level=logging.INFO)
    logging.info("Starting main program")

    # Step 1: Industry Research
    research_agent = IndustryResearchAgent('configs/project_config.yaml')
    industry_data = research_agent.fetch_industry_info("Example Company")
    industry, offerings = research_agent.segment_industry(industry_data)
    logging.info(f"Industry: {industry}, Offerings: {offerings}")

    # Step 2: Use Case Generation
    use_case_agent = UseCaseGenerationAgent('configs/agent_settings.yaml')
    use_cases = use_case_agent.generate_use_cases(industry, offerings)
    logging.info(f"Use Cases: {use_cases}")

    # Step 3: Resource Collection
    resource_agent = ResourceAssetCollectionAgent('configs/project_config.yaml')
    for use_case in use_cases:
        links = resource_agent.search_datasets(use_case)
        resource_agent.save_resource_links(use_case, links)
        logging.info(f"Resources for {use_case}: {links}")

    # Step 4: GenAI Solution Suggestions
    genai_agent = GenAISolutionAgent('configs/agent_settings.yaml')
    for use_case in use_cases:
        suggestions = genai_agent.propose_genai_solutions(use_case)
        logging.info(f"GenAI Solutions for {use_case}: {suggestions}")

if __name__ == "__main__":
    main()
