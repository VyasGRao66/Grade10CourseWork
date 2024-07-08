# Programmer: Vyas Rao
# Date: 2023-13-15
# Discription: Calculator

import tkinter # importing tkinter


# initalizing variubles
num = ''
num2 = 0
choice = ''
decimal_amt = False  #ensuing 1 decimal for value 

class Calculator:
    
    def __init__(self):
        #Creating
        self.main = tkinter.Tk()
        self.main.minsize(260, 380)
        self.main.title('Calculator')

        self.value_var = tkinter.StringVar()
        self.label_value = tkinter.Label(self.main,textvariable=self.value_var, fg = 'white', bg = 'black', anchor = 'e', font=15).place(x = 20, y = 20, width = 220, height = 40)
        
        # Creating advanced functions 
        self.factorial_button = tkinter.Button(self.main, text='!', command=self.factorials).place(x = 20, y = 80, width = 40, height = 40)
        self.lcm_button = tkinter.Button(self.main, text='LCM', command=self.lcm).place(x = 80, y = 80, width = 40, height = 40)
        self.gcf_button = tkinter.Button(self.main, text='GCF', command=self.gcf).place(x = 140, y = 80, width = 40, height = 40)

        # Creating Basic Numbers
        self.one_button = tkinter.Button(self.main, text='1', command=self.one).place(x = 20, y = 140, width = 40, height = 40)
        self.two_button = tkinter.Button(self.main, text='2', command=self.two).place(x = 80, y = 140, width = 40, height = 40)
        self.three_button = tkinter.Button(self.main, text='3', command=self.three).place(x = 140, y = 140, width = 40, height = 40)
        self.four_button = tkinter.Button(self.main, text='4', command=self.four).place(x = 20, y = 200, width = 40, height = 40)
        self.five_button = tkinter.Button(self.main, text='5', command=self.five).place(x = 80, y = 200, width = 40, height = 40)
        self.six_button = tkinter.Button(self.main, text='6', command=self.six).place(x = 140, y = 200, width = 40, height = 40)
        self.seven_button = tkinter.Button(self.main, text='7', command=self.seven).place(x = 20, y = 260, width = 40, height = 40)
        self.eight_button = tkinter.Button(self.main, text='8', command=self.eight).place(x = 80, y = 260, width = 40, height = 40)
        self.nine_button = tkinter.Button(self.main, text='9', command=self.nine).place(x = 140, y = 260, width = 40, height = 40)
        self.zero_button = tkinter.Button(self.main, text='0', command=self.zero).place(x = 20, y = 320, width = 40, height = 40)

        # Creating operations and decimal
        self.decimal_button = tkinter.Button(self.main, text='.', command=self.decimal).place(x = 80, y = 320, width = 40, height = 40)
        self.add_button = tkinter.Button(self.main, text='+', command=self.add).place(x = 200, y = 260, width = 40, height = 40)
        self.equals_button = tkinter.Button(self.main, text='=', command=self.equal).place(x = 140, y = 320, width = 40, height = 40)
        self.subtract_button = tkinter.Button(self.main, text='-', command=self.subtract).place(x = 200, y = 320, width = 40, height = 40)
        self.divide_button = tkinter.Button(self.main, text='÷', command=self.divide).place(x = 200, y = 200, width = 40, height = 40)
        self.multiply_button = tkinter.Button(self.main, text='x', command=self.multiply).place(x = 200, y = 140, width = 40, height = 40)
        self.clear_button = tkinter.Button(self.main, text='Clear',command=self.clear).place(x = 200, y = 80, width = 40, height = 40)
        
        tkinter.mainloop()
        
    def one(self): # Adding number 1 to label
        global num
        print(self)
        num = num + '1'
        self.value_var.set(num)
        
    def two(self): # Adding number 2 to label
        global num
        num = num + '2'
        self.value_var.set(num)
        
    def three(self): # Adding number 3 to label
        global num
        num = num + '3'
        self.value_var.set(num)
        
    def four(self): # Adding number 4 to label
        global num
        num = num + '4'
        self.value_var.set(num)
        
    def five(self): # Adding number 5 to label
        global num
        num = num + '5'
        self.value_var.set(num)
        
    def six(self): # Adding number 6 to label
        global num
        num = num + '6'
        self.value_var.set(num)
        
    def seven(self): # Adding number 7 to label
        global num
        num = num + '7'
        self.value_var.set(num)
        
    def eight(self): # Adding number 8 to label
        global num
        num = num + '8'
        self.value_var.set(num)
        
    def nine(self): # Adding number 9 to label
        global num
        num = num + '9'
        self.value_var.set(num)
        
    def zero(self): # Adding number 0 to label
        global num
        num = num + '0'
        self.value_var.set(num)
        
    def clear(self): # clearing label
        global num, choice, number, decimal_amt
        num = ''
        number = 0
        choice = ''
        decimal_amt = False
        self.value_var.set(num)
        
    def decimal(self): # Adding decmial label
        global num, decimal_amt
        if decimal_amt == False: # ensuing only one decimal
            num = num + '.'
            decimal_amt = True
        self.value_var.set(num)
        
    def add(self): # using add operator
        global num, num2, choice, decimal_amt 
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = '+'
            num = ''
            decimal_amt = False
        self.value_var.set(num)
        
    def subtract(self): # using subtract operator
        global num, num2, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = '-'
            num = ''
            decimal_amt = False
        self.value_var.set(num)
        
    def multiply(self): # using multiply opeator
        global num, num2, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = '*'
            num = ''
            decimal_amt = False
        self.value_var.set(num)
        
    def divide(self): # using divide operator
        global num, num2, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = '/'
            num = ''
            decimal_amt = False
        self.value_var.set(num)
        
    def factorials(self): # using factorials operator
        global num, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            choice = '!'
            decimal_amt = False
        self.value_var.set(num)
        
    def gcf(self): # using gcf operator
        global num, num2, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = 'gcf'
            num = ''
        self.value_var.set(num)
        
    def lcm(self): # using lcm operator
        global num, num2, choice, decimal_amt
        if num == '.' or num == '' or num == 'INVALID':
            self.invalid()
        else:
            num2 = float(num)
            choice = 'lcm'
            num = ''
            decimal_amt = False
        self.value_var.set(num)
        
    def equal(self): # all the math in equals
        
        global num, num2, choice
        total = 0

        
        if num == '.' or num == 'INVALID' or num == '': #ensuring no errors AFTER equals
            self.invalid()
            
        elif choice == '/': # diviing
            if float(num) == 0:  # ensuing nunmber is not 0 so no invalid
                self.invalid()
            else:
                num = num2/float(num)
                
        elif choice == '*':  # mulitplying
            num = num2*float(num)
            
        elif choice == '-': # subtracting
            num = num2 - float(num)
            
        elif choice == '+': # adding
            num = num2+float(num)
            
        elif choice == '!': # factorials
            if float(num)%1 != 0: # ensuing its a integer
                self.invalid()
            else:
                total = float(num)
                num2 = float(num)
                while num2 > 1:
                    num2 -= 1
                    total = total * num2
                num = total
                
        elif choice == 'gcf':  # gcf
            num_smaller = 0
            if float(num) > 1 and num2 > 1:                      
                if int(num) > num2:
                    num_smaller = int(num2)
                elif int(num) < num2:
                    num_smaller = int(num)
                elif int(num) == num2:
                    num_smaller = int(num2)
                for count in range(1, num_smaller + 1):
                    if int(num) % count == 0 and num2 % count == 0:
                        total = count
                num = total
            else:
                self.invalid()

                
        elif choice == 'lcm':  # lcm
            if float(num) > 1 and num2 > 1:  
                replacement1 = int(num)
                replacement2 = num2
                while total == 0:
                    if replacement1 > replacement2:
                        replacement2 += num2 
                    elif replacement1 < replacement2:
                        replacement1 += int(num)
                    elif replacement1 == replacement2:
                        total = replacement1
                        num = total
            else:
                self.invalid()
                
        self.value_var.set(str(num))


        
    def invalid(self):  # invalid
        global num
        num = 'INVALID'
        self.value_var.set(str(num))
    
            
calculator = Calculator()
