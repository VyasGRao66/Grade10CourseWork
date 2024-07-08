PASSWORD = 'abc123'
THREE_ATTEMPTS = 3


def main():
    incorrect_attempts = 1
    user_enter = ''
    user_enter = ask_user(user_enter)
    verify(incorrect_attempts, user_enter)
    

def ask_user(entered):
    entered = input('Enter password: ')
    return entered

def verify(attempts ,entered_password):
    
        if entered_password == PASSWORD:
            print('Access Granted')
        elif entered_password != PASSWORD:
            while entered_password != PASSWORD and attempts < THREE_ATTEMPTS:
                attempts += 1
                entered_password = ask_user(entered_password)
            if attempts >= THREE_ATTEMPTS:
                print('Access Denied')
            elif entered_password == PASSWORD:
                print('Access Granted')
main()
                
            
        
