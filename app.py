import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

ui.page_opts(title="Pyshiny App with Plot",fillable=True)
with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins", 
        "Number of Bins", 
        0, 
        75, 
        10,)


@render.plot(alt="A histogram")
def draw_histogram():
    count_of_points: int = 500
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.title("Single Color Histogram Plot")
    plt.xlabel("Bins")
    plt.ylabel("Value")
    plt.hist(random_data_array, input.selected_number_of_bins(), color='green', edgecolor='black', linewidth=1.2, density=True)
