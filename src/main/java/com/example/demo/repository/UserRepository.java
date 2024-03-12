package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.demo.models.Users;

@Repository
public interface UserRepository extends JpaRepository<Users, Long> {
    // Anda dapat menambahkan metode repositori khusus di sini jika diperlukan
}
