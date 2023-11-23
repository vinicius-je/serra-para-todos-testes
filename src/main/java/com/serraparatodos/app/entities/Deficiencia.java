package com.serraparatodos.app.entities;

import jakarta.persistence.*;

import java.io.Serializable;

@Entity
@Table(name = "deficiencia")
public class Deficiencia implements Serializable {
    static final Long serialVersionUID = 1l;
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer id;
    private String nomeDeficiencia;

//    @Column(name="fk_categoria")
//    private Long codigoCategoria;

    @ManyToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "fk_categoria")
    private CategoriaDeficiencia categoriaDeficiencia;

    public Deficiencia() { }

    public Deficiencia(Integer id, String nomeDeficiencia, CategoriaDeficiencia categoriaDeficiencia) {
        this.id = id;
        this.nomeDeficiencia = nomeDeficiencia;
        this.categoriaDeficiencia = categoriaDeficiencia;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNomeDeficiencia() {
        return nomeDeficiencia;
    }

    public void setNomeDeficiencia(String nomeDeficiencia) {
        this.nomeDeficiencia = nomeDeficiencia;
    }

    public CategoriaDeficiencia getCategoriaDeficiencia() {
        return categoriaDeficiencia;
    }

    public void setCategoriaDeficiencia(CategoriaDeficiencia categoriaDeficiencia) {
        this.categoriaDeficiencia = categoriaDeficiencia;
    }
}
