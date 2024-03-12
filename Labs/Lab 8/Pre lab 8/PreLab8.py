import matplotlib.pyplot as plt

def evaluate_line(x0, y0, x1, y1, alpha):
    """
    Inputs: x0 : x-coordinate of the 1st point
            y0 : y-coordinate of the 1st point
            x1 : x-coordinate of the 2nd point
            y1 : y-coordinate of the 2nd point
            alpha : Point at which the line will be evaluated.
        
    Outputs: y_alpha : The value of the line at point alpha.
    """
    # Calculate the slope of the line
    slope = (y1 - y0) / (x1 - x0)
    
    # Calculate the y-intercept of the line using point-slope form: y - y0 = m(x - x0)
    y_intercept = y0 - slope * x0
    
    # Evaluate the line at point alpha using the equation of a line: y = mx + c
    y_alpha = slope * alpha + y_intercept
    
    return y_alpha

#####################################
# Main
# Example
x0 = 1
y0 = 2
x1 = 3
y1 = 4
alpha = 2.5

result = evaluate_line(x0, y0, x1, y1, alpha)
print("The y value of the line at alpha =", alpha, "is", result)

# Plot the points and the linear spline
plt.scatter([x0, x1], [y0, y1], color='red', label='Initial Points')
plt.scatter(alpha, result, label='Alpha')
plt.plot([x0, x1], [y0, y1], color='blue', label='Linear Spline')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Spline Evaluation')
plt.legend()
plt.show()
