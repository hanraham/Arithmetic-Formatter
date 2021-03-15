def arithmetic_arranger(problems, show_answer = False):
    # Error checking

    #Can't be more then 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Operands must be addition and subtraction
    # Numbers must be digits only
    # Numbers can only have 4 digits

    for problem in problems:
        split_problem = problem.split()

        try:
            int(split_problem[0])
            int(split_problem[2])
        except:
            return 'Error: Numbers must only contain digits.'
        
        if split_problem[1] != '+' and split_problem[1] != '-':
            return "Error: Operator must be '+' or '-'."
        
        

    
    arranged_problems = ""

    if show_answer:
        arranged_problems = 'Show answer'

    return arranged_problems
