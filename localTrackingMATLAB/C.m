function [ cl ] = C(xd, yd, zd, ancore )
cl = [  2*(xd -ancore(1,1))   0   0   2*(yd- ancore(1,2))   0   0   2*(zd-ancore(1,3))   0  0
        2*(xd -ancore(2,1))   0   0   2*(yd- ancore(2,2))   0   0   2*(zd-ancore(2,3))   0  0
        2*(xd -ancore(3,1))   0   0   2*(yd- ancore(3,2))   0   0   2*(zd-ancore(3,3))   0  0
        2*(xd -ancore(4,1))   0   0   2*(yd- ancore(4,2))   0   0   2*(zd-ancore(4,3))   0  0]; 
end

