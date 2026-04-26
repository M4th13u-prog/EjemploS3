using System;

class Program
{
    static void Main()
    {
        Console.Write("Cantidad de empleados: ");
        int n = int.Parse(Console.ReadLine());
        double totalPlanilla = 0;

        for (int i = 1; i <= n; i++)
        {
            Console.WriteLine($"\nEmpleado {i}");
            Console.Write("Nombre: ");
            string nombre = Console.ReadLine();

            Console.Write("Horas trabajadas: ");
            double horas = double.Parse(Console.ReadLine());

            double sueldoBruto, horasExtra;

            if (horas <= 160)
            {
                sueldoBruto = horas * 12.5;
                horasExtra = 0;
            }
            else
            {
                horasExtra = horas - 160;
                sueldoBruto = (160 * 12.5) + (horasExtra * 25);
            }

            double descuento = sueldoBruto * 0.05;
            double sueldoNeto = sueldoBruto - descuento;

            totalPlanilla += sueldoNeto;

            Console.WriteLine($"Nombre: {nombre}");
            Console.WriteLine($"Horas extra: {horasExtra}");
            Console.WriteLine($"Sueldo bruto: {sueldoBruto}");
            Console.WriteLine($"Descuento: {descuento}");
            Console.WriteLine($"Sueldo neto: {sueldoNeto}");
        }

        Console.WriteLine($"\nTotal planilla: {totalPlanilla}");
    }
}