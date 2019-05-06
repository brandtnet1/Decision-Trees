# Starter file for subset sum problem

# Add your own fitness function and verify that it solves the five
# randomly generated trials

import random

from deap import base
from deap import creator
from deap import tools

#----------
# Global setup
#----------

# Choose FitnessMax or FitnessMin on the third line based on the design
# of your fitness function: do you want to solve for the individual that
# maximizes a certain score, or the one that minimizes it?

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator 
#                      define 'attr_bool' to be an attribute ('gene')
#                      which corresponds to integers sampled uniformly
#                      from the range [0,1] (i.e. 0 or 1 with equal
#                      probability)
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
#                         define 'individual' to be an individual
#                         consisting of 100 'attr_bool' elements ('genes')
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_bool, 100)

# define the population to be a list of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


#----------
# Create data for the problem
#----------
sum_target = 0
numbers = []

def create_problem_instance():
    global numbers
    global sum_target
    numbers = [random.randint(1, 100) for i in range(100)]
    sum_target = random.randint(1, 1000)


#----------
# the goal ('fitness') function to be maximized
#----------
def evalSubsetSum(individual):
    
    #--- Fill in your code to evaluate the fitness of an individual
    n = 0
    for i in range(50,100):
        n = n + individual[i]
        
    fitness = (1.0 / (1.0 + n)) * 100.0

    return fitness, # <--- need a comma after the return value

#----------
# Operator registration
#----------
# register the goal / fitness function
toolbox.register("evaluate", evalSubsetSum)

# register the crossover operator
toolbox.register("mate", tools.cxTwoPoint)

# register a mutation operator with a probability to
# flip each attribute/gene of 0.05
toolbox.register("mutate", tools.mutFlipBit, indpb=0.01)

# operator for selecting individuals for breeding the next
# generation: each individual of the current generation
# is replaced by the 'fittest' (best) of three individuals
# drawn randomly from the current generation.
toolbox.register("select", tools.selTournament, tournsize=3)

#----------

def main():
    # Create an initial population of 300 individuals
    # Each individual is a binary vector
    pop = toolbox.population(n=300)

    # CXPB  is the probability with which two individuals
    #       are crossed
    #
    # MUTPB is the probability for mutating an individual
    #
    # NGEN  is the number of generations for which the
    #       evolution runs
    CXPB, MUTPB, NGEN = 1.0, 1.0, 40
    
    print("Start of evolution")
    
    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
    
    print("  Evaluated %i individuals" % len(pop))
    
    # Begin the evolution
    for g in range(NGEN):
        print("-- Generation %i --" % g)
        
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
    
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):

            # cross two individuals with probability CXPB
            if random.random() < CXPB:
                toolbox.mate(child1, child2)

                # fitness values of the children
                # must be recalculated later
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:

            # mutate an individual with probability MUTPB
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values
    
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        print("  Evaluated %i individuals" % len(invalid_ind))
        
        # The population is entirely replaced by the offspring
        pop[:] = offspring
        
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    
    print("-- End of (successful) evolution --")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))
    
    # Print numbers in the sum defined by the best individual and validate
    # its result
    print ''
    result = [numbers[i] for i in range(len(best_ind)) if best_ind[i] == 1]
    print 'Target = %d' % sum_target
    print 'Numbers in best individual =', result
    print 'Sum of best individual = %d' % sum(result)
    print ''


#----------
# Main
#----------
if __name__ == "__main__":
    random.seed(0)
    
    for i in range(5):
        create_problem_instance()
        main()
