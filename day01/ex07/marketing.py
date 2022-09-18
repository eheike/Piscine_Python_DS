import sys
def marketing():
    clients=(['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 
                'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
            )
    participants=(['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
                )
    recipients=(['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'])
    if sys.argv[1] == "call_center":
        call_c = set(set(clients) - set(recipients))
        return list(call_c)
    elif sys.argv[1] == "potential_clients":
        pot_cl = set(set(participants) - set(clients))
        return list(pot_cl)
    elif sys.argv[1] == "loyalty_program":
        loy_pr = set(set(clients) - set(participants))
        return list(loy_pr)
    else:
        raise Exception("Error argument")
                                                                                                                                    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print (marketing())