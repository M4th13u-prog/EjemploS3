using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese el monto de la compra: ");
        double monto = Convert.ToDouble(Console.ReadLine());

        double descuento = 0;

        if (monto >= 100)
        {
            descuento = monto * 0.10;
        }

        double total = monto - descuento;

        Console.WriteLine("Total a pagar: " + total);
    }
}