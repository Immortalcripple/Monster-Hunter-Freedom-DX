import array
import os

def replace(data_path, repl_path, addr, size):
    size_adj = 0
    if not os.path.exists(repl_path):
        return size_adj
        
    with open(data_path, "rb") as fp:
        data_bin = bytearray(fp.read())
    
    with open(repl_path, "rb") as fp:
        repl_data = fp.read()
        size_adj = len(repl_data) - size
        
    if len(repl_data) < size:
        repl_data = repl_data.ljust(size, b"\x00")
        
    before = data_bin[:addr]
    after = data_bin[addr + size:]
    
    combined = before + repl_data + after
    
    with open(data_path, "wb") as fp:
        fp.write(combined)
    
    return size_adj
 
def memset(data_path, value, addr, size):
    with open(data_path, "rb") as fp:
        data_bin = bytearray(fp.read())
        
    before = data_bin[:addr]
    after = data_bin[addr + size:]
    combined = before + (bytes([value]) * size) + after
    
    with open(data_path, "wb") as fp:
        fp.write(combined)
        
def memcpy(data_path, arr, addr):
    with open(data_path, "rb") as fp:
        data_bin = bytearray(fp.read())
        
    before = data_bin[:addr]
    after = data_bin[addr + len(arr):]
    combined = before + bytes(arr) + after
    
    with open(data_path, "wb") as fp:
        fp.write(combined)

def translate(build_dir):
    DATA_BIN = os.path.join(build_dir, "ULJM05066", "DATA.BIN")
    if not os.path.exists(DATA_BIN):
        return
     
    memset(DATA_BIN, 0, 0x5B00, 0x386)
    memcpy(DATA_BIN, [0x1A, 0x00, 0x05, 0x34], 0x1A6396D0);
    memcpy(DATA_BIN, [0x28, 0x00, 0x05, 0x34, 0x38, 0xC5, 0x21, 0x0E, 0x14, 0x00, 0x06, 0x34], 0x1A639D04);
    replace(DATA_BIN, os.path.join("translation", "4674-4922"), 0x1D757000, 0x2D3800)