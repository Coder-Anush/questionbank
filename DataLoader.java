package com.questionbank.questionbank;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Runs once at application startup:
 *   • guarantees the table is created (Hibernate does it automatically)
 *   • inserts sample rows if the table is empty
 */
@Configuration
public class DataLoader {

    @Bean
    CommandLineRunner initDatabase(PaperRepository repo) {
        return args -> {
            if (repo.count() == 0) {          // only bootstrap on an empty DB
                repo.save(new PaperInfo(
                        "CS101", "Programming Basics", "CS101_QP_May2023.pdf"));
                repo.save(new PaperInfo(
                        "MA201", "Mathematics II",    "MA201_Final_2022.pdf"));
                repo.save(new PaperInfo(
                        "EE110", "Electrical Circuits","EE110_Quiz1_2023.pdf"));
            }
        };
    }
}
