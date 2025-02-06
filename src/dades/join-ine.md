# Issue with `mundissec` Column in `certificats.csv`

Brought to you by Team Raposos 🦊

## Problem Description

The `mundissec` column in `certificats.csv` represents the **unique identifier of the census section** where the building is located. In theory, this column should allow for a direct join with data from the **INE (Institut Nacional d'Estadística)**, using the census section identifier from both datasets. However, the codes **do not match**, preventing a straightforward merge.

## Example of the Issue

For example, in the municipality of **Abrera**:

- An example of a unique identifier of the census section from **INE** is:  
  **`0800101001`**  
  - `08001` → Municipal code  
  - `01001` → Section code  

- However, in **certificats.csv**, the `mundissec` value appears as:  
  **`08001801001`**  
  - Notice the **extra "8"** inserted between the municipal code and the section code.

This pattern appears across **all `mundissec` codes** in `certificats.csv`, making it impossible to directly join the datasets.

## Proposed Solution

The simplest way to fix this issue is to **remove the 6th character** from the `mundissec` column. This transformation will align the codes with those in the INE dataset.
This issue should be **taken into account** when performing analyses requiring census section-level information.

---

This document serves as a reference for anyone attempting to merge the datasets and ensures that the `mundissec` column is properly aligned with official census codes.