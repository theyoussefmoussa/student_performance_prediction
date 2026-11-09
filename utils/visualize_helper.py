import matplotlib.pyplot as plt
import os

def title_labels(title, xlabel, ylabel = 'Frquency'):
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)


def highlight_max(ax, color="red"):
    bars = ax.patches

    if not bars:
        return

    max_bar = max(bars, key=lambda bar: bar.get_height())
    max_bar.set_facecolor(color)


def annotate_bars(ax, fmt="{:.0f}"):
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt=fmt,
            padding=3
        )




def add_mean_median(ax, data):
    mean = data.mean()
    median = data.median()

    ax.axvline(
        mean,
        color="red",
        linestyle="--",
        label=f"Mean: {mean:.2f}"
    )

    ax.axvline(
        median,
        color="green",
        linestyle="-.",
        label=f"Median: {median:.2f}"
    )

    ax.legend()


from pathlib import Path

def save_plot(fig, filename, folder="univariate_analysis"):
    output_dir = Path(f"{os.getenv('PROJECT_ROOT')}/outputs/{folder}")
    output_dir.mkdir(parents=True, exist_ok=True)

    fig.savefig(output_dir / filename, bbox_inches="tight")
    plt.close(fig)



def separator(title=None, length = 50):
    if title: 
        print(f"\n {'-' * 10} {title} {'-' * 10}")
    else: 
        print(f"\n {'-' * length}")