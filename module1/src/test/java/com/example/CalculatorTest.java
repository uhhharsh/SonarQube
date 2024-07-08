package com.example; //NOSONAR
 //NOSONAR
import org.junit.jupiter.api.Test; //NOSONAR
import static org.junit.jupiter.api.Assertions.assertEquals; //NOSONAR
 //NOSONAR
public class CalculatorTest { //NOSONAR
 //NOSONAR
    @Test //NOSONAR
    public void testAdd() { //NOSONAR
        Calculator calculator = new Calculator(); //NOSONAR
        assertEquals(5, calculator.add(2, 3)); //NOSONAR
        assertEquals(-1, calculator.add(2, -3)); //NOSONAR
        assertEquals(0, calculator.add(0, 0)); //NOSONAR
    } //NOSONAR
 //NOSONAR
    @Test //NOSONAR
    public void testSubtract() { //NOSONAR
        Calculator calculator = new Calculator(); //NOSONAR
        assertEquals(1, calculator.subtract(3, 2)); //NOSONAR
        assertEquals(5, calculator.subtract(2, -3)); //NOSONAR
        assertEquals(0, calculator.subtract(0, 0)); //NOSONAR
    } //NOSONAR
} //NOSONAR
