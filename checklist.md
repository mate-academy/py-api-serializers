# Check Your Code Against the Following Points

## Code Style

1. Do not forget about type annotation in class methods.

2. You do not need `.all()` method before 
`.prefetch_related()` and `.select_related()` methods:

Good example:

```python
queryset = Movie.objects.prefetch_related("actors")
```

Bad example:

```python
queryset = Movie.objects.all().prefetch_related("actors")
```

3. You can provide multiple arguments into prefetch_related method:

Good example:

```python
queryset = Movie.objects.prefetch_related("actors", "genres")
```

Bad example:

```python
queryset = Movie.objects.prefetch_related("actors").prefetch_related("genres")
```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
