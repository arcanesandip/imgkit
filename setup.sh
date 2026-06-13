#!/bin/bash

CYAN="\033[96m"
GREEN="\033[92m"
YELLOW="\033[93m"
WHITE="\033[97m"
DIM="\033[2m"
BOLD="\033[1m"
RESET="\033[0m"

echo ""
echo -e "${BOLD}${CYAN}┌─────────────────────────────┐${RESET}"
echo -e "${BOLD}${CYAN}│         imgkit setup        │${RESET}"
echo -e "${BOLD}${CYAN}└─────────────────────────────┘${RESET}"
echo ""
echo -e "  ${YELLOW}Setting up environment...${RESET}"
echo ""

# Create virtual environment
python3 -m venv venv
echo -e "  ${GREEN}✔${RESET}  Virtual environment created"

# Install dependencies inside venv
./venv/bin/pip install --quiet -r requirements.txt
echo -e "  ${GREEN}✔${RESET}  Dependencies installed"

echo ""
echo -e "  ${WHITE}${BOLD}Setup complete. Now run:${RESET}"
echo ""
echo -e "  ${CYAN}source venv/bin/activate${RESET}"
echo ""
echo -e "  ${DIM}Your prompt will change to (venv). Then run:${RESET}"
echo ""
echo -e "  ${CYAN}python process.py${RESET}"
echo ""