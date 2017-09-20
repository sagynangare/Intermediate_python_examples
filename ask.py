def ask_ok(prompt, retries=4, reminder = 'Please try again!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'yes', 'ye','yuo'):
            print("You quited")
            return True
        if ok in ('n','no','nop','nope'):
            print("You are still in race. ")
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?: ')

