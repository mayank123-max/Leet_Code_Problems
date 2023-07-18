#include<stdio.h>
void func_arr(int arr1[])
{
    int func_arr_size;
    fun_arr_size = sizeof(arr1)/sizeof(arr1[0]);
    printf("Array size in function:%d", func_arr_size);
}
int main()
{
    int arr1[4]= {1,2,3,4};
    func_arr(arr1);
    printf("\n Array size in main function:%d",sizeof(arr1)/sizeof(arr1[0]));
    return 0;
}