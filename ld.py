import ldclient
from ldclient.config import Config

# Initialize the LaunchDarkly client with your SDK key
ldclient.set_config(Config("sdk-3ccc338f-edf5-40f9-93be-ad03fcf2a03d"))

# Set up a feature flag key
FEATURE_FLAG_KEY = "my-feature-flag-1"

# Set up a code reference key
CODE_REF_KEY = "my-code-reference"

def main():
    # Initialize the client
    ld_client = ldclient.get()

    try:
        # Check if the feature flag is enabled for the current user
        flag_value = ld_client.variation(FEATURE_FLAG_KEY, {"key": "user_key"}, False)

        if flag_value:
            # Execute the code reference
            code_reference = ld_client.variation(CODE_REF_KEY, {"key": "user_key"}, "")
            if code_reference:
                print("Executing code reference:", code_reference)
                # Here you can execute your code reference logic
            else:
                print("Code reference is not set")
        else:
            print("Feature flag is not enabled")
    finally:
        # Remember to close the client
        ld_client.close()

if __name__ == "__main__":
    main()

