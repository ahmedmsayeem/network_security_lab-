import random

# Step 1: Public parameters
p = 23  # Prime number (example)
g = 5   # Primitive root modulo p (example)

# Step 2: Generate private keys for A and B
private_key_A = random.randint(1, p - 1)  # Private key for A
private_key_B = random.randint(1, p - 1)  # Private key for B

# Step 3: Compute public keys
public_key_A = pow(g, private_key_A, p)  # A's public key: (g^a) mod p
public_key_B = pow(g, private_key_B, p)  # B's public key: (g^b) mod p

# Step 4: Exchange public keys and compute the shared secret
shared_secret_A = pow(public_key_B, private_key_A, p)  # A computes: (B^a) mod p
shared_secret_B = pow(public_key_A, private_key_B, p)  # B computes: (A^b) mod p

# Step 5: Verify that the shared secrets are the same
assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"

# Output results
print("Public Parameters:")
print(f"  Prime number (p): {p}")
print(f"  Primitive root (g): {g}\n")

print("Private Keys:")
print(f"  Private key for A: {private_key_A}")
print(f"  Private key for B: {private_key_B}\n")

print("Public Keys:")
print(f"  Public key for A: {public_key_A}")
print(f"  Public key for B: {public_key_B}\n")

print("Shared Secret Key (computed by both A and B):")
print(f"  Shared key: {shared_secret_A}")

