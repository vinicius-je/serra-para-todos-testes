package com.serraparatodos.app.repository;

import com.serraparatodos.app.entities.CategoriaDeficiencia;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CategoriaDeficienciaRepository extends JpaRepository<CategoriaDeficiencia, Integer> {
}
