def get_p_distance(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
    return diff_count / len(s1)

def get_p_distance_matrix(matrix):
    n = len(matrix)
    p_distance_matrix = []
    for i in range(n):
        row = [0.0] * n
        p_distance_matrix.append(row)
    
    for i in range(n):
        for j in range(i + 1, n):
            d = get_p_distance(matrix[i], matrix[j])
            p_distance_matrix[i][j] = p_distance_matrix[j][i] = d
    return p_distance_matrix
