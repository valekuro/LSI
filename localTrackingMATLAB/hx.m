function [ cnl ] = hx(xd, yd, zd, ancore)

cnl = [ (xd -ancore(1,1))^2 + (yd- ancore(1,2))^2 + (zd-ancore(1,3))^2
        (xd -ancore(2,1))^2 + (yd- ancore(2,2))^2 + (zd-ancore(2,3))^2
        (xd -ancore(3,1))^2 + (yd- ancore(3,2))^2 + (zd-ancore(3,3))^2
        (xd -ancore(4,1))^2 + (yd- ancore(4,2))^2 + (zd-ancore(4,3))^2]; 

end
