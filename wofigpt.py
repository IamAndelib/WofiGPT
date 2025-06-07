#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import urllib.parse
import shutil

def is_wofi_running():
    """Check if wofi is already running"""
    try:
        result = subprocess.run(['pgrep', '-x', 'wofi'], capture_output=True)
        return result.returncode == 0
    except:
        return False

def kill_wofi():
    """Kill wofi if running"""
    try:
        subprocess.run(['pkill', '-x', 'wofi'], check=False)
    except:
        pass

def wofi_dmenu(prompt, options=None, lines=None):
    """Run wofi dmenu with given prompt and options"""
    cmd = ['wofi', '--dmenu', '--prompt', prompt, '--insensitive']
    if lines:
        cmd.extend(['--lines', str(lines)])
    
    try:
        if options:
            result = subprocess.run(cmd, input=options, text=True, capture_output=True)
        else:
            result = subprocess.run(cmd, text=True, capture_output=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except:
        return None

def open_browser(url):
    """Open URL in browser"""
    try:
        subprocess.run(['xdg-open', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def type_prompt(text):
    """Type prompt using xdotool"""
    if shutil.which('xdotool'):
        try:
            time.sleep(1)
            # Focus the browser window
            subprocess.run(['xdotool', 'search', '--sync', '--onlyvisible', '--class', 'browser', 'windowactivate', '--sync'], check=False)
            # Type the prompt
            subprocess.run(['xdotool', 'type', '--delay', '20', text], check=False)
            subprocess.run(['xdotool', 'key', 'Return'], check=False)
        except:
            pass
    else:
        try:
            subprocess.run(['notify-send', 'AI Search', 'Install xdotool for automatic prompt insertion'], check=False)
        except:
            pass

def main():
    # Kill wofi if already running
    if is_wofi_running():
        kill_wofi()
        sys.exit(0)
    
    # Define main search options
    search_options = "🌐 Google\n🤖 ChatGPT"
    
    # Run wofi prompt with search options
    selection = wofi_dmenu("Search", search_options)
    
    # Exit if no selection
    if not selection:
        sys.exit(0)
    
    # Extract command prefix and query
    parts = selection.split(' ', 1)
    prefix = parts[0]
    query = parts[1].strip() if len(parts) > 1 else ""
    
    if prefix == '🌐' or selection.startswith('🌐 Google'):
        # Google search
        if not query or query == 'Google':
            query = wofi_dmenu("Google Search:")
        elif query == 'Google':
            query = wofi_dmenu("Google Search:")
        if not query:
            sys.exit(0)
        encoded_query = urllib.parse.quote_plus(query)
        open_browser(f"https://www.google.com/search?q={encoded_query}")
    
    elif prefix == '🤖' or selection.startswith('🤖 ChatGPT'):
        # ChatGPT
        if not query or query == 'ChatGPT' or query.isspace():
            prompt = wofi_dmenu("Ask ChatGPT:", lines=3)
            if not prompt:
                sys.exit(0)
            encoded_prompt = urllib.parse.quote_plus(prompt)
            open_browser(f"https://chat.openai.com/?q={encoded_prompt}")
        else:
            encoded_query = urllib.parse.quote_plus(query)
            open_browser(f"https://chat.openai.com/?q={encoded_query}")
    
    else:
        # Default: Google search
        encoded_selection = urllib.parse.quote_plus(selection)
        open_browser(f"https://www.google.com/search?q={encoded_selection}")

if __name__ == "__main__":
    main()
