import json

def another_program():
    print('\nthis is another program, but it can use the same JSON to take data:')
    
    with open('vars.json') as f:
        variable = json.load(f)
    print(variable)