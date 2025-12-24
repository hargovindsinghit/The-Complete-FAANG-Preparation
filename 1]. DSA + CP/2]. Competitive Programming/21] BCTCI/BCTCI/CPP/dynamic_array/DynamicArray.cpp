#include "DynamicArray.h"
#include <iostream>

DynamicArray::DynamicArray() : size(0), capacity(10)
{
    arr = new int[capacity];
}

DynamicArray::DynamicArray(const DynamicArray& d) : size(d.size), capacity(d.capacity)
{
    arr = new int[capacity];
    for (int i = 0; i < size; i++)
    {
        arr[i] = d.arr[i];
    }
}

DynamicArray::~DynamicArray()
{
    delete[] arr;
}

void DynamicArray::push_back(int value)
{
    if (size == capacity)
    {
        resize(capacity * 2);
    }
    arr[size++] = value;
}

void DynamicArray::pop_back()
{
    if (size > 0)
    {
        size--;
    }
    if (size < capacity / 4)
    {
        resize(capacity / 2);
    }
}

int DynamicArray::get(int index)
{
    if (index < 0 || index >= size)
    {
        std::cout << "Index out of bounds" << std::endl;
        return -1;
    }
    return arr[index];
}

void DynamicArray::set(int index, int value)
{
    if (index < 0 || index >= size)
    {
        std::cout << "Index out of bounds" << std::endl;
        return;
    }
    arr[index] = value;
}

void DynamicArray::resize(int new_capacity)
{
    int *new_arr = new int[new_capacity];
    for (int i = 0; i < size; i++)
    {
        new_arr[i] = arr[i];
    }
    delete[] arr;
    arr = new_arr;
    capacity = new_capacity;
}

int DynamicArray::get_size()
{
    return size;
}

