import simpleai.search as ss 

class StringProblem(ss.SearchProblem):
    def set_target(self, target_string):
        self.target_string = target_string

    def actions(self, state):
        if len(state) < len(self.target_string):
            alphabets = 'abcdefghijklmnopqrstuvwxyz'
            return list(alphabets + ' ' + alphabets.upper())
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == self.target_string

    def heuristic(self, state):
        dist = sum([1 if state[i] != self.target_string[i] else 0 for i in range(len(state))])
        diff = len(self.target_string) - len(state)
        return dist + diff

if __name__ == "__main__":
    problem = StringProblem()
    problem.set_target("Artificial Intelligence")
    problem.initial_state = ""
    
    output = ss.greedy(problem)

    print('\nTarget string: Artificial Intelligence')
    print('\nPath to solution:')
    for item in output.path():
        print(item)


