package tema9;

public class Tema9 {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.edad = 19;
        cliente.nombre = "Jesús";
        cliente.telefono = 666555444;
        cliente.credito = 3500.5;
        
        System.out.println("La edad del cliente es: " + cliente.edad);
        System.out.println("El nombre del cliente es: " + cliente.nombre);
        System.out.println("El teléfono del cliente es: " + cliente.telefono);
        System.out.println("El credito del cliente es: " + cliente.credito);

        Trabajador trabajador = new Trabajador();
        trabajador.edad = 25;
        trabajador.nombre = "Pepe";
        trabajador.telefono = 666444555;
        trabajador.salario = 1999.99;
        
        System.out.println("La edad del trabajador es: " + trabajador.edad);
        System.out.println("El nombre del trabajador es: " + trabajador.nombre);
        System.out.println("El teléfono del trabajador es: " + trabajador.telefono);
        System.out.println("El credito del trabajador es: " + trabajador.salario);
    }
}

class Persona {
    int edad;
    String nombre;
    int telefono;
}

class Cliente extends Persona {
    double credito;
}

class Trabajador extends Persona {
    double salario;
}