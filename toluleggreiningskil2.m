%T�luleg greinging skilaverkefni 2
%% Li�ur eitt.
close all
clear all
T=[20 30 40 50 60 70 80 90 100];
Y=[1.003 0.799 0.657 0.548 0.467 0.405 0.355 0.316 0.283];
% l�nugerum exp(c1+c2/T+c3/t^2)= Y i lnY = c1+c2/T + c3/T^2
tildaY=log(Y); %lnY
% b�um til fylki� � �r uppl�singum �t t�flu.
A=[ 1 1/20 1/20^2;1 1/30 1/30^2;1 1/40 1/40^2;1 1/50 1/50^2; 
    1 1/60 1/60^2;1 1/70 1/70^2; 1  1/80 1/80^2;
    1  1/90 1/90^2; 1 1/100 1/100^2];

%notum l�nulega a�fallsgreingu til �ess a� finna bestu gildi � C1,C2,C3
ATA=transpose(A)*A;
B=transpose(A)*transpose(tildaY);
C=ATA\B;
Yaprox=(C(1)+C(2)./T+C(3)./T.^2);
Yaprox2=(C(1)+C(2)./T+C(3)./T.^2);
plot(T,Y,T,exp(Yaprox));
figure
plot(T,tildaY,T,Yaprox2);
Err=0;
for i =1:9
Err=(Y(i)-exp(Yaprox(i)))^2+Err;

end
MSRE=sqrt(Err)/3;
%% Li�ur 2
Condition =cond(ATA); % tala af st�r�argr��unni 10^7 h�fum �v� 9 markver�a t�lustafi a� h�marki.






%% Li�ur 3
GiskX=[1;1;1];
[lambdamax, eigenmax]=powerit(ATA,GiskX,100);
[lambdamin, eigenmin]=invpowerit(ATA,GiskX,0,100);
%fyrir fylki sem hafa normal gildir a� |max(lambda)|/|min(lambda)|
condaprox=lambdamax/lambdamin;
% sj�um a� �etta er sama tala og vi� f�um �t �r cond (A)
%%li�ur 4 a�fer� newton til a� reikna n�kv�mari C1 ,C2 og C3

res=C; % notum ni�urst��una �r l�nulegri a�fallsgreiningu sem firsta gisk fyrir a�fer� newton-gauss.
for l =1:20 %for lykkja sem inniheldur reiknirit fyrir newton gauss a�fer�ina.
jakobiF=makejakobi(res,T); %fall sem reiknar Jak�b�fylki� 
FX=MakeR(res(1),res(2),res(3),Y,T); % fall sem reiknar R(c)

A=jakobiF'*jakobiF;
B=-jakobiF'*(FX);
S=A\(B);
res=res+S;

end
Ta=20:100;
NewtonAproxdraw=exp(res(1)+res(2)./Ta+res(3)./Ta.^2);
linaprox=exp(C(1)+C(2)./Ta+C(3)./Ta.^2);
figure
plot(T,Y,Ta,NewtonAproxdraw,Ta,linaprox);
NewtonAprox=exp(res(1)+res(2)./T+res(3)./T.^2);
NewtonError=0;
for i=1:9 
 NewtonError=(Y(i)-NewtonAprox(i))^2+NewtonError;  % reiknum MSRE fyrir Betur stillt C
end
 MSRENewton=sqrt(NewtonError)/3;

 % li�ur 5 gefum okkur a� U0 s� fasti 1. skiptum fjarl�g�inni h � 1000
 % jafnst�r bil og heildum me� tiliti til hita � sta�setningu �ar sem
 % T(y)=20+80/1000*(0+i) i er � bilinu [0:1000]
 f=@(s) 1/exp(res(1)+res(2)/s+res(3)/s^2);
 Uh1=adapquad(f,20,100,5*10^(-7));
 Uh2=zeros(1001,1);
 for i = 0:1000
 Uh2(i+1)=adapquad(f,20,80/1000*i+20,5*10^(-7));
 end
 M=Uh2/Uh1; % hra� m.v hitastig fyrir T0=20 T1=100, skiptum H � 1001 jafn st�r bil.
 
 f=@(s) 1/exp(res(1)+res(2)/s+res(3)/s^2);
 UHH=adapquad(f,100,20,5*10^(-7));
 YH=linspace(20,100,1001); % hitastigs mi�a� vi� sta�setningu
 UHH2=zeros(1001,1);
 
 for i = 0:1000;
 UHH2(i+1)=adapquad(f,100,100-80/1000*i,5*10^(-7));
 end
 M2=UHH2/UHH;  % Hra�i mi�a� vi� fjarl�g� fr� Pl�tu �egar T1 = 20 , T0=100
 H=linspace(0,1,1001); %sta�setning bilinu h skipt � 1001 b�ta �ar sem hver b�tur er h/1000 a� st�r� 
for i = 0:200 %einf�ld sem s�nir hverning hra�inn �r�ast 
    plot(M2*i,H,M*i,H);
    axis([-5 200 0 1]);
    title('Sta�setning M.t.t t�ma');
    xlabel('Sta�setning  eining [U0]')
   ylabel('Sta�setning � v�kva mi�a� vi� h');
    legend({'T0=100, T1=20','T0=20 T1=100'},'location','southeast');
    drawnow;
    
    pause(0.1);
end 
     

 