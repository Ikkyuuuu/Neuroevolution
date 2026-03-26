# visualizer.py — Matplotlib real-time visualization

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from config import GRID_WIDTH, GRID_HEIGHT


class Visualizer:
    def __init__(self):
        self.fig, self.axes = plt.subplots(1, 2, figsize=(14, 6))
        self.fig.patch.set_facecolor('#1a1a2e')

        # --- Left: Grid ---
        self.ax_grid = self.axes[0]
        self.ax_grid.set_facecolor('#0f0f23')
        self.ax_grid.set_title("Simulation Grid", color='white', fontsize=13)
        self.ax_grid.set_xticks([])
        self.ax_grid.set_yticks([])

        # Food layer
        self.food_img = self.ax_grid.imshow(
            np.zeros((GRID_HEIGHT, GRID_WIDTH)),
            cmap='YlGn', vmin=0, vmax=1,
            origin='upper', interpolation='nearest', alpha=0.6
        )

        # Agent scatter
        self.agent_scatter = self.ax_grid.scatter(
            [], [], s=18, c='cyan', zorder=5, alpha=0.85, label='Agents'
        )

        legend = self.ax_grid.legend(
            handles=[
                mpatches.Patch(color='#5ffa68', label='Food'),
                mpatches.Patch(color='cyan', label='Agents'),
            ],
            loc='upper right', facecolor='#1a1a2e', labelcolor='white', fontsize=8
        )

        # --- Right: Stats ---
        self.ax_stats = self.axes[1]
        self.ax_stats.set_facecolor('#0f0f23')
        self.ax_stats.set_title("Population Stats", color='white', fontsize=13)
        self.ax_stats.tick_params(colors='white')
        for spine in self.ax_stats.spines.values():
            spine.set_edgecolor('#444')

        self.gen_history = []
        self.avg_fit_history = []
        self.max_fit_history = []
        self.alive_history = []

        self.line_avg, = self.ax_stats.plot([], [], color='cyan', label='Avg Fitness', lw=1.8)
        self.line_max, = self.ax_stats.plot([], [], color='lime', label='Max Fitness', lw=1.8)
        self.ax_stats.legend(facecolor='#1a1a2e', labelcolor='white', fontsize=9)
        self.ax_stats.set_xlabel("Generation", color='white')
        self.ax_stats.set_ylabel("Fitness", color='white')
        self.ax_stats.yaxis.label.set_color('white')
        self.ax_stats.xaxis.label.set_color('white')

        self.info_text = self.ax_grid.text(
            0.01, 0.01, '', transform=self.ax_grid.transAxes,
            color='white', fontsize=8, verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.7)
        )

        plt.tight_layout()
        plt.ion()
        plt.show()

    def update(self, food_grid, agents, generation, step, stats):
        # Update food layer
        self.food_img.set_data(food_grid)

        # Update agent positions
        alive_agents = [a for a in agents if a.alive]
        if alive_agents:
            xs = [a.x for a in alive_agents]
            ys = [a.y for a in alive_agents]
            self.agent_scatter.set_offsets(np.column_stack([xs, ys]))
        else:
            self.agent_scatter.set_offsets(np.empty((0, 2)))

        # Info overlay
        self.info_text.set_text(
            f"Gen: {generation}  Step: {step}\n"
            f"Alive: {stats['alive']}  Avg E: {stats['avg_energy']:.1f}"
        )

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def update_stats(self, generation, stats):
        self.gen_history.append(generation)
        self.avg_fit_history.append(stats['avg_fitness'])
        self.max_fit_history.append(stats['max_fitness'])
        self.alive_history.append(stats['alive'])

        self.line_avg.set_data(self.gen_history, self.avg_fit_history)
        self.line_max.set_data(self.gen_history, self.max_fit_history)

        self.ax_stats.relim()
        self.ax_stats.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def close(self):
        plt.ioff()
        plt.show()