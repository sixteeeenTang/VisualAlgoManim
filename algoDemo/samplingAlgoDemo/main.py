import sys
import os

from animations.simple_random_sampling import simpleRandomSamplingScene
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import get_logger


current_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_dir, "..", "logs", "main.log")
logger = get_logger(name='main', log_file=log_file)
logger.info("main.py started")

if __name__ == '__main__':
    scene = simpleRandomSamplingScene()
    scene.render(preview=True)
