# Accepts a list containing the round scores of all pub quiz players (no dupes)
# Determines the index of the player who won the most rounds (no dupes)
def most_rounds_won(player_breakdown) -> int:

    players_in_quiz = len(player_breakdown)
    rounds_in_quiz = len(player_breakdown[0])
    
    # Regroup (transpose/zip) the 2D list to compare more easily
    # Example: [[1, 2, 3], [4, 5, 6]] into [[1, 4], [2, 5], [3, 6]]
    round_breakdown = [
        [scores[round_num] for scores in player_breakdown] for round_num in range(rounds_in_quiz)
    ]

    counts = [0 for _ in range(players_in_quiz)]  # Used to store the rounds won per player index

    for round_scores in round_breakdown:
        # Find player index of max value for this round, and count it
        max_idx = round_scores.index(max(round_scores))
        counts[max_idx] += 1

    # Return the index with the most rounds won
    return counts.index(max(counts))


print(most_rounds_won([[5, 8, 0, 3], [4, 7, 2, 4], [9, 4, 6, 1]]))