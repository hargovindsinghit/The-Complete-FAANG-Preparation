#include "DynamicArray.h"
#include <iostream>

int main() {
    DynamicArray d;
    d.push_back(1);
    d.push_back(2);
    d.push_back(3);
    d.push_back(4);

    std::cout << d.get(0) << std::endl;
    std::cout << d.get(1) << std::endl;
    std::cout << d.get(2) << std::endl;
    std::cout << d.get(3) << std::endl;
    
    return 0;
}