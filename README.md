## Session 4 - Numeric Types II
Description of the classes and methods in session4.py and test_session4.py

### Qualean
Qualean class is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place

