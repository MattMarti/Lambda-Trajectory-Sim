import numpy as np
import scipy as scp

def runge_kutta_int(ydot, y0, tlims, h, N=4):
    '''
    Runge-Kutta integration
    This function uses an N-th order Runge Kutta integration technique to
    solve a time-dependent differential equation.
    
    @arg
    ydot      - Anonymous Function
                Function which returns the time derivative of the state, 
                which is a Ny x 1 double vector. Function takes the form:
                    ydot = f(t, y)
    y0        - Ny x 1 double vector
                Initial condition
    tlims     - 2 x 1 double
                Integration time limits: [ Initial time; Final time ]
    h         - double
                Time step value for integration
    N         - int (optional)
                Number of stages of Runge-Kutta integration. Default
                Butcher Tableaus are written into the function, so "cvec",
                "amat", and "bvec" need not be specified.
    
    @return
    ykhist    - Ny x Nt double matrix
                Time history of state values
    tkhist    - 1 x Nt double vector
                Time history of time values of integration steps
    ydotkhist - Ny x Nt double matrix
                Time derivative values at each integration step
    
    @author: Matt Marti
    @date: 2019-06-28
    '''
    
    # Input checking
    # Make sure y0 is the correct format (1-D), then squeeze it
    y0 = y0.squeeze();
    
    # Runge-Kutta Butcher Tableaus
    oo2 = 0.5;
    oo3 = 1/3;
    oo6 = 1/6;
    if N == 4:
        cvec = np.array([ 0, oo2, oo2, 1 ], dtype=np.float64);
        amat = np.array([
            [0,   0,   0,   0],
            [oo2, 0,   0,   0],
            [0,   oo2, 0,   0],
            [0,   0,   1,   0]],\
            dtype=np.float64);
        bvec = np.array([[ oo6, oo3, oo3, oo6 ]],dtype=np.float64);
        
    elif N == 3:
        cvec = np.array([ 0, oo2, 1 ],dtype=np.float64);
        amat = np.array([ 
            [0,   0,   0],
            [oo2, 0,   0],
            [0,   1,   0]],\
            dtype=np.float64);
        bvec = np.array([[ oo6, 4*oo6, oo6 ]],dtype=np.float64);
        
    elif N == 2:
        cvec = np.array([ 0, oo2 ],dtype=np.float64);
        amat = np.array([ 
            [0,   0],
            [oo2, 0]],\
            dtype=np.float64);
        bvec = np.array([[ 0, 1 ]],dtype=np.float64);
        
    elif N == 1:
        cvec = np.array([0],dtype=np.float64);
        amat = np.array([[0]],dtype=np.float64);
        bvec = np.array([[1]],dtype=np.float64);
        
    elif N == 6: # Default Dormand-Prince tableau from Orbit Determination
        cvec = np.array([0, 0.2, 0.3, 0.8, 8/9, 1, 1],dtype=np.float64);
        amat = np.array([
            [0,          0,           0,          0,        0,           0,     0],
            [1/5,        0,           0,          0,        0,           0,     0],
            [3/40,       9/40,        0,          0,        0,           0,     0],
            [44/45,      -56/15,      32/9,       0,        0,           0,     0],
            [19372/6561, -25360/2187, 64448/6561, -212/729, 0,           0,     0],
            [9017/3168,  -355/33,     46732/5247, 49/176,   -5103/18656, 0,     0],
            [35/384,     0,           500/1113,   125/192,  -2187/6784,  11/84, 0]],\
            dtype=np.float64);
        bvec = np.array([[35/384, 0, 500/1113, 125/192, -2187/6784, 11/84]],\
            dtype=np.float64);
        
    else:
        raise ValueError('Unsupported Runge-Kutta integration order');
    #
    bvec = bvec.T;
    
    # Compute time history
    tkhist = np.arange(tlims[0], tlims[1]+h, h);
    
    # Input sizes
    ny = y0.shape[0];
    nt = tkhist.shape[0];
    
    # Initialize integration loop
    ydotkhist = np.zeros((ny, nt));
    ykhist = np.zeros((ny, nt));
    ykhist[:,0] = y0;
    
    # Runge-Kutta integration loop
    for k in range(1,nt):
        
        # Initialize Runge Kutta step
        Kjhist = np.zeros((ny, N));
        ykm1 = ykhist[:,k-1];
        tkm1 = tkhist[k-1];
        
        # Runge-Kutta loop formulation
        Kjhist[:,0] = ydot(tkm1, ykm1).squeeze();
        for j in range(1,N):
            targ = tkm1 + h*cvec[j];
            Karg = ykm1.copy();
            for i in range(0, j):
                if amat[j,i] is not 0:
                    Karg = Karg + h*amat[j,i]*Kjhist[:,i];
                #
            #
            Kjhist[:,j] = ydot(targ, Karg).squeeze();
        #
        
        # Final compute state at time tk
        ykhist[:,k] = ykm1 + (h*np.matmul( Kjhist, bvec ).T);
        
        # Save ydot for ouptut
        ydotkhist[:,k-1] = Kjhist[:,0].squeeze();
    #
    
    # Save ydot for ouptut
    ydotkhist[:,nt-1] = ydot(tlims[1], ykhist[:,nt-1]).squeeze();
    return ykhist, tkhist, ydotkhist;
#