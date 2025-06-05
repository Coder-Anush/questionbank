package com.questionbank.questionbank;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home() {
        return "index";
    }

    @GetMapping("/search")
    public String search(@RequestParam("query") String query, Model model) {
        String folderPath = "src/main/resources/static/papers";
        File folder = new File(folderPath);
        String[] files = folder.list();
        List<String> matchingFiles = new ArrayList<>();
        if (files != null) {
            matchingFiles = Arrays.stream(files)
                    .filter(name -> name.toLowerCase().contains(query.toLowerCase()))
                    .collect(Collectors.toList());
        }
        model.addAttribute("results", matchingFiles);
        return "result";
    }
}