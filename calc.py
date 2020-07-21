'''
@Author: your name
@Date: 2020-07-21 21:25:04
@LastEditTime: 2020-07-21 21:30:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python_Test\calc.py
'''

def neuron(x,w,b):
    y = x * w + b
    y = max(0, y)
    return y

if __name__ == "__main__":
    print(f"neuron(4,1,3):{neuron(4,1,3)}")
