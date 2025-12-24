public class DynamicArray {
    private int[] array;
    private int size;
    private int capacity;

    // Constructor
    public DynamicArray() {
        this.size = 0;
        this.capacity = 10;
        this.array = new int[capacity];
    }

    // Add element to the array
    public void append(int element) {
        if (size == capacity) {
            resize();
        }
        array[size] = element;
        size++;
    }

    // Resize the array (double the capacity)
    private void resize() {
        int[] newArray = new int[capacity * 2];
        for (int i = 0; i < size; i++) {  // Use size instead of capacity to avoid copying unused elements
            newArray[i] = array[i];
        }
        array = newArray;
        capacity *= 2;
    }

    // Get the element at a specific index
    public int get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        return array[index];
    }

    // Set the element at a specific index
    public void set(int index, int element) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        array[index] = element;
    }

    // Remove the last element and return it
    public int pop_back() {
        if (size == 0) {
            throw new IndexOutOfBoundsException("Array is empty");
        }
        int element = array[size - 1];
        size--;
        if (size > 0 && size < capacity / 4) {  // Shrink only if size > 0
            shrink();
        }
        return element;
    }

    // Shrink the array (halve the capacity)
    private void shrink() {
        int newCapacity = Math.max(10, capacity / 2);  // Ensure a minimum capacity of 10
        int[] newArray = new int[newCapacity];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
        capacity = newCapacity;
    }

    // Get the current size of the array
    public int size() {
        return size;
    }

    // Get the current capacity of the array
    public int capacity() {
        return capacity;
    }

    // Main method for testing
    public static void main(String[] args) {
        DynamicArray dynamicArray = new DynamicArray();

        // Test appending elements
        System.out.println("Appending elements:");
        for (int i = 1; i <= 15; i++) {
            dynamicArray.append(i);
            System.out.println("Added: " + i + ", Size: " + dynamicArray.size() + ", Capacity: " + dynamicArray.capacity());
        }

        // Test getting elements
        System.out.println("\nAccessing elements:");
        for (int i = 0; i < dynamicArray.size(); i++) {
            System.out.println("Element at index " + i + ": " + dynamicArray.get(i));
        }

        // Test setting elements
        System.out.println("\nSetting element at index 5 to 100:");
        dynamicArray.set(5, 100);
        System.out.println("Element at index 5 after setting: " + dynamicArray.get(5));

        // Test pop_back
        System.out.println("\nPopping elements from the back:");
        for (int i = 0; i < 10; i++) {
            int removed = dynamicArray.pop_back();
            System.out.println("Popped: " + removed + ", Size: " + dynamicArray.size() + ", Capacity: " + dynamicArray.capacity());
        }

        // Test shrinking to ensure capacity doesn't drop below minimum
        System.out.println("\nFinal Size: " + dynamicArray.size());
        System.out.println("Final Capacity: " + dynamicArray.capacity());
    }
}
