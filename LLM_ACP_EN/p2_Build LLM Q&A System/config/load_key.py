import os
import getpass
import json

# Try to import dashscope; if it fails, set it to None. This does not affect core functionality.
try:
    import dashscope
except ImportError:
    dashscope = None

# --- Constants ---
# Path to the configuration file
CONFIG_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '../Key.json'))

# Keys used for environment variables and in the JSON file
API_KEY_KEY = 'DASHSCOPE_API_KEY'
# Kept original name, used for OpenAI compatibility mode
OPENAI_COMPAT_URL_KEY = 'DASHSCOPE_API_BASE'
# New variable, uppercased, for the native DashScope SDK
SDK_URL_KEY = 'DASHSCOPE_BASE_HTTP_API_URL'


def _prompt_for_environment() -> str:
    """Interactively prompts the user to select their cloud environment and returns 'intl' or 'cn'."""
    while True:
        prompt = "Are you using the Alibaba Cloud International site? (Y/N): "
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            print("-> Environment selected: Alibaba Cloud International")
            return "intl"
        elif response in ['n', 'no']:
            print("-> Environment selected: Alibaba Cloud Mainland China")
            return "cn"
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def load_key():
    """
    Loads/prompts for DashScope settings, writes them to a file, and sets them as environment variables.
    - os.environ['DASHSCOPE_API_KEY']
    - os.environ['DASHSCOPE_API_BASE'] (OpenAI compatible URL)
    - os.environ['DASHSCOPE_BASE_HTTP_API_URL'] (Native SDK URL)
    """
    config_data = {}
    config_changed = False

    # Step 1: Read existing configuration from Key.json
    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as file:
                config_data = json.load(file)
        except json.JSONDecodeError:
            print(f"Warning: Config file '{CONFIG_FILE_PATH}' is corrupted. A new one will be created.")

    # Step 2: Check for and interactively complete missing configuration
    # Check for API Key
    if not config_data.get(API_KEY_KEY):
        print("DashScope API Key not found in config.")
        api_key = getpass.getpass("Please enter your DashScope API Key: ").strip()
        if api_key:
            config_data[API_KEY_KEY] = api_key
            config_changed = True

    # Check if both URLs exist. If one is missing, re-prompt for the environment.
    if not config_data.get(OPENAI_COMPAT_URL_KEY) or not config_data.get(SDK_URL_KEY):
        print("Complete environment setting not found in config.")
        env_choice = _prompt_for_environment()

        if env_choice == 'intl':
            config_data[OPENAI_COMPAT_URL_KEY] = 'https://dashscope-intl.aliyuncs.com/compatible-mode/v1'
            config_data[SDK_URL_KEY] = 'https://dashscope-intl.aliyuncs.com/api/v1'
        else:  # 'cn'
            config_data[OPENAI_COMPAT_URL_KEY] = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
            config_data[SDK_URL_KEY] = 'https://dashscope.aliyuncs.com/api/v1'
        config_changed = True

    # Step 3: Write back to file if the configuration was changed
    if config_changed:
        try:
            os.makedirs(os.path.dirname(CONFIG_FILE_PATH), exist_ok=True)
            with open(CONFIG_FILE_PATH, 'w', encoding='utf-8') as json_file:
                json.dump(config_data, json_file, indent=4, ensure_ascii=False)
            print(f"-> Configuration saved/updated to: {CONFIG_FILE_PATH}")
        except IOError as e:
            print(f"Error: Could not write to config file: {e}")

    # Step 4: Set the configuration as environment variables and for the dashscope library
    if all(key in config_data for key in [API_KEY_KEY, OPENAI_COMPAT_URL_KEY, SDK_URL_KEY]):
        os.environ[API_KEY_KEY] = config_data[API_KEY_KEY]
        os.environ[OPENAI_COMPAT_URL_KEY] = config_data[OPENAI_COMPAT_URL_KEY]
        os.environ[SDK_URL_KEY] = config_data[SDK_URL_KEY]

        # Also configure the dashscope library if it's installed
        if dashscope:
            dashscope.api_key = config_data[API_KEY_KEY]
            # Note: The dashscope library's api_base property should use the native SDK URL
            dashscope.api_base = config_data[SDK_URL_KEY]
        
        print("-> Configuration loaded into environment variables successfully.")
    else:
        print("Warning: Configuration is incomplete. Some features may not work correctly.")


def display_config_summary():
    """Reads configuration from environment variables and prints a summary, masking the sensitive API key."""
    api_key = os.environ.get(API_KEY_KEY, 'Not Set')
    openai_compat_url = os.environ.get(OPENAI_COMPAT_URL_KEY, 'Not Set')
    sdk_url = os.environ.get(SDK_URL_KEY, 'Not Set')

    # Determine environment name from the URL
    if "intl" in openai_compat_url:
        env_name = "International"
    elif "aliyuncs.com" in openai_compat_url:
        env_name = "Mainland China"
    else:
        env_name = "Unknown"

    # Mask the API Key for display
    if len(api_key) > 8 and api_key != 'Not Set':
        masked_key = f"{api_key[:4]}...{api_key[-4:]}"
    else:
        masked_key = "Valid" if api_key != 'Not Set' else 'Not Set'
    
    print("\n" + "-" * 65)
    print("                    Configuration Summary")
    print("-" * 65)
    # Use fixed key names for aligned formatting
    print(f"  ✅ {API_KEY_KEY:<32}: {masked_key}")
    print(f"  ✅ {'Environment':<32}: Alibaba Cloud {env_name}")
    print(f"  ✅ {OPENAI_COMPAT_URL_KEY:<32}: {openai_compat_url}")
    print(f"  ✅ {SDK_URL_KEY:<32}: {sdk_url}")
    print("-" * 65)


if __name__ == '__main__':
    print("--- Starting DashScope Environment Configuration Workflow ---")
    load_key()
    display_config_summary()
