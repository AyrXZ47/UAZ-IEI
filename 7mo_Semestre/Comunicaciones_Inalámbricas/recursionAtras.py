import numpy as np


def backward_recursion(gamma):
    N = gamma.shape[1]
    beta = np.zeros((4, N))
    beta[0, N - 1] = 1

    i = N - 1
    sigma_i_1 = [0, 1]
    beta[sigma_i_1[0], i - 1] = gamma[0, i]
    beta[sigma_i_1[1], i - 1] = gamma[4, i]

    i = N - 2
    sigma_i_1 = [0, 1, 2, 3]
    beta[sigma_i_1[0], i - 1] = gamma[0, N - 1] * gamma[0, i]
    beta[sigma_i_1[1], i - 1] = gamma[0, N - 1] * gamma[4, i]
    beta[sigma_i_1[2], i - 1] = gamma[4, N - 1] * gamma[9, i]
    beta[sigma_i_1[3], i - 1] = gamma[4, N - 1] * gamma[13, i]

    for i in range(N - 3, 1, -1):
        beta[sigma_i_1[0], i - 1] = beta[0, i] * gamma[0, i] + beta[2, i] * gamma[2, i]
        beta[sigma_i_1[1], i - 1] = beta[0, i] * gamma[4, i] + beta[2, i] * gamma[6, i]
        beta[sigma_i_1[2], i - 1] = beta[1, i] * gamma[9, i] + beta[3, i] * gamma[11, i]
        beta[sigma_i_1[3], i - 1] = beta[3, i] * gamma[15, i] + beta[1, i] * gamma[13, i]

    i = 1
    sigma_i_1 = [0, 2]
    beta[sigma_i_1[0], i - 1] = beta[0, i] * gamma[0, i] + beta[2, i] * gamma[2, i]
    beta[sigma_i_1[1], i - 1] = beta[1, i] * gamma[9, i] + beta[3, i] * gamma[11, i]

    i = 0
    beta_0 = beta[0, i] * gamma[0, i] + beta[2, i] * gamma[2, i]

    return beta, beta_0


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    gamma = rng.random((16, 6))
    beta, beta_0 = backward_recursion(gamma)
    print("beta =")
    print(beta)
    print("beta_0 =", beta_0)
    assert beta.shape == (4, 6)
    assert beta[0, -1] == 1
