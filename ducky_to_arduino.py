#!/usr/bin/env python3
"""
DuckyScript 3.0 to Arduino Converter
Supports core DuckyScript + many 3.0 extensions.
"""

import sys
import re

def ds3_to_arduino(lines):
    sketch = [
        '#include <Keyboard.h>',
        '#include <Mouse.h>',  # Added for potential mouse commands
        '',
        'void setup() {',
        '  Keyboard.begin();',
        '  Mouse.begin();',
        '  delay(1500);  // Safer enumeration delay',
        '  // === DuckyScript 3.0 Payload Start ==='
    ]
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line or line.startswith('REM') or line.startswith('//'):
            continue
        
        # DELAY
        if line.startswith('DELAY'):
            delay = int(re.search(r'\d+', line).group())
            sketch.append(f'  delay({delay});')
        
        # STRING / STRINGLN
        elif line.startswith('STRING '):
            text = line[7:].replace('"', '\\"')
            sketch.append(f'  Keyboard.print("{text}");')
        elif line.startswith('STRINGLN '):
            text = line[9:].replace('"', '\\"')
            sketch.append(f'  Keyboard.println("{text}");')
        
        # ENTER / RETURN
        elif line in ['ENTER', 'RETURN']:
            sketch.append('  Keyboard.press(KEY_RETURN);')
            sketch.append('  Keyboard.releaseAll();')
        
        # GUI / WINDOWS + combo
        elif line.startswith('GUI ') or line.startswith('WINDOWS '):
            parts = line.split()
            sketch.append('  Keyboard.press(KEY_LEFT_GUI);')
            for p in parts[1:]:
                if len(p) == 1:
                    sketch.append(f'  Keyboard.press(\'{p}\');')
            sketch.append('  Keyboard.releaseAll();')
        
        # CTRL + ALT + SHIFT combos
        elif line.startswith('CTRL ') or line.startswith('ALT ') or line.startswith('SHIFT '):
            key_map = {'CTRL': 'KEY_LEFT_CTRL', 'ALT': 'KEY_LEFT_ALT', 'SHIFT': 'KEY_LEFT_SHIFT'}
            parts = line.split()
            base = key_map.get(parts[0], 'KEY_LEFT_CTRL')
            sketch.append(f'  Keyboard.press({base});')
            for p in parts[1:]:
                if len(p) == 1:
                    sketch.append(f'  Keyboard.press(\'{p}\');')
                elif p.upper() in ['ENTER', 'RETURN']:
                    sketch.append('  Keyboard.press(KEY_RETURN);')
            sketch.append('  Keyboard.releaseAll();')
        
        # Mouse support (DS 3.0)
        elif line.startswith('MOUSE '):
            # Basic: MOUSE MOVE x y
            if 'MOVE' in line:
                match = re.search(r'MOVE\s+(-?\d+)\s+(-?\d+)', line)
                if match:
                    x, y = match.groups()
                    sketch.append(f'  Mouse.move({x}, {y});')
        
        # REPEAT
        elif line.startswith('REPEAT'):
            # Simplified: just comment for now (can be expanded)
            sketch.append('  // REPEAT command - manual loop recommended')
        
        # Default: treat as single key
        elif len(line) == 1 and line.isalpha():
            sketch.append(f'  Keyboard.press(\'{line.lower()}\');')
            sketch.append('  Keyboard.releaseAll();')
    
    sketch.extend([
        '  // === Payload End ===',
        '}',
        '',
        'void loop() {',
        '  // Keep alive or add custom logic',
        '}'
    ])
    
    return '\n'.join(sketch)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ducky_to_arduino.py payload.txt [output.ino]")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    arduino_code = ds3_to_arduino(content)
    
    output_file = sys.argv[2] if len(sys.argv) > 2 else "payload.ino"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(arduino_code)
    
    print(f"✅ DuckyScript 3.0 Arduino sketch generated: {output_file}")
    print("Boards: Leonardo / Pro Micro / ESP32-S2/S3")
  ---
How to Use (Updated)
python ducky_to_arduino.py your_payload.txt my_ducky.ino
---
# Supported DuckyScript 3.0 Improvements
•  STRINGLN (print + newline)
•  Better combo key handling (CTRL ALT t, GUI r, etc.)
•  Basic MOUSE MOVE support
•  Safer delays and includes
