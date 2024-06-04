package com.example.module2;

import org.junit.Test;
import static org.junit.Assert.*;

public class HelloModule2Test {
    @Test
    public void testSayHello() {
        HelloModule2 helloModule2 = new HelloModule2();
        assertEquals("Hello from Module 2", helloModule2.sayHello());
    }
}
