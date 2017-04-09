from zd import GameState, RedDie


def bailhard(gs):
    return gs.shotguns > 0


def greg(gs):
    def all_red(l):
        return all([isinstance(d, RedDie) for d in l])

    if gs.shotguns > 0:
        return True
    elif (gs.brains > 0 and
          all_red(gs.hand) and
          (len(gs.hand) == 3 or all_red(gs.pot))):
        print("Gregtime")
        return True
    return False


def risque(gs):
    return (gs.shotguns + len([isinstance(d, RedDie) for d in gs.hand])) >= 3


def turn(strategy):
    gs = GameState(interactive=False)
    while gs.can_continue():
        gs.roll()
        if strategy(gs):
            break
    return gs.score()


def monticarlo(strategy, n):
    samples = [turn(strategy) for i in range(n)]
    e = sum(samples)/n
    return e
