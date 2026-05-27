# Claude Limit Skill

A custom skill for Claude that manages and enforces token/usage limits.

## Features

- Track token usage across conversations
- Set maximum token limits
- Monitor usage statistics
- Reset usage counters

## Installation

1. Clone or reference this repository
2. Register the skill with Claude through your preferred integration method
3. Use the skill functions in your Claude interactions

## Usage

See `skill-definition.json` for the skill schema and available functions.

## Functions

### `set_token_limit`
Set a maximum token limit for tracking.

**Parameters:**
- `limit` (number): Maximum tokens allowed

### `get_current_usage`
Get current token usage statistics.

**Returns:**
- Current token count
- Remaining tokens
- Usage percentage

### `reset_usage`
Reset the usage counter to zero.

## File Structure

- `skill-definition.json` - Skill schema and function definitions
- `README.md` - This file
