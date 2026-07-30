class Program
{
    static double CalcularPorcentaje(int presentes, int matriculados)
    {
        // Se hace un casting a double para no perder decimales
        return (double)presentes * 100 / matriculados;
    }

    static void Main(string[] args)
    {
        double sumaPorcentajes = 0;

        for (int sesion = 1; sesion <= 4; sesion++)
        {
            Console.WriteLine($"\n-- Sesión {sesion} --");
            Console.Write("Cantidad de presentes: ");
            int presentes = int.Parse(Console.ReadLine());
            
            Console.Write("Cantidad de matriculados: ");
            int matriculados = int.Parse(Console.ReadLine());
            
            double porcentaje = CalcularPorcentaje(presentes, matriculados);
            Console.WriteLine($"Porcentaje sesión {sesion}: {porcentaje:F2}%");
            
            sumaPorcentajes = sumaPorcentajes + porcentaje;
        }

        double promedio = sumaPorcentajes / 4;
        Console.WriteLine($"\nPromedio de asistencia: {promedio:F2}%");

        if (promedio >= 75) // En el texto indica "al menos 75%" (>= 75)
        {
            Console.WriteLine("Participación adecuada");
        }
        else
        {
            Console.WriteLine("Reforzar asistencia");
        }
    }
}