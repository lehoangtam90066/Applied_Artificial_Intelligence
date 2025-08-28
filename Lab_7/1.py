from simpleai.search import CspProblem, backtrack
class CSPBacktrackingSolver:
    def __init__(self):
        self.variables = ["C1", "C2", "C3", "C4", "C5"]
        self.domains = {
            'C1': ['C'],
            'C2': ['B', 'C'],
            'C3': ['A', 'B', 'C'],
            'C4': ['A', 'B', 'C'],
            'C5': ['B', 'C']
        }
        self.constraints = self.create_constraints()
    @staticmethod
    def constraint_difference(variables, values):
        return values[0] != values[1]
    def create_constraints(self):
        return [
            (('C1', 'C2'), self.constraint_difference),
            (('C2', 'C3'), self.constraint_difference),
            (('C3', 'C4'), self.constraint_difference),
            (('C4', 'C5'), self.constraint_difference),
            (('C2', 'C4'), self.constraint_difference),
            (('C3', 'C5'), self.constraint_difference)
        ]
    def solve(self):
        problem = CspProblem(self.variables, self.domains, self.constraints)
        return backtrack(problem)
if __name__ == '__main__':
    solver = CSPBacktrackingSolver()
    solution = solver.solve()
    print("Kết quả là:", solution)