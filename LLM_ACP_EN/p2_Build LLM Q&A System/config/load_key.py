import os
import getpass
import json
import dashscope

def _select_environment():
    """Interactively prompts the user to select their cloud environment."""
    while True:
        prompt = "Are you using the Alibaba Cloud International site? (Y/N): "
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            print("-> Environment selected: Alibaba Cloud International")
            return "intl"
        elif response in ['n', 'no']:
            print("-> Environment selected: Alibaba Cloud Mainland China")
            return ""
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def load_key():
    """
    Loads/prompts for DashScope settings and sets them as environment variables.
    - os.environ['DASHSCOPE_API_KEY']
    - os.environ['DASHSCOPE_API_BASE']
    This function does not return any value.
    """
    script_dir = os.path.dirname(__file__)
    file_name = os.path.join(script_dir, '..', '../Key.json')
    config_data = {}

    # Step 1: Load or create config data from Key.json
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                config_data = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: Config file '{file_name}' is corrupted. A new one will be created.")

    if not config_data.get("DASHSCOPE_API_KEY"):
        print("DashScope API Key not found in config.")
        api_key = getpass.getpass("Please enter your DashScope API Key: ").strip()
        config_data["DASHSCOPE_API_KEY"] = api_key

    if config_data.get("DASHSCOPE_ENV_SUFFIX") is None:
        print("Environment setting not found in config.")
        env_suffix = _select_environment()
        config_data["DASHSCOPE_ENV_SUFFIX"] = env_suffix

    try:
        with open(file_name, 'w') as json_file:
            json.dump(config_data, json_file, indent=4)
        print(f"-> Configuration saved/updated: {os.path.abspath(file_name)}")
    except IOError as e:
        print(f"Error writing to config file: {e}")

    # Step 2: Set the environment variables for this session
    api_key = config_data["DASHSCOPE_API_KEY"]
    env_suffix = config_data.get("DASHSCOPE_ENV_SUFFIX", "")

    if env_suffix:
        api_base_url = f"https://dashscope-{env_suffix}.aliyuncs.com/compatible-mode/v1"
    else:
        api_base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

    os.environ['DASHSCOPE_API_KEY'] = api_key
    os.environ['DASHSCOPE_API_BASE'] = api_base_url
    
    # Also configure the dashscope library's global state
    dashscope.api_key = api_key
    
    print("-> Configuration loaded into environment variables.")

def display_config_summary():
    """
    Reads configuration from environment variables and prints a summary,
    masking the sensitive API key.
    """
    api_key = os.environ.get('DASHSCOPE_API_KEY', 'Not Set')
    api_base = os.environ.get('DASHSCOPE_API_BASE', 'Not Set')

    # Determine environment name from the final URL
    if "intl" in api_base:
        env_name = "International"
    elif "Not Set" in api_base:
        env_name = "Unknown"
    else:
        env_name = "Mainland China"

    # Mask the API Key
    if len(api_key) > 9:
        masked_key = f"{api_key[:5]}...{api_key[-4:]}"
    else:
        masked_key = "Key is valid but too short to mask." if api_key != 'Not Set' else 'Not Set'

    print("-" * 30)
    print("Configuration Summary:")
    print(f'  ✅ API Key Loaded: {os.environ["DASHSCOPE_API_KEY"][:5]+"*"*5}')
    print(f"  ✅ Environment:   Alibaba Cloud {env_name}")
    print(f"  ✅ API Base URL:  {api_base}")
    
    
    print("-" * 30)


if __name__ == '__main__':
    # Test the workflow
    print("--- Testing the environment variable-based workflow ---")
    load_key()
    display_config_summary()