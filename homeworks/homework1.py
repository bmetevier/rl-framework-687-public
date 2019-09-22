import numpy as np
from IPython import embed
from rl687.environments.gridworld import Gridworld
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42  # avoid type 3 fonts
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def runEnvironment(getAction, numeps=10000):

    returns = np.zeros(numeps)

    grid = Gridworld()
    for ep in range(numeps):
        grid.reset()
        step = 0
        g = 0
        while not grid.isEnd:
            s, r, e = grid.step(getAction(grid.state))
            g += (grid.gamma ** step) * r
            step += 1
        returns[ep] = g

    print("Average: {}\nStandard Deviation: {}\nMin: {}\nMax: {}".format( \
        np.mean(returns), np.std(returns), np.min(returns), np.max(returns)))
    return returns


def problemA():
    """
    Have the agent uniformly randomly select actions. Run 10,000 episodes.
    Report the mean, standard deviation, maximum, and minimum of the observed 
    discounted returns.
    """

    print("Problem A:")
    getAction = lambda s: np.random.randint(0, 4)
    returns = runEnvironment(getAction)
    return returns


def problemC():
    """
    Run the optimal policy that you found for 10,000 episodes. Report the 
    mean, standard deviation, maximum, and minimum of the observed 
    discounted returns
    """

    print("\nProblem C")

    def getAction(svec):
        if isinstance(svec, int):
            s = svec
        else:
            s = int(np.where(svec == 1)[0])
        if s in [5, 10, 15, 20, 24]:  # up
            return 0
        elif s in [4, 9, 11, 14, 19]:  # down
            return 1
        elif s in [0, 1, 2, 3, 6, 7, 8, 13, 18, 22, 23]:  # right
            return 3
        elif s in [16, 21]:  # left
            return 2
        else:
            # embed()
            raise ValueError('invalid state!!')

    returns = runEnvironment(getAction)
    return returns

def plot_quantiles(data, labels):
    fig, ax = plt.subplots()
    for d in data:
        d.sort()
        N = d.shape[0]
        q = np.arange(1, N + 1) / N
        ax.plot(q, d)
    ax.legend(labels)
    ax.set_xlabel(r"Probability $\tau$")
    ax.set_ylabel("Return")
    ax.set_title("More-Watery Gridworld-687")
    pp = PdfPages('return_distributions_hw1.pdf')
    pp.savefig()
    pp.close()


def problemD(returnsA, returnsC):
    """
    Plot the distribution of returns for both the random policy and the optimal
    using 10,000 trials each. You must clearly label each line and axis. 
    Additionally, report the random seed used for the experiments. 
    """

    plot_quantiles([returnsA, returnsC], ["Random Policy", "Optimal Policy"])


def problemE():
    """
    Using simulations,  empirically estimate the probability that S_19=21
    given that S_8=18 (the state above the goal) when running the
    uniform random policy.  Describe how you estimated this quantity (there
    is not a typo in this problem, nor an oversight)
    NOTE: State 18 is state 19 in this gridworld implementation and state 21 is 22.
    """
    print("\nProblem E")
    env = Gridworld()
    success = 0
    N = 100000
    for trial in range(N):
        env.reset()
        env._state = 19
        step = 0

        while not env.isEnd:
            env.step(np.random.choice(range(4)))
            step += 1
            if step == 11:
                break
        if env._state == 22:
            success += 1
    p = success / N
    eps = np.sqrt((1 / (2 * N)) * np.log(2 / 0.05))  # Hoeffding's inequality
    print("Pr(S_19=s_22 | S_8=s_18)={0:.5f} empirically and is in ({1:.5f},{2:.5f}) with 95% confidence using Hoeffding's inequality".format(p, p - eps, p + eps))


def main():
    #np.random.seed(1156)
    returnsRand = problemA()
    returnsOpt = problemC()
    problemD(returnsRand, returnsOpt)
    problemE()

if __name__ == "__main__":
    main()
