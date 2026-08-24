//Constantes
var numero = 10.20;
Console.WriteLine(numero);
numero = 3000;
Console.WriteLine(numero);

const int numero = 150;
Console.WriteLine("Valor de constante: " + numero2);
numero2 = 80;
Console.WriteLine(numero2);

const double PI = 3.1416;
const string MENSAJE = "Bienvenido a C#";
//Casting
//Casting implicito
int valor = 200;
int total = valor;
Console.WriteLine("implicito: " + valor);

//Casting explicito
double precio = 500.32;
int descuento = (int)precio;
Console.WriteLine("explicito: " + descuento);

char letra = 'A';
int codigoAsci = letra;
Console.WriteLine(codigoAsci);

string palabra = "123456";
int numero = Convert.ToInt32(palabra);
Console.WriteLine(numero);

string TextoDecimal= "123.45";
double valor3 = double.Parse(textoDecimal);
Console.WriteLine(valor3);