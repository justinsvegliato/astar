import anytime_astar
import astar
import n_puzzle
import utils

def main():
    problem = utils.Problem(
        n_puzzle.get_difficult_puzzle(3, 20),
        n_puzzle.is_goal,
        n_puzzle.get_successors,
        n_puzzle.get_cost,
        n_puzzle.get_heuristic
    )

    print('Solving using A*...')
    solutions = astar.solve(problem)
    print(solutions)
    print('')

    print('Solving using Anytime A*...')
    anytime_astar.solve(problem, 1.5)


if __name__ == '__main__':
    main()
