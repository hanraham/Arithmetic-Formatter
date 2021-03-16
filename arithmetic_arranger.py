def arithmetic_arranger(problems, show_answer = False):
    arranged_problems = ""

    # Error checking
    # Can't be more then 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."   
   
    topString = ''
    bottomString = ''
    dashString = ''
    answerString = ''


    for problem in problems:
        split_problem = problem.split()

        # Numbers must be digits only
        answer = ''
        try:
            if split_problem[1] == '+':
                answer = str(int(split_problem[0]) + int(split_problem[2]))
            elif split_problem[1] == '-':
                answer = str(int(split_problem[0]) - int(split_problem[2]))
            else:    
                return "Error: Operator must be '+' or '-'."
        except:
            return "Error: Numbers must only contain digits."

        # Numbers can only have 4 digits
        lengthTop = len(split_problem[0])
        lengthBottom = len(split_problem[2])

        if lengthTop > 4 or lengthBottom > 4:
            print("Too long")
            return "Error: Numbers cannot be more than four digits."

        # Create strings and check if top or bottom is larger to set
        # problem length for formatting
        if lengthTop >= lengthBottom:    
            topString = ''.join([topString, '  ',
                        split_problem[0], '    '
                        ])
    
            bottomString = ''.join([bottomString, split_problem[1], ' ' * (lengthTop - lengthBottom + 1),
                            split_problem[2], '    '
                            ])

            dashString = ''.join([dashString, '-' * (lengthTop + 2), '    '])

            answerString = ''.join([answerString, ' ' * (lengthTop - len(answer) + 2), answer, '    '])

        else:
            topString = ''.join([topString, ' ' * (lengthBottom - lengthTop + 2),
                            split_problem[0], '    '
                            ])
            
            bottomString = ''.join([bottomString, split_problem[1], ' ', split_problem[2], '    '])

            dashString = ''.join([dashString, '-' * (lengthBottom + 2), '    ']) 

            answerString = ''.join([answerString, ' ' * (lengthBottom - len(answer) + 2), answer, '    '])

        
    arranged_problems = ''.join([arranged_problems, topString.rstrip(), '\n', 
                            bottomString.rstrip(), '\n',
                            dashString.rstrip()])
   
    
    if show_answer:
         arranged_problems = '\n'.join([arranged_problems, answerString.rstrip()])
    return arranged_problems
