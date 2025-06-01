from Board_init.board_init import Board
from Search.search import Search
import time
import psutil
import os

def print_memory_usage():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1024 / 1024 
    print(f"Memory usage: {mem:.2f} MB")

def run():
    size: int = 20
    if size <= 0:
        print("Size must be a positive integer.")
        return
    print_memory_usage()
    print(f"=== Solving {size}-Queens Problem ===\n")
    
    # DFS
    print("Running DFS...")
    print_memory_usage()
    board = Board(size)
    start = time.perf_counter()
    found = Search.solve_nqueens_dfs(board, 0)
    end = time.perf_counter()
    print_memory_usage()
    if found:
        positions = [(q.row, q.col) for q in board.queens]
        print(f"DFS solved. Depth: {len(positions)}")
        print(f"Queens positions: {positions}")
    else:
        print("DFS found no solution.")
    print(f"DFS Time: {end - start:.6f} sec\n")
    print_memory_usage()

    # Hill Climbing
    print("Running Hill Climbing...")
    print_memory_usage()
    start = time.perf_counter()
    hc_result = Search.hill_climbing(size)
    end = time.perf_counter()
    print_memory_usage()
    if hc_result:
        positions = [(row, col) for row, col in enumerate(hc_result)]
        print(f"Hill Climbing solved. Depth: {len(hc_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Hill Climbing found no solution.")
    print(f"Hill Climbing Time: {end - start:.6f} sec\n")
    print_memory_usage()

    # Simulated Annealing
    print("Running Simulated Annealing...")
    print_memory_usage()
    start = time.perf_counter()
    sa_result = Search.simulated_annealing(size)
    end = time.perf_counter()
    print_memory_usage()
    if sa_result:
        positions = [(row, col) for row, col in enumerate(sa_result)]
        print(f"Simulated Annealing solved. Depth: {len(sa_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Simulated Annealing found no solution.")
    print(f"Simulated Annealing Time: {end - start:.6f} sec\n")
    print_memory_usage()

    # Genetic Algorithm
    print("Running Genetic Algorithm...")
    print_memory_usage()
    start = time.perf_counter()
    ga_result = Search.genetic_algorithm(size, population_size=100, generations=1000)
    if ga_result is None:
        ga_result = Search.genetic_algorithm(size, population_size=50, generations=500)  # Retry with smaller params
    end = time.perf_counter()
    print_memory_usage()
    if ga_result:
        positions = [(row, col) for row, col in enumerate(ga_result)]
        print(f"Genetic Algorithm solved. Depth: {len(ga_result)}")
        print(f"Queens positions: {positions}")
    else:
        print("Genetic Algorithm found no solution.")
    print(f"Genetic Algorithm Time: {end - start:.6f} sec\n")
    print_memory_usage()

    print("=== Done ===")

if __name__ == "__main__":
    run()
