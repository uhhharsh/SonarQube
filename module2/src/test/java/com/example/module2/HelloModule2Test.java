package com.example.module2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class HelloModule2Test {
    @Test
    public void testGetMessage() {
        HelloModule2 hello = new HelloModule2();
        assertEquals("Hello from module2", hello.getMessage());
    }
}
