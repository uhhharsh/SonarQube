package com.example.module1;

import com.example.module2.HelloModule2;

public class HelloModule1 {
    public String sayHello() {
        HelloModule2 module2 = new HelloModule2();
        return "Hello from Module 1 and " + module2.getMessage();
    }

}
