def secant_root_solve(f, a, b, maxiter=1000, errstop=1e-12):
    '''
    Solves for the roots of a function using the secant method
    
    @arg
    f       - Lambda Function
              Function handle to solve root for.
              Must accept a scalar argument. Must return a scalar
    a       - double
              Upper bound
    b       - double
              Lower bound
    maxiter - int (optional)
              Maximum number of iterations
    errstop - double (optional)
              Minimum error stopping criteria (in difference)
    
    @return
    x       - double
              Function root
    niter   - int
              Nnumber of iterations
    erra    - double
              Root error
    
    @author: Matt Marti
    @date: 2019-06-16
    '''
    
    # Check that root exists (Intermediate value theorem)
    fa = f(a);
    fb = f(b);
    assert f(a) * f(b) <= 0, 'Root does not exist';
    
    # Initialize loop
    if abs(fa) < abs(fb):
        pim1 = a;
    else:
        pim1 = b;
    #
    erra = abs(f(pim1));
    
    # Loop
    i = 0; niter = 0;
    while erra > errstop and i < maxiter:
        
        # Secant method
        p = a - fa * (b - a) / (fb - fa);
        
        # Assign this guess to next bounds
        fp = f(p);
        if (fp*fa < 0):
            b = p;
        elif (fp*fb < 0):
            a = p;
        else: # fp = 0
            break;
        #
        
        # Measure error
        if pim1 != 0:
            erra = abs( (p - pim1) / pim1 );
        else:
            erra = abs( p - pim1 );
        #
        
        # Stopping criteria for prompt
        if not niter and erra < errstop:
            break;
        #
        
        # Iterate
        pim1 = p;
        i = i + 1;
    #
    
    # Assign output
    x = p;
    niter = i;
    
    # Return
    return x, niter, erra
#