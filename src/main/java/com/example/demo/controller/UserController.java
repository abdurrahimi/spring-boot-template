package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import java.util.List;
import com.example.demo.repository.UserRepository;
import com.example.demo.models.Users;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserRepository userRepository;

    public UserController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @GetMapping
    public List<Users> getAllUsers() {
        return userRepository.findAll();
    }

    @SuppressWarnings("null")
    @GetMapping("/{id}")
    public Users getUserById(@PathVariable Long id) {
        System.out.println(id);
        return userRepository.findById(id).orElse(null);
    }

    @SuppressWarnings("null")
    @PostMapping("/")
    public Users createUser(@RequestBody Users user) {
        System.out.println("Received user data: " + user);
        user = userRepository.save(user); // Simpan objek setelah mencetak
        return user;
    }

    @SuppressWarnings("null")
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userRepository.deleteById(id);
    }
}