# Dinosaurs Data Analysis & Interactive Dashboard

An end-to-end exploratory data analysis and visualization project built out of curiosity to examine dinosaur species diversity, diets, geological eras, and geographic fossil distributions. The workflow combines Python for data cleaning and feature engineering with Power BI for interactive visual storytelling.

---

## Project Overview

* **Dataset Scope:** 312 dinosaur records spanning 53 countries, 6 geological eras, and 118 recorded discovery years.
* **Tools Used:** Python (`pandas`, `matplotlib`, `seaborn`) and Microsoft Power BI.
* **Deliverables:** Cleaned dataset (`updated_dinos.csv`), Python preprocessing script, and an interactive Power BI report.

---

## Data Cleaning & Feature Engineering

Starting from a raw dataset of **318 records**, the data was prepared in Python through the following steps:

1. **Data Retention & Missing Values:** Removed incomplete rows to retain **312 clean entries** (~98.1% retention).
2. **Manual Verification:** Manually verified and populated **4 missing field values** using external paleontological references to preserve record completeness.
3. **Schema Refinement:** Dropped ~8 unused columns and standardized location column naming (`found_it` → `founded_in_country`).
4. **Feature Engineering:**
   * **`era`:** Extracted the primary geological era from the raw `when_it_lived` text field.
   * **`decade`:** Derived the discovery decade using floor division (`(year // 10) * 10`) to enable grouped historical filtering.
5. **Domain-Specific Modeling:** Preserved multi-country fossil ranges (such as `Canada, USA`) as distinct categories rather than splitting them, accurately reflecting shared cross-border geological formations.

---

## Dashboard Highlights & Key Insights

The Power BI dashboard features interactive slicers for **Geological Era**, **Discovery Decade**, and **Diet**, alongside four high-level KPI cards and four core visuals:

* **Geological Era Distribution:** The **Late Cretaceous** period accounts for the largest share of entries (**143**), followed by the **Early Cretaceous** (**67**) and **Late Jurassic** (**43**).
* **Dietary Breakdown:** **Herbivorous** dinosaurs make up the majority of the dataset (**189**), followed by **carnivorous** (**95**) and **omnivorous** (**27**) species.
* **Dinosaur Types:** **Large theropods** (**61**), **sauropods** (**58**), and **small theropods** (**55**) represent the most common classifications.
* **Geographic Hotspots:** **China** (**49**) and the **USA** (**49**) lead in recorded fossil counts, followed by **Mongolia** (**39**) and **Argentina** (**30**).
