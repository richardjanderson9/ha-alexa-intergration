# ha-alexa-intergration

This repository contains a minimal Python Lambda intended to be deployed via GitHub Actions on push to `main`.

Setup notes:

- Create a GitHub repository and push this directory as the repository root.
- In the repository settings > Secrets, set these secrets:
	- `AWS_ACCESS_KEY_ID`
	- `AWS_SECRET_ACCESS_KEY`
	- `AWS_REGION` (e.g. `us-east-1`)
	- `LAMBDA_FUNCTION_NAME` (the target Lambda function name)

- The Actions workflow at [.github/workflows/deploy.yml](.github/workflows/deploy.yml) runs on pushes to `main` and will update the Lambda code using `aws lambda update-function-code`.

Files added:

- [pyproject.toml](pyproject.toml)
- [requirements.txt](requirements.txt)
- [src/lambda_function.py](src/lambda_function.py)
- [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
