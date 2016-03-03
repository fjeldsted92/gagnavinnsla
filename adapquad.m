%Breyt fall úr bók  búði að breyta if lykkju úr tol0*3 í tol0*10 þar sem
%Þar sem trapízu regluni er skipt út fyrir simpson regluna
function int=adapquad(f,a0,b0,tol0)
int=0; 
n=1; 
a(1)=a0; 
b(1)=b0; 
tol(1)=tol0; 
app(1)=simp(f,a,b);
while n>0
     C=(a(n)+b(n))/2; 
     oldapp=app(n);
     app(n)=simp(f,a(n),C); 
     app(n+1)=simp(f,C,b(n));
     if abs(oldapp-(app(n)+app(n+1)))< 15*tol(n)
         int=int+app(n)+app(n+1);
         n=n-1;
     else 
         b(n+1)=b(n); b(n)=C;
         a(n+1)=C;
     tol(n)=tol(n)/2; 
     tol(n+1)=tol(n);
     n=n+1;
     end
end

function s=simp(f,a,b)
s=(b-a)/6 *(f(a)+4*f((b+a)/2)+f(b));