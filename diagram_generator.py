

def is_process_query(query: str) -> bool:
    """
    Check if the query is asking for a process or step-by-step guide.
    """
    process_keywords = ["steps", "process", "how to", "algorithm", "procedure", "guide", "method", "instruction",
    "workflow", "stages", "phases", "plan", "approach", "step-by-step", "diagram", "recipe", 
    "blueprint", "structure", "system", "model", "flowchart", "sequence", "plan of action", 
    "roadmap", "timeline", "tutorial", "checklist", "framework", "manual", "formula", "path",
    "technique", "steps involved", "order", "stages of", "action plan", "process flow", 
    "operation", "implementation", "guide to", "procedure to", "methodology", "recipe for",
    "course of action", "process map", "setup", "steps for", "steps to", "routine", "manual steps",
    "direction", "rules", "process guide", "flow process", "circuit", "pathway", "stepwise",
    "step sequence", "guidebook", "tutorial for", "operation flow", "setup guide", "steps outline",
    "plan steps", "workflow diagram", "execution steps", "instructional steps"]

    return any(keyword in query.lower() for keyword in process_keywords)
