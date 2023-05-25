INITIAL_STATE = (0, 0, 0, 0, 0, 0)
TRIGGER_STATE = (0, 1, 0, 1, 1, 0)
FIRING_STATE = 'fire'

def transition_rule(previous, target, following):
    _, p1, _, p3, p4, _ = previous or syn(target)
    t0, t1, t2, t3, t4, t5 = target
    f0, _, f2, _, f4, _ = following or syn(target)

    if t4 and f4 and p4:
        return FIRING_STATE

    if (t3 == 3 and f0) or (t1 and f2 == 3):
        return (1, 0, 1, 0, 1, 0)

    if (p3 == 3 and t0) or (p1 and t2 == 3):
        return (0, 1, 0, 1, 1, 0)

    if (t3 == 1 and f0) or (p1 and t2 == 1):
        return (1, 1, 1, 1, 1, 0)

    lh = t5 or (f0 and not p1)
    rh = t5 or (p1 and not f0)

    lf = f2 == 3 or t2 and (t2 + 1) % 4
    rf = p3 == 3 or t3 and (t3 + 1) % 4

    return (lh, rh, lf, rf, 0, f0 and p1)

def syn(T):
    t0, t1, t2, t3, t4, t5 = T
    return (t1, t0, t3, t2, t4, t5)
