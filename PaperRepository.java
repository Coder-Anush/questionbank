package com.questionbank.questionbank;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

/**
 * CRUD methods are inherited from JpaRepository.
 */
public interface PaperRepository extends JpaRepository<PaperInfo, Long> {

    /* Custom finder for the search screen */
    List<PaperInfo> findByCodeContainingIgnoreCaseOrCourseContainingIgnoreCase(
            String codePart, String coursePart);
}
