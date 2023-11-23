package com.serraparatodos.app.entities;

import jakarta.persistence.*;

import java.io.Serializable;

@Entity
@Table(name = "categoria_deficiencia")
public class CategoriaDeficiencia implements Serializable {
    static final Long serialVersionUID = 1l;
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer id;
    private String nomeCategoria;

    public CategoriaDeficiencia() {}

    public CategoriaDeficiencia(Integer id, String nomeCategoria) {
        this.id = id;
        this.nomeCategoria = nomeCategoria;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNomeDeficiencia() {
        return nomeCategoria;
    }

    public void setNomeDeficiencia(String nomeCategoria) {
        this.nomeCategoria = nomeCategoria;
    }
}
