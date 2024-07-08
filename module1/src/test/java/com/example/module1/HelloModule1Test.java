package com.example.module1; //NOSONAR
 //NOSONAR
import org.junit.jupiter.api.Test; //NOSONAR
import static org.junit.jupiter.api.Assertions.assertEquals; //NOSONAR
 //NOSONAR
public class HelloModule1Test { //NOSONAR
    @Test //NOSONAR
    public void testSayHello() { //NOSONAR
        HelloModule1 helloModule1 = new HelloModule1(); //NOSONAR
        assertEquals("Hello from Module 1 and Hello from module2", helloModule1.sayHello()); //NOSONAR
    } //NOSONAR
} //NOSONAR
