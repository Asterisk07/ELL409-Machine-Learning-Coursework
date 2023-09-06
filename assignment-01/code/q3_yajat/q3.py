#all import statements
import os
import pandas as pd
import torch 
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


model_directory = 'saved_models'
model_filename = 'linear_regression_model.pth'
model_file_path = os.path.join(model_directory, model_filename)

# Ensure the directory exists, create it if it doesn't
os.makedirs(model_directory, exist_ok=True)

# Function to load or initialize the model
def load_or_initialize_model(X_train, y_train):

# Load the model if it exists, otherwise initialize a new model
    if os.path.exists(model_file_path):
        print('Model exist so using it')
        model = torch.load(model_file_path)
    else:
        print('Model does not exist so initialising from scratch')
        input_size = X_train.shape[1]
        model = nn.Linear(input_size, 1).double()
        torch.save(model, model_file_path)
    return model



#function to train the model
def modeltrain(X_train,y_train):
    input_size = X_train.shape[1]
    model = nn.Linear(input_size, 1).double()  # Double data type for weight tensor

# Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model (rest of the code remains the same)
    num_epochs = 1000

    for epoch in range(num_epochs):
    # Forward pass
        outputs = model(X_train.double())  # Ensure input data type matches model's weight data type
        loss = criterion(outputs, y_train.view(-1, 1))

    # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
    


    print('Training Done')
    return model


#function to test the model
def modeltest(X_test,y_test,model):
    print("Testing starting")
    # Assuming 'model' is your trained linear regression model
    with torch.no_grad():
        predictions = model(X_test)


    print('testing over now accuracy analysis')

    predictions = predictions.numpy()
    y_test = y_test.numpy()  # Replace with actual ground truth if available

    # Calculate MAE and MSE
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)

    print(f'MAE: {mae}')
    print(f'MSE: {mse}')

def create_plot(X,y):
    # Replace 'X1' with the name of the feature you want to plot.
    n=int(input("Enter the feature for which you want the plot, enter any value b/w 0-2:"))
    feature_to_plot = X[:,n] 

    # Create a scatter plotc.ear
    plt.plot(feature_to_plot, y, alpha=0.5)
    plt.xlabel('Feature No:')  # Replace with the appropriate feature name
    plt.ylabel('y')
    plt.title('Line Plot of Feature vs. y')
    plt.show()



df = pd.read_csv('assignment-01/code/q3_yajat/q3.py')
#print(df.head())



# Separate the target variable 'y' from the input features.
X = df.drop(columns=['y'])
y = df['y']

# Handle categorical variables using one-hot encoding.
X = pd.get_dummies(X, columns=['X3'], prefix=['X3'])

for column in X.columns:
    try:
        X[column] = X[column].astype(float)
    except ValueError:
        print(f"Column '{column}' cannot be converted to float.")



# Convert the DataFrame to a PyTorch tensor.
X = torch.tensor(X.values, dtype=torch.float64)

# Convert the target variable to a PyTorch tensor.
y = torch.tensor(y.values, dtype=torch.float64)
size=len(X)
train_ratio=0.6
train_size=int(size*train_ratio)
test_size=size-train_size


#Splitting the data in training and testing data 


#Training data
X_train=X[:train_size]
y_train=y[:train_size]

#Testing data
X_test=X[train_size:]
y_test=y[train_size:]

# print(len(X_train),len(X_test))








create_plot(X_train,y_train)
# model = load_or_initialize_model(X_train, y_train)
# model=modeltrain(X_train,y_train)
# modeltest(X_test,y_test,model)



