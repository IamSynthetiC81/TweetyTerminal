import cProfile, pstats, app, os
from memory_profiler import profile
from pstats import SortKey

# Results are saved into this folder in text format.
PATH = 'prof/'

pr = cProfile.Profile()

fp = open(PATH + 'memory_profiler.log', 'w+')


@profile(stream=fp)
def ProfileRunnable(runnable: str) -> None:
    pr.enable()
    cProfile.run(runnable, PATH + 'restats')
    pr.disable()


def printOut(filename: str) -> None:
    prof = pstats.Stats(PATH + 'restats')
    prof.sort_stats(SortKey.CUMULATIVE).dump_stats(PATH + 'profiling.prof')

    stream = open(PATH + filename + '.log', 'w')
    stats = pstats.Stats(PATH + 'profiling.prof', stream=stream)
    stats.sort_stats('cumtime')
    stats.print_stats()

    os.remove(PATH + 'restats')
    os.remove(PATH + 'profiling.prof')


if __name__ == "__main__":
    try:
        ProfileRunnable('app.main(" ")')
    except Exception as e:
        os.remove(PATH + 'restats')
        os.remove(PATH + 'profiling.prof')
        os.remove('output.json')
        print("Program did not exit properly")
        exit()

    fp.close()
    printOut('profiling')
