for rw in range(1,5):
    
    for cl1 in range(1,5):
        if rw<2:
            print(" ___  ",end='') 
            print(" ",end=' ')
    print()
    for cl2 in range(1,5):
        if cl2 == 4:  # Check if it's the last column
            print("/   \ ", end='')
        else:
            
            print("/   \___",end='')
        
        
   
    print()
    for cl3 in range(1,5):
        print("\___/  ",end=' ')
    
