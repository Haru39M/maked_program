#include <stdio.h>
double calc(int area,int people){
    double dens;
    dens = (double)people/area;
    return dens;
}

int main(void){
    int area_m,people_m;
    double dens_m;
    printf("calculate population density.\n");
    printf("population?[peoples]:");
    scanf("%d",&people_m);
    printf("area?[km^2]:");
    scanf("%d",&area_m);
    dens_m = calc(area_m,people_m);
    printf("pupulation density is %.3f [people/km^2]\n",dens_m);
    return 0;
}