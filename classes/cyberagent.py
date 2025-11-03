from classes.agent import Agent



class CyberAgent(Agent):
    def __init__(self, specialty, code_name,clearance_level):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty



    def report(self):
        super().report() ,print(f"specialty: {self.specialty}")


