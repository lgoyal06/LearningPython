for a in 'ABC':
    for b in 'ABC':
        if b != a :
            for c in 'ABC':
                if c!=b and c!=a :
                    print(a+b+c)
