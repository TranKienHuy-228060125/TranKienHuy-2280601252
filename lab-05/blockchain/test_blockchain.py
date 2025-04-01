from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Thêm giao dịch
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Charlie', 'Alice', 15)

# Đào một khối mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
previous_hash = previous_block.compute_hash()
new_proof = my_blockchain.proof_of_work(previous_proof)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị blockchain
for block in my_blockchain.chain:
    print(f"Block # {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Proof: {block.proof}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.compute_hash()}")
    print("-" * 50)

# Kiểm tra blockchain có hợp lệ không
is_valid = my_blockchain.is_chain_valid()
print(f"Is Blockchain Valid: {my_blockchain.is_chain_valid()}")

