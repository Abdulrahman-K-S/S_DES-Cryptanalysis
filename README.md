# <p align='center'>S-DES Cryptanalysis</p>

![Project License](https://img.shields.io/badge/license-MIT-green.svg)

This repository contains a cryptanalysis implementation for the Simplified Data Encryption Standard (S-DES). It explores various cryptanalysis techniques to demonstrate weaknesses in S-DES encryption and evaluates their effectiveness.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Cryptanalysis Techniques](#cryptanalysis-techniques)
- [Contributing](#contributing)
- [License](#license)

## Introduction

S-DES is a simplified version of the Data Encryption Standard (DES), primarily used for teaching and learning cryptographic concepts. This project provides an implementation of S-DES encryption and decryption, along with cryptanalysis techniques to highlight its vulnerabilities. 

The goal of this project is to:
1. Understand the design and operation of S-DES.
2. Experiment with cryptanalysis methods like brute-force attacks.

## Features

- Implementation of S-DES encryption and decryption.
- Key generation for S-DES.
- Cryptanalysis techniques, including brute-force attacks.
- Easy-to-understand code structure for educational purposes.

## Requirements

To run this project, you need:

- Python 3.8 or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Abdulrahman-K-S/S_DES-Cryptanalysis.git
   cd S_DES-Cryptanalysis
   ```

## Usage

To use the project, follow these steps:

1. Run the cryptanalysis techniques:

   ```bash
   python main.py
   ```

2. Enter the known plaintext & known ciphertext.

## File Structure

- `rounds/`: Contains the implementation of S-DES encryption and decryption processes.
- `key_generation/`: Implements key generation and supports cryptanalysis techniques.
- `utils/`: Includes utility functions for key generation and additional operations.

## Cryptanalysis Techniques - Brute-Force Attack

The brute-force attack generates all possible keys for `K1` and `K2` from the given plaintext and ciphertext. For each generated `K1`, it checks whether there is a similar `K2` among the generated K2s. The similarity exists because `K1` undergoes a left shift by 2 and then a P8 permutation, ultimately producing `K2`. If such a similarity is found, a valid key pair `(K1, K2)` is identified; otherwise, the process continues.

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore, learn, and improve the project! If you have any questions or suggestions, please open an issue or contact the me.
