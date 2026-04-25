using System;

class Program
{
    static void Main()
    {
        Console.Write("Parcial: ");
        double parcial = Convert.ToDouble(Console.ReadLine());

        Console.Write("Final: ");
        double final = Convert.ToDouble(Console.ReadLine());

        Console.Write("P1: ");
        double p1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("P2: ");
        double p2 = Convert.ToDouble(Console.ReadLine());

        Console.Write("P3: ");
        double p3 = Convert.ToDouble(Console.ReadLine());

        double menor = Math.Min(p1, Math.Min(p2, p3));
        double prom_prac = (p1 + p2 + p3 - menor) / 2;
        double prom_final = (parcial + final + prom_prac) / 3;

        Console.WriteLine("Promedio final: " + prom_final);

        if (prom_final >= 18)
            Console.WriteLine("Excelente");
        else if (prom_final >= 14)
            Console.WriteLine("Bueno");
        else if (prom_final >= 10)
            Console.WriteLine("Regular");
        else
            Console.WriteLine("Deficiente");
    }
}