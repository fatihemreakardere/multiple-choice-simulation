import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_random_answers(question_amount, choices):
    answers = np.random.randint(1, choices + 1, question_amount)
    return answers

def control_test(correct_answers, given_answers):
    correct = np.array(correct_answers)
    given = np.array(given_answers)
    correct_count = np.sum(correct == given)
    wrong_count = len(correct) - correct_count
    accuracy = correct_count / len(correct) * 100
    return accuracy, correct_count, wrong_count

def create_bulk_test(correct_answers, number_of_tests, choices):
    bulk_test = []
    all_created_answers = []
    number_of_questions = len(correct_answers)
    for _ in range(number_of_tests):
        created_answers = generate_random_answers(number_of_questions, choices)
        control_test_result = control_test(correct_answers, created_answers)
        all_created_answers.append(created_answers)
        bulk_test.append(control_test_result)
    return bulk_test, all_created_answers

def results(test_results, correct_answer_point, wrong_answer_point):
    scores = []
    for i in range(len(test_results)):
        correct_answers = test_results[i][1]
        wrong_answers = test_results[i][2]
        score = correct_answers * correct_answer_point - wrong_answers * wrong_answer_point
        scores.append(score)
    return scores

tests, generated_answers = create_bulk_test([2, 1, 4, 4, 3, 4, 2, 4, 1, 3, 1, 2, 2, 3, 3], 1000000, 4)
results_list = results(tests, 1, 1/3)

# Calculate basic statistics
mean_score = np.mean(results_list)
std_score = np.std(results_list)

print(f"Mean Score: {mean_score:.5f}")
print(f"Standard Deviation: {std_score:.5f}")
print(f"Minimum Score: {min(results_list)}")
print(f"Maximum Score: {max(results_list)}")

# plotting
plt.figure(figsize=(10, 6))
# Plot histogram as density
count, bins, _ = plt.hist(results_list, bins=20, density=True, edgecolor='black', alpha=0.7)
# Fit and plot normal distribution curve
x = np.linspace(min(results_list), max(results_list), 1000)
pdf = norm.pdf(x, mean_score, std_score)
plt.plot(x, pdf, 'r', linewidth=2, label='Normal Distribution Fit')
# Plot mean line
plt.axvline(mean_score, color='k', linestyle='dashed', linewidth=1.5, label=f'Mean: {mean_score:.5f}')
plt.xlabel('Scores', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Histogram of Scores with Normal Fit', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()