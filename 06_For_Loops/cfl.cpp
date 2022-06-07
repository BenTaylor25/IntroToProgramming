#include <iostream>

void print(int i)
{
    std::cout << i << std::endl;
}

int main()
{
    for (int i = 0; i < 5; i++)
    {
        print(i);
    }

    int lst[] = {10, 9, 8};
    for (int x : lst)
    {
        print(x);
    }
}
