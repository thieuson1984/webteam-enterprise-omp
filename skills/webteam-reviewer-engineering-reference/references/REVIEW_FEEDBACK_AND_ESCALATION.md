# Independent Review Communication and Escalation

1. **Helpful priority order:** one-line verdict, release blockers, high risk, medium, low, nonblocking nits, positive observations.
2. **Comment format:** Location → observed behavior → concrete failure scenario → requested behavior → minimal test or safe alternative. State uncertainty as question, not accusation.
3. **Independence:** author, reviewer and quality gate must be distinguishable for critical changes. An agent that wrote the patch cannot independently approve it; use a different reviewer context and evidence, with human oversight where warranted.
4. **Disagreement:** compare facts and counterexamples; ask Product/Architect/Security for domain arbitration, or owner for judgment; never majority-vote without evidence.
5. **Repair:** delegate writing to owner; Reviewer can recommend but not silently edit. Re-review changed paths and targeted adjacent flows. Escalate unresolved blocking risk and capture final approver.
6. **Avoid toxic review:** no personal comments, no style policing outside established project standards, no endless speculative architecture rewrites.

References: Google Engineering Practices: https://google.github.io/eng-practices/review/reviewer/looking-for.html ; https://google.github.io/eng-practices/review/reviewer/standard.html ; https://google.github.io/eng-practices/review/reviewer/comments.html .
