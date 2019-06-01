close all
clc 
clear all

parametri;
sistema;
traiettoria;

passi    = numel(pos(:,1));
% inizializzo variabili per plot
kalman   = zeros(passi,3);
reale    = [pos(:,1) pos(:,2) pos(:,3)];
nofilter = zeros(passi,3);
P_trace  = zeros(passi,3);

% funzione per triangolazione iperbolica
f_triang = @(x,dist) [(x(1) - BEACON(1,1))^2 + (x(2) - BEACON(1,2))^2 + (x(3) - BEACON(1,3))^2 - dist(1)
                      (x(1) - BEACON(2,1))^2 + (x(2) - BEACON(2,2))^2 + (x(3) - BEACON(2,3))^2 - dist(2)
                      (x(1) - BEACON(3,1))^2 + (x(2) - BEACON(3,2))^2 + (x(3) - BEACON(3,3))^2 - dist(3)
                      (x(1) - BEACON(4,1))^2 + (x(2) - BEACON(4,2))^2 + (x(3) - BEACON(4,3))^2 - dist(4)];
                  
x_triang = [pos(1,1) pos(1,2) pos(1,3)];

% Inizializzo filtro
% stato iniziale
x =[pos(1,1) 0 0 pos(1,2) 0 0 pos(1,3) 0 0]';

% covarianza d'errore di stima iniziale
P = eye(9);


for i = 1:passi
    x    = A*x;
    P    = A*P*A' + F*Q*F';
    Clin = C(x(1),x(4),x(7),BEACON);
    K = (P*Clin')/(Clin*P*Clin' + R);
    
    % simulo misure con rumore
    misure = hx(pos(i,1),pos(i,2),pos(i,3),BEACON) + VAR_MISURA*[randn randn randn randn]';
    
    x_triang =  fminsearch(@(x) norm(f_triang(x,misure)),[0 0 0]);
    nofilter(i,:) = x_triang;
    
    x = x+ K *(misure - hx(x(1),x(4),x(7),BEACON));
    kalman(i,:) = [x(1) x(4) x(7)];
    P_trace(i,:) = [P(1,1)  P(4,4)  P(7,7)];
    P = (eye(9)- K*Clin)*P;
    
end

asse_x = 0:TC:TFIN;

figure(1)

subplot(3,1,1)
plot(asse_x,reale(:,1),'r-',asse_x,nofilter(:,1),'g-',asse_x,kalman(:,1),'b-');
legend('reale','no filter','kalman')
title('Stima posizioni x y z');
ylabel('Pos. X')

subplot(3,1,2)
plot(asse_x,reale(:,2),'r-',asse_x,nofilter(:,2),'g-',asse_x,kalman(:,2),'b-');
legend('reale','no filter','kalman')
ylabel('Pos. Y')

subplot(3,1,3)
plot(asse_x,reale(:,3),'r-',asse_x,nofilter(:,3),'g-',asse_x,kalman(:,3),'b-');
legend('reale','no filter','kalman')
ylabel('Pos. Z')

figure(2)
subplot(3,1,1)
plot(asse_x, reale(:,1) - nofilter(:,1), 'r-',asse_x, reale(:,1) - kalman(:,1), 'b-')
legend('no filter','kalman')
title('Errore di stima x y z');
ylabel('Err. X')

subplot(3,1,2)
plot(asse_x, reale(:,2) - nofilter(:,2), 'r-',asse_x, reale(:,2) - kalman(:,2), 'b-')
legend('no filter','kalman')
ylabel('Err. Y')

subplot(3,1,3)
plot(asse_x, reale(:,3) - nofilter(:,3), 'r-',asse_x, reale(:,3) - kalman(:,3), 'b-')
legend('no filter','kalman')
ylabel('Err. Z')

asse_x = 0:TC:1;

figure(3)
subplot(3,1,1)
plot(asse_x,P_trace(1:numel(asse_x),1),'r-');
title('Covarianza errore di stima x y z');
ylabel('Cov. P(X)')
subplot(3,1,2)
plot(asse_x,P_trace(1:numel(asse_x),2),'g-');
ylabel('Cov. P(Y)')
subplot(3,1,3)
plot(asse_x,P_trace(1:numel(asse_x),3),'b-');
ylabel('Cov. P(Z)')