function df=makejakobi(C,T)
%fall sem b�r til jak�b�li�inn og F(x) fyrir hvert gildi � T sem vi� f�um.
df=zeros(9,3);

for i=1:9
df(i,1)=-exp(C(1)+C(2)/T(i)+C(3)/T(i)^2);
df(i,2)=-(1/T(i)*exp(C(1)+C(2)/T(i)+C(3)/T(i)^2));
df(i,3)=-(1/T(i)^2*exp(C(1)+C(2)/T(i)+C(3)/T(i)^2));
end