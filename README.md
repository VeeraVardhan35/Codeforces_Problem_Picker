cat > README.md << 'EOF'
# Codeforces Problem Picker

A Django web application that helps competitive programmers practice by randomly selecting Codeforces problems based on difficulty rating and tags.

![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

**Live Demo:** [https://codeforces-problem-picker-2.onrender.com](https://codeforces-problem-picker-2.onrender.com)

---

## 🚀 Features

- **Random Problem Selection:** Get random Codeforces problems with a single click.
- **Rating Filter:** Filter problems by difficulty (800-4000).
- **Tag Filter:** Filter by problem tags (DP, Greedy, Math, Graphs, etc.).
- **User Accounts:** Sign up to track problems you've already seen.
- **No Repeat Problems:** Logged-in users won’t see the same problem twice.
- **Responsive Design:** Works perfectly on desktop and mobile devices.
- **Codeforces Integration:** Direct links to problems on Codeforces.

---

## 🛠️ Technology Stack

- **Backend:** Django 5.2.4  
- **Frontend:** Bootstrap 5, HTML5, CSS3  
- **Database:** SQLite (Development), PostgreSQL (Production)  
- **Deployment:** Render.com  
- **Authentication:** Django Built-in Authentication  

---

## 📦 Installation

### Prerequisites

- Python 3.11+  
- pip  
- Git  

### Local Development Setup

1. **Clone the repository**

```bash
git clone https://github.com/VeeraVardhan35/Codeforces_Problem_Picker.git
cd Codeforces_Problem_Picker
