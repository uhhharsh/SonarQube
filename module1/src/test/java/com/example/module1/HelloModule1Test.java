package com.example.module1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class HelloModule1Test {
    @Test
    public void testSayHello() {
        HelloModule1 helloModule1 = new HelloModule1();
        assertEquals("Hello from Module 1 and Hello from module2", helloModule1.sayHello());
    }
}