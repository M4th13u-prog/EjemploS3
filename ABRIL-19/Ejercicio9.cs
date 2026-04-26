using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese una opción (1-3): ");
        int opcion = int.Parse(Console.ReadLine());

        switch (opcion)
        {
            case 1:
                Console.WriteLine("Elegiste opción 1");
                break;
            case 2:
                Console.WriteLine("Elegiste opción 2");
                break;
            case 3:
                Console.WriteLine("Elegiste opción 3");
                break;
            default:
                Console.WriteLine("Opción inválida");
                break;
        }
    }
}