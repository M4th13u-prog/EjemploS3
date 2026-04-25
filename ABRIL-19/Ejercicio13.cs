using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese promedio: ");
        double prom = Convert.ToDouble(Console.ReadLine());

        if (prom < 0 || prom > 20)
            Console.WriteLine("Valor inválido");
        else if (prom < 10)
            Console.WriteLine("Malo");
        else if (prom < 14)
            Console.WriteLine("Regular");
        else if (prom < 15)
            Console.WriteLine("Bueno");
        else
            Console.WriteLine("Excelente");
    }
}