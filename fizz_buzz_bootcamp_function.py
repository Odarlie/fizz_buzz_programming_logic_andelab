def fizz_buzz(number):
    ''' This function returns 'Fizz,'Buzz,FizzBuzz' or the argument it recieves based
on the argument the function recieves.. '''
    if number %5 ==0 and number %3 ==0:
        return 'FizzBuzz'
    else:
        if number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            return number
            
    
        
    
        
  
    

    
