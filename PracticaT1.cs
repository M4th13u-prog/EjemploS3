using System;

// VARIABLES PARA LOS CONTADORES
int nuevos = 0;
int renovacion = 0;
int vencidos = 0;

Console.WriteLine("=== GESTIÓN DE CARNETS UNIVERSITARIOS ===");
Console.Write("Ingrese cuántos estudiantes desea evaluar: ");

// Validación básica para evitar errores al escribir
if (int.TryParse(Console.ReadLine(), out int cantidad))
{
    // ESTRUCTURA REPETITIVA
    for (int i = 1; i <= cantidad; i++)
    {
        Console.WriteLine($"\n--- Estudiante {i} ---");
        Console.Write("Ingrese el año de ingreso: ");
        
        if (int.TryParse(Console.ReadLine(), out int anio))
        {
            // ESTRUCTURA CONDICIONAL MÚLTIPLE
            if (anio == 2025)
            {
                Console.WriteLine("RESULTADO: Carnet nuevo");
                nuevos++;
            }
            else if (anio >= 2023 && anio <= 2024)
            {
                Console.WriteLine("RESULTADO: Carnet en renovación");
                renovacion++;
            }
            else // Para años anteriores a 2023
            {
                Console.WriteLine("RESULTADO: Carnet vencido, requiere trámite especial");
                vencidos++;
            }
        }
    }

    // RESUMEN FINAL SOLICITADO
    Console.WriteLine("\n=====================================");
    Console.WriteLine("          RESUMEN DE ENTREGA");
    Console.WriteLine("=====================================");
    Console.WriteLine($"Número de carnets nuevos: {nuevos}");
    Console.WriteLine($"Número de carnets en renovación: {renovacion}");
    Console.WriteLine($"Número de carnets vencidos: {vencidos}");
    Console.WriteLine("=====================================");
}
else
{
    Console.WriteLine("Error: Debe ingresar un número válido.");
}

Console.WriteLine("\nPresione cualquier tecla para cerrar...");
Console.ReadKey();