
def startAutoGpt() -> None:
    """
    Start an Auto-GPT assistant.
    """
    
    from autogpt.commands.command import CommandRegistry
    from autogpt.config.config import Config, check_openai_api_key
    from autogpt.config.ai_config import AIConfig

    cfg = Config()
    check_openai_api_key()
    # Create a CommandRegistry instance and scan default folder
    command_registry = CommandRegistry()
    command_registry.import_commands("autogpt.commands.datetime")

    ai_config = AIConfig()
    ai_config.command_registry = command_registry

    system_prompt = ai_config.construct_full_prompt()
    agent = Agent(
        ai_name=ai_name,
        memory=memory,
        full_message_history=full_message_history,
        next_action_count=next_action_count,
        command_registry=command_registry,
        config=ai_config,
        system_prompt=system_prompt,
        triggering_prompt=triggering_prompt,
    )
    agent.start_interaction_loop()