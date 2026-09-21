import numpy as np


def forward_recursion(gamma):
    N = gamma.shape[1]
    alpha = np.zeros((4, N))

    i = 0
    alpha[0, i] = gamma[0, i]
    alpha[2, i] = gamma[2, i]

    for i in range(1, N - 2):
        alpha[0, i] = gamma[0, i] * alpha[0, i - 1] + gamma[4, i] * alpha[1, i - 1]
        alpha[1, i] = gamma[9, i] * alpha[0, i - 1] + gamma[13, i] * alpha[3, i - 1]
        alpha[2, i] = gamma[2, i] * alpha[0, i - 1] + gamma[6, i] * alpha[1, i - 1]
        alpha[3, i] = gamma[11, i] * alpha[2, i - 1] + gamma[15, i] * alpha[3, i - 1]

    i = N - 2
    alpha[0, i] = gamma[0, i] * alpha[0, i - 1] + gamma[4, i] * alpha[1, i - 1]
    alpha[1, i] = gamma[9, i] * alpha[2, i - 1] + gamma[13, i] * alpha[3, i - 1]

    i = N - 1
    alpha[0, i] = gamma[0, i] * alpha[0, i - 1] + gamma[4, i] * alpha[1, i - 1]

    return np.column_stack(([1, 0, 0, 0], alpha))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    gamma = rng.random((16, 6))
    alpha = forward_recursion(gamma)
    print("alpha =")
    print(alpha)
    assert alpha.shape == (4, 7)
    assert list(alpha[:, 0]) == [1, 0, 0, 0]
