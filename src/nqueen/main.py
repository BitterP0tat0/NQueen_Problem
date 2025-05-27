from Board_init.board_init import Board
from Search.search import Search
import time


def run():
    size: int = 8
    if size <= 0:
        print("Size must be a positive integer.")
        return
    print(f"=== Solving {size}-Queens Problem ===\n")

    # DFS
    print("Running DFS...")
    board = Board(size)
    start = time.perf_counter()
    found = Search.solve_nqueens_dfs(board, 0)
    end = time.perf_counter()
    if found:
        positions = [(q.row, q.col) for q in board.queens]
        print(f"DFS solved. Depth: {len(positions)}")
        print(f"Queens positions: {positions}")
    else:
        print("DFS found no solution.")
    print(f"DFS Time: {end - start:.6f} sec\n")

    # Hill Climbing
    print("Running Hill Climbing...")
    start = time.perf_counter()
    hc_result = Search.hill_climbing(size)
    end = time.perf_counter()
    if hc_result:
        positions = [(row, col) for row, col in enumerate(hc_result)]
        print(f"Hill Climbing solved. Depth: {len(hc_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Hill Climbing found no solution.")
    print(f"Hill Climbing Time: {end - start:.6f} sec\n")

    # Simulated Annealing
    print("Running Simulated Annealing...")
    start = time.perf_counter()
    sa_result = Search.simulated_annealing(size)
    end = time.perf_counter()
    if sa_result:
        positions = [(row, col) for row, col in enumerate(sa_result)]
        print(f"Simulated Annealing solved. Depth: {len(sa_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Simulated Annealing found no solution.")
    print(f"Simulated Annealing Time: {end - start:.6f} sec\n")

    # Genetic Algorithm
    print("Running Genetic Algorithm...")
    start = time.perf_counter()
    ga_result = Search.genetic_algorithm(size, population_size=100, generations=1000)
    if ga_result is None:
        ga_result = Search.genetic_algorithm(size, population_size=50, generations=500)  # Retry with smaller params
    end = time.perf_counter()
    if ga_result:
        positions = [(row, col) for row, col in enumerate(ga_result)]
        print(f"Genetic Algorithm solved. Depth: {len(ga_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Genetic Algorithm found no solution.")
    print(f"Genetic Algorithm Time: {end - start:.6f} sec\n")

    print("=== Done ===")


if __name__ == "__main__":
    run()
