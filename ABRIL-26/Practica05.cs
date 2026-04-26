using System;

class Program
{
    static void Main()
    {
        Console.Write("Número de días: ");
        int n = int.Parse(Console.ReadLine());

        double total = 0;
        double mayor = 0;
        double menor = double.MaxValue;

        int diaMayor = 0, diaMenor = 0;
        int excelente = 0, bueno = 0, regular = 0, malo = 0;

        for (int i = 1; i <= n; i++)
        {
            Console.Write($"Día {i} venta: ");
            double venta = double.Parse(Console.ReadLine());

            total += venta;

            if (venta > mayor)
            {
                mayor = venta;
                diaMayor = i;
            }

            if (venta < menor)
            {
                menor = venta;
                diaMenor = i;
            }

            if (venta >= 500)
                excelente++;
            else if (venta >= 200)
                bueno++;
            else if (venta >= 50)
                regular++;
            else
                malo++;
        }

        double promedio = total / n;

        Console.WriteLine("\nRESULTADOS:");
        Console.WriteLine("Total: " + total);
        Console.WriteLine("Promedio: " + promedio);
        Console.WriteLine($"Mayor venta: Día {diaMayor} = {mayor}");
        Console.WriteLine($"Menor venta: Día {diaMenor} = {menor}");

        Console.WriteLine("\nClasificación:");
        Console.WriteLine("Excelente: " + excelente);
        Console.WriteLine("Bueno: " + bueno);
        Console.WriteLine("Regular: " + regular);
        Console.WriteLine("Malo: " + malo);
    }
}