# visualizer.py — Matplotlib visualization with speed control buttons

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Button
from config import GRID_WIDTH, GRID_HEIGHT

SPEED_OPTIONS = [1, 5, 10, 50]   # render every N steps


class Visualizer:
    def __init__(self):
        self.render_interval = SPEED_OPTIONS[0]  # start at 1x

        self.fig = plt.figure(figsize=(15, 7))
        self.fig.patch.set_facecolor('#1a1a2e')

        # Layout: grid | stats | buttons (column on right)
        self.ax_grid  = self.fig.add_axes([0.02, 0.12, 0.44, 0.82])
        self.ax_stats = self.fig.add_axes([0.52, 0.12, 0.44, 0.82])

        # Speed buttons (bottom strip)
        btn_labels = ["1x  (all)", "5x  (fast)", "10x", "50x  (turbo)"]
        self._btn_axes = []
        self._btns = []
        btn_w = 0.18
        btn_gap = 0.005
        total_w = len(SPEED_OPTIONS) * btn_w + (len(SPEED_OPTIONS) - 1) * btn_gap
        start_x = (1.0 - total_w) / 2

        for i, (label, speed) in enumerate(zip(btn_labels, SPEED_OPTIONS)):
            ax_btn = self.fig.add_axes([
                start_x + i * (btn_w + btn_gap),
                0.01, btn_w, 0.07
            ])
            btn = Button(ax_btn, label,
                         color='#2a2a4a', hovercolor='#3a3a6a')
            btn.label.set_color('white')
            btn.label.set_fontsize(9)

            # Closure to capture speed value
            def make_callback(s, b_list, i_idx):
                def callback(event):
                    self.render_interval = s
                    for j, b in enumerate(b_list):
                        b.ax.set_facecolor('#4a4a8a' if j == i_idx else '#2a2a4a')
                    self.fig.canvas.draw_idle()
                return callback

            self._btn_axes.append(ax_btn)
            self._btns.append(btn)

        # Wire callbacks now that _btns list is complete
        for i, (btn, speed) in enumerate(zip(self._btns, SPEED_OPTIONS)):
            btn.on_clicked(make_callback(speed, self._btns, i))

        # Highlight default button
        self._btns[0].ax.set_facecolor('#4a4a8a')

        # --- Grid panel ---
        self.ax_grid.set_facecolor('#0f0f23')
        self.ax_grid.set_title("Simulation Grid", color='white', fontsize=13)
        self.ax_grid.set_xticks([])
        self.ax_grid.set_yticks([])

        self.food_img = self.ax_grid.imshow(
            np.zeros((GRID_HEIGHT, GRID_WIDTH)),
            cmap='YlGn', vmin=0, vmax=1,
            origin='upper', interpolation='nearest', alpha=0.5
        )

        self.agent_scatter = self.ax_grid.scatter(
            [], [], s=20, zorder=5, alpha=0.9
        )

        self.info_text = self.ax_grid.text(
            0.01, 0.01, '', transform=self.ax_grid.transAxes,
            color='white', fontsize=8, verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.7)
        )

        # Speed overlay (top-right of grid)
        self.speed_text = self.ax_grid.text(
            0.99, 0.99, '▶  1x', transform=self.ax_grid.transAxes,
            color='yellow', fontsize=10, va='top', ha='right',
            bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.8)
        )

        # --- Stats panel ---
        self.ax_stats.set_facecolor('#0f0f23')
        self.ax_stats.set_title("Population Stats", color='white', fontsize=13)
        self.ax_stats.tick_params(colors='white')
        for spine in self.ax_stats.spines.values():
            spine.set_edgecolor('#444')

        self.step_history   = []
        self.avg_fit_history = []
        self.alive_history  = []

        self.line_avg,   = self.ax_stats.plot([], [], color='cyan', label='Avg Fitness', lw=1.8)
        self.line_alive, = self.ax_stats.plot([], [], color='lime', label='Alive Count', lw=1.8)
        self.ax_stats.legend(facecolor='#1a1a2e', labelcolor='white', fontsize=9)
        self.ax_stats.set_xlabel("Step", color='white')
        self.ax_stats.set_ylabel("Value",  color='white')
        self.ax_stats.xaxis.label.set_color('white')
        self.ax_stats.yaxis.label.set_color('white')

        plt.ion()
        plt.show()

    def update(self, food_grid, agents, step, stats):
        # Food
        self.food_img.set_data(food_grid)

        # Agents with lineage colors
        alive = [a for a in agents if a.alive]
        if alive:
            xs     = np.array([a.x for a in alive])
            ys     = np.array([a.y for a in alive])
            colors = np.array([a.color for a in alive], dtype=np.float32) / 255.0
            self.agent_scatter.set_offsets(np.column_stack([xs, ys]))
            self.agent_scatter.set_facecolor(colors)
        else:
            self.agent_scatter.set_offsets(np.empty((0, 2)))

        # Info + speed overlay
        self.info_text.set_text(
            f"Step: {step}\n"
            f"Alive: {stats['alive']}  Avg E: {stats['avg_energy']:.1f}"
        )
        speed_idx = SPEED_OPTIONS.index(self.render_interval) + 1
        self.speed_text.set_text(f"▶{'▶' * (speed_idx - 1)}  {self.render_interval}x")

        # Stats chart
        self.step_history.append(step)
        self.avg_fit_history.append(stats['avg_fitness'])
        self.alive_history.append(stats['alive'])

        self.line_avg.set_data(self.step_history,   self.avg_fit_history)
        self.line_alive.set_data(self.step_history, self.alive_history)

        self.ax_stats.relim()
        self.ax_stats.autoscale_view()

        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
   
    def close(self):
        plt.ioff()
        plt.show()