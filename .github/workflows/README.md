# CI/CD Pipeline Documentation

This document explains the CI/CD (Continuous Integration/Continuous Deployment) setup for the Helldivers 2 Database project.

## Overview

The CI/CD pipeline is implemented using GitHub Actions, which is free for public repositories and offers a generous free tier for private repositories. The pipeline consists of several workflows that handle different aspects of the development process:

1. **Main Workflow** (`main.yml`): Handles testing, linting, building, and deployment
2. **Database Migrations Workflow** (`migrations.yml`): Manages database schema changes
3. **Security Scanning Workflow** (`security.yml`): Checks for security vulnerabilities
4. **Code Coverage Workflow** (`coverage.yml`): Tracks test coverage

## Workflow Details

### Main Workflow (`main.yml`)

This workflow runs on pushes and pull requests to the `main` and `develop` branches. It consists of the following jobs:

- **Test**: Runs Django tests to ensure functionality works as expected
- **Lint**: Checks code quality using flake8
- **Build**: Builds a Docker image of the application
- **Deploy-Staging**: Deploys to the staging environment when changes are pushed to the `develop` branch
- **Deploy-Production**: Deploys to the production environment when changes are pushed to the `main` branch

### Database Migrations Workflow (`migrations.yml`)

This workflow runs when changes are made to migration files or model files. It consists of the following jobs:

- **Migrate**: Applies database migrations
- **Backup-DB**: Creates a database backup before applying migrations to production

### Security Scanning Workflow (`security.yml`)

This workflow runs on pushes, pull requests, and on a weekly schedule. It consists of the following job:

- **Security-Scan**: Scans code for security vulnerabilities using Bandit and checks dependencies for known vulnerabilities using Safety

### Code Coverage Workflow (`coverage.yml`)

This workflow runs on pushes and pull requests to the `main` and `develop` branches. It consists of the following job:

- **Coverage**: Runs tests with coverage tracking and ensures that code coverage stays above 70%

## Customization

### Deployment Steps

The deployment steps in the main workflow are currently placeholders. To implement actual deployment:

1. For **Deploy-Staging** and **Deploy-Production** jobs, replace the echo statements with actual deployment commands
2. If deploying to a server via SSH, use GitHub Secrets to store credentials
3. If deploying to a cloud provider, use their respective GitHub Actions

Example for deploying to a server via SSH:

```yaml
- name: Deploy to server
  uses: appleboy/ssh-action@master
  with:
    host: ${{ secrets.HOST }}
    username: ${{ secrets.USERNAME }}
    key: ${{ secrets.SSH_KEY }}
    script: |
      cd /path/to/project
      git pull
      docker-compose up -d
```

### Database Backup

The database backup step in the migrations workflow is a placeholder. To implement actual database backup:

1. For PostgreSQL:
```yaml
- name: Backup PostgreSQL database
  run: |
    pg_dump -h ${{ secrets.DB_HOST }} -U ${{ secrets.DB_USER }} -d ${{ secrets.DB_NAME }} > backup.sql
```

2. For MySQL/MariaDB:
```yaml
- name: Backup MySQL database
  run: |
    mysqldump -h ${{ secrets.DB_HOST }} -u ${{ secrets.DB_USER }} -p${{ secrets.DB_PASSWORD }} ${{ secrets.DB_NAME }} > backup.sql
```

## Additional Features

### Dependabot

This project uses Dependabot to keep dependencies up-to-date. Dependabot is configured in `.github/dependabot.yml` and will:

- Check for updates to Python dependencies weekly
- Check for updates to GitHub Actions weekly
- Create pull requests for updates with appropriate labels
- Limit the number of open pull requests to 10

When Dependabot creates a pull request, the CI/CD pipeline will run automatically to ensure that the updated dependencies don't break anything.

## Benefits of This Setup

1. **Free**: GitHub Actions is free for public repositories and offers a generous free tier for private repositories
2. **Automated Testing**: Ensures code changes don't break existing functionality
3. **Code Quality**: Maintains code quality through linting and coverage requirements
4. **Security**: Regularly checks for security vulnerabilities
5. **Deployment Automation**: Automates the deployment process to reduce human error
6. **Database Safety**: Ensures database migrations are applied safely with backups
7. **Dependency Management**: Automatically keeps dependencies up-to-date with Dependabot

## Troubleshooting

If a workflow fails, check the GitHub Actions tab in your repository to see the error logs. Common issues include:

1. **Test Failures**: A test is failing, fix the code or update the test
2. **Linting Errors**: Code doesn't meet quality standards, fix the issues
3. **Security Vulnerabilities**: Security issues found, address them
4. **Low Coverage**: Test coverage is below threshold, add more tests
5. **Deployment Failures**: Issues with deployment, check server connectivity and credentials
