package com.serraparatodos.app.repository;

import com.serraparatodos.app.entities.Deficiencia;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DeficienciaRepository extends JpaRepository<Deficiencia, Integer> {
}
