def alert_on_three_time(list, max):
    """
    algo to warn 
    """
    c = 0
    warn = 0
    for i in list:
        if (i > max):
            c = c + 1
            if c >= 3:
                print('alert - warn')
                warn = warn + 1
                c = 0
        else: 
            c = 0
    return warn


print("waring sample: ", alert_on_three_time(**{"list":[40,89,77,40,89,77,20,40,89,0], "max":20}))
