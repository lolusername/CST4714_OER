# Reusable Course Diagrams

These nine original illustrations accompany the textbook and slides. Each PNG
has an editable Graphviz `.dot` source or, for vector geometry, an SVG source.

| Diagram | Image | Editable source |
|---|---|---|
| Question, model, test, and interpretation | [PNG](evidence_cycle.png) | [DOT](evidence_cycle.dot) |
| Relational join | [PNG](relational_join.png) | [DOT](relational_join.dot) |
| Query-plan flow | [PNG](query_plan_flow.png) | [DOT](query_plan_flow.dot) |
| Recovery timeline | [PNG](recovery_timeline.png) | [DOT](recovery_timeline.dot) |
| NoSQL models | [PNG](nosql_models.png) | [DOT](nosql_models.dot) |
| Graph path | [PNG](graph_path.png) | [DOT](graph_path.dot) |
| Vector geometry | [PNG](vector_geometry.png) | [SVG](vector_geometry.svg) |
| Replica set | [PNG](replica_set.png) | [DOT](replica_set.dot) |
| Polyglot system and outbox | [PNG](polyglot_outbox.png) | [DOT](polyglot_outbox.dot) |

The original illustrations are CC BY-NC-SA 4.0. With Graphviz installed, rebuild
an individual diagram with `dot -Tpng query_plan_flow.dot -o query_plan_flow.png`.
Retain the surrounding explanation when reusing a diagram and provide a text
description of its important relationships.

Cloud-interface screenshots embedded in the book and decks are dated teaching
examples. They are not included as a standalone open image library; the product
interface elements and marks retain their respective owners' rights.
