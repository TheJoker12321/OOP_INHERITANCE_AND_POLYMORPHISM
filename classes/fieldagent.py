from classes.agent import Agent


class FieldAgent(Agent):
    def __init__(self, region, code_name,clearance_level):
        super().__init__(code_name, clearance_level)
        self.region = region


    def report(self):
        super().report() , print(f"region: {self.region}")

x = FieldAgent("kjhdlakjd", "akhdsfl", 5)
