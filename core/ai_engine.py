class AIAgent:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def run(self, data, mem):
        return self.fn(data, mem)

class AIMultiAgent:
    def __init__(self):
        self.agents = []
        self.memory = {}

    def register(self, a):
        self.agents.append(a)

    def broadcast(self, data):
        out = []
        for a in self.agents:
            r = a.run(data, self.memory)
            if r:
                out.append({"agent": a.name, "result": r})
        return out
