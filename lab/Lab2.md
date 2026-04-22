# Lab 2: Version Control with Git

## Step 1: Initialize Git repository

### Commands
```bash
git init python-project
cd python-project

# Create initial files
echo "print('Hello DevOps')" > app.py
\end{lstlisting}
```

## Step 2: First commit
### Commands
```bash
git checkout -b vedantha_1BM23CD069
git add .
git commit -m "Initial commit: Add app.py"

# Create remote repository
git remote add origin https://github.com/SANDHYAGOPAL/devops26lab.git
git push
```