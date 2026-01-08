# Tumblr Image Fetcher (API v1)

This project fetches images from a public Tumblr blog using **Tumblr API v1**.
It retrieves basic blog information and lists the highest-quality image URLs
(1280 resolution) for a user-specified range of photo posts.

---

# Features

- Uses **Tumblr API v1** (JSON over HTTPS)
- Fetches **public photo posts**
- Prints basic blog metadata:
  - Title
  - Name
  - Description
  - Total number of posts
- Extracts **highest-quality images (1280)**
- Supports:
  - Single-image posts
  - Multi-image posts (photosets)
- Follows **Clean Code principles**

---



## Python dependencies
```bash
pip install requests
