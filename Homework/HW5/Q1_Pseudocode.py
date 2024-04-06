## Pseudocode

def barycentric_lagrange_interpolation(x, y, z):
    # x = array of interpolation points
    # y = array of function values at each x
    # z = array of target points 
    # p_z = barycentric lagrange interpolation
    n = length(x)
    m = length(z)
    p = np.zeros(m) #preallocate p(z)

    for j in range(length(z)):
        weighted_sum_numerator = 0
        weighted_sum_denomenator = 0
        for k in range(n):
            w = 1.0
            for i in range(n ):
                if i != k:
                    # Find w_i
                    w *= 1 / (x[k] - x[i])
            weighted_sum_numerator += w * y[k] / (z[j] - x[k])
            weighted_sum_denomenator += w / (z[j] - x[k])
        p[j] = weighted_sum_numerator / weighted_sum_denomenator

    return p

