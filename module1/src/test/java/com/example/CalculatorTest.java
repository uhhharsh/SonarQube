package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {
    
    @Test
    public void testAdd() {
        Calculator calculator = new Calculator();
        assertEquals(5, calculator.add(2, 3));
        assertEquals(-1, calculator.add(2, -3));
        assertEquals(0, calculator.add(0, 0));
    }

    @Test
    public void testSubtract() {
        Calculator calculator = new Calculator();
        assertEquals(1, calculator.subtract(3, 2));
        assertEquals(5, calculator.subtract(2, -3));
        assertEquals(0, calculator.subtract(0, 0));
    }
}
