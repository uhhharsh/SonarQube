package com.example.module1; //NOSONAR
 //NOSONAR
import com.example.module2.HelloModule2; //NOSONAR
 //NOSONAR
public class HelloModule1 { //NOSONAR
    public String sayHello() { //NOSONAR
 //NOSONAR
        System.out.println("Testing PR"); //NOSONAR
 //NOSONAR
        System.out.println("Testing git diff"); //NOSONAR
 //NOSONAR
        System.out.println("Branch Test1"); //NOSONAR
 //NOSONAR
        HelloModule2 module2 = new HelloModule2(); //NOSONAR
        return "Hello from Module 1 and " + module2.getMessage(); //NOSONAR
    } //NOSONAR
 //NOSONAR
    public int task1(int a, int b) { //NOSONAR
        return a + b; //NOSONAR
    } //NOSONAR
 //NOSONAR
    public int task2(int a, int b) { //NOSONAR
        int sum = a  + b; //NOSONAR
        return sum; //NOSONAR
    } //NOSONAR
 //NOSONAR
    //TODO //NOSONAR
} //NOSONAR
