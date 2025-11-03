from classes.agent import *
from classes.cyberagent import CyberAgent
from classes.fieldagent import FieldAgent

agent1 = CyberAgent("hacker", "28765987", 7)
agent2 = FieldAgent("TelAviv", "9876549", 4)
print_report([agent1, agent2])

