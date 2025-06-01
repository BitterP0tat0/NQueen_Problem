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
    def simulated_annealing(size: int, max_steps: int = 200000, temperature: float = 100.0, cooling_rate: float = 0.995):
        def compute_conflicts(state):
            conflicts = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if abs(state[i] - state[j]) == abs(i - j):
                        conflicts += 1
            return conflicts

        state = list(range(size))
        random.shuffle(state)
        current_conflicts = compute_conflicts(state)
        best_state = state[:]
        best_conflicts = current_conflicts

        for step in range(max_steps):
            if current_conflicts == 0:
                return state

            i, j = random.sample(range(size), 2)
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            new_conflicts = compute_conflicts(new_state)
            delta = new_conflicts - current_conflicts

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                state = new_state
                current_conflicts = new_conflicts
                if current_conflicts < best_conflicts:
                    best_state = state[:]
                    best_conflicts = current_conflicts

            temperature *= cooling_rate

        return best_state if best_conflicts == 0 else None

        
    @staticmethod
    def genetic_algorithm(size: int, population_size: int = 300, generations: int = 3000, mutation_rate: float = 0.1):
        def compute_fitness(state):
            conflicts = 0
            for i in range(size):
                for j in range(i + 1, size):
                    if abs(state[i] - state[j]) == abs(i - j):
                        conflicts += 1
            return -conflicts

        def crossover(parent1, parent2):
            size_ = len(parent1)
            start, end = sorted(random.sample(range(size_), 2))
            child = [None] * size_
            child[start:end+1] = parent1[start:end+1]
            fill_pos = (end + 1) % size_
            p2_pos = (end + 1) % size_
            while None in child:
                if parent2[p2_pos] not in child:
                    child[fill_pos] = parent2[p2_pos]
                    fill_pos = (fill_pos + 1) % size_
                p2_pos = (p2_pos + 1) % size_
            return child

        def mutate(state):
            i, j = random.sample(range(size), 2)
            state[i], state[j] = state[j], state[i]

        population = [random.sample(range(size), size) for _ in range(population_size)]

        for _ in range(generations):
            population.sort(key=compute_fitness, reverse=True)
            best = population[0]
            if compute_fitness(best) == 0:
                return best

            elite_count = max(10, population_size // 10)
            new_population = population[:elite_count]

            while len(new_population) < population_size:
                p1, p2 = random.choices(population[:population_size//2], k=2)
                child = crossover(p1, p2)
                if random.random() < mutation_rate:
                    mutate(child)
                new_population.append(child)

            population = new_population
        best = max(population, key=compute_fitness)
        return None