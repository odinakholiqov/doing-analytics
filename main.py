import matplotlib.pyplot as plt


def main():
    print("Hello from doing-analytics!")
    print("Hello one more  time")

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y,
        color='purple',
        linestyle='--',
        marker='o',
        markersize=8,
        linewidth=2)
    plt.title("Customized Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True, linestyle=':')
    plt.show()

if __name__ == "__main__":
    main()
