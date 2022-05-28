import simpy
import random

# Define the number of penalties to be taken by each team.
NUM_PENALTIES = 5

def penalty_simulation(env, team):
    """Simulate a penalty shootout between Real Madrid and Liverpool FC."""

    num_penalties_scored = 0

    # Simulate the penalty shootout.
    for i in range(NUM_PENALTIES):
        #print('+' * 25)  # Print the number of penalties taken by the team in this simulation to the console window.
        
        penalty_probability = random.random()

        save_probability = random.random()

        # Generate a random number between 0 and 1. If it is less than p, then the penalty is scored. Otherwise, it is missed.
        if save_probability < penalty_probability:

            # Increment the number of penalties scored by this team by 1.
            num_penalties_scored += 1

            #print('%s scores!' % team)

        #else:

            #print('%s misses!' % team)
        

        #print(f"penalty probability: {penalty_probability}")
        #print(f"save probability: {save_probability}")

        yield env.timeout(1)  # Wait for 1 time unit before taking the next penalty.


        

    return num_penalties_scored  # Return the number of penalties scored by this team in this simulation.


def main(number_of_simulations):

    # Create an environment to simulate the penalty shootout in.
    env = simpy.Environment()

    liverpool_wins = 0
    real_madrid_wins = 0

    # Create a list to store the number of penalties scored by Real Madrid in each simulation in.
    real_madrid_penalties = []

    # Create a list to store the number of penalties scored by Liverpool FC in each simulation in.
    liverpool_fc_penalties = []

    for i in range(number_of_simulations):  # Run number_of_simulations simulations of the penalty shootout between Real Madrid and Liverpool FC.

        #print('\nSimulation %d' % (i + 1))  # Print which simulation is being run at this time step to the console window.

        real_madrid = env.process(penalty_simulation(env, 'Real Madrid'))  # Simulate Real Madrid taking their penalties first in this simulation using simpy's process function and store it in real_madrid variable for later use (to get its return value).

        liverpool_fc = env.process(penalty_simulation(env, 'Liverpool FC'))  # Simulate Liverpool FC taking their penalties second in this simulation using simpy's process function and store it in liverpool_fc variable for later use (to get its return value).

        env.run()  # Run the simulation.

        real_madrid_penalties.append(real_madrid.value)  # Append the number of penalties scored by Real Madrid in this simulation to the real_madrid_penalties list.

        liverpool_fc_penalties.append(liverpool_fc.value)  # Append the number of penalties scored by Liverpool FC in this simulation to the liverpool_fc_penalties list.

        #print('Real Madrid scored %d penalties.' % real_madrid.value)  # Print the number of penalties scored by Real Madrid in this simulation to the console window.

        #print('Liverpool FC scored %d penalties.' % liverpool_fc.value)  # Print the number of penalties scored by Liverpool FC in this simulation to the console window.

        if real_madrid.value > liverpool_fc.value:
            real_madrid_wins += 1
        elif real_madrid.value < liverpool_fc.value:
            liverpool_wins += 1
        else:
            while real_madrid.value == liverpool_fc.value:
                real_madrid = env.process(penalty_simulation(env, 'Real Madrid'))
                liverpool_fc = env.process(penalty_simulation(env, 'Liverpool FC'))
                env.run()
                if real_madrid.value > liverpool_fc.value:
                    real_madrid_wins += 1
                    break
                elif real_madrid.value < liverpool_fc.value:
                    liverpool_wins += 1
                    break

    # Calculate the probability of Real Madrid winning the penalty shootout against Liverpool FC in each simulation.
    real_madrid_win_probability = (real_madrid_wins / number_of_simulations) * 100

    # Calculate the probability of Liverpool FC winning the penalty shootout against Real Madrid in each simulation.
    liverpool_fc_win_probability = (liverpool_wins / number_of_simulations) * 100


    #print('\nProbability of Liverpool winning: %.2f%%' % liverpool_fc_win_probability)
    #print('Shootouts won by Liverpool: %d' % liverpool_wins)

    #print('\nProbability of Real Madrid winning: %.2f%%' % real_madrid_win_probability)  # Print the probability of Real Madrid winning the penalty shootout against Liverpool FC over all simulations to the console window.
    #print('Shootouts won by Real Madrid: %d' % real_madrid_wins)

    #print('\nProbability of a draw: %.2f%%' % draw_probability)  # Print the probability of a draw between Real Madrid and Liverpool FC over all simulations to the console window.
    #print('Shootouts that would go into extra rounds: %d' % draws)

    return [[liverpool_wins,liverpool_fc_win_probability],  [real_madrid_wins, real_madrid_win_probability]]


if __name__ == '__main__':
    main()