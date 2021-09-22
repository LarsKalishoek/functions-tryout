def sayHelloWorld(hellocounter):
    loopcounter = hellocounter
    hellocounter = 1
    while (loopcounter != "0"):
            print(hellocounter, ". Hello World!")
            if (loopcounter == 1):
                break
            else:
                loopcounter = loopcounter - 1
                hellocounter = hellocounter + 1
                continue


sayHelloWorld(9)
        