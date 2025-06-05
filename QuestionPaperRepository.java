package com.questionbank.questionbank.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.questionbank.questionbank.model.QuestionPaper;

public interface QuestionPaperRepository extends JpaRepository<QuestionPaper, Long> {
    // Custom query methods can be defined here
}
