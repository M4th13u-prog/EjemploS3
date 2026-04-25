using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese su edad: ");
        int edad = int.Parse(Console.ReadLine());

        if (edad >= 18)
        {
            Console.WriteLine("Acceso permitido");
        }
        else
        {
            int faltan = Math.Abs(18 - edad);
            Console.WriteLine("Acceso denegado. Te faltan " + faltan + " años");
        }
    }
}