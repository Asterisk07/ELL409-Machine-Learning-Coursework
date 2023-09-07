import papermill as pm
import os

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the filename you want to join to the script directory
filename = "a1-LR.ipynb"  # Replace with your desired filename

# Join the script directory and the filename
file_path = os.path.join(script_directory, filename)


learning_rates = [0.01]
reduceLR_factors = [0.1]
reduceLR_patience_values = [5]
# learning_rates = [0.01, 0.1, 0.5, 0.9]
# reduceLR_factors = [0.1, 0.5, 0.9]
# reduceLR_patience_values = [5, 7, 9]

total=len(learning_rates)*len(reduceLR_factors)*len(reduceLR_patience_values)
# Loop through the parameter sets and run the main script with each set
i=1
for reduceLR_patience in reduceLR_patience_values:
    for reduceLR_factor in reduceLR_factors:
        for learning_rate in learning_rates:
            # pm.execute_notebook(input_notebook, parameters=parameters)


            # Replace 'your_command' with the actual command you want to run
            command = f'papermill {file_path} {file_path} -p learning_rate {learning_rate} -p reduceLR_factor {reduceLR_factor} -p reduceLR_patience {reduceLR_patience}'

            # Execute the command in the terminal
            os.system(command)
            print(f'{i}/{total}')
            i+=1
            # subprocess.call(["python", "main_script.py", str(learning_rate), str(reduceLR_factor), str(reduceLR_patience)])

# Define the parameters you want to set
# parameters = {
#     "learning_rate": 0.01,
#     "batch_size": 32,
#     "num_epochs": 10,
# }

# Execute the notebook without specifying an output file
# pm.execute_notebook(input_notebook, parameters=parameters)
