# CI/CD Demo App (FastAPI + Vercel)

A lightweight Python/FastAPI REST API with an automated CI/CD pipeline using GitHub Actions and Vercel.  
Every push to `main` is automatically tested, and — **only if all tests pass** — deployed to production.

---

## 🔗 Live Application

**[https://dev-ops-assigment1.vercel.app](https://dev-ops-assigment1.vercel.app)**

---

## 📸 Screenshots

### Hosted Application
<img width="413" height="133" alt="image" src="https://github.com/user-attachments/assets/12b63d3f-4dda-4966-abb2-8a2f9c7107a3" />

### Successful GitHub Actions Run
<img width="1895" height="774" alt="image" src="https://github.com/user-attachments/assets/d7ab0c1b-6c91-458c-b289-f113327716e6" />

### Blocked Deployment (Failing Tests)
<img width="1895" height="774" alt="image" src="https://github.com/user-attachments/assets/9613b1a1-d7d6-4a54-a166-6f2ec7c7ad09" />

> **When tests fail, the deploy job is skipped. Broken code never reaches production.**

---

## 🧪 Test Scenario (Proof)

- I intentionally changed the API response from `ok` to `OK`, so the test failed and the pipeline blocked deployment.
- Then I reverted/fixed the change, pushed again, and the pipeline deployed successfully — proving the CI gate works.

---

## ⚙️ Pipeline Description

The pipeline is defined in `.github/workflows/main.yml` and consists of two sequential stages:

```text
Push to `main`
     │
     ▼
┌───────────────────────────────┐
│  STAGE 1 — CI (Test)          │  Runs on: push / pull_request
│  • setup Python 3.12          │
│  • pip install -r requirements│
│  • python -m pytest -q        │
└───────────────┬───────────────┘
                │  PASS?
          YES ──┴──► NO → Pipeline stops. Deploy is skipped.
                │
                ▼
┌───────────────────────────────┐
│  STAGE 2 — CD (Deploy)        │  Only on: push to main
│  • npm i -g vercel            │
│  • vercel deploy --prod       │
└───────────────────────────────┘
```

> **Key rule:** the deploy job declares `needs: test`. GitHub Actions will not start the deploy job unless the CI job succeeded.

---

## 🔄 Trigger Conditions

| Event | CI (Test) | CD (Deploy) |
|---|---|---|
| Push to `main` | ✅ Runs | ✅ Runs (only if CI passes) |
| Pull request to `main` | ✅ Runs | ❌ Skipped |

---

## 📁 Project Structure

.

├── .github/workflows/main.yml   # CI/CD pipeline

├── api/index.py                 # FastAPI app (Vercel entry)

├── tests/test_health.py         # PyTest suite

├── requirements.txt             # dependencies

└── vercel.json                  # Vercel config


---

## 🌐 API Endpoint

| Method | Path | Response |
|---|---|---|
| `GET` | `/` | `{ "status": "ok", "service": "DevOps-Assigment1" }` |

---

## 🔵 Update Strategy: Blue-Green (Simulated)

- `main` acts as **Production** — auto-deployed only after tests pass
- PRs act as the **safe validation gate**

---

## ↩️ Rollback Guide (Vercel)

### Option A — Dashboard
1. Vercel dashboard → Project → **Deployments**
2. Select last stable deploy → **Promote to Production**

### Option B — Git revert
1. Revert the bad commit and push to `main`
2. CI runs; if tests pass, CD deploys the stable version

---

## 💻 Local Setup

```bash
git clone https://github.com/levanilekvinadze24/DevOps-Assigment1.git
cd DevOps-Assigment1
python -m pip install -r requirements.txt
python -m pytest -q
```
