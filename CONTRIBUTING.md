# 🤝 Contributing to SHILP AI (Team Guidelines)

Welcome to the team! To ensure everyone can code peacefully without merge conflicts, follow this simple workflow:

## 🌿 Git Branching Strategy
Never push directly to `main`. Always create a branch for your area:
```bash
# Frontend (Prakriti & Saira):
git checkout -b feature/ui-ergonomics

# Backend (Anikeat):
git checkout -b feature/database-models

# AI / Vision (Kartik):
git checkout -b feature/vision-prompt-tuning

# ML / Pricing (Ishaan):
git checkout -b feature/pricing-algorithms
```

## 🧪 Pre-Commit Verification Rule
Before submitting a pull request, always run:
```bash
scripts\verify_all.bat   # Windows
# or
python backend/tests/test_e2e_suite.py
```
If all tests pass, commit and open your Pull Request!
