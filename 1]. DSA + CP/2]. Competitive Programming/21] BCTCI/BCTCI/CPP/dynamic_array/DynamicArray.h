#ifndef DYANMIC_ARRAY_H
#define DYANMIC_ARRAY_H

#include <iostream>
class DynamicArray
{
private:
    int *arr;
    int size;
    int capacity;
    void resize(int new_capacity);
public:    
    DynamicArray();
    DynamicArray(const DynamicArray& d);
    ~DynamicArray();
    void push_back(int value);
    void pop_back();
    int get(int index);
    void set(int index, int value);
    int get_size();
};

#endif // DYANMIC_ARRAY_H