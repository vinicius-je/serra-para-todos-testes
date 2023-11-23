package com.serraparatodos.app.controller;


import com.serraparatodos.app.entities.Deficiencia;
import com.serraparatodos.app.repository.CategoriaDeficienciaRepository;
import com.serraparatodos.app.repository.DeficienciaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin
@RequestMapping("/deficiencia")
public class DeficienciaController {

    @Autowired
    private DeficienciaRepository deficienciaRepository;
    @Autowired
    private CategoriaDeficienciaRepository categoriaDeficienciaRepository;


    @GetMapping("/")
    public ResponseEntity<List<Deficiencia>> GetAllDeficiencias(){
        return ResponseEntity.ok().body(deficienciaRepository.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Deficiencia> GetDeficiencia(@PathVariable Integer id){
        return ResponseEntity.ok().body(deficienciaRepository.findById(id).get());
    }

}

