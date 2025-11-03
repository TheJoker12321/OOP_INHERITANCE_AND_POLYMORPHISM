from classes.agent import Agent


class Mission:
    def __init__(self, mission_name: str, target_location: str):
        self.assigned_agent = None
        self.mission_name = mission_name
        self.target_location = target_location
        
    def assign(self, assigned_agent: Agent):
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}")



