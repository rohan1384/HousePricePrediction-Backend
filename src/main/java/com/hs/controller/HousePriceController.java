package com.hs.controller;


import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5176") // Allow frontend access
public class HousePriceController {

    private final RestTemplate restTemplate = new RestTemplate();

    @GetMapping("/predict")
    public ResponseEntity<?> predictHousePrice(
            @RequestParam double medInc,
            @RequestParam double houseAge,
            @RequestParam double aveRooms,
            @RequestParam double aveOccup) {

        try {
            // Flask API URL
            String flaskUrl = "http://localhost:5000/predict?medInc=" + medInc +
                    "&houseAge=" + houseAge +
                    "&aveRooms=" + aveRooms +
                    "&aveOccup=" + aveOccup;

            // Call Flask API
            ResponseEntity<Map> response = restTemplate.getForEntity(flaskUrl, Map.class);

            return ResponseEntity.ok(response.getBody());

        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("error", "Server error: " + e.getMessage()));
        }
    }
}

