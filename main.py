# Remove quotes from a List of Strings in Python

my_list = ['"bobby"', '"hadz"', '"com"']

# ✅ Remove all quotes from list of strings

new_list = [item.replace('"', '') for item in my_list]
print(new_list)  # 👉️ ['bobby', 'hadz', 'com']

# -------------------------------------------------

# ✅ Remove leading and trailing quotes from list of strings

new_list = [item.strip('"') for item in my_list]
print(new_list)  # 👉️ ['bobby', 'hadz', 'com']