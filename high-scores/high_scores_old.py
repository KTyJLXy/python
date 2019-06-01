def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    high_scores = []
    while (scores != [] and len(high_scores) < 4):
        high_scores = high_scores + [max(scores)]
        scores.remove(max(scores))
    return high_scores
