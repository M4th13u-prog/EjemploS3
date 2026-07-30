using System;

class Program
{
    static void Main(string[] args)
    {
        double[] temperaturas = new double[7];
        int diaEncontrado = -1;

        // Registrar temperaturas
        for (int i = 0; i < temperaturas.Length; i++)
        {
            Console.Write($"Ingrese temperatura del día {i + 1}: ");
            temperaturas[i] = double.Parse(Console.ReadLine());
        }

        // Buscar la primera temperatura mayor a 30°C
        for (int i = 0; i < temperaturas.Length; i++)
        {
            if (temperaturas[i] > 30 && diaEncontrado == -1)
            {
                diaEncontrado = i;
            }
        }

        // Mostrar resultado
        if (diaEncontrado != -1)
        {
            Console.WriteLine($"Primera alerta en día {diaEncontrado + 1}");
        }
        else
        {
            Console.WriteLine("No hubo alerta de temperatura");
        }

        Console.ReadKey();
    }
}