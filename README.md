# NFT in Vyper 

# 1 - Setting up the environment:

## Recommendations:

The following tools are not required but highly recommended for a better coding experience:

- **Terminal (Mac OS only):** iTerm 2 ([download](https://iterm2.com/))
- **Shell:** Oh my ZSH ([download](https://ohmyz.sh/#install))
- **Code Editor:** VS Code ([download](https://code.visualstudio.com/))
- **VS Code Plugins:**
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [Vyper](https://marketplace.visualstudio.com/items?itemName=tintinweb.vscode-vyper)

<br/>
<br/>

## Requirements:
- **Git** of course :-)
- **Node JS:** Make sure to have [Node JS](https://nodejs.org/en/download/) installed.
- **Infura:** Create an [Infura](https://infura.io/) account and project and get the project id
- **Etherscan:** Create an [Etherscan](https://etherscan.io/) account and api key
- **pyenv-virtualenv** :
   - Mac OS:
      1. Install **Homebrew** ([install](https://brew.sh/))

      1. Install package:
         ```sh
         brew install pyenv-virtualenv
         ```
      1. Add it to path (assuming you are using ZSH)
         ```sh
         echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
         ```
         ```sh
         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
         ```
         ```sh
         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
         ```
   - Other OS:
      ([Follow instructions to install](https://github.com/pyenv/pyenv-virtualenv))

<br/>
<br/>

## Configuration Steps:

1. Clone the repo

   ```sh
   git clone git@github.com:hightop-web3/vyper-nft.git
   ```

   and then:

   ```sh
   cd vyper-nft
   ```

1. Install Ganache globally (Only needed once)

   ```sh
   npm install -g ganache
   ```

1. Install python version
   ```sh
   pyenv install 3.9.8
   ```

1. Create the Python virtual environment (Only needed once)
   ```sh
   pyenv virtualenv 3.9.8 vyper-nft

   ```
1. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```
<br />
<br />

## Running the project:

- **To Compile** the smart-contracts, run:
  ```sh
  brownie compile
  ```
- **Run tests** with:
  ```sh
  brownie test
  ```

## Dependencies

- **When adding a new dependency** run the command below to update the `requirements.txt` file.
  ```sh
  pip freeze > requirements.txt
  ```
