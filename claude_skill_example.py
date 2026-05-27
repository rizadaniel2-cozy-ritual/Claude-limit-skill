import anthropic
import json

# Initialize the Anthropic client
# Make sure you have set your ANTHROPIC_API_KEY environment variable
client = anthropic.Anthropic()

# Load the skill definition from your repository
skill_definition = {
    "name": "Claude Limit Skill",
    "version": "1.0.0",
    "description": "A skill for managing and tracking token usage limits in Claude conversations",
    "author": "rizadaniel2-cozy-ritual",
    "tools": [
        {
            "name": "set_token_limit",
            "description": "Set a maximum token limit for conversation tracking",
            "input_schema": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of tokens allowed"
                    }
                },
                "required": ["limit"]
            }
        },
        {
            "name": "get_current_usage",
            "description": "Get current token usage statistics",
            "input_schema": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "reset_usage",
            "description": "Reset the usage counter to zero",
            "input_schema": {
                "type": "object",
                "properties": {}
            }
        },
        {
            "name": "get_usage_report",
            "description": "Get a detailed usage report with breakdown",
            "input_schema": {
                "type": "object",
                "properties": {
                    "format": {
                        "type": "string",
                        "enum": ["json", "text"],
                        "description": "Format of the report"
                    }
                }
            }
        }
    ]
}

# Extract just the tools from the skill definition
tools = skill_definition["tools"]

# Example: Send a message to Claude with the skill tools available
def chat_with_claude_skills(user_message):
    """Send a message to Claude and make the skill tools available."""
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,  # Your skill tools are available here
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    
    return response

# Example usage - uncomment to test
if __name__ == "__main__":
    print("Testing Claude with Limit Skill...")
    
    # Try asking Claude to use one of the skill tools
    result = chat_with_claude_skills("Set my token limit to 5000 and tell me the current usage")
    
    print("Response from Claude:")
    print(result)
