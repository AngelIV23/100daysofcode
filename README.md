# 100daysofcode
A group of us will be following https://www.udemy.com/course/100-days-of-code and meet up once a week to have open discussions.  Day/Time TBD.

If you want to join us visit: https://artofneteng.com/iaatj and let us know in the #100daysofcode channel.

# Setting up environment
```
git clone https://github.com/Its-All-About-the-Journey/100daysofcode.git

cd 100daysofcode

python3 -m venv venv

source venv/bin/activate
```

Each of us will build our own branch by executing the following git command:

```
git checkout -b your_discord_name
```

You can use build_source_code_structure.py to update README.md file specific to your environment.  In particular you should edit the readme_contents variable in the script.

````markdown
readme_contents = '''
# DAY {}

# Description
Keep track of 100 days to code Python course from beginner to professional. My focus is to become proficient in python for personal and professional reason.
I want to learn Python with the primary focus on performing automation tasks. I have procrastrinated for a long time and I have finally decided to make this decision.

# Environment
OS: Mac OS Big Sur V11.1 (20C69)

Python version:
3.9.1

# Dependencies

# How to run script
```
enter instructions here
```

# Sample output
```
paste output here
```
'''
````

Afterwards, you can edit README.md specifics for the day such as description,
howto, and sample output.  It is not mandatory.  The purpose of the script is
to standarize our structure.  Improvements are welcomed.

```
python build_source_code_structure.py
```

