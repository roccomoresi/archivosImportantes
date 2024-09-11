package org.example.workZone;

public class CustomStack implements IStackTwo {

    private final int[] array;
    private int count;

    public CustomStack() {
        this.array = new int[10000];
        this.count = 0;
    }

    @Override
    public void add(int a) {
        this.array[this.count] = a;
        this.count++;
    }

    @Override
    public void remove() {

        if (count == 0) {

            System.out.println("No se puede remover nada de una pila que esta vacia");
            return;
        }
    }

    @Override
    public boolean isEmpty(){

        return this.count == 0;

    }

    @Override
    public int getTop() {
        if (count == 0) {
            System.out.println("No se puede desapilar una pila que esta vacia");
            return -1;
        }
        return this.array[this.count - 1];
    }
    public static void main(String[] args) {



    }


}
