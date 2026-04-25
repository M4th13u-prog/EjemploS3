using System;

class Program
{
    static void Main()
    {
        Console.Write("Ingrese su peso: ");
        double peso = Convert.ToDouble(Console.ReadLine());

        Console.Write("Ingrese su estatura: ");
        double estatura = Convert.ToDouble(Console.ReadLine());

        double imc = peso / Math.Pow(estatura, 2);

        Console.WriteLine("IMC: " + Math.Round(imc, 2));

        if (imc < 18.5)
            Console.WriteLine("Bajo peso");
        else if (imc < 25)
            Console.WriteLine("Normal");
        else if (imc < 30)
            Console.WriteLine("Sobrepeso");
        else
            Console.WriteLine("Obesidad");
    }
}