  #!/bin/bash

  # Colors for output
  RED='\033[0;31m'
  GREEN='\033[0;32m'
  YELLOW='\033[1;33m'
  BLUE='\033[0;34m'
  NC='\033[0m' # No Color

  # Banner
  echo -e "${BLUE}"
  echo "╔════════════════════════════════════════╗"
  echo "║  🗺️  MMG - Markmap Generator Setup    ║"
  echo "║  Auto Installation Script              ║"
  echo "╚════════════════════════════════════════╝"
  echo -e "${NC}\n"

  # Check Python version
  echo -e "${YELLOW}[1/6] Checking Python version...${NC}"
  if ! command -v python3 &> /dev/null; then
      echo -e "${RED}❌ Python 3 is not installed${NC}"
      echo "Please install Python 3.8 or higher from https://www.python.org/"
      exit 1
  fi

  PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
  echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}\n"

  # Check pip
  echo -e "${YELLOW}[2/6] Checking pip...${NC}"
  if ! command -v pip3 &> /dev/null; then
      echo -e "${RED}❌ pip3 is not installed${NC}"
      echo "Installing pip..."
      python3 -m ensurepip --upgrade
  fi
  echo -e "${GREEN}✅ pip is ready${NC}\n"

  # Create virtual environment (optional)
  echo -e "${YELLOW}[3/6] Setting up environment...${NC}"
  if [ ! -d "venv" ]; then
      echo "Creating virtual environment..."
      python3 -m venv venv
      echo -e "${GREEN}✅ Virtual environment created${NC}"
  else
      echo -e "${GREEN}✅ Virtual environment already exists${NC}"
  fi

  # Activate virtual environment
  if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
      source venv/Scripts/activate
  else
      source venv/bin/activate
  fi
  echo -e "${GREEN}✅ Virtual environment activated${NC}\n"

  # Upgrade pip, setuptools, wheel
  echo -e "${YELLOW}[4/6] Upgrading pip and setuptools...${NC}"
  pip3 install --upgrade pip setuptools wheel
  echo -e "${GREEN}✅ Dependencies upgraded${NC}\n"

  # Install MMG
  echo -e "${YELLOW}[5/6] Installing MMG...${NC}"
  if [ -f "pyproject.toml" ]; then
      pip3 install -e .
      echo -e "${GREEN}✅ MMG installed successfully${NC}\n"
  else
      echo -e "${RED}❌ pyproject.toml not found${NC}"
      exit 1
  fi

  # Verify installation
  echo -e "${YELLOW}[6/6] Verifying installation...${NC}"
  if command -v mmg &> /dev/null; then
      echo -e "${GREEN}✅ MMG command is available${NC}\n"
      
      # Show available templates
      echo -e "${BLUE}Available templates:${NC}"
      mmg --list
      
      echo -e "\n${GREEN}═══════════════════════════════════════${NC}"
      echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
      echo -e "${GREEN}═══════════════════════════════════════${NC}\n"
      
      echo -e "${BLUE}Quick start commands:${NC}"
      echo -e "  ${YELLOW}mmg --list${NC}                    # List all templates"
      echo -e "  ${YELLOW}mmg --type novel${NC}             # Generate from template"
      echo -e "  ${YELLOW}mmg --interactive${NC}            # Interactive mode"
      echo -e "  ${YELLOW}mmg --type planning --html${NC}   # Export as HTML"
      echo ""
      
      echo -e "${BLUE}Next steps:${NC}"
      echo -e "  1. Run: ${YELLOW}mmg --interactive${NC}"
      echo -e "  2. Or: ${YELLOW}mmg --type novel --html${NC}"
      echo -e "  3. Check: ${YELLOW}README.md${NC} for more examples"
      echo ""
      
  else
      echo -e "${RED}❌ Installation verification failed${NC}"
      exit 1
  fi

  # Optional: Install dev dependencies
  echo -e "${BLUE}Would you like to install development dependencies?${NC}"
  read -p "Install pytest, black, flake8? (y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
      echo -e "${YELLOW}Installing dev dependencies...${NC}"
      pip3 install -e ".[dev]"
      echo -e "${GREEN}✅ Dev dependencies installed${NC}\n"
  fi

  echo -e "${GREEN}Setup complete! Happy mindmapping! 🗺️${NC}\n"