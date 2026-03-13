from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Electronics():
    """Electronics crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def preference_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['preference_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def market_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_agent'], # type: ignore[index]
            verbose=True
        )
    @agent
    def review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['review_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['recommendation_agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analyze_preferences(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_preferences'], # type: ignore[index]
            output_file='analysis.md'
        )

    @task
    def market_research(self) -> Task:
        return Task(
            config=self.tasks_config['market_research'], # type: ignore[index]
            output_file='market_research.md'
        )
    @task
    def review_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['review_analysis'], # type: ignore[index]
            output_file='review_analysis.md'
        )

    @task
    def final_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['final_recommendation'], # type: ignore[index]
            output_file='final_recommendation.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Electronics crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
