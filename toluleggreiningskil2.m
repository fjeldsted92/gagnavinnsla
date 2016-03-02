%Töluleg greinging skilaverkefni 2
%% Liður eitt.
close all
clear all
T=[20 30 40 50 60 70 80 90 100];
Y=[1.003 0.799 0.657 0.548 0.467 0.405 0.355 0.316 0.283];
% línugerum exp(c1+c2/T+c3/t^2)= Y i lnY = c1+c2/T + c3/T^2
tildaY=log(Y); %lnY
% búum til fylkið á úr upplýsingum út töflu.
A=[ 1 1/20 1/20^2;1 1/30 1/30^2;1 1/40 1/40^2;1 1/50 1/50^2; 
    1 1/60 1/60^2;1 1/70 1/70^2; 1  1/80 1/80^2;
    1  1/90 1/90^2; 1 1/100 1/100^2];

%kafli 5.4 laga kóða  til að nota simpson.
ATA=transpose(A)*A;
B=transpose(A)*transpose(tildaY);
C=ATA\B;
Yaprox=(C(1)+C(2)./T+C(3)./T.^2);
plot(T,Y,T,exp(Yaprox));
MSRE=0;
for i =1:9
MSRE=(Y(i)-exp(Yaprox(i)))^2+MSRE;
end
MSRE=sqrt(MSRE)/3;
%% Liður 2
Condition =cond(ATA); % tala af stærðargráðunni 10^7 höfum því 9 markverða tölustafi að hámarki.






%% Liður 3
GiskX=[1;1;1];
[lambdamax, eigenmax]=powerit(ATA,GiskX,100);
[lambdamin, eigenmin]=invpowerit(ATA,GiskX,0,100);
%fyrir fylki sem hafa normal gildir að |max(lambda)|/|min(lambda)|
condaprox=lambdamax/lambdamin;
% sjáum að þetta er sama tala og við fáum út úr cond (A)
%%liður 5 aðferð newton til að reikna nákvæmari C1 ,C2 og C3

res=C; % notum niðurstöðuna úr línulegri aðfallsgreiningu sem firsta gisk fyrir aðferð newton-gauss.
for l =1:20 %for lykkja sem inniheldur reiknirit fyrir newton gauss aðferðina.
jakobiF=makejakobi(res,T); %fall sem reiknar Jakóbífylkið 
FX=MakeR(res(1),res(2),res(3),Y,T); % fall sem reiknar R(c)

A=jakobiF'*jakobiF;
B=-jakobiF'*(FX);
S=A\(B);
res=res+S;

end
Ta=20:100;
NewtonAprox=exp(res(1)+res(2)./Ta+res(3)./Ta.^2);
linaprox=exp(C(1)+C(2)./Ta+C(3)./Ta.^2);
figure
plot(T,Y,Ta,NewtonAprox,Ta,linaprox);
NewtonError=0;
for i=1:9 
 NewtonError=Y(i)^2-NewtonAprox(i)^2+NewtonError;  % reiknum MSRE fyrir Betur stillt C
end
 MSRENewton=sqrt(NewtonError)/3;
 