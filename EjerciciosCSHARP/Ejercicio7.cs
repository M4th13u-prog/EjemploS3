using System;

class Program
{
    static void Main()
    {
        // Inicializar el arreglo de asistencias de tamaño 5 y la bandera lógica
        int[] asistencia = new int[5];
        bool existeCero = false;
        int indiceModificar, nuevoValor;

        // 1. Registrar la asistencia de cada sesión
        Console.WriteLine("--- Registro de Asistencias ---");
        for (int i = 0; i < 5; i++)
        {
            Console.Write($"Ingrese la cantidad de asistentes para la sesión {i}: ");
            asistencia[i] = int.Parse(Console.ReadLine());
        }

        // 2. Mostrar todas las asistencias registradas
        Console.WriteLine("\n--- Asistencias Registradas ---");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Sesión {i}: {asistencia[i]}");
        }

        // 3. Verificar si alguna sesión tuvo exactamente 0 asistentes
        for (int i = 0; i < 5; i++)
        {
            if (asistencia[i] == 0)
            {
                existeCero = true;
            }
        }

        Console.WriteLine("\n--- Verificación de Asistencia ---");
        if (existeCero)
        {
            Console.WriteLine("Alerta: existe una sesión con 0 asistentes");
        }
        else
        {
            Console.WriteLine("No hay sesión con 0 asistentes");
        }

        // 4. Permitir modificar una asistencia indicando su índice
        Console.WriteLine("\n--- Modificar Asistencia ---");
        Console.Write("Ingrese el índice de la sesión a modificar (0 a 4): ");
        indiceModificar = int.Parse(Console.ReadLine());

        // Validación del índice (Equivalente al SI...SINO)
        if (indiceModificar >= 0 && indiceModificar < 5)
        {
            Console.Write("Ingrese el nuevo valor de asistencia: ");
            nuevoValor = int.Parse(Console.ReadLine());
            asistencia[indiceModificar] = nuevoValor;
            
            // 5. Mostrar las asistencias actualizadas
            Console.WriteLine("\n--- Asistencias Actualizadas ---");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Sesión {i}: {asistencia[i]}");
            }
        }
        else
        {
            Console.WriteLine("Índice no válido");
        }
    }
}