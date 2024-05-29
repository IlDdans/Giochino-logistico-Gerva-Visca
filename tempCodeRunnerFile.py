if n<7:
                    rami[9]=Ramo(screen, rami[8].stato, -2)
                else:
                    if rami[8].stato==0:
                        rami[9]=Ramo(screen, 2, -2)
                    else:
                        rami[9]=Ramo(screen, 0, -2)
                        
                    rami[8]=Ramo(screen, 1, -1)