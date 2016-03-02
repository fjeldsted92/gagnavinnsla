function X=MakeR(C1,C2,C3,Y,T)

X=zeros(9,1);
for i=1:9
X(i)=Y(i)-exp(C1+C2/T(i)+C3/T(i)^2);
end