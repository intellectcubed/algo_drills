
### ChatGPT Context
The file .algo_context.yaml contains the context.  When you start a new chatgpt session, you can do the following: 

```
Project Context:
(then paste the YAML)

You are my assistant for the algo_drills project.
Every time I say “add exercise X,” use this context to generate the files, tests, and structure as described.
```

Next, you can say: 

```
Add exercise dfs_traversal using the same structure as BFS
```

## Running Tests: 
You can run your implementation, or run the default implementation

### First, source: 
```shell
cd /Users/george.nowakowski/Projects/python/algo_drills
source venv/bin/activate
cd tests
```

### Running default implementation: 
**All**
```shell
ALGO_IMPL=implementations pytest
```

**Specific**
```shell
ALGO_IMPL=implementations pytest test_bfs_traversal.py
```

### Running your code: 
**All**
```shell
pytest
```

***Specific**
```shell
pytest -s test_bfs_traversal.py
```


### To run all tests: 
```
ALGO_IMPL=implementations pytest
```


If you want to run a specific file, you can use: 
```
ALGO_IMPL=implementations pytest test_bfs_traversal.py

# Or just: 
pytest test_bfs_traversal.py
```

---
# Suggested Drill Practice: 
## Monday
- bfs_traversal.py

## Tuesday
- test_union_find.py

## Wednesday
## Thursday
## Friday

## New week
```
cd /Users/george.nowakowski/Projects/python/algo_drills
git reset --hard origin/main
```
