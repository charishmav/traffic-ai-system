# 🚦 Traffic AI System

### Real-Time Traffic Signal Optimization using RT-DETR, OC-SORT and PPO Reinforcement Learning

## 📌 Project Overview

This project implements an intelligent traffic management system that performs:

* Vehicle Detection using **RT-DETR**
* Vehicle Tracking using **OC-SORT**
* Lane-wise Vehicle Counting
* Traffic Signal Decision Making using **Proximal Policy Optimization (PPO)**
* Real-time Traffic Visualization
* Performance Analysis using CSV reports and graphs

The system processes traffic video frames, detects vehicles, tracks movement, estimates congestion per lane, and dynamically selects traffic signal actions.

---

## 🏗️ System Architecture

Input Video
↓
RT-DETR Vehicle Detection
↓
OC-SORT Tracking
↓
Vehicle Counting
↓
Traffic State Generation
↓
PPO Reinforcement Learning
↓
Traffic Signal Decision
↓
Visualization & Analytics

---

## 📂 Project Structure

```plaintext
traffic-ai-system
│
├── README.md
├── requirements.txt
├── main.py
│
├── src
│   ├── environment.py
│   ├── detector.py
│   ├── tracker.py
│   ├── counter.py
│   ├── train.py
│   ├── validate.py
│   ├── integrated_system.py
│   ├── analysis.py
│   └── utils.py
│
├── models
│   ├── ppo_train_model.zip
│   └── rtdetr-l.pt
│
├── outputs
│
├── videos
│
└── notebooks
```

---

## ⚙️ Technologies Used

* Python
* OpenCV
* PyTorch
* RT-DETR
* OC-SORT
* Stable-Baselines3
* Gymnasium
* NumPy
* Pandas
* Matplotlib

---

## 🚀 Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/traffic-ai-system.git

cd traffic-ai-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

Train PPO Model:

```bash
python src/train.py
```

Validate Model:

```bash
python src/validate.py
```

Run Full Integrated Pipeline:

```bash
python src/integrated_system.py
```

Generate Analysis Graphs:

```bash
python src/analysis.py
```

Run Entire Project:

```bash
python main.py
```

---

## 📊 Output

The system generates:

* Vehicle Detection Output
* Traffic Signal Decisions
* Reward Curves
* Vehicle Count Graphs
* Action Distribution Graphs
* Saved Output Frames

Output files are stored in:

```plaintext
outputs/
```

---

## 🎯 Features

✔ Real-time Vehicle Detection
✔ Multi-Lane Vehicle Counting
✔ Reinforcement Learning Traffic Control
✔ Traffic Visualization
✔ Automated Performance Evaluation

---

## 🔮 Future Improvements

* Multi-camera traffic management
* Edge deployment optimization
* Cross-attention traffic fusion
* Cloud monitoring dashboard
* Smart city integration

---

