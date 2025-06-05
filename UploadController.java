package com.questionbank.questionbank.controller;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

@Controller
@RequestMapping("/upload")
public class UploadController {

    @PostMapping
    public String handleFileUpload(
            @RequestParam("courseName") String courseName,
            @RequestParam("courseCode") String courseCode,
            @RequestParam("year") String year,
            @RequestParam("files") MultipartFile[] files,
            Model model) {

        String uploadDir = "src/main/resources/static/papers";
        File dir = new File(uploadDir);
        if (!dir.exists()) dir.mkdirs();

        for (MultipartFile file : files) {
            try {
                file.transferTo(new File(dir, file.getOriginalFilename()));
                // Optionally, append metadata to a CSV file
                try (FileWriter fw = new FileWriter("src/main/resources/metadata.csv", true)) {
                    fw.write(String.format("%s,%s,%s,%s\n", file.getOriginalFilename(), courseName, courseCode, year));
                }
            } catch (IOException e) {
                model.addAttribute("message", "Failed to upload " + file.getOriginalFilename());
                return "upload";
            }
        }
        model.addAttribute("message", "Files uploaded successfully!");
        return "upload";
    }
}