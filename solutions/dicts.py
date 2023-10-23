# Nested Dictionaries Exercise

# --- Instructions ---
# For the following exercises, you'll be manipulating nested dictionaries. 
# A nested dictionary is a dictionary where some values are dictionaries themselves.

# --- Basic Operations ---

# 1. Retrieve Information:
# Given the outer and inner keys, retrieve the associated value from the nested dictionary.
def get_information(data, outer_key, inner_key):
    """
    Parameters:
    - data: A nested dictionary
    - outer_key: Key of the outer dictionary
    - inner_key: Key of the inner dictionary within the outer dictionary

    Returns:
    - Value associated with the inner key or None if the keys are not found.
    """
    # Your code here
    pass


# 2. Add Information:
# Add or modify information in the nested dictionary using the given outer and inner keys.
def add_information(data, outer_key, inner_key, value):
    """
    Parameters:
    - data: A nested dictionary
    - outer_key: Key of the outer dictionary
    - inner_key: Key of the inner dictionary within the outer dictionary
    - value: Value to be added or updated in the nested dictionary

    Returns:
    - Modified data with the new value
    """
    # Your code here
    pass


# 3. Remove Information:
# Given the outer and inner keys, remove the associated key-value pair from the nested dictionary.
def remove_information(data, outer_key, inner_key):
    """
    Parameters:
    - data: A nested dictionary
    - outer_key: Key of the outer dictionary
    - inner_key: Key of the inner dictionary within the outer dictionary

    Returns:
    - Modified data with the key-value pair removed or original data if the keys are not found.
    """
    # Your code here
    pass


# --- Advanced Operations ---

# 4. Retrieve Nested Value:
# Retrieve the value of a given key chain from the nested dictionary.
def get_nested_value(data, key_chain):
    """
    Parameters:
    - data: A nested dictionary
    - key_chain: A list of keys indicating the path to retrieve the value

    Returns:
    - Value at the end of the key chain or None if the path doesn't exist.
    """
    # Your code here
    pass


# 5. Set Nested Value:
# Modify the nested dictionary to set a value at a specific key chain.
def set_nested_value(data, key_chain, value):
    """
    Parameters:
    - data: A nested dictionary
    - key_chain: A list of keys indicating the path to set the value
    - value: Value to be set at the end of the key chain

    Returns:
    - Modified data with the value set at the specified key chain.
    """
    # Your code here
    pass


