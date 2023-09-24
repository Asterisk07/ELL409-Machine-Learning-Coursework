import papermill as pm
import os
import time

# Get the directory of the currently executing script
script_directory = os.path.dirname(os.path.abspath(__file__))
print("script dir",script_directory)
os.chdir(script_directory)
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Define the filename you want to join to the script directory
filename = "q1.ipynb"  # Replace with your desired filename


# Join the script directory and the filename
file_path = os.path.join(script_directory, filename)
outfile = os.path.join(script_directory, "q1out.ipynb")

learning_rates = [0.01, 0.1, 0.5, 0.9]
reduceLR_factors = [0.1, 0.5, 0.9]
reduceLR_patience_values = [5, 7, 9]

total=len(learning_rates)*len(reduceLR_factors)*len(reduceLR_patience_values)
# Loop through the parameter sets and run the main script with each set
i=1

print(script_directory)

def execute(command):
    a=time.time()    
               

    # Execute the command in the terminal
    os.system(command)
    b=time.time()
    print(f'\t time taken= {b-a} \n')
    


def tune_LR():
    param_name='LR'
    for reduceLR_patience in reduceLR_patience_values:
        for reduceLR_factor in reduceLR_factors:
            for learning_rate in learning_rates:
                command = f'papermill {file_path} {outfile} -p learning_rate {learning_rate} -p reduceLR_factor {reduceLR_factor} -p reduceLR_patience {reduceLR_patience} tuning_type {param_name}'
                

                execute(command)
                print(f'\t{i}/{total} finished\n')
                i+=1
#You can uncomment this function to run it             
# tune_LR()

dict={'weight_decay_rate':[0.01, 0.1, 0.5, 0.9],'batchSize':[32,64,128,256],'optimizer_name':['SGD','Adam','RMSprop']}

def tune(param_name):
    params=dict[param_name]
    for param in params:
        command = f'papermill {file_path} {outfile} -p {param_name} {param} -p tuning_type {param_name}'

        execute(command)
        print(f'\t{i}/{total} finished\n')
        i+=1

#You can uncomment this function to run it  with different parameter names
# tune('weight_decay_rate')  
# tune('batchSize')  
# tune('optimizer_name')  