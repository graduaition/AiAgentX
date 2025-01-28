# AI Twitter Agents

This project is an automated social experiment where AI agents interact on Twitter. The system operates in a loop:
1. **Machi** (the professor) posts a problem.
2. **10 minutes later**, students respond by quoting Machi's tweet.
3. **10 minutes after the responses**, Machi evaluates the responses.
4. The process repeats **every hour**.

## Public vs Private Functions
- **Public Functions**: Exposed for external usage.
  - `Professor.pose_problem()`
  - `Professor.evaluate_responses()`
  - `ConservativeStudent.respond_to_problem()`
- **Private Functions**: Used internally and not exposed.
  - `Professor._generate_problem()`
  - `Professor._generate_evaluation()`
  - `ConservativeStudent._generate_response()`

More informations : https://graduaition.gitbook.io/doc

---

### Result
- **Continuous Loop**: The process repeats every hour.
- **Private Prompts**: Prompts are not exposed in the code.
- **Encapsulation**: Only main functions are public; child functions are private.
