from evaluation import simulateGame
import csv

def runTestsMCTS():

    results = open("results/mcts.csv", "w", newline = "")
    writer = csv.writer(results)
    fields = ["rollouts", "win_rate", "time_taken"]
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

    import csv

def runComparisons():
    file = open("comparisons.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["depth", "rollouts", "minimax_win_rate", "avg_minimax_time", "avg_mcts_time"])

    depths = [2, 4, 6]
    rolloutSettings = [200, 400, 600, 800]
    gamesPerSetting = 50

    for d in depths:
        for r in rolloutSettings:
            times = {1: 0, 2: 0}
            wins = {1: 0, 2: 0}

            for i in range(gamesPerSetting):
                if i % 2 == 0:
                    # player 1 = minimax(d), player 2 = MCTS(r)
                    result, average_times, _ = simulateGame(1, 2, True, d, r, None)
                    times[1] += average_times[1]
                    times[2] += average_times[2]
                    wins[result] += 1
                else:
                    # swap who goes first
                    result, average_times, _ = simulateGame(2, 1, r, None, True, d)
                    times[1] += average_times[2]
                    times[2] += average_times[1]
                    wins[2 if result == 1 else 1] += 1

            writer.writerow([
                d, r,
                wins[1] / gamesPerSetting,
                times[1] / gamesPerSetting,
                times[2] / gamesPerSetting
            ])
    file.close()

if __name__ == "__main__":
    runComparisons()

    