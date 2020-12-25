#include <stdio.h>

double BMI_calc(double weight,double height){
    double BMI = weight/((height/100)*(height/100));
    return BMI;
}

double Rohrer_calc(double weight,double height){
    double Rohrer = weight*10/((height/100)*(height/100)*(height/100));
    return Rohrer;
}

int main(){
    double BMI = 0.0;
    double Rohrer = 0.0;
    double height = 0.0;
    double weight = 0.0;
    int AorC = 0;

    printf("Input (Adult: 0, Child:1)");
    scanf("%d",&AorC);
    
    if((AorC != 0)&&(AorC != 1)){
        printf("Error!\n");
        return 0;
    }
    
    printf("Input height(cm):");
    scanf("%lf",&height);
    printf("Input weight(kg):");
    scanf("%lf",&weight);

    printf("Height(cm) = %f \n",height);
    printf("Weight(kg) = %f \n",weight);

    //計算
    if(AorC == 0){
    
        BMI = BMI_calc(weight,height);

        if(BMI >= 30){
            printf("BMI:%f --> Obese \n",BMI);
        }else if(BMI >= 25){
            printf("BMI:%f --> Oberweight \n",BMI);
        }else if(BMI >= 18.5){
            printf("BMI:%f --> Normal \n",BMI);
        }else{
            printf("BMI:%f --> Underweight \n",BMI);
        }
        
    }else if(AorC == 1){
    
        Rohrer = Rohrer_calc(weight,height);

        if(Rohrer >= 160){
            printf("Rohrer index:%f --> Obese \n",Rohrer);
        }else if(Rohrer >= 145){
            printf("Rohrer index:%f --> Overweight \n",Rohrer);
        }else if(Rohrer >= 115){
            printf("Rohrer index:%f --> Normal \n",Rohrer);
        }else{
            printf("Rohrer index:%f --> Underweight \n",Rohrer);
        }
        
    }
    return 0;
}
