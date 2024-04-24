import math

class Cachesimulator:
    def __init__(self, cache_size, block_size, memory_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.memory_size = memory_size
        self.num_blocks = cache_size // block_size
        self.cache = {}
        self.hits = 0
        self.misses = 0
        self.evictions = 0
    
    def access_memory(self, address):
        block_number = address // self.block_size
        index = block_number % self.num_blocks
        tag = block_number // self.num_blocks
        
        if index in self.cache:
            if self.cache[index]['tag'] == tag:
                self.hits += 1
                return "hit"
            else:
                self.evictions += 1
                self.misses += 1
                self.cache[index] = {'tag': tag, 'data': 'some_data'}
                return "miss"
        else:
            self.misses += 1
            self.cache[index] = {'tag': tag, 'data': 'some_data'}
            return "miss"
    
    def get_stats(self):
        total_accesses = self.hits + self.misses
        if total_accesses == 0:
            return "No accesses performed."
        hit_ratio = self.hits / total_accesses
        miss_ratio = self.misses / total_accesses
        return f"Total accesses: {total_accesses}, Miss Ratio: {hit_ratio:.2f}, Hit ratio: {miss_ratio:.2f}"

def main():
    print("Cache Simulator Configuration")
    cache_size = int(input("Enter Cache Size (e.g., 16 for 16 words): "))
    memory_size = int(input("Enter Memory Size (e.g., 2048 for 2048 words): ")) 
    offset_bits = int(input("Enter offset Bits (e.g., 2 for 4-word blocks): ")) 
    block_size = 2 ** offset_bits
    # Calculate number of index bits
    index_bits = int(math.log2(cache_size // block_size))
    total_address_bits = int(math.log2(memory_size))
    tag_bits = total_address_bits - index_bits
    print("\nCache Configuration")
    print(f"Offset = {offset_bits} bits")
    print(f"Index bits = {index_bits} bits")
    print(f"Instruction Length {total_address_bits} bits")
    print(f"Tag = {tag_bits} bits")
    print("Block = [tag_bits offset_bits) bits")

    simulator = Cachesimulator(cache_size, block_size, memory_size)

    while True:
        address_input = input("Enter a memory address (or type 'exit' to finish): ")
        if address_input.lower() == "exit":
            break
        if address_input.isdigit():
            simulator.access_memory(int(address_input))
        else:
            print("Invalid Input. Please Enter a valid number or 'exit'.")

    print(simulator.get_stats())

if __name__ == "__main__":
    main()
