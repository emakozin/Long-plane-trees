library(matlab)
#A je eden od zgeneriranih povpreččnih časov v pythonu
povprecen_cas=c(0.9841807842254638, 1.811055326461792, 3.1727452754974363, 5.515920400619507, 8.263189220428467, 12.534284591674805)
X=c(7,8,9,10,11,12)
X2=X^2
X3=X^3
X4=X^4
X5=X^5

model1 = lm(povprecen_cas~ X+ X2+X3)
model2 = lm(povprecen_cas~ X+ X2+X3+X4)


coefficients(model1)
coefficients(model2)

plot(X,povprecen_cas)

polinnom_4<-function(x){
y=100.93148059 -43.83011734*x   + 7.05648863*x^2  -0.50309271*x^3 +  0.01402215*x^4
return(y)}

polinnom_3<-function(x){
y= -4.7634621  +  2.4509826*x  -0.4413540*x^2  + 0.0297489*x^3 
return(y)}

G=linspace(6,15)
plot(X,povprecen_cas)
lines(G,polinnom_4(G))



