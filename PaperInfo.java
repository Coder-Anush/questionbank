package com.questionbank.questionbank;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * Represents one past‑question paper.
 */
@Entity
@Table(name = "paper_info")          // ← table name in H2
public class PaperInfo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;                 // primary key (auto)

    private String code;             // e.g. CS101
    private String course;           // e.g. Programming Basics
    private String file;             // e.g. cs101_2024.pdf (must exist in /static/papers)

    public PaperInfo() {}            // JPA needs a no‑arg constructor

    public PaperInfo(String code, String course, String file) {
        this.code   = code;
        this.course = course;
        this.file   = file;
    }

    /* ---------- getters / setters ---------- */
    public Long getId()      { return id; }
    public String getCode()  { return code; }
    public String getCourse(){ return course; }
    public String getFile()  { return file; }

    public void setCode(String code)       { this.code = code; }
    public void setCourse(String course)   { this.course = course; }
    public void setFile(String file)       { this.file = file; }
}
