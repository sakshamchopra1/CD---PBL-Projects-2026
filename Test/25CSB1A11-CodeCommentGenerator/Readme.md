# 25CSB1A11 — SafeDocGen: Intelligent Secure Code Comment Generator & AST Vulnerability Defense System

**Course:** Compiler Design (CD) — PBL Projects 2026  
**Institution:** National Institute of Technology Warangal (NITW)  
**Student Name:** Saksham Chopra  
**Roll Number:** 25CSB1A11  
**Specialization:** CSE (AI & Data Science)  
**Original GitHub Repository:** [https://github.com/sakshamchopra1/CodeCommentGenerator](https://github.com/sakshamchopra1/CodeCommentGenerator)  

---

## 1. Project Title & Overview
**SafeDocGen (CodeCommentGenerator):** An offline-first, compiler-grounded neurosymbolic documentation engine and agentic security defense system for Python. It parses source code using deterministic Abstract Syntax Trees (AST), lowers code to linearized Intermediate Representation (Three-Address Code), conducts dataflow analysis (reaching definitions & dead code elimination), and produces verified PEP-257 docstrings and inline comments while defending against 19 prompt injection vectors and 12 OWASP/CWE static code flaws.

---

## 2. File Manifest (Uploaded Files & Descriptions)

| File / Directory | Category | Size | Description |
| :--- | :--- | :--- | :--- |
| **`Readme.md`** | Documentation | ~5 KB | Project submission overview, student metadata, file inventory, and verification guide. |
| **`CodeCommentGenerator_FinalReport.pdf`** | Academic Report | 1.6 MB | Complete 16-page formal academic report with publication-grade 300 DPI figures, confusion matrix, ROC curve, and algorithms. |
| **`CodeCommentGenerator.pptx`** | Presentation | 514 KB | Comprehensive project presentation slide deck covering architecture, benchmarks, and demo screenshots. |
| **`FinalScreenrecording.mp4`** | Video Demo | 10.3 MB | Complete screen recording demo showing the web interface on port 5000, docstring generation, and live prompt injection blocking. |
| **`25CSB1A11.zip`** | Project Archive | 11.8 MB | Standalone compressed archive containing all source code, tests, documentation, and evaluation data. |
| **`DOCUMENTATION.md`** | Technical Manual | 75 KB | In-depth technical guide to compiler frontend passes, IR TAC instructions, and AST visitor methods. |
| **`src/`** | Core Source Code | ~150 KB | Python source code for compiler frontend, security gateway, IR generator, and neural model. |
| ├── `src/main.py` | CLI & Orchestrator | 23 KB | Pipeline coordinator connecting lexing, AST parsing, DFA, and output formatting. |
| ├── `src/security.py` | Security Layer | 30 KB | Stage 0 security gateway implementing 19 direct/indirect injection filters and lexical sanitizer. |
| ├── `src/ast_extractor.py` | AST Compiler Frontend | 10 KB | Python AST node visitor extracting arguments, type hints, docstrings, and return paths. |
| ├── `src/comment_generator.py`| Docstring Engine | 33 KB | Grounded docstring synthesizer with PEP-257 docstring formatting. |
| ├── `src/ir/` | Intermediate Repr. | 35 KB | Three-Address Code (TAC) linearizer and basic block control flow graph generator. |
| ├── `src/analysis/` | Dataflow Analysis | 30 KB | Intraprocedural reaching definitions, live variables, and dead code detector. |
| ├── `src/ml/` | Model Core | 20 KB | CodeT5 / neural generation interface with offline inference support. |
| ├── `src/security_analyzer.py`| Static Code Scanner | 11 KB | AST static code analyzer detecting 12 OWASP/CWE flaws (SQLi, eval, shell injection). |
| **`tests/`** | Test Suite | ~80 KB | Automated test suite containing 118 PyTest test cases (all passing in 1.42 seconds). |
| ├── `tests/test_basic.py` | Unit Tests | 2.3 KB | Parser, syntax validation, and type annotation tests (16 tests). |
| ├── `tests/test_ir.py` | Unit Tests | 9.5 KB | Linearized TAC generation and CFG partitioning tests (24 tests). |
| ├── `tests/test_analysis.py` | Unit Tests | 9.3 KB | Reaching definitions, dead code elimination, and DFA tests (28 tests). |
| ├── `tests/test_security.py` | Security Tests | 21 KB | Prompt injection blocking, surgical sanitizer, and audit logging tests (32 tests). |
| ├── `tests/test_ast_nlp_model.py`| Model Tests | 3.4 KB | CodeT5 tokenizer, feature serialization, and BLEU/ROUGE math tests (18 tests). |
| **`web_server.py`** | Web Dashboard | 48 KB | Full-featured dark-theme web dashboard (Flask/HTTP) running on `http://localhost:5000`. |
| **`report_assets/`** | Figures & Charts | ~1.2 MB | 300 DPI Matplotlib charts (BLEU/ROUGE, confusion matrix, ROC curve, terminal output). |

---

## 3. Key Quantitative Benchmark Results

- **Unit & Security Test Suite:** 118 / 118 tests passed (100% pass rate in 1.42s).
- **Adversarial Threat Detection:** 98.3% classification accuracy on 400 test samples (0 false positives on benign student code).
- **ROC-AUC Score:** 0.992 area under the receiver operating characteristic curve.
- **Natural Language Quality:** BLEU-4 of 0.428 and ROUGE-L of 0.512.
- **Local Inference Latency:** 220 ms on CUDA GPU, 1.18 s on standard CPU (100% offline).

---

## 4. How to Run the Project

### Prerequisites
```bash
python --version  # Requires Python 3.10+
pip install -r requirements.txt  # Or: pip install pytest flask torch transformers
```

### Running the Test Suite (118 Tests)
```bash
pytest test_security.py tests/ -v
```

### Running the Web Dashboard
```bash
python web_server.py
# Open your web browser to: http://localhost:5000
```

### Running the CLI Generator
```bash
python -m src.main --input your_script.py --output annotated_script.py
```

---

## 5. Large File Cloud Mirror (Google Drive / GitHub)
In accordance with course guidelines for submissions with multimedia files:
- All core files (source code, 16-page PDF, PPTX, and MP4 screen recording) are directly included in this repository.
- A standalone all-in-one ZIP archive is also provided: `25CSB1A11-CodeCommentGenerator/25CSB1A11.zip`.
- If external viewing permissions are needed, the repository is mirrored publicly at:
  [https://github.com/sakshamchopra1/CodeCommentGenerator](https://github.com/sakshamchopra1/CodeCommentGenerator)
