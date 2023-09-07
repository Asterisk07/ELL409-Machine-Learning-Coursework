import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'plott.png')
import matplotlib.pyplot as plt
x1=[0, 1, 2, 3, 4]
plt.plot(x1, [0, 3, 5, 9, 11], marker='o')
plt.title("Ere")
plt.xticks(x1, x1)
plt.savefig(file_path)
plt.show()