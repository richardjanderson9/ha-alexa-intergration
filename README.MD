# ha-alexa-intergration

## 1. Project Outline

This project provides a minimal Python AWS Lambda function that acts as a proxy between Alexa and Home Assistant. The Lambda function forwards Alexa events to your Home Assistant instance, supporting up to two authentication tokens for reliability. Deployment is automated using GitHub Actions, which updates the Lambda function on every push to the `main` branch.

---

## 2. Setup Notes

1. **Clone or fork this repository** and push it to your own GitHub account.
2. **Create the target Lambda function** in AWS Lambda (Python 3.14+ recommended).
3. **Add required secrets** (see below) in your GitHub repository under `Settings > Secrets and variables > Actions`.
4. **Push changes** to the `main` branch to trigger the deployment workflow.
5. The GitHub Actions workflow at `.github/workflows/push_lambda.yml` will:
    - Validate secrets
    - Install dependencies
    - Package and deploy the Lambda code to AWS

---

## 3. Secrets to Add (with Examples)

Add these secrets in your GitHub repository settings:

| Secret Name                | Example                              | Description                                 |
|---------------------------|--------------------------------------|---------------------------------------------|
| `AWS_ACCESS_KEY_ID`       | `AKIA...EXAMPLE`                     | AWS IAM access key for Lambda deployment    |
| `AWS_SECRET_ACCESS_KEY`   | `wJalr...EXAMPLEKEY`                 | AWS IAM secret key for Lambda deployment    |
| `AWS_REGION`              | `eu-west-1`                          | AWS region where Lambda is deployed         |
| `LAMBDA_FUNCTION_NAME`    | `your-lambda-function-name`          | Name of your AWS Lambda function            |
| `PYTHON_DEPENDENCES`      | `urllib3`                            | Comma-separated list of Python dependencies |
| `HA_LONGLIFETOKEN_1`      | `eyJ0eXAiOiJKV1QiLCJ...`             | Home Assistant long-lived token (primary)   |
| `HA_LONGLIFETOKEN_2`      | `eyJ0eXAiOiJKV1QiLCJ...`             | Home Assistant long-lived token (backup)    |
| `HA_ACCESSDOMAIN`         | `your-home.example.com`              | Home Assistant domain (no protocol)         |
| `HA_API_Path`             | `/api/{data}/{data2}`                | Home Assistant API path (e.g. `/api/alexa/smart_home`) |

---
