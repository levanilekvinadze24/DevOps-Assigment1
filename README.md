## Assignment 1 — CI/CD Pipeline Automation & Deployment Strategies

### Live application
- **URL**: `https://dev-ops-assigment1.vercel.app`

### Screenshots
- **Hosted application**
  <img width="468" height="126" alt="image" src="https://github.com/user-attachments/assets/24d7faf6-6454-439f-8509-9bf2ccbfa9b4" />


- **GitHub Actions (successful run)**
  <img width="1813" height="738" alt="image" src="https://github.com/user-attachments/assets/8434a96d-b7d9-4e0b-b846-3174965d8a10" />



### Pipeline description
- **CI**: GitHub Actions runs on every `push` and `pull_request` to `main`, installs dependencies, then runs `python -m pytest -q`. If tests fail, the workflow stops.
- **CD**: Only if CI succeeds (and only on push to `main`), GitHub Actions deploys to Vercel using `vercel deploy --prod`.

### Strategy explanation
- **Update strategy**: Blue-Green (simulated)
- **How it’s applied**:
  - `main` acts as **production** (auto-deployed after tests pass).
  - PRs act as the **safe gate** before merging to production.
  - (Optional) A separate `staging` branch/project can be used for a true Blue-Green split.

### Rollback guide (Vercel)
- Go to Vercel dashboard → Project → **Deployments**
- Select the last stable deployment → **Promote to Production**
- (Alternative) Revert the bad commit in GitHub and push to `main` to redeploy the previous stable code through the pipeline.
