import sys
import os

from animations.simple_random_sampling import simpleRandomSamplingScene
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import get_logger


current_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_dir, "..", "logs", "main.log")
logger = get_logger(name='main', log_file=log_file)

if __name__ == '__main__':
    logger.info("main.py started")
    try:
        scene = simpleRandomSamplingScene()
        scene.render(preview=True)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    logger.info("main.py finished")
