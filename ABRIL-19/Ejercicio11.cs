using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese categoría (A/B): ");
        string categoria = Console.ReadLine();

        Console.Write("Ingrese años de servicio: ");
        int años = int.Parse(Console.ReadLine());

        double sueldo = 1000;
        double bono = 0;

        if (categoria == "A")
        {
            if (años >= 5)
                bono = 200;
            else
                bono = 100;
        }
        else
        {
            if (años >= 5)
                bono = 150;
            else
                bono = 50;
        }

        double total = sueldo + bono;

        Console.WriteLine("Sueldo final: " + total);
    }
}