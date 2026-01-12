package data;


import java.util.ArrayList;
import java.util.List;

public class StockRepository {
    // Esta lista simula nuestra Base de Datos
    private final List<String> database = new ArrayList<>();

    public StockRepository() {
        // Datos iniciales
        //database.add("Portátil Gaming");
        //database.add("Ratón USB");
    }

    // Método para LEER datos
    public List<String> getAllProducts() {
        return new ArrayList<>(database);
    }

    // Método para ESCRIBIR datos
    public void addProduct(String product) {
        database.add(product);
    }
    public  boolean removeLast(){
        if (database.isEmpty()){
            return false;}
        else{
            database.remove(database.size()-1);
            return true;
        }

    }
}