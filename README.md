
## 🧪 Glucose Estimator (Colorimetric Method)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/yourusername/glucose-estimator.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A simple Python tool to estimate **glucose concentration** in biological samples using the **colorimetric method** and **linear regression**.
This project helps students and researchers analyze absorbance–concentration relationships and predict unknown glucose levels from standard curve data — all from the command line.

---

### 🚀 Features

* Input standard glucose concentrations and absorbance values manually
* Fits a linear regression model automatically
* Estimates glucose concentration for unknown/test samples
* Displays the standard curve equation (Y = mX + c)
* Lightweight and easy to run — only uses `numpy` and `scikit-learn`

---

### 🧰 Requirements

Ensure you have Python and the following libraries installed:

```bash
python >= 3.8
numpy
scikit-learn
```

Install dependencies using pip:

```bash
pip install numpy scikit-learn
```

---

### 🧫 Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/glucose-estimator.git
   cd glucose-estimator
   ```

2. Run the Python script:

   ```bash
   python glucose_estimator.py
   ```

3. Enter standard data points:

   * Example:

     ```
     Concentration (mg/dL): 50  
     Absorbance: 0.12  
     Concentration (mg/dL): 100  
     Absorbance: 0.24  
     done
     ```

4. Enter test absorbance value when prompted.
   The program will display:

   * Estimated glucose concentration
   * Standard curve regression equation

---

### 📈 Example Output

```
--- Glucose Estimator (Colorimetric method) ---

Enter standard values for Glucose estimation (Enter 'done' to finish):
Concentration (mg/dL): 50
Absorbance: 0.12
Concentration (mg/dL): 100
Absorbance: 0.25
done

Enter absorbance of unknown/test sample: 0.20

--- Results ---
Estimated Glucose Concentration: 80.00 mg/dL
Standard Curve Equation: Y = 392.1568 * X + 2.1132
```

---

### 📘 Educational Use

This project is ideal for:

* Biochemistry and Life Sciences students
* Practicing regression-based estimations
* Integrating Python into biological data analysis

---

### 🧑‍💻 Author

**shad**
B.Sc. Life Sciences (Computer Applications)
Jamia Millia Islamia, New Delhi

---

### 📜 License

This project is licensed under the [MIT License](LICENSE) — free for educational and research use.

```
MIT License © 2025 shad921z
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction...
```

