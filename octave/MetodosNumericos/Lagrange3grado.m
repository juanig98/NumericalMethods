 function [p] = Lagrange3grado (x ,y)
format short;
a = 1;
b = [ abs(x(2) * x(3) * x(4)) ^ (1/3) , 
        abs(x(1) * x(3) * x(4)) ^ (1/3) , 
        abs(x(1) * x(2) * x(4)) ^ (1/3) , 
        abs(x(1) * x(2) * x(3)) ^ (1/3)]
        
m = [ a,  -3*(a^2)*b(1),  3*a*(b(1)^2),   -b(1)^3; 
          a,  -3*(a^2)*b(2),  3*a*(b(2)^2),   -b(2)^3; 
          a,  -3*(a^2)*b(3),  3*a*(b(3)^2),   -b(3)^3; 
          a,  -3*(a^2)*b(4),  3*a*(b(4)^2),   -b(4)^3]

disp("\nP(x) =");
disp(m);

for i=1:4
  divisor = 1;
  for j=1:4
    if i~=j
      divisor = divisor * (x(i)-x(j));
    endif
  endfor
  
  if divisor ~= 0
    m(i,:) = y(i) * m(i,:) / divisor;
  endif
endfor


##m(1,:) = y(1) * m(1,:) / ( (x(1)-x(2)) * (x(1)-x(3)) * (x(1)-x(4)) );
##m(2,:) = y(2) * m(2,:) / ( (x(2)-x(1)) * (x(2)-x(3)) * (x(2)-x(4)) );
##m(3,:) = y(3) * m(3,:) / ( (x(3)-x(1)) * (x(3)-x(2)) * (x(3)-x(4)) );
##m(4,:) = y(4) * m(4,:) / ( (x(4)-x(1)) * (x(4)-x(2)) * (x(4)-x(3)) );

p = m(1,:)+m(2,:)+m(3,:)+m(4,:);

disp("\nP(x) =");
disp(m);