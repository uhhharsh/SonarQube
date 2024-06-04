package com.example.module2;

public class HelloModule2 {
    public String sayHello() {
        return "Hello from Module 2";
    }

    public static void main(String[] args){
        HelloModule2 hello = new HelloModule2();
        System.out.println(hello.sayHello());
    }
}
