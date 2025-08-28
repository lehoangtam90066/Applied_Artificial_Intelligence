import sys
import io
from simpleai.search import CspProblem, backtrack, min_conflicts, \
    MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, \
    LEAST_CONSTRAINING_VALUE
    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


variables = {'A', 'B', 'C', 'D', 'E'}


domains = {
    'A': [1, 2, 3, 4],
    'B': [1, 2, 4],
    'C': [1, 3, 4],
    'D': [1, 2, 3, 4],
    'E': [1, 2, 3, 4],
}


def constraint_equality(variables, values):
    return values[0] == values[1]

def constraint_difference(variables, values):
    return values[0] != values[1]

def constraint_less_than(variables, values):
    return values[0] < values[1]


constraints = [
    (('A', 'B'), constraint_difference),
    (('A', 'D'), constraint_equality),
    (('E', 'A'), constraint_less_than),
    (('E', 'C'), constraint_difference),
    (('B', 'C'), constraint_difference),
    (('C', 'D'), constraint_less_than),
    (('E', 'C'), constraint_less_than),
]


if __name__ == '__main__':
    
    problem = CspProblem(variables, domains, constraints)

    print('\nSolutions: \n', backtrack(problem))
    print('\nGiải pháp bình thường: ', backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))
    print('\nGiải pháp có bậc cao nhất: ', backtrack(problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))
    print('\nGiải pháp với giá trị ràng buộc thấp nhất: ', backtrack(problem, variable_heuristic=LEAST_CONSTRAINING_VALUE))
