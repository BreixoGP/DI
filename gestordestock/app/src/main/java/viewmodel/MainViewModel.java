package viewmodel;

import data.StockRepository;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import java.util.List;

public class MainViewModel extends ViewModel {

    private final StockRepository repository;

    // LiveData del estado
    private final MutableLiveData<String> _stockState = new MutableLiveData<>();
    private final MutableLiveData<String> _errorState = new MutableLiveData<>();
    private final MutableLiveData<String> _eventoConfirmacion = new MutableLiveData<>(null);
    public MainViewModel(StockRepository repository) {
        this.repository = repository;
        refreshData();
    }

    public LiveData<String> getStockList() {
        return _stockState;
    }

    public LiveData<String> getError() {
        return _errorState;
    }
    public LiveData<String> getEventoConfirmacion(){
        return _eventoConfirmacion;
    }
    public void addNewProduct(String productName) {
        if (productName == null || productName.trim().isEmpty()) {
            _errorState.setValue("El nombre no puede estar vacío");
            return;
        }

        repository.addProduct(productName);
        refreshData();
    }
    public void deleteProduct(){
        boolean borrado = repository.removeLast();
        if (!borrado){
            _errorState.setValue("No hay productos para borrar");
            return;
        }
        refreshData();
        _eventoConfirmacion.setValue("Producto elimiado");

    }
    private void refreshData() {
        List<String> products = repository.getAllProducts();
        StringBuilder sb = new StringBuilder();
        for (String p : products) {
            sb.append("• ").append(p).append("\n");
        }
        _stockState.setValue(sb.toString());
    }
    public void consumirEventoConfirmacion(){
        _eventoConfirmacion.setValue(null);
    }
    public void consumirError(){
        _errorState.setValue(null);
    }
}