def RSCC_57_Encoder(u):
    r1 = r2 = r3 = 0
    c_sys, c_pc = [], []
    for u_t in u:
        c_sys.append(u_t)
        r1_t = (r3 + r2 + u_t) % 2
        r3, r2, r1 = r2, r1, r1_t
        c_pc.append((r1 + r3) % 2)
    return c_sys, c_pc


if __name__ == "__main__":
    u = [1, 0, 1, 1, 0]
    c_sys, c_pc = RSCC_57_Encoder(u)
    print("c_sys =", c_sys)
    print("c_pc  =", c_pc)
    assert c_sys == u
