#include<stdio.h>
#include<math.h>
float find_des(float a,float b,float c){
	float D;
	D=(pow(b,2)-(4*a*c));
	return D;
}

float main(){
	float a,b,c,D,x1,x2,x;
	printf("enter a and b and c");
	scanf("%d%d%d",&a,&b,&c);
	

	D=find_des(a,b,c);
	if (D>0){
		x1=((-b)+sqrt(D))/(2*a);
		x2=((-b)-sqrt(D))/(2*a);

		printf("the roots are %d and %d",x1,x2);
		
	}else if(D==0){
		x=(-b)/(2*a);
		printf("the roots are %d",x);
	
	}else{
		printf("NO ROOTS EXIST  ");
	}
	return 0;
	
}
	
