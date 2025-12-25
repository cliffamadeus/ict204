import numpy as np
import matplotlib.pyplot as plt

# LAGRANGE INTERPOLATION FUNCTION
def lagrange_interpolation(x_vals, y_vals, x_target):
    """
    Computes the Lagrange interpolating polynomial value at x_target.
    """
    n = len(x_vals)
    result = 0

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x_target - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term

    return result

# USER INPUT
n = int(input("Enter the number of data points: "))

x_vals = []
y_vals = []

print("\nEnter the x and y values:")
for i in range(n):
    x_vals.append(float(input(f"x[{i+1}]: ")))
    y_vals.append(float(input(f"y[{i+1}]: ")))

x_interp = float(input("\nEnter the x value to interpolate: "))


# COMPUTATION
y_interp = lagrange_interpolation(x_vals, y_vals, x_interp)
print(f"\nInterpolated value at x = {x_interp}: y = {y_interp}")


# PLOTTING
x_plot = np.linspace(min(x_vals), max(x_vals), 500)
y_plot = [lagrange_interpolation(x_vals, y_vals, x) for x in x_plot]

plt.figure(figsize=(8, 6))

# Colors for clarity
plt.plot(
    x_vals, y_vals,
    label="Original Data Points",
    color="darkorange",
    linestyle="--",
    marker="o"
)

plt.plot(
    x_plot, y_plot,
    label="Lagrange Polynomial",
    color="royalblue",
    linewidth=2
)

plt.scatter(
    x_interp, y_interp,
    color="crimson",
    s=80,
    label=f"Interpolated Point (x = {x_interp})",
    zorder=5
)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)
plt.show()
