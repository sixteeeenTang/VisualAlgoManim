from typing import Union


def simpleRandomSampling(data: Union[list, tuple], sampleSize: int) -> list:
    import random
    return random.sample(data, sampleSize)


if __name__ == "__main__":
    data = ([1, 2], (3, 4, 5, 6), 7, 8, 9, 10)
    sampleSize = 3
    print(simpleRandomSampling(data, sampleSize))
