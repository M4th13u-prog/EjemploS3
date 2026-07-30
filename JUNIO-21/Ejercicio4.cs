class Program
{
    static int ContarDigitos(int codigo)
    {
        int contador = 0;
        // Obtenemos el valor absoluto en caso de que sea negativo
        codigo = Math.Abs(codigo);
        
        if (codigo == 0) 
        {
            return 1;
        }
        
        while (codigo > 0)
        {
            contador = contador + 1;
            codigo = codigo / 10;
        }
        
        return contador;
    }

    static void Main(string[] args)
    {
        Console.Write("Ingrese el código: ");
        int codigo = int.Parse(Console.ReadLine());
        
        int digitos = ContarDigitos(codigo);
        
        if (digitos >= 6 && digitos <= 8)
        {
            Console.WriteLine("Código válido");
        }
        else
        {
            Console.WriteLine("Código inválido");
        }
    }
}