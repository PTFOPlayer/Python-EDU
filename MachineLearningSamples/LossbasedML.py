import numpy as np
from numpy.lib.function_base import gradient

x = np.array([1, 2, 3, 4], dtype=np.float32)
y = np.array([2, 4, 6, 8], dtype=np.float32)

w = 0.0

def forward(x):
    return w * x

def loss(y, y_pred):
    return ((y_pred - y)**2).mean()

def gradient(x , y, y_pred):
    return np.dot(2*x, y_pred - y).mean()

print(f'Prediction before training: f(5) = {forward(5):.3f}' )

learning_rate = 0.01
n_iters = 20

for epoch in range(n_iters):
    y_pred = forward(x)
    
    l = loss(y, y_pred)
    
    dw = gradient(x, y, y_pred)
    
    w -= learning_rate * dw
    
    if epoch % 1 == 0:
        print(f'epoch {epoch +1}: w = {w:.3f}, loss = {l:.8f}')
print(f'Prediction after training: f(5) = {forward(5):.3f}' )
