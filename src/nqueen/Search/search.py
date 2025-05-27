import heapq
from collections import deque
from copy import deepcopy
import random
from time import perf_counter
from Queen_init.queen_init import Queen
from Board_init.board_init import Board
import math
class Search:

    @staticmethod
    def solve_nqueens_dfs(board: Board, row: int) -> bool:
        if row == board.size:
            return True
        for col in range(board.size):
            if board.is_safe(row, col):
                queen = Queen(row, col, f"Q{row}")
                board.place_queen(queen)
                if Search.solve_nqueens_dfs(board, row + 1):
                    return True
                board.remove_queen(row)
        return False

    @staticmethod
    def run_dfs(size: int):
        board = Board(size)
        start_time = perf_counter()
        found = Search.solve_nqueens_dfs(board, 0)
        end_time = perf_counter()
        if found:
            print(f"DFS solved! Depth: {len(board.queens)}")
            print(f"Queens positions: {[ (q.row, q.col) for q in board.queens ]}")
        else:
            print("DFS no solution found.")
        print(f"DFS Time elapsed: {end_time - start_time:.6f} seconds\n")

    
    @staticmethod
    def hill_climbing(size: int, max_restarts: int = 1000):
        def compute_conflicts(positions):
            conflicts = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if positions[i] == positions[j] or abs(positions[i] - positions[j]) == j - i:
                        conflicts += 1
            return conflicts

        def get_neighbors(state):
            neighbors = []
            for row in range(size):
                for col in range(size):
                    if col != state[row]:
                        new_state = state[:]
                        new_state[row] = col
                        neighbors.append(new_state)
            return neighbors

        for _ in range(max_restarts):
            state = [random.randint(0, size - 1) for _ in range(size)]
            while True:
                current_conflicts = compute_conflicts(state)
                if current_conflicts == 0:
                    return state
                neighbors = get_neighbors(state)
                neighbor_conflicts = [compute_conflicts(n) for n in neighbors]
                min_conflicts = min(neighbor_conflicts)
                if min_conflicts >= current_conflicts:
                    break 
                min_index = neighbor_conflicts.index(min_conflicts)
                state = neighbors[min_index]
        return None
    
    @staticmethod
    def simulated_annealing(size: int, max_steps: int = 10000, temperature: float = 100.0, cooling_rate: float = 0.99):
        def compute_conflicts(state):
            conflicts = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                        conflicts += 1
            return conflicts

        state = [random.randint(0, size - 1) for _ in range(size)]
        current_conflicts = compute_conflicts(state)

        for step in range(max_steps):
            if current_conflicts == 0:
                return state
            row = random.randint(0, size - 1)
            new_col = random.randint(0, size - 1)
            new_state = state[:]
            new_state[row] = new_col
            new_conflicts = compute_conflicts(new_state)
            delta = new_conflicts - current_conflicts

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                state = new_state
                current_conflicts = new_conflicts

            temperature *= cooling_rate

        return None
    
    @staticmethod
    def genetic_algorithm(size: int, population_size: int = 100, generations: int = 1000, mutation_rate: float = 0.03):
        def compute_fitness(state):
            max_pairs = size * (size - 1) // 2
            conflicts = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                        conflicts += 1
            return max_pairs - conflicts

        def crossover(parent1, parent2):
            point = random.randint(1, size - 2)
            child = parent1[:point] + parent2[point:]
            return child

        def mutate(state):
            if random.random() < mutation_rate:
                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1)
                state[row] = col
            return state

        population = [[random.randint(0, size - 1) for _ in range(size)] for _ in range(population_size)]
        for _ in range(generations):
            population.sort(key=lambda s: -compute_fitness(s))
            if compute_fitness(population[0]) == size * (size - 1) // 2:
                return population[0]
            new_population = population[:10]  # elitism
            while len(new_population) < population_size:
                parent1, parent2 = random.choices(population[:50], k=2)
                child = mutate(crossover(parent1, parent2))
                new_population.append(child)
            population = new_population
        return None