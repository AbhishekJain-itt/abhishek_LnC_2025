# 📍 Location Validation Utility

A lightweight Python utility to validate and sanitize user-provided location input before processing it in a geocoding workflow.

---

## 🚀 Overview

This module ensures that location input is valid, clean, and safe to use before making external API calls (e.g., Google Geocoding API).

It helps prevent:
- Invalid or empty requests
- Unnecessary API calls
- Runtime errors due to bad input

---

## ✅ Features

- Validates empty or null input  
- Handles whitespace-only strings  
- Enforces minimum length requirement  
- Sanitizes input using `.strip()`  
- Provides clear error messages  

---
