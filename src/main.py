from classes.my_evdev import periferals

def main():
    '''
    Main python function
    '''
    my_periferals = periferals()        # Instantiate periferals
    my_periferals.list_periferals()     # Show periferals
    pass

if __name__=="__main__":
    main()