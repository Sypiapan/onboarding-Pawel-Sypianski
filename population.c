#include <stdio.h>
#include <cs50.h>


int main(void)
{
int start;
int end;
int year = 0;

do
{
  start = get_int("Enter start population ");
}
while(start < 9);

do
{
  end = get_int("Enter end population ");
}
while(end < start);

while(start<end)

{
  start+=start/4;
  start-=start/3;

  year++;
}
}

printf("Growth population from: %i\n to: %i\n takes: %i\n", start, end, year);