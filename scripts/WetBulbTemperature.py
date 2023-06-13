# Imports
from numpy import arctan, ndarray, power, sqrt
from pathlib import Path

from backend import TimeIt, get_logger

# Variables
logger = get_logger(Path(__file__).name)


# Functions and classes
def wet_bulb_temperature(temperature: ndarray, humidity: ndarray) -> ndarray:
    """

    Source:
     - Approximation equation https://www.omnicalculator.com/physics/wet-bulb
     - An experimental use https://journals.physiology.org/doi/full/10.1152/japplphysiol.00738.2021

    :param (ndarray) temperature:
    :param (ndarray) humidity:
    :return:
    """

    t_wet_bulb: ndarray = temperature * arctan(
        sqrt(
            0.151977 * (humidity + 8.313659)
        )
    ) + \
    arctan(temperature + humidity) − \
    arctan(humidity − 1.676331) + \
    0.00391838 * power(humidity, 3/2) * arctan(0.023101 * humidity) - \
    4.686035


    return t_wet_bulb


@TimeIt
def main() -> None:
    logger.info("Started main!")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.info("Completed main!")
    pass


if __name__ == "__main__":
    main()