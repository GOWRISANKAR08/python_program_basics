def  merge(L,R):
    m,n = len(L),len(R)
    c,i,j,k = [],0,0,0
    while k<m+n:
        if i == m:
            c.extend (R)
