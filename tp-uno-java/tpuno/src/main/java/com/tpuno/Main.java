package com.tpuno;

import java.util.Scanner;

public class Main {
    static Scanner sctr = new Scanner(System.in);
    public static void main(String[] args) {
        
        System.out.println("Ingresa un numero");
        int numero = sctr.nextInt();
         
        for(int i = 0 ; i <= numero;i++){
            System.out.println("*".repeat(i));
        }
        
        System.out.println("Ingresa un numero");
        int N = sctr.nextInt();
        String linea = "";
        for(int i = 0 ; i < N ; i++ ){
            if(i % 2 != 0){
                linea = linea + String.valueOf(i);
                System.out.println(linea);
            }
        }

        

    }
}