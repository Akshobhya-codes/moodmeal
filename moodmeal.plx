[pipe.moodmeal.seq]
type = "PipeSequence"
description = "Groceries + mood → 3 recipes"

[[pipe.moodmeal.seq.steps]]
name = "parse_groceries"
type = "PipeLLM"
system_prompt = "List ingredients from groceries_text as JSON array."
input = { groceries_text = "{{input.groceries_text}}" }

[[pipe.moodmeal.seq.steps]]
name = "classify_mood"
type = "PipeLLM"
system_prompt = "Classify mood into cuisine and flavor profile."
input = { mood = "{{input.mood}}" }

[[pipe.moodmeal.seq.steps]]
name = "generate_recipes"
type = "PipeLLM"
system_prompt = "Use mood and ingredients to suggest 3 recipes (title, reason, steps). Output valid JSON."
input = { ingredients = "{{parse_groceries.output}}", profile = "{{classify_mood.output}}" }

[pipe.moodmeal.seq.output]
select = { recipes = "{{generate_recipes.output}}" }
