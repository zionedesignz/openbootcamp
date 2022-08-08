public class Tema4{

    public static void main(String args[]) {
        /* IF */
        int numeroIf = 5;
        
        if(numeroIf > 0){
            System.out.println("El número " + numeroIf + " es positivo");
        } else if (numeroIf < 0) {
            System.out.println("El número " + numeroIf + " es negativo");
        } else {
            System.out.println("El número " + numeroIf + " es cero");
        }

        /* WHILE */
        int numeroWhile = 0;

        while(numeroWhile < 3) {
            numeroWhile++;
            System.out.println(numeroWhile);
        }

        /* DO WHILE */
        int numeroDoWhile = 3;

        do{
            numeroDoWhile++;
            System.out.println(numeroDoWhile);
        } while(numeroDoWhile < 3);

        /* FOR */
        for(int numeroFor=0; numeroFor<=3; numeroFor++){
            System.out.println(numeroFor);
        }

        /* SWITCH */
        String estacion = "VERANO";

        switch(estacion) {
            case "INVIERNO":
                System.out.println("La estación indicada es: " + estacion);
                break;
            case "PRIMAVERA":
                System.out.println("La estación indicada es: " + estacion);
                break;
            case "VERANO":
                System.out.println("La estación indicada es: " + estacion);
                break;
            case "OTOÑO":
                System.out.println("La estación indicada es: " + estacion);
                break;
            default:
                System.out.println("El valor no es una estación del año");
                break;
        }
    }
}