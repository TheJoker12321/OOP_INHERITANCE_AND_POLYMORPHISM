class Agent:
    total_agents = 0
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self.__clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.__clearance_level}", end=" ")

    def get_level(self):
        return self.__clearance_level

    def set_level(self, level):
        if 1 < level < 10:
            self.__clearance_level = level
        else:
            raise AttributeError

    @staticmethod
    def print_agents(total_agents):
        print(total_agents)


def print_report(lst_agent: list[Agent]):
    for i in lst_agent:
        i.report()
