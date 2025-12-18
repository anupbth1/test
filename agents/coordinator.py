from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.experimenter import ExperimenterAgent
from agents.efficiency_agent import EfficiencyAgent
from agents.critic import CriticAgent
from agents.reflector import ReflectorAgent
from agents.summarizer import SummarizerAgent

class CoordinatorAgent:
    def __init__(self, state_manager, memory):
        self.state_manager = state_manager
        self.memory = memory

        self.planner = PlannerAgent(memory)
        self.researcher = ResearcherAgent(memory)
        self.experimenter = ExperimenterAgent(memory)
        self.efficiency = EfficiencyAgent()
        self.critic = CriticAgent()
        self.reflector = ReflectorAgent()
        self.summarizer = SummarizerAgent()

    def plan(self):
        plan = self.planner.plan()
        self.state_manager.set_state("PLANNED")
        return plan
