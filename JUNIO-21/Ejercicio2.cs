class Program
{
    static double CalcularImporte(int cantidad, double precio)
    {
        // El importe se obtiene multiplicando cantidad por precio.
        return cantidad * precio;
    }

    static void MostrarPedido(string plato, int cantidad, double importe)
    {
        Console.WriteLine($"Pedido: {plato} | Cantidad: {cantidad} | Importe: S/{importe:F2}");
    }

    static void Main(string[] args)
    {
        Console.WriteLine("=== CONTROL DE PEDIDOS DEL DÍA ===");
        // Acumulador del total vendido.
        double totalDia = 0;
        
        // Se registran 3 pedidos (según enunciado y caso de prueba).
        for (int i = 1; i <= 3; i++)
        {
            Console.WriteLine($"\nPedido {i}");
            Console.Write("Nombre del plato: ");
            string plato = Console.ReadLine();
            Console.Write("Cantidad: ");
            int cantidad = int.Parse(Console.ReadLine());
            Console.Write("Precio unitario: S/");
            double precio = double.Parse(Console.ReadLine());
            
            // Llamamos a la función que calcula el importe.
            double importe = CalcularImporte(cantidad, precio);
            
            // Acumulamos el importe del pedido.
            totalDia = totalDia + importe;
            
            // Mostramos el resumen del pedido actual.
            MostrarPedido(plato, cantidad, importe);
        }
        Console.WriteLine($"\nTotal vendido del día: S/{totalDia:F2}");
    }
}