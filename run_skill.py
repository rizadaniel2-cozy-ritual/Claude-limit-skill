import anthropic
import json
import os

# Get API key from environment
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("ERROR: ANTHROPIC_API_KEY not set")
    print("Please set your API key first")
    exit(1)

client = anthropic.Anthropic(api_key=api_key)

# Your skill tools
tools = [
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

def chat_with_claude_skills(user_message):
    """Send a message to Claude with your skill tools available."""
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        tools=tools,
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    return response

if __name__ == "__main__":
    print("🚀 Claude Limit Skill is now active!")
    print("Testing connection...\n")
    
    result = chat_with_claude_skills("Set my token limit to 5000 and tell me the current usage")
    
    print("✅ Response from Claude:")
    print(result)
