
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


If you want to run a specific file, you can use: 
```
ALGO_IMPL=implementations pytest test_bfs_traversal.py

# Or just: 
pytest test_bfs_traversal.py
```