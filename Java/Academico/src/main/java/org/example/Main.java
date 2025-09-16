package org.example;

import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double salario, credito;

        System.out.printf("Informe seu salário: ");
        salario = sc.nextDouble();

        if (salario > 0 && salario < 200.1) {
            System.out.printf("Nenhum crédito disponível.");
        } else if (salario > 200.1 &&  salario < 400) {
            credito = (salario * 0.2);
            System.out.println("Seu crédito é de R$" + credito);
        } else if (salario > 400.1 && salario < 600) {
            credito = (salario * 0.3);
            System.out.println("Seu crédito é de R$" + credito);
        } else if (salario > 600) {
            credito = (salario * 0.4);
            System.out.println("Seu crédito é de R$" + credito);
        } else {
            System.out.printf("Valor inválido.");
        }
    }
}