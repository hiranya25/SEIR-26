# SEIR Coursework Repository

This repository contains all assignments and practical lab code developed for the SEIR course.

---

## Overview

The repository currently includes two Python-based projects focused on web data extraction and similarity analysis.

---

## Project 1 – Web Scraper (`Project1.py`)

**Purpose:**
Scrape a given URL and extract structured information.

**Functionality:**

* Accepts a URL as input
* Extracts:

  * Page title
  * Body content
  * All URLs (hyperlinks) present on the page
* Displays extracted data in a structured format

**Core Concepts Used:**

* HTTP requests
* HTML parsing
* DOM traversal
* Data extraction

---

## Project 2 – SimHash Similarity (`Project2.py`)

**Purpose:**
Compare similarity between two web pages using SimHash.

**Functionality:**

* Accepts two URLs as input
* Extracts body content from both pages
* Generates SimHash values for each page
* Computes number of common bits between the two hashes
* Measures similarity using bit comparison logic

**Core Concepts Used:**

* Text preprocessing
* Feature hashing
* SimHash algorithm
* Bitwise comparison 

---

## Repository Structure

SEIR
├── Project1.py
├── Project2.py
└── README.md

---

## Requirements

* Python 3.x
* Required libraries:

  * requests
  * beautifulsoup4
  * sys

---

## How to Run

Run Project 1:

```
python Project1.py <url>
```

Run Project 2:

```
python Project2.py <url1> <url2>
```

---

## Academic Purpose

This repository is maintained for coursework, assignments, and practical lab submissions related to the SEIR course.
