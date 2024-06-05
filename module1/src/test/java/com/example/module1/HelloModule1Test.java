package com.example.module1;

import org.junit.Test;
import static org.junit.Assert.*;

public class HelloModule1Test {
    @Test
    public void testSayHello() {
        HelloModule1 helloModule1 = new HelloModule1();
        assertEquals("Hello from Module 1 and Hello from Module 2", helloModule1.sayHello());
        //TODO

    }
}