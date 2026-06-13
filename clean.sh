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
echo -e "${BOLD}${CYAN}│         imgkit clean        │${RESET}"
echo -e "${BOLD}${CYAN}└─────────────────────────────┘${RESET}"
echo ""
echo -e "  ${YELLOW}Cleaning up...${RESET}"

# Clear input folder
rm -f input/*

# Remove output/images folder
rm -rf output/images

echo -e "  ${GREEN}✔${RESET}  input/ cleared"
echo -e "  ${GREEN}✔${RESET}  output/images/ removed"
echo ""
echo -e "  ${WHITE}All clean. Ready for next batch.${RESET}"
echo ""