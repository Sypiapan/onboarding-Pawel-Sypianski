#include <stdio.h>
#include <cs50.h>


int main(void)
{
int space;
int column;

do
{
  int height = get_int("Height: ");
}
while(1 > height || height > 8)


for(int row=0; row <height; row++)
{
    for(int space=0; space<height-row-1; space++)
    {
    printf(" ");
}
    
   for(int column=0; column <=row; column++)
    {
    printf("x");
}

printf("\n");
}