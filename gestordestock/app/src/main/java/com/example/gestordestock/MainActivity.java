package com.example.gestordestock;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

// IMPORTS DE NUESTRAS CLASES (Porque están en otros paquetes)
import data.StockRepository;
import viewmodel.MainViewModel;
import viewmodel.MainViewModelFactory;
import com.example.gestordestock.R; // Importante para encontrar R.layout

public class MainActivity extends AppCompatActivity {

    private MainViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //INICIALIZAR VISTAS
        EditText etProducto = findViewById(R.id.etProducto);
        Button btnGuardar = findViewById(R.id.btnGuardar);
        Button btnBorrar = findViewById(R.id.btnBorrar);
        TextView tvListado = findViewById(R.id.tvListado);

        // ARQUITECTURA
        StockRepository repository = new StockRepository();
        MainViewModelFactory factory = new MainViewModelFactory(repository);

        viewModel = new ViewModelProvider(this, factory).get(MainViewModel.class);

        // OBSERVAR DATOS
        viewModel.getStockList().observe(this, textoActualizado -> {
            tvListado.setText(textoActualizado);
        });
        // IMPORTANTE - En el caso de usar un fragment en vez de una activity cuando
        // hacemos el observe, usaremos getViewLifecycleOwner() en vez de this

        viewModel.getError().observe(this, mensajeError -> {
            if(mensajeError!=null) {
                Toast.makeText(this, mensajeError, Toast.LENGTH_SHORT).show();
                viewModel.consumirError();
            }
        });
        viewModel.getEventoConfirmacion().observe(this, mensaje ->{
            if(mensaje!=null){
                Toast.makeText(this, mensaje, Toast.LENGTH_SHORT).show();
                viewModel.consumirEventoConfirmacion();
            }
        });

        //CAPTURAR EVENTOS
        btnGuardar.setOnClickListener(v -> {
            String nombre = etProducto.getText().toString();
            viewModel.addNewProduct(nombre);
            etProducto.setText("");
        });
        btnBorrar.setOnClickListener( v ->  {
            viewModel.deleteProduct();
        });
    }
}