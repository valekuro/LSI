A_ = [ 1   TC   0.5*TC^2
       0   1    TC
       0   0    1       ];
   
A = [ A_ zeros(3,6)
      zeros(3,3) A_ zeros(3,3)
      zeros(3,6) A_];
  
F = [ 0.5*TC    0         0
      TC        0         0
      1         0         0
      0         0.5*TC    0
      0         TC        0
      0         1         0
      0         0         0.5*TC
      0         0         TC
      0         0         1      ];
  
Q = VAR_STATO * eye(3);
R = VAR_MISURA * eye(4);

