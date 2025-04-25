import sys
import os
from manim import *
from manim import config
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))
sys.path.append(os.path.dirname(os.path.dirname(current_dir)))
from samplingAlgos.simpleRandomSampling import simpleRandomSampling
from utils.logger import get_logger, log_scene


config.pixel_height = 720
config.pixel_width = 1280
config.frame_height = 4
config.frame_width = 7.2
config.media_dir = os.path.join(os.path.dirname(current_dir), "..", "media")
# config.background_color = WHITE

class simpleRandomSamplingScene(Scene):    
    def title(self):
        title = Tex("Simple Random Sampling", font_size=40).to_edge(UP)
        logo = ImageMobject(os.path.join(os.path.dirname(os.path.dirname(current_dir)), "utils/WUSTClimber_logo.png")).scale(0.3).to_edge(DOWN)
        self.play(Write(title), FadeIn(logo))
        self.wait(1)
        self.play(
            FadeOut(title),
            logo.animate.to_corner(DL*0.1)
        )

    @log_scene()
    def construct(self):
        # Title
        self.title()

        # Create a list of points
        grid_size = 1
        positions = [
            np.array([x, y, 0])
            for x in [-grid_size, 0, grid_size]
            for y in [-grid_size, 0, grid_size]
        ]
        points = [Dot(point=pos, color=BLUE) for pos in positions]

        # Create a list of points to be sampled
        sampled_points = simpleRandomSampling(points, 3)

        # Add the points to the scene
        self.play(FadeIn(Group(*points)))
        # self.add(*points)
        self.wait(1)

        # Animate the sampling process
        for point in sampled_points:
            self.play(Flash(point, color=YELLOW), point.animate.set_color(YELLOW))
            self.wait(1)

        self.wait(1)

        # Remove the sampled points from the scene
        unsampled_points = [point for point in points if point not in sampled_points]
        self.play(FadeOut(*unsampled_points), run_time=1)

        self.wait(2)