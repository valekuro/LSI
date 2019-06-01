Tk = 0:TC:TFIN;

pos = [ cos(Tk)'  sin(Tk)'  (1+0.5*sin(2*Tk))'];
vel = [-sin(Tk)'  cos(Tk)'  cos(2*Tk)'];
aac = [-cos(Tk)' -sin(Tk)' -2*cos(2*Tk)'];