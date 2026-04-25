## Assignment 1 — CI/CD Pipeline Automation & Deployment Strategies

### Live application
- **URL**: (paste your Vercel production URL here after first deploy)

### Screenshots (add images)
- Hosted application screenshot
- GitHub Actions successful run screenshot

### Pipeline description
- **CI**: On every `push` / `pull_request`, GitHub Actions installs dependencies and runs `pytest`. If tests fail, the pipeline stops.
- **CD**: On push to `main` (only after CI passes), GitHub Actions deploys to Vercel using the Vercel CLI.

### Update strategy (chosen)
- **Strategy**: Blue-Green (simulated)
- **How it’s applied**:
  - `main` is treated as **production** (auto-deployed).
  - Pull Requests act as the **safe validation gate** (tests must pass).
  - (Optional) Create a `staging` branch and deploy it to a separate Vercel project for a true Blue-Green environment split.

### Rollback guide (Vercel)
Option A (recommended): Roll back to a previous deployment
- Open Vercel dashboard → your project → **Deployments**
- Pick the last stable deployment → **Promote to Production**

Option B: Roll back via Git
- Revert the bad commit in GitHub (or reset to a known good commit) and push to `main`
- CI runs tests → CD redeploys the last stable code

