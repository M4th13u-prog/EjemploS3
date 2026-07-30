using System;
using System.Windows.Forms;

namespace Ejercicio1_PlanillaTurnos //[cite: 1]
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Función para leer sueldos
        // Esta función recibe varios TextBox, lee sus valores y los guarda en un arreglo.[cite: 1]
        private double[] LeerSueldos(TextBox[] cajas)
        {
            // Creamos un arreglo del mismo tamaño que la cantidad de TextBox recibidos.[cite: 1]
            double[] sueldos = new double[cajas.Length];
            
            // Recorremos cada TextBox, convertimos su texto a double y lo guardamos.[cite: 1]
            for (int i = 0; i < cajas.Length; i++)
            {
                sueldos[i] = double.Parse(cajas[i].Text);
            }
            
            // Devolvemos el arreglo lleno.[cite: 1]
            return sueldos;
        }

        // Función para calcular total
        // Esta función suma todos los sueldos de un turno.[cite: 1]
        private double CalcularTotal(double[] datos)
        {
            // Acumulador para sumar los sueldos.[cite: 1]
            double total = 0;
            
            // Recorremos el arreglo y sumamos cada sueldo.[cite: 1]
            for (int i = 0; i < datos.Length; i++)
            {
                total = total + datos[i];
            }
            return total;
        }

        // Función para ordenar por burbuja
        // Esta función ordena un arreglo de menor a mayor.[cite: 1]
        private void OrdenarBurbuja(double[] datos)
        {
            // Método burbuja ascendente: ordena de menor a mayor.[cite: 1]
            for (int i = 0; i < datos.Length - 1; i++)
            {
                for (int j = 0; j < datos.Length - i - 1; j++)
                {
                    // Si el elemento actual es mayor que el siguiente, se intercambian.[cite: 1]
                    if (datos[j] > datos[j + 1])
                    {
                        double auxiliar = datos[j];
                        datos[j] = datos[j + 1];
                        datos[j + 1] = auxiliar;
                    }
                }
            }
        }

        // Función para mostrar resultados - Mostrar un arreglo en el ListBox
        // Esta función muestra los sueldos ordenados de un turno.[cite: 1]
        private void MostrarArreglo(string nombreTurno, double[] datos)
        {
            // Construimos una línea de texto con los sueldos del turno.[cite: 1]
            string linea = nombreTurno + ": ";
            
            // Agregamos cada sueldo a la línea.[cite: 1]
            for (int i = 0; i < datos.Length; i++)
            {
                linea += $"S/{datos[i]:F2} ";
            }
            
            // Mostramos la línea en el ListBox.[cite: 1]
            lstResultados.Items.Add(linea);
        }

        // Evento btnCalcular_Click
        // Este es el bloque principal. Se ejecuta cuando el usuario presiona Calcular y ordenar.[cite: 1]
        private void btnCalcular_Click(object sender, EventArgs e)
        {
            try
            {
                // Limpiamos resultados anteriores.[cite: 1]
                lstResultados.Items.Clear();
                
                // 1. Leemos los sueldos de cada turno.[cite: 1]
                double[] manana = LeerSueldos(new TextBox[] { txbM1, txbM2, txbM3 });
                double[] tarde = LeerSueldos(new TextBox[] { txbT1, txbT2 });
                double[] noche = LeerSueldos(new TextBox[] { txbN1, txbN2 });
                
                // 2. Calculamos el total de cada turno.[cite: 1]
                double totalManana = CalcularTotal(manana);
                double totalTarde = CalcularTotal(tarde);
                double totalNoche = CalcularTotal(noche);
                
                // 3. Mostramos los totales.[cite: 1]
                lstResultados.Items.Add("=== TOTALES POR TURNO ===");
                lstResultados.Items.Add($"Mañana: S/{totalManana:F2}");
                lstResultados.Items.Add($"Tarde: S/{totalTarde:F2}");
                lstResultados.Items.Add($"Noche: S/{totalNoche:F2}");
                
                // 4. Identificamos el turno con mayor gasto.[cite: 1]
                string turnoMayor = "Mañana";
                double mayorGasto = totalManana;
                
                if (totalTarde > mayorGasto)
                {
                    mayorGasto = totalTarde;
                    turnoMayor = "Tarde";
                }
                
                if (totalNoche > mayorGasto)
                {
                    mayorGasto = totalNoche;
                    turnoMayor = "Noche";
                }
                
                lblTurnoMayor.Text = $"Turno con mayor gasto: {turnoMayor} (S/{mayorGasto:F2})";
                
                // 5. Ordenamos los sueldos de cada turno.[cite: 1]
                OrdenarBurbuja(manana);
                OrdenarBurbuja(tarde);
                OrdenarBurbuja(noche);
                
                // 6. Mostramos los sueldos ordenados.[cite: 1]
                lstResultados.Items.Add("");
                lstResultados.Items.Add("=== SUELDOS ORDENADOS DE MENOR A MAYOR ===");
                MostrarArreglo("Mañana", manana);
                MostrarArreglo("Tarde", tarde);
                MostrarArreglo("Noche", noche);
            }
            catch (FormatException)
            {
                MessageBox.Show("Ingrese solo números válidos en los sueldos.", "Dato no válido", MessageBoxButtons.OK, MessageBoxIcon.Warning); //[cite: 1]
            }
            catch (Exception ex)
            {
                MessageBox.Show("Ocurrió un error: " + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error); //[cite: 1]
            }
        }

        // Evento btnLimpiar_Click
        // Este botón deja el formulario como al inicio.[cite: 1]
        private void btnLimpiar_Click(object sender, EventArgs e)
        {
            // Limpiamos los TextBox.[cite: 1]
            txbM1.Clear();
            txbM2.Clear();
            txbM3.Clear();
            txbT1.Clear();
            txbT2.Clear();
            txbN1.Clear();
            txbN2.Clear();
            
            // Limpiamos resultados.[cite: 1]
            lstResultados.Items.Clear();
            
            // Reiniciamos el texto del Label.[cite: 1]
            lblTurnoMayor.Text = "-";
            
            // Enviamos el foco al primer TextBox.[cite: 1]
            txbM1.Focus();
        }

        // Evento btnDatosPrueba_Click y método CargarDatosDePrueba
        // Este botón carga valores para probar rápidamente el programa.[cite: 1]
        private void btnDatosPrueba_Click(object sender, EventArgs e)
        {
            // Permite recargar los datos de prueba.[cite: 1]
            CargarDatosDePrueba();
        }

        private void CargarDatosDePrueba()
        {
            // Datos del turno mañana.[cite: 1]
            txbM1.Text = "1500";
            txbM2.Text = "1200";
            txbM3.Text = "1800";
            
            // Datos del turno tarde.[cite: 1]
            txbT1.Text = "1100";
            txbT2.Text = "1400";
            
            // Datos del turno noche.[cite: 1]
            txbN1.Text = "1000";
            txbN2.Text = "950";
            
            // Limpiamos resultados anteriores.[cite: 1]
            lstResultados.Items.Clear();
            lblTurnoMayor.Text = "Turno con mayor gasto: -";
        }
    }
}