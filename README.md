# Chapter 4 – Comments (Clean Code Refactoring)

##  Objective

This exercise focuses on identifying **bad comments** in existing code and refactoring it by applying **Clean Code principles**.  
The goal is to write **self-documenting code** that minimizes the need for comments while improving readability, maintainability, and clarity.

---

## Why Most Comments Were Removed

In Clean Code, comments are not a substitute for poor naming or complex logic.  
Many comments exist only because the code is not clear enough.

> **The best comment is the one you don’t need to write.**  
> — Robert C. Martin (Clean Code)

After refactoring, most comments were removed because the code itself now explains the intent.

---

##  Types of Bad Comments Identified

### 1. Redundant Comments
Comments that repeat exactly what the code already states.

**Example:**
// Check if order is null
if (order == null)

Issue:
The comment repeats exactly what the code already states.

Resolution:
Removed the comment and relied on clear code.

### 2. Noise Comments

Example:

// This method processes an order
public async Task<OrderResult> ProcessOrder(Order order)

Issue:
Adds no new information beyond the method name.

Resolution:
Removed in favor of expressive method naming.

### 3. TODO / Placeholder Comments

Example:

// TODO: Fix this later

Issue:
Lacks context, intent, or ownership.

Resolution:
Replaced with proper validation logic or removed.

### 4. Historical / Attribution Comments

Example (Before):

// Added by John on 12/15/2023

Issue:
Version control systems already track authorship and history.

Resolution:
Removed completely.

### 5. Emotional or Emphasized Comments

Example (Before):

// This is important!!!

Issue:
Emotion does not explain intent.

Resolution:
Replaced with clear, structured code.

### 6. Obvious Comments

Example (Before):

// Log the error
Console.WriteLine(ex.Message);

Issue:
States the obvious.

Resolution:
Removed.
