from evaluation import simulateGame
import csv

def runTestsMCTS():

    results = open("results/mcts.csv", "w", newline = "")
    writer = csv.writer(results)
    fields = ["rolllouts", "win_rate", "time_taken"]
    writer.writerow(fields)

    baseline = 500
    simulations = int(input("Enter number of simulations: "))

    for rollouts in range(100, 1000, 100):

        wins = {1:0, 2:0}
        times = {1:0, 2:0}
        nodes = {1:0, 2:0}

        for i in range(simulations):
            if i % 2 == 0:
                result, average_times, average_nodes = simulateGame(2, 2, rollouts, 1, baseline, 1)
                nodes[1], nodes[2] = nodes[1] + average_nodes[1], nodes[2] + average_nodes[2]
                times[1], times[2] = times[1] + average_times[1], times[2] + average_times[2]
                wins[result] += 1
            else:
                # swap who goes first, then swap the result back
                result, average_times, average_nodes = simulateGame(2, 2, baseline, 1, rollouts, 1)
                times[2], times[1] = times[2] + average_times[1], times[1] + average_times[2]
                nodes[2], nodes[1] = nodes[2] + average_nodes[1], nodes[1] + average_nodes[2]
                if result == 1:
                    wins[2] += 1
                else:
                    wins[1] += 1

        writer.writerow([rollouts, wins[1]/simulations, times[1]/simulations])
            

    results.close()

if __name__ == "__main__":
    runTestsMCTS()
