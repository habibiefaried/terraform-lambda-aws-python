import os

def app(event, context): 
    print('## ENVIRONMENT VARIABLES')
    print(os.environ)
    print('## EVENT')
    
    return "Hello World"
