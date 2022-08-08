public class Tema3{

    public static void main(String args[]) {
        int value1 = 10;
        int value2 = 20;
        int value3 = 30;

        var result = sumar(value1, value2, value3);
        System.out.println(result);

        Coche miCoche = new Coche();
        miCoche.agregarPuertas();
        System.out.println(miCoche.numeroPuertas);
    }

    public static int sumar(int a, int b, int c) {
        return a + b + c;
    }
}

class Coche{
    int numeroPuertas = 4;

    public void agregarPuertas(){
        this.numeroPuertas++;
    }
}