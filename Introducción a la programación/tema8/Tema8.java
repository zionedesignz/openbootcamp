public class Tema8 {
    public static void main(String[] args) {
        Persona myPersona = new Persona();
        myPersona.setEdad(55);
        myPersona.setNombre("Roberto");
        myPersona.setTelefono(666555444);

        System.out.println(myPersona.getEdad());
        System.out.println(myPersona.getNombre());
        System.out.println(myPersona.getTelefono());
    }
}

class Persona {

    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad(){
        return this.edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre(){
        return this.nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono(){
        return this.telefono;
    }
    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
}