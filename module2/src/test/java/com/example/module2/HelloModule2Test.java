package com.example.module2; //NOSONAR
 //NOSONAR
import org.junit.jupiter.api.Test; //NOSONAR
import static org.junit.jupiter.api.Assertions.assertEquals; //NOSONAR
 //NOSONAR
public class HelloModule2Test { //NOSONAR
    @Test //NOSONAR
    public void testGetMessage() { //NOSONAR
        HelloModule2 hello = new HelloModule2(); //NOSONAR
        assertEquals("Hello from module2", hello.getMessage()); //NOSONAR
    } //NOSONAR
} //NOSONAR
