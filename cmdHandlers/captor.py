jal: list[dict] = []


def sak(t=None):
    global jal
    if t:
        jal.append(t)
    return jal
