# 💾 Storage State Model

```mermaid
stateDiagram-v2
    [*] --> Empty
    Empty --> CollectionAvailable: create first record
    CollectionAvailable --> CollectionAvailable: create / update / favorite
    CollectionAvailable --> CollectionAvailable: delete one of several
    CollectionAvailable --> Empty: delete final record
    CollectionAvailable --> [*]: browser data cleared
    Empty --> [*]: browser data cleared
```

The state model is conceptual and reflects the collection lifecycle. It is not a transactional database state machine. Current helper edge-case assumptions are listed in [known issues](../known-issues.md).
