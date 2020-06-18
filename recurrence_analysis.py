import numpy as np

def recurrence_quantification_analysis(recurrence_matrix, minimum_diagonal_line_length, minimum_vertical_line_length, minimum_white_vertical_line_length):
    # Calculating the number of states - N
    number_of_vectors = recurrence_matrix.shape[0]
    
    # Calculating the diagonal frequency distribution - P(l)
    diagonal_frequency_distribution = np.zeros(number_of_vectors+1)
    for i in range(number_of_vectors-1, -1, -1):
        diagonal_line_length = 0
        for j in range(0, number_of_vectors-i):
            if recurrence_matrix[i+j,j] == 1:
                diagonal_line_length += 1
                if j == (number_of_vectors-i-1):
                    diagonal_frequency_distribution[diagonal_line_length] += 1.0
            else:
                if diagonal_line_length != 0:
                    diagonal_frequency_distribution[diagonal_line_length] += 1.0
                    diagonal_line_length = 0
    for k in range(1,number_of_vectors):
        diagonal_line_length = 0
        for i in range(number_of_vectors-k):
            j = i + k
            if recurrence_matrix[i,j] == 1:
                diagonal_line_length += 1
                if j == (number_of_vectors-1):
                    diagonal_frequency_distribution[diagonal_line_length] += 1.0
            else:
                if diagonal_line_length != 0:
                    diagonal_frequency_distribution[diagonal_line_length] += 1.0
                    diagonal_line_length = 0

    # Calculating the vertical frequency distribution - P(v)
    vertical_frequency_distribution = np.zeros(number_of_vectors+1)
    for i in range(number_of_vectors):
        vertical_line_length = 0
        for j in range(number_of_vectors):
            if recurrence_matrix[i,j] == 1:
                vertical_line_length += 1
                if j == (number_of_vectors-1):
                    vertical_frequency_distribution[vertical_line_length] += 1.0
            else:
                if vertical_line_length != 0:
                    vertical_frequency_distribution[vertical_line_length] += 1.0
                    vertical_line_length = 0

    # Calculating the white vertical frequency distribution - P(w)
    white_vertical_frequency_distribution = np.zeros(number_of_vectors+1)
    for i in range(number_of_vectors):
        white_vertical_line_length = 0
        for j in range(number_of_vectors):
            if recurrence_matrix[i,j] == 0:
                white_vertical_line_length += 1
                if j == (number_of_vectors-1):
                    white_vertical_frequency_distribution[white_vertical_line_length] += 1.0
            else:
                if white_vertical_line_length != 0:
                    white_vertical_frequency_distribution[white_vertical_line_length] += 1.0
                    white_vertical_line_length = 0

    # Calculating the recurrence rate - RR
    recurrence_rate = np.float(np.sum(recurrence_matrix))/np.power(number_of_vectors, 2)

    # Calculating the determinism - DET
    numerator = np.sum([l * diagonal_frequency_distribution[l] for l in range(minimum_diagonal_line_length, number_of_vectors)])
    denominator = np.sum([l * diagonal_frequency_distribution[l] for l in range(1, number_of_vectors)])
    determinism = numerator / denominator

    # Calculating the average diagonal line length - L
    numerator = np.sum([l * diagonal_frequency_distribution[l] for l in range(minimum_diagonal_line_length, number_of_vectors)])
    denominator = np.sum([diagonal_frequency_distribution[l] for l in range(minimum_diagonal_line_length, number_of_vectors)])
    average_diagonal_line_length = numerator / denominator

    # Calculating the longest diagonal line length - Lmax
    for l in range(number_of_vectors-1, 0, -1):
        if diagonal_frequency_distribution[l] != 0:
            longest_diagonal_line_length = l
            break

    # Calculating the  divergence - DIV
    divergence = 1. / longest_diagonal_line_length

    # Calculating the entropy diagonal lines - Lentr
    sum_diagonal_frequency_distribution = np.float(np.sum(diagonal_frequency_distribution[minimum_diagonal_line_length:-1]))
    entropy_diagonal_lines = 0
    for l in range(minimum_diagonal_line_length, number_of_vectors):
        if diagonal_frequency_distribution[l] != 0:
            entropy_diagonal_lines +=  (diagonal_frequency_distribution[l]/sum_diagonal_frequency_distribution) * np.log(diagonal_frequency_distribution[l]/sum_diagonal_frequency_distribution)
    entropy_diagonal_lines *= -1

    # Calculating the ratio determinism_recurrence - DET/RR
    ratio_determinism_recurrence_rate = determinism / recurrence_rate

    # Calculating the laminarity - LAM
    numerator = np.sum([v * vertical_frequency_distribution[v] for v in range(minimum_vertical_line_length, number_of_vectors+1)])
    denominator = np.sum([v * vertical_frequency_distribution[v] for v in range(1, number_of_vectors+1)])
    laminarity = numerator / denominator

    # Calculating the average vertical line length - V
    numerator = np.sum([v * vertical_frequency_distribution[v] for v in range(minimum_vertical_line_length, number_of_vectors+1)])
    denominator = np.sum([vertical_frequency_distribution[v] for v in range(minimum_vertical_line_length, number_of_vectors+1)])
    average_vertical_line_length = numerator / denominator

    # Calculating the longest vertical line length - Vmax
    for v in range(number_of_vectors, 0, -1):
        if vertical_frequency_distribution[v] != 0:
            longest_vertical_line_length = v
            break

    # Calculating the entropy vertical lines - Ventr
    sum_vertical_frequency_distribution = np.float(np.sum(vertical_frequency_distribution[minimum_vertical_line_length:]))
    entropy_vertical_lines = 0
    for v in range(minimum_vertical_line_length, number_of_vectors+1):
        if vertical_frequency_distribution[v] != 0:
            entropy_vertical_lines +=  (vertical_frequency_distribution[v]/sum_vertical_frequency_distribution) * np.log(vertical_frequency_distribution[v]/sum_vertical_frequency_distribution)
    entropy_vertical_lines *= -1

    # Calculatint the ratio laminarity_determinism - LAM/DET
    ratio_laminarity_determinism = laminarity / determinism

    # Calculating the average white vertical line length - W
    numerator = np.sum([w * white_vertical_frequency_distribution[w] for w in range(minimum_white_vertical_line_length, number_of_vectors+1)])
    denominator = np.sum([white_vertical_frequency_distribution[w] for w in range(minimum_white_vertical_line_length, number_of_vectors+1)])
    average_white_vertical_line_length = numerator / denominator

    # Calculating the longest white vertical line length - Wmax
    for w in range(number_of_vectors, 0, -1):
        if white_vertical_frequency_distribution[w] != 0:
            longest_white_vertical_line_length = w
            break

    # Calculating the entropy white vertical lines - Wentr
    sum_white_vertical_frequency_distribution = np.float(np.sum(white_vertical_frequency_distribution[minimum_white_vertical_line_length:]))
    entropy_white_vertical_lines = 0
    for w in range(minimum_white_vertical_line_length, number_of_vectors+1):
        if white_vertical_frequency_distribution[w] != 0:
            entropy_white_vertical_lines +=  (white_vertical_frequency_distribution[w]/sum_white_vertical_frequency_distribution) * np.log(white_vertical_frequency_distribution[w]/sum_white_vertical_frequency_distribution)
    entropy_white_vertical_lines *= -1

    return diagonal_frequency_distribution, vertical_frequency_distribution, white_vertical_frequency_distribution, recurrence_rate, determinism, average_diagonal_line_length, longest_diagonal_line_length, divergence, entropy_diagonal_lines, laminarity, average_vertical_line_length, longest_vertical_line_length, entropy_vertical_lines, average_white_vertical_line_length, longest_white_vertical_line_length, entropy_white_vertical_lines, ratio_determinism_recurrence_rate, ratio_laminarity_determinism
