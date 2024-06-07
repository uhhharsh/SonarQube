package com.example.module1;

import com.example.module2.HelloModule2;

public class HelloModule1 {
    public String sayHello() {
        HelloModule2 module2 = new HelloModule2();
        return "Hello from Module 1 and " + module2.getMessage();
    }

    public static void main(String[] args){
        HelloModule1 hello = new HelloModule1();
        System.out.println(hello.sayHello());

        //TODO

        System.out.println("YO");

        System.out.println("Automatic Assign?");
    }
}
