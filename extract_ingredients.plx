[pipe.extract_ingredients.seq]
type = "PipeSequence"
description = "Extract ingredients from grocery receipts or fridge images"

[[pipe.extract_ingredients.seq.steps]]
name = "vision_extract"
type = "PipeVision"
system_prompt = """
Read the image. Identify every food item, product, or ingredient visible.
If it looks like a receipt, extract each line that is a food or grocery item.
Return ONLY a JSON array of ingredient names, e.g. ["eggs","milk","spinach"].
"""
input = { image_path = "{{input.image_path}}" }

[pipe.extract_ingredients.seq.output]
select = { ingredients = "{{vision_extract.output}}" }
