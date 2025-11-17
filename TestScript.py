import os
env = os.getenv("ENVIRONMENT", "dev")
print(f"🚀 Deploying to {env.upper()} environment!")
print("Extra line added")
