package com.example.aula.ui;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.AuthRepository;
import com.example.aula.viewmodel.AuthViewModel;
import com.example.aula.viewmodel.AuthViewModelFactory;
import com.example.aula.viewmodel.SettingsViewModel;
import com.example.aula.viewmodel.SettingsViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.materialswitch.MaterialSwitch;

public class ProfileFragment extends Fragment {

    private AuthViewModel vm;

    public ProfileFragment(){
        super(R.layout.fragment_profile);
    }


    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState){
        super.onViewCreated(view, savedInstanceState);


        TextView Username = view.findViewById(R.id.textViewUsername);
        MaterialButton botonLogout = view.findViewById(R.id.btnLogout);
        MaterialSwitch switchDark = view.findViewById(R.id.switchDarkMode);

        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        SettingsViewModelFactory settingsFactory = new SettingsViewModelFactory(requireContext());
        SettingsViewModel settingsVm = new ViewModelProvider(this, settingsFactory)
                .get(SettingsViewModel.class);


        settingsVm.getDarkMode().observe(getViewLifecycleOwner(), enabled -> {
            if (enabled == null) return;

            if (switchDark.isChecked() != enabled) {
                switchDark.setChecked(enabled);
            }

            AppCompatDelegate.setDefaultNightMode(
                    enabled ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });

        switchDark.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsVm.setDarkMode(isChecked);
        });

        vm = new ViewModelProvider(requireActivity(), factory).get(AuthViewModel.class);

        vm.getUserEmail().observe(getViewLifecycleOwner(), email -> {
            if (email != null) {
                Username.setText(email); //
            }
        });


        vm.getNavEvent().observe(getViewLifecycleOwner(), event -> {
            if ("LOGIN".equals(event)) {
                NavHostFragment.findNavController(this).navigate(R.id.action_fragment_profile_to_loginFragment);
                vm.consumeNavEvent();
            }
        });

        botonLogout.setOnClickListener(v -> vm.logout());
        // 6. Pedimos cargar el email al entrar
        vm.loadUserEmail(); // Solicita la carga de la información del usuario
    }
}
